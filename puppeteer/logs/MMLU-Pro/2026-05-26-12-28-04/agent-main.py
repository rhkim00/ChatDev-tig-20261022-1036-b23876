import math

def calculate_average_rate_of_change(i1, i2):
    rate_of_change = (i2 - i1) / (2 * math.sqrt(i1 * i2))
    print(f"Initial values: {i1}, {i2}")
    print(f"Average rate of change: {rate_of_change}")

calculate_average_rate_of_change(25, 100)
calculate_average_rate_of_change(25, 225)