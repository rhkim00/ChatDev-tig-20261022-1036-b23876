price_per_cleaner = 32.50
commission_rate = 0.25
num_cleaners_sold = 14
total_accessories_supplies = 237.40

total_cleaners_income = num_cleaners_sold * price_per_cleaner
commission_income = total_accessories_supplies * commission_rate
total_income = total_cleaners_income + commission_income

print("Total income from cleaners: $", total_cleaners_income)
print("Commission from accessories and supplies: $", commission_income)
print("Total income: $", total_income)