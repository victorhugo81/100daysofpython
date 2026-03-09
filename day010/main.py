# ======================
# Project Name: Day 10 - The Calculator
# Section: Beginner Python Projects
# Description: Python lists, dictionaries, functions and outputs
# ======================

# Import ASCII logo from external file
from art import LOGO   

# Display the calculator logo and welcome message
print(LOGO)
print("*******************************************")
print("Welcome to The Calculator!")
print("*******************************************")

# --- Basic arithmetic functions ---

def addition(n1, n2):
    """Returns the sum of two numbers."""
    return n1 + n2

def subtraction(n1, n2):
    """Returns the difference of two numbers."""
    return n1 - n2

def multiplication(n1, n2):
    """Returns the product of two numbers."""
    return n1 * n2

def division(n1, n2):
    """Returns the quotient of two numbers."""
    return n1 / n2

# Dictionary mapping operator symbols to their corresponding functions
operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def get_number(prompt):
    """Keeps asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculator():
    """Main calculator loop. Allows the user to chain operations or start fresh."""

    # Get the initial number from the user
    num1 = get_number("What is the first number?: ")

    # Flag to control whether we keep accumulating results
    should_accumulate = True

    while should_accumulate:
        # Display all available operators
        for symbol in operations:
            print(symbol)

        # Keep asking until a valid operator is chosen
        while True:
            operation_symbol = input("Pick an operation: ")
            if operation_symbol in operations:
                break
            print("Invalid operator! Please choose +, -, * or /")

        # Get the second number, with validation
        num2 = get_number("What is the next number?: ")

        # Look up and call the matching function from the operations dictionary
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask the user if they want to continue with the current result or start over
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            # Use the current answer as the first number for the next operation
            num1 = answer
        else:
            # Exit the loop, clear the screen, and restart the calculator
            should_accumulate = False
            print("\n" * 20)  # Clear the console output
            calculator()      # Recursively start a new calculation session

# Entry point — start the calculator
calculator()