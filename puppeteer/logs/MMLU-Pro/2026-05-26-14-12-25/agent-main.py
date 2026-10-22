# Define the prices and quantities of the purchases
prices = [33.9, 32.9, 31.9, 29.9]
quantities = [10, 14, 12, 8]

# Calculate the total cost and total gallons
total_cost = 0
total_gallons = 0
for i in range(len(prices)):
    total_cost += prices[i] * quantities[i]
    total_gallons += quantities[i]

print(f"Total cost of purchases: ${total_cost}")
print(f"Total gallons purchased: {total_gallons} gallons")

# Calculate the average cost per gallon
average_cost = total_cost / total_gallons

# Round the average cost to the nearest tenth of a cent
average_cost = round(average_cost, 1)

# Print the result
print(f"The average cost per gallon is {average_cost} cents.")