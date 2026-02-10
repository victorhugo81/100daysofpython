# ======================
# Project Name: Day 4 - The Rock, Paper, Scissors Game
# Section: Beginner Python Projects
# Description: Randomization and Python Lists
# ======================
import random

def main():
    # ASCII art for the game


    rock ="""
        ______
    ---'   ___)
        (____)
        (____)
        (____)
    ---._(___)
    """

    paper ="""
            __ 
          /   )
    ---''    /_______
            _________)
            __________)
            _________)
    ---.___________)
    """

    scissors = """
        ______
    ---'  ____)___
            ______)
        __________)
        (____)
    ---.__(___)
    """

    game_images = [rock, paper, scissors]

    print("Welcome to the Rock, Paper, Scissors Game!\n")
    print("Type a number to play the game. If you type an invalid number or character, you lose!\n")
    print("Rock = 0\nPaper = 1\nScissors = 2\n")


    # User input
    user_choice = input("What do you choose? ")
    # User choice with input validation
    if user_choice.isdigit() and int(user_choice) in [0, 1, 2]:
        user_choice = int(user_choice)
        print(game_images[int(user_choice)])

        # Computer choice
        computer_choice = random.randint(0, 2)
        print(f"Computer chose: {game_images[computer_choice]}")

        # comparing player choice
        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif user_choice == 1 and computer_choice == 0:
            print("You win!")
        elif user_choice == 2 and computer_choice == 1:
            print("You win!")
        elif user_choice == computer_choice:
            print("It's a draw!")
        else:
            print("You lose!")

    else:
        print("You typed an invalid number or character. You lose!")





# Run the main function when the script is executed
if __name__ == "__main__":
    main()