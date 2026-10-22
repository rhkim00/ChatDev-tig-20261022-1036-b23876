
# Given values
i = 0.005  # 5(1/2)% = 4
n = 10  # Assuming n = 10 for demonstration purposes

# Calculate factors
usca, cr, uspw = calculate_factors(i, n)

# Return results in JSON format
result = {
    "USCA": round(usca, 4),
    "CR": round(cr, 4),
    "USPW": round(uspw, 4)
}
print(result)