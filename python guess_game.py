import random
import os

FILENAME = "highscore.txt"

# Get saved high score
def load_high_score():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return int(file.read())
    return None

# Save new high score
def save_high_score(score):
    with open(FILENAME, "w") as file:
        file.write(str(score))

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Guess must be between 1 and 100.")
                continue

            if guess < number:
                print("📉 Too low!")
            elif guess > number:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")

                high_score = load_high_score()
                if high_score is None or attempts < high_score:
                    print("🏆 New High Score!")
                    save_high_score(attempts)
                else:
                    print(f"High Score remains at {high_score} tries.")
                break

        except ValueError:
            print("⚠️ Please enter a valid number.")

    else:
        print(f"❌ You ran out of attempts! The number was {number}.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()

