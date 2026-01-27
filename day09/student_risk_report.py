from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from collections import defaultdict


INPUT_PATH = "subjects.txt"          # or "/mnt/data/subjects.txt"
TIME_FMT = "%Y-%m-%dT%H:%M:%SZ"

# EXACTLY 9 required assignments: Day01..Day08 + Final Project proposal
FINAL_CANONICAL = "Final Project proposal"
REQUIRED_ASSIGNMENTS = [f"Day{d:02d}" for d in range(1, 9)] + [FINAL_CANONICAL]

# Timing phrase trigger (relative-to-cohort percentile)
OFTEN_LATE_THRESHOLD = 70  # avg percentile >= 70% => "often late vs peers"

# Normalization helpers
DAY_RE = re.compile(r"(?i)\bday\s*0*(\d+)\b")  # matches Day08, day 8, DAY02, etc.
BY_RE = re.compile(r"(?i)\bby\b")

# Accept small “dictation” variations for the final assignment title (before "by")
FINAL_ALIASES = {
    "final project proposal",
    "final project proposals",
    "final proposal",
    "project proposal",
    # add more if needed based on your dataset
}


@dataclass(frozen=True)
class Submission:
    status: str          # OPEN/CLOSED
    assignment: str      # normalized: Day01..Day08 or "Final Project proposal"
    student: str         # e.g. "Sana Khatib"
    submitted_at: datetime


def normalize_assignment(title: str) -> str:
    """Extract a normalized assignment name from the title."""
    t = title.strip()

    # DayX normalization (case-insensitive, supports Day1/day01/etc.)
    m = DAY_RE.search(t)
    if m:
        day_num = int(m.group(1))
        return f"Day{day_num:02d}"

    # Everything else: take text before "by"
    parts = BY_RE.split(t, maxsplit=1)
    name = parts[0].strip().replace("  ", " ") if parts else t

    # Normalize final project proposal variants
    if name.lower() in FINAL_ALIASES:
        return FINAL_CANONICAL

    return name


def extract_student(title: str) -> str:
    """Get student name as the text after 'by'."""
    parts = BY_RE.split(title, maxsplit=1)
    if len(parts) < 2:
        return "UNKNOWN"
    return parts[1].strip()


def parse_line(line: str) -> Submission | None:
    line = line.rstrip("\n")
    if not line.strip():
        return None

    # Tab-separated; some lines have an empty 4th column.
    cols = line.split("\t")
    if len(cols) < 5:
        return None

    # cols: [id, status, title, "", timestamp]
    status = cols[1].strip().upper()
    title = cols[2].strip()
    ts = cols[4].strip()

    submitted_at = datetime.strptime(ts, TIME_FMT).replace(tzinfo=timezone.utc)
    assignment = normalize_assignment(title)
    student = extract_student(title)

    return Submission(status=status, assignment=assignment, student=student, submitted_at=submitted_at)


def load_submissions(path: str) -> list[Submission]:
    subs: list[Submission] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = parse_line(line)
            if s:
                subs.append(s)
    return subs


def percentile_rank(sorted_times: list[datetime], t: datetime) -> float:
    """
    Returns percentile in [0,100].
    0 = earliest, 100 = latest (relative to cohort for that assignment).
    """
    if not sorted_times:
        return 0.0

    lo, hi = 0, len(sorted_times)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_times[mid] <= t:
            lo = mid + 1
        else:
            hi = mid

    return 100.0 * (lo - 1) / max(1, (len(sorted_times) - 1))


def build_report(subs: list[Submission]):
    required = REQUIRED_ASSIGNMENTS[:]  # fixed 9 items

    # Collect submission times per required assignment
    times_by_assignment: dict[str, list[datetime]] = defaultdict(list)
    for s in subs:
        if s.assignment in required:
            times_by_assignment[s.assignment].append(s.submitted_at)
    for a in times_by_assignment:
        times_by_assignment[a].sort()

    # Collect per-student items: (assignment, submitted_at, percentile)
    by_student: dict[str, list[tuple[str, datetime, float]]] = defaultdict(list)
    for s in subs:
        if s.assignment not in required:
            continue
        cohort_times = times_by_assignment[s.assignment]
        p = percentile_rank(cohort_times, s.submitted_at)
        by_student[s.student].append((s.assignment, s.submitted_at, p))

    # Summarize per student
    rows = []
    for student, items in by_student.items():
        # Keep earliest submission per assignment if duplicates exist
        best: dict[str, tuple[datetime, float]] = {}
        for a, t, p in items:
            if a not in best or t < best[a][0]:
                best[a] = (t, p)

        submitted = set(best.keys())
        missing = [a for a in required if a not in submitted]

        percentiles = [best[a][1] for a in submitted]
        avg_pct = sum(percentiles) / len(percentiles) if percentiles else 0.0

        # Simple risk score (internal sorting only)
        score = 0
        score += int(round(avg_pct / 20))               # 0..5
        score += 3 if len(missing) >= 2 else (1 if len(missing) == 1 else 0)

        if score >= 7:
            label = "HIGH"
        elif score >= 4:
            label = "MEDIUM"
        else:
            label = "STABLE"

        rows.append((label, score, student, avg_pct, missing))

    # Sort: HIGH first, then score desc, then name
    order = {"HIGH": 0, "MEDIUM": 1, "STABLE": 2}
    rows.sort(key=lambda r: (order[r[0]], -r[1], r[2].lower()))
    return required, rows


def print_concise_report(required: list[str], rows):
    print("RISK REPORT")
    print("-" * 70)
    print("Required assignments:", ", ".join(required))
    print("-" * 70)

    for label, score, student, avg_pct, missing in rows:
        bits = []

        # Missing count + which ones
        if missing:
            bits.append(f"missing ({len(missing)}): " + ", ".join(missing))

        # Timing signal (phrase only)
        if avg_pct >= OFTEN_LATE_THRESHOLD:
            bits.append("often late vs peers")

        if not bits:
            bits.append("no issues detected")

        print(f"{label:6} | {student:25} | " + " | ".join(bits))


def main():
    subs = load_submissions(INPUT_PATH)
    required, rows = build_report(subs)
    print_concise_report(required, rows)


if __name__ == "__main__":
    main()

