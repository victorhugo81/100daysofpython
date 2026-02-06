def main():
    print("Welcome to the tip calculator!")

    bill = float(input("What was the total bill?\n$"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
    people = int(input("How many people to split the bill?\n"))

    tip_amount = bill * (tip / 100)
    total_bill = bill + tip_amount
    bill_per_person = total_bill / people

    print(f"Each person should pay: ${bill_per_person:.2f}")

if __name__ == "__main__":
    main()