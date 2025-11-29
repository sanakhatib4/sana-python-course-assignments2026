# 💡 Game idea: “DNA Code Breaker”

## A Mastermind-style game, but with DNA bases:

The computer picks a secret 4-letter DNA sequence using A, C, G, T (e.g. ACGT).

The player must guess the sequence in a limited number of attempts.

After each guess, the game tells the player:

* how many bases are correct and in the correct position

* how many bases are correct but in the wrong position

Example feedback:

“2 correct in the right position, 1 correct but in the wrong position.”

## 🧠 Game Rules

- The secret sequence is 4 bases long (A, C, G, T).
- You have 10 attempts to guess it.
- Each guess must:
  - be exactly 4 characters long
  - only contain the letters A, C, G, T (case-insensitive)
- You can type `quit` at any time to give up and reveal the answer.