import json

# Define the interest rates and tax rates
interest_rates = {
    'A': 0.045,
    'B': 0.035,
    'C': 0.05,
    'D': 0.06,
    'E': 0.06,
    'F': 0.05,
    'G': 0.055,
    'H': 0.05,
    'I': 0.03,
    'J': 0.04
}
tax_rate = 0.5

# Calculate the net return for each option
net_returns = {}
for option, interest_rate in interest_rates.items():
    net_return = interest_rate * (1 - tax_rate)
    net_returns[option] = net_return
    print(f"Net return for option {option}: {net_return}")

# Find the option with the highest net return
max_net_return = max(net_returns.values())
best_option = [option for option, net_return in net_returns.items() if net_return == max_net_return][0]

# Print the result
print("Information about the best option:")
print(f"Interest Rate for the best option: {interest_rates[best_option]}")
print(f"Tax Rate: {tax_rate}")
print(f"Best Option: {best_option}")
print(json.dumps({'Interest Rate': interest_rates[best_option], 'Tax Rate': tax_rate, 'Best Option': best_option}))