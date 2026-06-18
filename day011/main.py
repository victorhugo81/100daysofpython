# ======================
# Project Name: Day 11 - Blackjack Game
# Section: Beginner Python Projects
# Description: A simple command-line Blackjack game where the user plays against the computer (dealer). The game includes features such as card dealing,
#               score calculation, and determining the winner based on standard Blackjack rules.
# ======================

# Import ASCII logo from external file
from art import LOGO
import random


# Display the blackjack logo and welcome message
print(LOGO)
print("*******************************************")
print("Welcome to The Blackjack Game!")
print("*******************************************")

# Returns a random card from the deck.
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

# Calculate the score of the given cards.
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        # Blackjack
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Compare scores and return (result_message, outcome) where outcome is "win", "lose", or "draw".
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃", "draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱", "lose"
    elif u_score == 0:
        return "Win with a Blackjack 😎", "win"
    elif u_score > 21:
        return "You went over. You lose 😭", "lose"
    elif c_score > 21:
        return "Opponent went over. You win 😁", "win"
    elif u_score > c_score:
        return "You win 😃", "win"
    else:
        return "You lose 😤", "lose"


wins = 0
losses = 0
draws = 0

def play_game():
    global wins, losses, draws

    print(LOGO)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal two cards to both the user and the computer at the start of the game
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Main game loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for immediate game over conditions (Blackjack or user score over 21)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    message, outcome = compare(user_score, computer_score)
    print(message)

    if outcome == "win":
        wins += 1
    elif outcome == "lose":
        losses += 1
    else:
        draws += 1

    print(f"\nScore — Wins: {wins} | Losses: {losses} | Draws: {draws}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
