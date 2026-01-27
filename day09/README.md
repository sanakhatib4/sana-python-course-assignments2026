## Students at risk report generator

This program analyzes raw submission logs from the course and generates a **concise** risk report for lecturers.  
It identifies students who may need attention by combining **missing required assignments** with **submission timing behavior relative to peers**.  


### Output meaning
- **Risk label (HIGH / MEDIUM / STABLE):** overall indication of student risk level.
- **Missing assignments:** how many (and which) required assignments were not submitted.
- **“Often late vs peers”:** the student usually submits later than most classmates (based on relative submission timing).

This enables early intervention of the lecturer/TAs (e.g., reminders, support, or follow-up) rather than reacting after grades are affected.

---

## AI usage summary
The task was to design a Python program that processes a raw text file of student submissions and produces a lecturer-useful report.  
The user requested a solution that:
- normalizes inconsistent assignment naming (e.g., Day/day variations),
- enforces a fixed set of required assignments,
- detects missing work and late submission patterns,
- and presents results in a **clear, minimal, human-readable format** rather than detailed statistics.
