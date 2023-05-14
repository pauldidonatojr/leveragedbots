def calculate_percentage_gain(entry_price, exit_price):
    percentage_gain = (exit_price - entry_price) / entry_price * 100
    return round(percentage_gain, 2)

# Prompt user for input
entry_price = float(input("Enter the entry price: "))
exit_price = float(input("Enter the exit price: "))

percentage_gain = calculate_percentage_gain(entry_price, exit_price)
print("Percentage Gain: {:.2f}%".format(percentage_gain))
