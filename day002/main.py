# ======================
# Project Name: Day 2 - Tip Calculator
# Section: Beginner Python Projects
# Description: Understanding data types and manipulate strings in Python to perform calculations based on user input.
# ======================

def main():
    print("Welcome to the tip calculator!")

    # Get user input for bill total, tip percentage, and number of people
    sub_total = float(input("What was the total bill?\n$"))
    tip = int(input("How much tip would you like to give? $10, $12, or $15?\n"))
    people = int(input("How many people to split the bill?\n"))

    # Calculate the total bill including tip and how much each person should pay
    tip_amount = sub_total * (tip / 100)
    total_bill = sub_total + tip_amount
    pay_per_person = total_bill / people

    print(f"Each person should pay: ${pay_per_person:.2f}")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()