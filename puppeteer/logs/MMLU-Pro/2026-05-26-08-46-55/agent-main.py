def calculate_rental_cost(days, miles, gallons, extra_hours):
    # Define the costs per unit
    cost_per_day = 32
    cost_per_mile = 0.22
    cost_per_gallon = 0.445
    cost_per_extra_hour = 2.75

    # Calculate the total cost
    total_cost = (cost_per_day * days) + (cost_per_mile * miles) + (cost_per_gallon * gallons) + (cost_per_extra_hour * extra_hours)

    return total_cost

# Define the input values
days = 5  # Assuming 5 days
miles = 516
gallons = 54
extra_hours = 17

# Calculate the total cost
total_cost = calculate_rental_cost(days, miles, gallons, extra_hours)

# Print the input values
print("Days rented:", days)
print("Miles driven:", miles)
print("Gallons used:", gallons)
print("Extra hours rented:", extra_hours)

# Print the total cost
print("The total cost of the rental is: $", round(total_cost, 2))