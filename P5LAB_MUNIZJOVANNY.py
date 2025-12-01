# Jovanny Muniz
# 11/30/2025
# P5LAB – Self-Checkout Simulation
# This program simulates a self-checkout machine, calculates change,
# and outputs the number of dollars, quarters, dimes, nickels, and pennies.

import random

# ---------------------------------------
# FUNCTION: disperse_change(amount)
# Takes 1 float (amount of change owed)
# Prints dollars, quarters, dimes, nickels, pennies
# ---------------------------------------
def disperse_change(change):
    # Convert float to cents to avoid float precision issues
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")


# ---------------------------------------
# MAIN FUNCTION
# ---------------------------------------
def main():
    # Generate random purchase amount
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${amount_owed}")

    # Prompt user for cash input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change}")

    # Call function
    disperse_change(change)


# ---------------------------------------
# Call main function
# ---------------------------------------
main()