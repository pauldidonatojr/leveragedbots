# Import the necessary functions
from calculate_percentage import calculate_percentage_gain
from profits_calculator import profits_calculator
# Add more imports as needed

# Prompt user for input
user_input = int(input("Enter a value: "))

# Call the imported function based on user input
if user_input == 1:
    calculate_percentage_gain()
elif user_input == 2:
    profits_calculator()
# Add more cases for other values and functions as needed
else:
    print("Invalid input.")
