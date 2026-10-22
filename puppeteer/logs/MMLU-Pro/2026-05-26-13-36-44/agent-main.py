# Define the assessed valuation and taxes
assessed_valuation = 52384600
taxes_new_local_project = 123475
taxes_educational_purposes = 931442.75
taxes_health_welfare_needs = 319878

# Calculate the total taxes
total_taxes = taxes_new_local_project + taxes_educational_purposes + taxes_health_welfare_needs
print(f'Total taxes: {total_taxes}')

# Calculate the tax rate in thousandths of a percent
tax_rate_thousandths_percent = (total_taxes / assessed_valuation) * 1000000
print(f'Tax rate (a) to thousandths of a percent: {tax_rate_thousandths_percent}')

# Calculate the tax rate in mills per $1 of assessed value
tax_rate_mills_per_dollar = (total_taxes / assessed_valuation) * 1000
print(f'Tax rate (b) in mills per $1 of assessed value: {tax_rate_mills_per_dollar}')

# Calculate the tax rate in cents per $100 of assessed value
tax_rate_cents_per_hundred = (total_taxes / assessed_valuation) * 100
print(f'Tax rate (c) in cents per $100 of assessed value: {tax_rate_cents_per_hundred}')

# Calculate the tax rate in mills per $1,000 of assessed value
tax_rate_mills_per_thousand = (total_taxes / assessed_valuation) * 1000
print(f'Tax rate (d) in mills per $1,000 of assessed value: {tax_rate_mills_per_thousand}')