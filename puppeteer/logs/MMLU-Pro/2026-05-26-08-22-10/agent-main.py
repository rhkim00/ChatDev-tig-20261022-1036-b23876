import math
import json

def calculate_binomial_lattice(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility, steps):
    # Calculate the up and down factors
    up_factor = math.exp((risk_free_rate + volatility**2/2) * time_to_maturity + volatility * math.sqrt(time_to_maturity))
    down_factor = 1 / up_factor

    print(f"Up Factor: {up_factor}")
    print(f"Down Factor: {down_factor}")

    # Calculate the probability of an up move
    probability = (math.exp(risk_free_rate * time_to_maturity) - down_factor) / (up_factor - down_factor)
    print(f"Probability of an up move: {probability}")

    # Create a 2D array to represent the binomial lattice
    lattice = [[0 for _ in range(steps+1)] for _ in range(steps+1)]

    # Initialize the lattice with the current stock price
    lattice[0][0] = stock_price

    # Calculate the stock prices at each node in the lattice
    for i in range(steps):
        for j in range(i+1):
            up_price = lattice[i][j] * up_factor
            down_price = lattice[i][j] * down_factor
            lattice[i+1][j] = up_price
            lattice[i+1][j+1] = down_price

    # Calculate the option prices at each node in the lattice
    for i in range(steps, -1, -1):
        for j in range(i, -1, -1):
            if i == steps:
                # If we're at the final time step, the option price is the maximum of the stock price and the strike price
                lattice[i][j] = max(lattice[i][j] - strike_price, 0)
            else:
                # Otherwise, the option price is the maximum of the stock price and the strike price, discounted by the risk-free rate
                lattice[i][j] = max(lattice[i][j] - strike_price, 0) * (1 + risk_free_rate) / (1 + volatility)

    # Return the option price at the initial node in the lattice
    return lattice[0][0]

# Define the parameters
stock_price = 12
strike_price = 14
time_to_maturity = 10/12  # 10 months is equivalent to 10/12 years
risk_free_rate = 0.10
volatility = 0.20
steps = 10  # The distance between nodes on the tree is 1 month, so we need 10 steps for 10 months

# Calculate the option price
option_price = calculate_binomial_lattice(stock_price, strike_price, time_to_maturity, risk_free_rate, volatility, steps)

# Print the result in JSON format
print(json.dumps({"action": "run_python", "parameter": f"calculate_binomial_lattice({stock_price}, {strike_price}, {time_to_maturity}, {risk_free_rate}, {volatility}, {steps})", "result": option_price}))