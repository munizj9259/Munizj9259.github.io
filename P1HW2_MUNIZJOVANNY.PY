# Name: Jovanny Muniz
# Date: 09/27/2025
# Assignment Name: P1HW2
# Description: Program that calculates and displays travel expenses

# Ask for user inputs
print("This program calculates and displays travel expenses")

budget = int(input("\nEnter budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

# Calculate total and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display results
print("\n-----Travel Expenses-----")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print()
print(f"Fuel: {gas}")
print(f"Accommodation: {accommodation}")
print(f"Food: {food}")
print()
print(f"Remaining Balance: {remaining_balance}")