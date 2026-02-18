# ======================
# Project Name: Day 7 - Dragon Ball Hangman Game
# Section: Beginner Python Projects
# Description: Python loops and if statements
# ======================


import random
from hangman_words import word_list
from hangman_art import HANGMANART, LOGO, TROPHY
 

def hangman():
    # Display the game logo at the start 
    print(LOGO)

    # you have 6 chances
    lives = 6

    # Randomly select a word from the word list
    chosen_word = random.choice(word_list)

    # length of the word.
    word_length = len(chosen_word)

    game_over = False
    correct_letters = []
    wrong_letters = []

    print("*******************************************")
    print("Welcome to the Dragon Ball Hangman Game!")
    print("*******************************************")
    print("Guess the name of a Dragon Ball character.\nYou have 6 chances before you lose.")
    print(f"Hint: The name you are looking for has {word_length} letters.")

    while not game_over:
        print(f"******************************** {lives}/6 LIVES LEFT ********************************")
        guess = input("\nGuess a letter: ").lower()

        # Warn the player if they've already guessed this letter and skip
        if guess in correct_letters or guess in wrong_letters:
            print(f"You have already guessed '{guess}', try a different letter.")
            continue 

        # Build the display string
        display = ""
        for letter in chosen_word:
            if letter == guess or letter in correct_letters:
                display += letter
            else:
                display += " _ "

        print("Word to guess: " + display)

        if guess in chosen_word:
            # add correct guesses here
            correct_letters.append(guess)  
        else:
            # add wrong guesses here
            wrong_letters.append(guess)
            lives -= 1
            print(f"You guessed '{guess}', that is not in the word. You lose a life.")

        # Check loss condition
        if lives == 0:
            game_over = True
            print(HANGMANART[lives])
            print("******************************** GAME OVER ********************************")
            print(f"You lose! The word was: {chosen_word}")

        # Check win condition
        elif " _ " not in display:
            game_over = True
            print("******************************** YOU WIN! ********************************")
            print(f"You Win! The word was: {chosen_word}")
            print(TROPHY)

        else:
            print(HANGMANART[lives])
            print(f"Wrong guesses: {wrong_letters}")

if __name__ == "__main__":
    hangman()