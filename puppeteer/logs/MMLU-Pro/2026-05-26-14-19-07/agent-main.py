def calculate_annual_interest_rate(purchase_price, monthly_payment, months):
    # Calculate the total amount paid
    total_amount_paid = monthly_payment * months
    print(f"Total amount paid: ${total_amount_paid:.2f}")
    
    # Calculate the annual interest rate
    annual_interest_rate = ((total_amount_paid - purchase_price) / purchase_price) / months * 12
    print(f"Annual interest rate calculated: {annual_interest_rate:.2f}")
    
    return annual_interest_rate * 100

# Define the variables
purchase_price = 720
monthly_payment = 47.20
months = 18

# Calculate the annual interest rate
annual_interest_rate = calculate_annual_interest_rate(purchase_price, monthly_payment, months)

print(f"The annual interest rate is {annual_interest_rate:.2f}%")