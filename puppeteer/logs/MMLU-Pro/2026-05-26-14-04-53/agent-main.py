import math

# Given values
initial_cost = 4500
scrap_value = 450
expected_life_hours = 11250
hours_used = 478

print(f"Initial cost: ${initial_cost}")
print(f"Scrap value: ${scrap_value}")
print(f"Expected life hours: {expected_life_hours} hours")
print(f"Hours used: {hours_used} hours")

# Calculate total depreciation
total_depreciation = initial_cost - scrap_value
print(f"Total depreciation: ${total_depreciation}")

# Calculate depreciation rate per hour
depreciation_rate_per_hour = total_depreciation / expected_life_hours
print(f"Depreciation rate per hour: ${depreciation_rate_per_hour:.2f}")

# Calculate depreciation charge for the month
depreciation_charge = depreciation_rate_per_hour * hours_used
print(f"The depreciation charge for the month is: ${depreciation_charge:.2f}")