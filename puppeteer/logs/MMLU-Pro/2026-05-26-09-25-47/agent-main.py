def calculate_cost():
    # Define the prices of the motors
    motor_a_price = 169
    motor_b_price = 149
    print(f"Motor A price: {motor_a_price}")
    print(f"Motor B price: {motor_b_price}")

    # Define the annual inspection and maintenance fee
    inspection_fee = 0.145
    print(f"Annual inspection and maintenance fee: {inspection_fee}")

    # Define the efficiency of the motors
    motor_a_efficiency = 0.852
    motor_b_efficiency = 0.821
    print(f"Motor A efficiency: {motor_a_efficiency}")
    print(f"Motor B efficiency: {motor_b_efficiency}")

    # Define the cost of electric energy
    energy_cost = 0.0235
    print(f"Cost of electric energy: {energy_cost}")

    # Calculate the cost of running the motors per hour
    motor_a_cost_per_hour = (motor_a_price * inspection_fee + (1 - motor_a_efficiency) * 746 * energy_cost) / 1000
    motor_b_cost_per_hour = (motor_b_price * inspection_fee + (1 - motor_b_efficiency) * 746 * energy_cost) / 1000
    print(f"Motor A cost per hour: {motor_a_cost_per_hour}")
    print(f"Motor B cost per hour: {motor_b_cost_per_hour}")

    # Calculate the number of hours per year at which the cost of both motors will be the same
    hours_per_year = (motor_b_price * inspection_fee - motor_a_price * inspection_fee) / (motor_a_cost_per_hour - motor_b_cost_per_hour)

    return hours_per_year

# Run the function and print the result
result = calculate_cost()
print(f"The number of hours per year at which the cost of both motors will be the same is: {result}")