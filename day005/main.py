# ======================
# Project Name: Day 5 - Python Number Guessing Game
# Section: Beginner Python Projects
# Description: Python while loops
# ======================

import random


trophy ="""
    * * * * * * * * * * * * * * *
    *         ___________       *
    *       '._==_==_=_.'       *
    *        .-\:      /-.      *   
    *       | (|:.     |) |     *
    *        '-|:.     |-'      *
    *          \::.    /        *
    *           '::. .'         *
    *             ) (           *
    *           _.' '._         *
    * * * * * * * * * * * * * * *
    """

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("Pick a number between 1 and 100. Try to guess it!")
    
    while True:
        # Get user input
        print("**********************************************")
        guess = input("Enter your guess (or 'q' to quit): ")
        
        # Check if user wants to quit
        if guess.lower() == 'q':
            print(f"Thanks for playing! The number was {secret_number}.")
            break
        
        # Try to convert input to integer
        try:
            guess = int(guess)
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print(" - Your guessed number is too low! Try again.")
            elif guess > secret_number:
                print(" - Your guessed number is too high! Try again.")
            else:
                print(f" - Congratulations! You guessed it in {attempts} attempts.")
                print(trophy)
                break
                
        except ValueError:
            print(" - Please enter a valid number or 'q' to quit.")



# Run the game
if __name__ == "__main__":
    number_guessing_game()