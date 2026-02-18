# ======================
# Project Name: Day 6 - Python Age Calculator
# Section: Beginner Python Projects
# Description: Python while loops, dates and time
# ======================


from datetime import datetime


def birthdate():
    while True:
        birth_input = input("Enter your birthdate (MM/DD/YYYY) or 'q' to quit: ")

        if birth_input.lower() == 'q':
            print("Exiting program.")
            break

        try:
            birthdate = datetime.strptime(birth_input, "%m/%d/%Y")
        except ValueError:
            print("Error: Wrong format. Please use MM/DD/YYYY.")
            continue  # Ask again

        now = datetime.now()
        time_in_between = now - birthdate
        total_days = time_in_between.days
        total_seconds = int(time_in_between.total_seconds())
        total_hours = total_seconds // 3600
        total_minutes = total_seconds // 60

        # Calculate years and months manually
        years = now.year - birthdate.year
        months = now.month - birthdate.month
        days = now.day - birthdate.day

        if days < 0:
            months -= 1
        if months < 0:
            years -= 1
            months += 12

        total_months = years * 12 + months
        formatted_birthdate = birthdate.strftime("%B %d, %Y")

        print(f"\nIf you were born on {formatted_birthdate}, you have lived:")
        print(f"Total Years: {years:,}")
        print(f"Total Months: {total_months:,}")
        print(f"Total Days: {total_days:,}")
        print(f"Total Hours: {total_hours:,}")
        print(f"Total Minutes: {total_minutes:,}")
        print(f"Total Seconds: {total_seconds:,}\n")




# Run the game
if __name__ == "__main__":
    birthdate()