# ======================
# Project Name: Day 11 - Blackjack Game
# Section: Beginner Python Projects
# Description: A simple command-line Blackjack game where the user plays against the computer (dealer). The game includes features such as card dealing, 
#               score calculation, and determining the winner based on standard Blackjack rules.
# ======================

# Import ASCII logo from external file
from art import LOGO  
from random import random
 

# Display the blackjack logo and welcome message
print(LOGO)
print("*******************************************")
print("Welcome to The Blackjack Game!")
print("*******************************************")


def deal_card():
    # Returns a random card from the deck.
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] 
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    # Calculate the score of the given cards.
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


