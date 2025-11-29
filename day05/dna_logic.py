import random

VALID_BASES = ["A", "C", "G", "T"]


def generate_secret(length=4):
    """
    Generate a random DNA sequence of the given length
    using the bases A, C, G, and T.
    Returns a string, e.g. "ACGT".
    """
    return "".join(random.choice(VALID_BASES) for _ in range(length))


def validate_guess(guess, length=4):
    """
    Validate and normalize the user's guess:
    - strips whitespace
    - converts to uppercase
    - checks length and allowed characters

    Returns the cleaned guess string if valid.
    Raises ValueError with an explanatory message if invalid.
    """
    cleaned = guess.strip().upper()

    if len(cleaned) != length:
        raise ValueError(f"Guess must be exactly {length} characters long.")

    for ch in cleaned:
        if ch not in VALID_BASES:
            raise ValueError(
                f"Invalid character '{ch}'. Only A, C, G, T are allowed."
            )

    return cleaned


def score_guess(secret, guess):
    """
    Compare a secret DNA sequence with a guess and return a tuple:
        (exact_matches, partial_matches)

    - exact_matches: correct base in the correct position
    - partial_matches: correct base but in the wrong position

    Both secret and guess must be strings of the same length.
    This function assumes they are already validated.
    """
    if len(secret) != len(guess):
        raise ValueError("Secret and guess must have the same length.")

    length = len(secret)

    exact = 0
    secret_unmatched = []
    guess_unmatched = []

    for i in range(length):
        if guess[i] == secret[i]:
            exact += 1
        else:
            secret_unmatched.append(secret[i])
            guess_unmatched.append(guess[i])

    partial = 0
    secret_counts = {}
    for base in secret_unmatched:
        secret_counts[base] = secret_counts.get(base, 0) + 1

    for base in guess_unmatched:
        if secret_counts.get(base, 0) > 0:
            partial += 1
            secret_counts[base] -= 1

    return exact, partial
