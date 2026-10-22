import numpy as np

# Define the revenue function
def revenue(x):
  return 3 * x**2

# Define the profit function
def profit(x):
  return 2 * x**2 - 5 * x + 1

# Define the cost function (cost = revenue - profit)
def cost(x):
  return revenue(x) - profit(x)

# Calculate the cost accrued over a three year period
cost_three_years = cost(3)
print(f"Cost accrued over a three year period: ${cost_three_years:.2f} million")

# Calculate the rate of change of cost of production by the end of the third year
rate_of_change = 2 * 3  # Since the cost function is quadratic, the rate of change is twice the coefficient of x
print(f"Rate of change of cost of production by the end of the third year: ${rate_of_change} million")