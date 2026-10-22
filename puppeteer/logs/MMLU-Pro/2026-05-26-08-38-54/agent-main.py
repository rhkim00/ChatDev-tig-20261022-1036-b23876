def calculate_cost():
    # Define the prices
    magee_data_high = 23 + 1/8
    magee_data_low = 22 + 5/8
    giant_industrials_high = 24 + 1/4
    giant_industrials_low = 23 + 1/2

    # Define the number of shares purchased
    magee_data_shares = 300
    giant_industrials_shares = 400

    # Calculate the cost of Magee Data shares
    magee_data_cost = magee_data_shares * magee_data_high
    print('Cost of Magee Data shares: $', magee_data_cost)

    # Calculate the cost of Giant Industrials shares
    giant_industrials_cost = giant_industrials_shares * giant_industrials_low
    print('Cost of Giant Industrials shares: $', giant_industrials_cost)

    # Calculate the total cost
    total_cost = magee_data_cost + giant_industrials_cost
    print('Total cost of the purchase is: $', total_cost)

    return total_cost

print('The cost of the purchase is: $', calculate_cost())