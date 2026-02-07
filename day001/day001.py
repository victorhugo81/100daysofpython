# ======================
# Project Name: Day 1 - Band Name Generator
# Section: Beginner Python Projects
# Description: Working with variables in Python to manage user's input data. 
# ======================


def main():
    print("Welcome to the Band Name Generator")

    # Get user input for city and pet name
    city = input("Which city did you grow up in?\n")
    pet = input("What is the name of a pet?\n")

    # Combine the city and pet name to create a band name
    print("Your band name could be: " + city + " " + pet)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
