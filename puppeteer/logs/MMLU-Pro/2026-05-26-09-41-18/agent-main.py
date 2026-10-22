def calculate_depreciation():
    # Initial cost of the bicycle
    initial_cost = 80
    print(f'Initial cost of the bicycle: ${initial_cost}')
    
    # Selling price after 4 years
    selling_price = 15
    print(f'Selling price after 4 years: ${selling_price}')
    
    # Calculate the total depreciation
    total_depreciation = initial_cost - selling_price
    print(f'Total depreciation: ${total_depreciation}')
    
    # Calculate the annual depreciation by the straight line method
    annual_depreciation = total_depreciation / 4
    print(f'Annual depreciation: ${annual_depreciation:.2f}')
    
    # Calculate the annual rate of depreciation
    annual_rate = (annual_depreciation / initial_cost) * 100
    print(f'Annual rate of depreciation: {annual_rate:.2f}%')

# Run the function
calculate_depreciation()