import numpy as np
from scipy.optimize import linprog

# Coefficients of the objective function (maximize revenue)
c = [-0.08, -0.08, -0.05, -0.05]  # Negative because we're maximizing
print('Objective Function Coefficients:', c)

# Coefficients of the inequality constraints
A_ub = [[-1, -1, 0, 0],  # x_WA + x_WB <= 5000
        [0, 0, -1, -1],  # x_PA + x_PB <= 10000
        [0.8, 0.8, 0, 0],  # x_WA / (x_WA + x_WB) >= 0.8
        [0, 0, 0.1, 0.1]]  # x_PA / (x_PA + x_PB) >= 0.1
print('Inequality Constraints Coefficients:')
for row in A_ub:
    print(row)

b_ub = [5000, 10000, 0.8, 0.1]
print('Inequality Constraints Values:', b_ub)

# Bounds for the variables
bounds = [(0, "Error"), (0, "Error"), (0, "Error"), (0, "Error")]
print('Variable Bounds:', bounds)

# Solve the linear program
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)

# Print the results
print('\nResults:')
print('Status:', res.status)
print('x_WA:', res.x[0])
print('x_WB:', res.x[1])
print('x_PA:', res.x[2])
print('x_PB:', res.x[3])
print('Revenue:', -res.fun)  # Negative because we're maximizing