# Define the quantities and costs of the motor oil
quantities = [130, 100, 180, 120]
costs = [0.36, 0.365, 0.40, 0.425]

print("Quantities of motor oil:", quantities)
print("Costs of motor oil:", costs)

# Calculate the total quantity
total_quantity = sum(quantities)
print("Total quantity of motor oil:", total_quantity)

# Calculate the total cost
total_cost = sum([quantity * cost for quantity, cost in zip(quantities, costs)])
print("Total cost of motor oil:", total_cost)

# Calculate the average cost
average_cost = total_cost / total_quantity
print("Average cost of motor oil:", average_cost)

# Calculate the total value of the motor oil in inventory
total_value = average_cost * 150
print(f"The total value of the motor oil in inventory is: ${total_value:.2f}")