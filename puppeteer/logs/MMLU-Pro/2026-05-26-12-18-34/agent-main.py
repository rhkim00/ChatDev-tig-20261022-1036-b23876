def calculate_book_value(cost, trade_in_value, years):
    # Calculate the total depreciation
    total_depreciation = cost - trade_in_value
    print(f"Total depreciation: ${total_depreciation:.2f}")
    
    # Calculate the sum of the years' digits
    sum_of_years_digits = sum(range(1, years + 1))
    print(f"Sum of years' digits: {sum_of_years_digits}")
    
    # Calculate the book value
    book_value = (total_depreciation / sum_of_years_digits) * sum(range(years, 0, -1))
    print(f"Book value: ${book_value:.2f}")
    
    return book_value

# Define the cost and trade-in value
cost = 15500
trade_in_value = 2600

# Define the number of years
years = 5

# Calculate the book value at the end of the first three years
book_value = calculate_book_value(cost, trade_in_value, 3)

print(f"The book value at the end of the first three years is: ${book_value:.2f}")