# Define the assessed value and tax rates
assessed_value = 16500
tax_rates = {
    "local college fund": 0.41,
    "special education": 0.02,
    "health and welfare": 0.001,
    "community construction": 0.089
}

# Calculate the total tax
total_tax = (assessed_value * 0.22) * 0.01
print("Total tax calculated.")

# Calculate the tax for each need
taxes = {}
for name, rate in tax_rates.items():
    taxes[name] = (assessed_value * 0.22 * rate) * 0.01

# Print the results
print("Tax for each need:")
for name, tax in taxes.items():
    print(f"{name}: ${tax:.2f}")
print(f"Total tax: ${total_tax:.2f}")