# Define the tax rates for corporations and individuals
corporate_tax_rates = {
    20000: 0.02,
    40000: 0.04,
    80000: 0.06,
    320000: 0.07,
    320000: 0.07
}

individual_tax_rates = {
    20000: 0.03,
    40000: 0.05,
    80000: 0.07,
    320000: 0.07,
    320000: 0.07
}

# Define the income and tax rates
income_before_taxes = 30000
income_from_other_sources = 12000
increase_in_income_before_taxes = 10000

# Calculate the total income before taxes
total_income_before_taxes = income_before_taxes + income_from_other_sources + increase_in_income_before_taxes
print("Total income before taxes: $", total_income_before_taxes)

# Calculate the tax for the corporation
tax_for_corporation = 0
for income in range(20000, total_income_before_taxes + 1, 20000):
    if income <= 20000:
        tax_for_corporation += income * corporate_tax_rates[income]
    else:
        tax_for_corporation += 20000 * corporate_tax_rates[20000]
        tax_for_corporation += (income - 20000) * corporate_tax_rates[40000]

print("Tax for the corporation: $", round(tax_for_corporation, 2))

# Calculate the tax for the individuals
tax_for_individuals = 0
for income in range(20000, total_income_before_taxes + 1, 20000):
    if income <= 20000:
        tax_for_individuals += income * individual_tax_rates[income]
    else:
        tax_for_individuals += 20000 * individual_tax_rates[20000]
        tax_for_individuals += (income - 20000) * individual_tax_rates[40000]

print("Tax for individuals: $", round(tax_for_individuals, 2))

# Calculate the total tax
total_tax = tax_for_corporation + tax_for_individuals
print("Total tax: $", round(total_tax, 2))

# Calculate the increase in stockholders' income after taxes
increase_in_stockholders_income_after_taxes = (increase_in_income_before_taxes - total_tax) / 2
print("The increase in stockholders' income after taxes is: $", round(increase_in_stockholders_income_after_taxes, 2))