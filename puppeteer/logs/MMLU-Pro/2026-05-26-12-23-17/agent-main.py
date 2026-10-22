import math

def calculate_compound_interest(principal, rate, time, n):
    amount = principal * (1 + rate/n) ** (n*time)
    return amount

principal = 0  # initial deposit
rate = 0.08 / 12  # 8% annual interest rate, compounded monthly
time = 5 * 12  # 5 years in months
n = 12  # monthly compounding

deposit = 500
total_principal = deposit * time
amount = calculate_compound_interest(total_principal, rate, time, n) + deposit * math.pow((1 + rate), time)

print(f"Initial deposit: ${principal:.2f}")
print(f"Annual interest rate: {rate*12*100:.2f}%")
print(f"Time in years: {time/12}")
print(f"Number of compounding periods per year: {n}")
print(f"Deposit amount: ${deposit}")
print(f"Total principal: ${total_principal}")
print(f"The final amount after {time/12} years will be: ${amount:.2f}")