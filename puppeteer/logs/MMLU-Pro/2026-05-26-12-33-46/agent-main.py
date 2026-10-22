import math

def calculate_premiums(policy_type, age, amount):
    # Calculate the annual premium for a 20-payment life policy
    annual_premium_20_payment = amount * (1 + 0.06) ** 20 / ((1 + 0.06) ** 20 - 1)
    
    # Calculate the annual premium for an ordinary life paid-up-at 65 policy
    annual_premium_ordinary_life = amount * (1 + 0.06) ** 65 / ((1 + 0.06) ** 65 - 1)
    
    # Calculate the difference in annual premiums
    difference_in_premiums = annual_premium_ordinary_life - annual_premium_20_payment
    
    return round(difference_in_premiums, 2)

def calculate_total_paid(policy_type, age, amount, years):
    # Calculate the total amount paid for a 20-payment life policy
    total_paid_20_payment = amount
    
    # Calculate the total amount paid for an ordinary life paid-up-at 65 policy
    total_paid_ordinary_life = amount * (1 + 0.06) ** years / ((1 + 0.06) ** 65 - 1)
    
    return round(total_paid_20_payment, 2), round(total_paid_ordinary_life, 2)

# Input values
age = 30
amount = 15000
years = 62

# Calculate the difference in annual premiums
difference_in_premiums = calculate_premiums('20-payment life', age, amount)
print("Difference in annual premiums: $", difference_in_premiums)

# Calculate the total amount paid for each policy
total_paid_20_payment, total_paid_ordinary_life = calculate_total_paid('20-payment life', age, amount, years)
print("Total paid for 20-payment life policy: $", total_paid_20_payment)
print("Total paid for ordinary life paid-up-at 65 policy: $", total_paid_ordinary_life)