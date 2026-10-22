def calculate_depreciation(initial_value, rate, years):
    # Calculate the depreciation rate as a decimal
    depreciation_rate = rate / 100
    print(f"Depreciation rate: {depreciation_rate}")

    # Calculate the book value after each year
    book_value = initial_value
    for _ in range(years):
        book_value *= (1 - depreciation_rate)
    print(f"Book value after {years} years: ${book_value:.2f}")
    
    return book_value

# Define the initial value and depreciation rate
initial_value = 1950
depreciation_rate = 15
years = 3

# Calculate the book value
book_value = calculate_depreciation(initial_value, depreciation_rate, years)

# Print the result
print(f"The book value of the cage after {years} years is: ${book_value:.2f}")