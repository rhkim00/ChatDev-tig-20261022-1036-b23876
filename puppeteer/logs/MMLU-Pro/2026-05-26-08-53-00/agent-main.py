# Define the balance sheet information
cash = 3390
notes_receivable = 2905
accounts_receivable = 8215
merchandise_inventory = 23600
store_supplies = 720
store_fixtures = 2895
furniture_and_equipment = 5600
notes_payable = 5250
accounts_payable = 4800

# Calculate total assets
total_assets = cash + notes_receivable + accounts_receivable + merchandise_inventory + store_supplies + store_fixtures + furniture_and_equipment - notes_payable - accounts_payable

# Print the total assets
print("Total assets: ", total_assets)

# Return the result in JSON format
import json
result = {"total_assets": total_assets}
print(json.dumps(result))