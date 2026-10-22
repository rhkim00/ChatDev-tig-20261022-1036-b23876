import math
principal = 500
rate = 0.08
time = 5
n = 4
future_value = principal * (1 + rate/n) ** (n*time)

print("Principal amount:", principal)
print("Annual interest rate:", rate)
print("Time in years:", time)
print("Number of times interest is compounded per year:", n)
print("Future value:", future_value)