principal = 2000
interest_rate = 0.06
days = 143
years = days / 365
exact_interest = principal * interest_rate * years
bankers_interest = principal * interest_rate * int(years)
difference = exact_interest - bankers_interest

print(f'Principal: ${principal}')
print(f'Interest Rate: {interest_rate}')
print(f'Days: {days}')
print(f'Years: {years:.2f}')
print(f'Exact Interest: ${exact_interest:.2f}')
print(f'Bankers Interest: ${bankers_interest:.2f}')
print(f'The difference in interest is: ${difference:.2f}')