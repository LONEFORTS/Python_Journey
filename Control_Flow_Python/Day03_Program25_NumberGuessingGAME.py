# Program 25: Number Guessing Game
# This program demonstrates random library usage, loops, and user input handling.

import random

def start_game():
    print("--- Welcome to the Number Guessing Game! ---")
    print("I am thinking of a number between 1 and 50.")
    
    # Generate a random number
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            
    if guess != secret_number:
        print(f"\nGame Over! You've used all attempts. The number was {secret_number}.")

if __name__ == "__main__":
    start_game()
