# Define the variables
price = 82
finance_charge = 0.10
months = 6

# Calculate the monthly interest rate
monthly_interest_rate = finance_charge / 12
print(f"Monthly interest rate: {monthly_interest_rate:.2f}")

# Calculate the total amount to be paid
total_amount = price * (1 + monthly_interest_rate * months)
print(f"Total amount to be paid: ${total_amount:.2f}")

# Calculate the monthly payment
monthly_payment = total_amount / months
print(f"The monthly payment should be: ${monthly_payment:.2f}")