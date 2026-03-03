# ======================
# Project Name: Day 9 - The Secret Auction
# Section: Beginner Python Projects
# Description: Python lists and dictionaries
# ======================

# Import ASCII logo from external file
from art import LOGO   

# Display the game logo
print(LOGO)

print("*******************************************")
print("Welcome to The Secret Auction!")
print("*******************************************")


def find_highest_bidder(bidding_dictionary):
    """
    Determines the highest bidder from the dictionary,
    prints total bids, all bids, and the winner.
    """

    # Store the name of the highest bidder
    winner = ""          
    # Store the highest bid amount
    highest_bid = 0      

    # Loop through each bidder in the dictionary
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]

        # Check if current bid is higher than previous highest
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("\n************* Auction Results *************")

    # Display total number of bids
    print(f"Total bids placed: {len(bidding_dictionary)}\n")
    print("\nName   |  Bid Amount")
    print("-------------------------------------------")

    # Get sorted list of amounts
    sorted_amounts = sorted(bidding_dictionary.values(), reverse=True)

    # Display all bids entered
    for amount in sorted_amounts:
        for bidder in bidding_dictionary:
            if bidding_dictionary[bidder] == amount:
                print(f"{bidder} - ${amount}")

    # Display winner information
    print("\n-------------------------------------------")
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    print("---------------------------------------------")



def secret_auction():
    """
    Main function that collects bids from users
    until they decide to stop.
    """


    # Dictionary to store bidder names and their bids
    bids = {}                 
    # Control variable for while loop
    continue_bidding = True   

    # Continue collecting bids until user chooses to stop
    while continue_bidding:

        # --- Validate Name ---
        while True:
            name = input("What is your name?: ").strip()
            if name == "":
                print("Name cannot be empty.")
            elif not name.replace(" ", "").isalpha():
                print("Name must contain only letters.")
            else:
                break

        # --- Validate Bid ---
        while True:
            try:
                price = int(input("What is your bid?: $"))
                if price <= 0:
                    print("Bid must be greater than 0.")
                else:
                    break
            except ValueError:
                print("Please enter a valid whole number.")


            # Store bid in dictionary (name as key, price as value)
        bids[name] = price

            # Ask if there are more bidders
        should_continue = input(
                "Are there any other bidders? Type 'y' if there other bidders. Otherwise type 'n'.\n"
            ).lower()

            # If no more bidders, stop loop and determine winner
        if should_continue == "n":
                continue_bidding = False
                find_highest_bidder(bids)
        elif should_continue == "y":
                print("\n")


# Start the auction program
secret_auction()