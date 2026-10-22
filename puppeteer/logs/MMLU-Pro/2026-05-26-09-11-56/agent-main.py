def calculate_break_even_point(C, R):
    # Define the cost and revenue functions
    def cost(x):
        return C[0]*x + C[1]
    
    def revenue(x):
        return R[0]*x + R[1]
    
    # Calculate the break-even point
    x = (C[1] - R[1]) / (R[0] - C[0])
    
    return x

# Test the function with the given data
data = [
    {"C": [10, 600], "R": [30, 0]},
    {"C": [5, 200], "R": [8, 0]},
    {"C": [0.2, 50], "R": [0.3, 0]},
    {"C": [1800, 3000], "R": [2500, 0]}
]

for i, d in enumerate(data):
    print(f"Break-even point for problem {i+1}:")
    x = calculate_break_even_point(d["C"], d["R"])
    print(f"x = {x:.2f} units")
    print()