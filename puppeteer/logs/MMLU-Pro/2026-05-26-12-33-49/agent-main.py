import math

def calculate_equivalent_annual_cost(initial_cost, salvage_value, annual_costs, life, interest_rate):
    # Calculate the present value of the costs
    present_value = 0
    for i in range(life):
        present_value += annual_costs[i] / (1 + interest_rate) ** (i + 1)

    # Calculate the equivalent annual cost
    equivalent_annual_cost = (initial_cost - salvage_value + present_value) / life

    return equivalent_annual_cost

# Define the costs for the gasoline pump
gasoline_initial_cost = 3500
gasoline_salvage_value = 500
gasoline_annual_costs = [2000]
for i in range(1, 6):
    gasoline_annual_costs.append(gasoline_annual_costs[i - 1] + 300)

# Define the costs for the electric pump
electric_initial_cost = 12000
electric_salvage_value = 1000
electric_annual_costs = [1000]
for i in range(1, 6):
    electric_annual_costs.append(electric_annual_costs[i - 1] + 150)

# Define the interest rate
interest_rate = 0.1

# Calculate the equivalent annual costs
gasoline_equivalent_annual_cost = calculate_equivalent_annual_cost(gasoline_initial_cost, gasoline_salvage_value, gasoline_annual_costs, 6, interest_rate)
electric_equivalent_annual_cost = calculate_equivalent_annual_cost(electric_initial_cost, electric_salvage_value, electric_annual_costs, 6, interest_rate)

# Print the results
print("Gasoline pump equivalent annual cost: $", round(gasoline_equivalent_annual_cost, 2))
print("Electric pump equivalent annual cost: $", round(electric_equivalent_annual_cost, 2))

if gasoline_equivalent_annual_cost < electric_equivalent_annual_cost:
    print("The gasoline pump is more economical.")
elif gasoline_equivalent_annual_cost > electric_equivalent_annual_cost:
    print("The electric pump is more economical.")
else:
    print("Both pumps have the same costs.")