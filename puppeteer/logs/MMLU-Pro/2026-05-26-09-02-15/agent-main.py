import math

def calculate_monthly_payment(principal, months):
    monthly_interest_rate = 0.01
    monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)
    print(f'Principal amount: ${principal}')
    print(f'Number of months: {months}')
    print(f'Monthly interest rate: {monthly_interest_rate}')
    print(f'Monthly payment calculation:')
    print(f'Principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** months) / ((1 + monthly_interest_rate) ** months - 1)')
    print(f'Monthly payment: ${round(monthly_payment, 2)}')
    return round(monthly_payment, 2)

principal = 3462.20
months = 35
monthly_payment = calculate_monthly_payment(principal, months)
print(f'The monthly payment is: ${monthly_payment}')