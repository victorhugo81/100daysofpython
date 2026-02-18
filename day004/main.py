# ======================
# Project Name: Day 4 - Python Password Generator
# Section: Beginner Python Projects
# Description: Python loops
# ======================
import random

def main():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+']
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    print("Welcome to the Python Password Generator!")

    pwd_letters = int(input("How many characters would you like in your password? "))
    pwd_symbols = int(input("How many symbols would you like? "))
    pwd_numbers = int(input("How many numbers would you like? "))

    password_chars = []

    # pick random letters
    for char in range(pwd_letters):
        password_chars.append(random.choice(letters))

    # pick random symbols
    for symbol in range(pwd_symbols):
        password_chars[symbol] = random.choice(symbols)

    # pick random numbers
    for number in range(pwd_numbers):
        password_chars[pwd_symbols + number] = random.choice(numbers)

    # shuffle so it's not predictable like letters→symbols→numbers
    random.shuffle(password_chars)
    password = "".join(password_chars)

    print(f"Your password is: {password}")



# Run the main function when the script is executed
if __name__ == "__main__":
    main()