import math

# Initial amount
P = 5000
print("Initial amount:", P)

# Final amount
A = 13000
print("Final amount:", A)

# Time in years
n = 12
print("Time in years:", n)

# Calculate interest rate using the formula for compound interest
r = (A / P) ** (1 / n) - 1

# Convert interest rate to a decimal between 0 and 1
r = r / 100

print("The interest rate is:", r)