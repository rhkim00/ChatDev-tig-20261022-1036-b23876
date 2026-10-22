import math

# Given values
principal = 45000
discount_rate = 0.06
days = 120

# Calculate the discount
discount = principal * discount_rate * (days / 360)
print(f'Discount: ${discount:.2f}')

# Calculate Mr. Atlas' proceeds
proceeds = principal - discount
print(f"Principal: ${principal}")
print(f"Discount Rate: {discount_rate}")
print(f"Days: {days}")
print(f'Mr. Atlas\' proceeds: ${proceeds:.2f}')