def profits_calculator(entry_price, exit_price, contract_size, num_contracts):
    profit = (exit_price - entry_price) * contract_size * num_contracts
    return profit

# Prompt user for input
entry_price = float(input("Enter the entry price: "))
exit_price = float(input("Enter the exit price: "))
contract_size = float(input("Enter the contract size: "))
num_contracts = int(input("Enter the number of contracts: "))

profit = profits_calculator(entry_price, exit_price, contract_size, num_contracts)
print("Profit: $", profit)
