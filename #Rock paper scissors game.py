#Rock paper scissors game

import random

# Options for the game
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type 'exit' to quit the game.\n")

while True:
    # User input
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice == "exit":
        print("Thanks for playing! Goodbye!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.\n")
        continue

    # Computer's random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!\n")
    else:
        print("You lose!\n")
