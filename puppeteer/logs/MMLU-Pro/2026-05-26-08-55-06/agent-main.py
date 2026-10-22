list_price = 32
discount_rate = 0.3
discount_amount = list_price * discount_rate
net_cost = list_price - discount_amount

print(f"The list price of the tape recorder is: ${list_price:.2f}")
print(f"The discount rate applied is: {discount_rate:.2f}")
print(f"The discount amount is: ${discount_amount:.2f}")
print(f"The net cost of the tape recorder is: ${net_cost:.2f}")