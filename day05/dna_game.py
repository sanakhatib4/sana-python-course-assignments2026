from dna_logic import generate_secret, validate_guess, score_guess


def main():
    print("=== DNA Code Breaker (day05) ===")
    print("The computer has chosen a secret DNA sequence.")
    print("Your goal: guess the sequence in a limited number of attempts.")
    print("Valid bases: A, C, G, T")
    print("Example guess: ACGT\n")

    sequence_length = 4
    max_attempts = 10

    secret = generate_secret(sequence_length)

    print(f"The sequence is {sequence_length} bases long.")
    print(f"You have {max_attempts} attempts. Type 'quit' to give up.\n")

    attempts_used = 0

    while attempts_used < max_attempts:
        guess_raw = input(f"Attempt {attempts_used + 1} – Enter your guess: ")

        if guess_raw.strip().lower() == "quit":
            print("You chose to quit. Better luck next time!")
            print(f"The secret sequence was: {secret}")
            return

        try:
            guess = validate_guess(guess_raw, length=sequence_length)
        except ValueError as e:
            print(f"Invalid guess: {e}")
            print("Please try again.\n")
            continue  

        attempts_used += 1

        exact, partial = score_guess(secret, guess)

        if exact == sequence_length:
            print(f"\n🎉 Congratulations! You guessed the sequence: {secret}")
            print(f"You won in {attempts_used} attempts.")
            break

        print(f"Result for {guess}:")
        print(f"  {exact} correct base(s) in the correct position.")
        print(f"  {partial} correct base(s) but in the wrong position.\n")

    else:
        print("\n❌ You've used all your attempts.")
        print(f"The secret sequence was: {secret}")

    print("\nThanks for playing DNA Code Breaker!")


if __name__ == "__main__":
    main()
