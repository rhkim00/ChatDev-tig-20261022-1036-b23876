def calculate_true_rate(principal, rate, time):
    # Calculate the discount
    discount = principal / (1 - (1 - rate/100)**time)
    print(f"Discount amount: {discount}")

    # Calculate the true rate of interest
    true_rate = (discount - principal) / principal * 100
    print(f"True rate of interest: {true_rate}%")
    
    return true_rate

# Test the function
principal = 1000  # Initial amount
time = 1  # Time in years
rate1 = 6  # Discount rate 1
rate2 = 8  # Discount rate 2

true_rate1 = round(calculate_true_rate(principal, rate1, time), 1)
true_rate2 = round(calculate_true_rate(principal, rate2, time), 1)

print(f"True rate of interest for {rate1}% discount rate: {true_rate1}%")
print(f"True rate of interest for {rate2}% discount rate: {true_rate2}%")