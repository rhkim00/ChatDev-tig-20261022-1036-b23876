initial_cost = 4000
salvage_value = 400
total_miles = 72000
miles_year1 = 20000
miles_year2 = 25000
miles_year3 = 18000
miles_year4 = 9000

depreciation_per_mile = (initial_cost - salvage_value) / total_miles
print(f"Depreciation per mile: ${depreciation_per_mile:.2f}")

depreciation_year1 = depreciation_per_mile * miles_year1
depreciation_year2 = depreciation_per_mile * miles_year2
depreciation_year3 = depreciation_per_mile * miles_year3
depreciation_year4 = depreciation_per_mile * miles_year4

print(f"Depreciation for Year 1: ${depreciation_year1:.2f}")
print(f"Depreciation for Year 2: ${depreciation_year2:.2f}")
print(f"Depreciation for Year 3: ${depreciation_year3:.2f}")
print(f"Depreciation for Year 4: ${depreciation_year4:.2f}")

total_depreciation = depreciation_year1 + depreciation_year2 + depreciation_year3 + depreciation_year4
print(f"Total depreciation: ${total_depreciation:.2f}")