import json

# Define the options
options = {
    "A": {"Taxes payable": "Liability section", "Capital stock": "Owner's Equity section", "Retained earnings": "Owner's Equity section", "Administrative expense": "Income Statement", "Prepaid expenses": "Asset side"},
    "B": {"Taxes payable": "Owner's Equity section", "Capital stock": "Asset side", "Retained earnings": "Income Statement", "Administrative expense": "Liability section", "Prepaid expenses": "Liability section"},
    "C": {"Taxes payable": "Asset side", "Capital stock": "Liability section", "Retained earnings": "Income Statement", "Administrative expense": "Owner's Equity section", "Prepaid expenses": "Income Statement"},
    "D": {"Taxes payable": "Owner's Equity section", "Capital stock": "Liability section", "Retained earnings": "Asset side", "Administrative expense": "Asset side", "Prepaid expenses": "Income Statement"},
    "E": {"Taxes payable": "Income Statement", "Capital stock": "Liability section", "Retained earnings": "Asset side", "Administrative expense": "Owner's Equity section", "Prepaid expenses": "Owner's Equity section"},
    "F": {"Taxes payable": "Owner's Equity section", "Capital stock": "Income Statement", "Retained earnings": "Asset side", "Administrative expense": "Asset side", "Prepaid expenses": "Liability section"},
    "G": {"Taxes payable": "Liability section", "Capital stock": "Asset side", "Retained earnings": "Liability section", "Administrative expense": "Income Statement", "Prepaid expenses": "Income Statement"},
    "H": {"Taxes payable": "Income Statement", "Capital stock": "Owner's Equity section", "Retained earnings": "Income Statement", "Administrative expense": "Liability section", "Prepaid expenses": "Asset side"},
    "I": {"Taxes payable": "Asset side", "Capital stock": "Income Statement", "Retained earnings": "Liability section", "Administrative expense": "Owner's Equity section", "Prepaid expenses": "Liability section"},
    "J": {"Taxes payable": "Liability section", "Capital stock": "Owner's Equity section", "Retained earnings": "Owner's Equity section", "Administrative expense": "Income Statement", "Prepaid expenses": "Asset side"}
}

# Define the questions
questions = [
    {"Taxes payable": "A", "Capital stock": "B", "Retained earnings": "C", "Administrative expense": "D", "Prepaid expenses": "E"},
    {"Taxes payable": "B", "Capital stock": "A", "Retained earnings": "E", "Administrative expense": "C", "Prepaid expenses": "D"},
    {"Taxes payable": "C", "Capital stock": "D", "Retained earnings": "A", "Administrative expense": "E", "Prepaid expenses": "B"},
    {"Taxes payable": "D", "Capital stock": "E", "Retained earnings": "B", "Administrative expense": "A", "Prepaid expenses": "C"},
    {"Taxes payable": "E", "Capital stock": "C", "Retained earnings": "D", "Administrative expense": "B", "Prepaid expenses": "A"},
    {"Taxes payable": "F", "Capital stock": "E", "Retained earnings": "D", "Administrative expense": "C", "Prepaid expenses": "B"},
    {"Taxes payable": "G", "Capital stock": "F", "Retained earnings": "E", "Administrative expense": "A", "Prepaid expenses": "C"},
    {"Taxes payable": "H", "Capital stock": "G", "Retained earnings": "F", "Administrative expense": "B", "Prepaid expenses": "D"},
    {"Taxes payable": "I", "Capital stock": "H", "Retained earnings": "G", "Administrative expense": "C", "Prepaid expenses": "E"},
    {"Taxes payable": "J", "Capital stock": "I", "Retained earnings": "H", "Administrative expense": "D", "Prepaid expenses": "A"}
]

# Create the output
output = []
for question in questions:
    answer = {}
    for key, value in question.items():
        answer[key] = options[value][key]
    output.append(answer)

# Print the output in JSON format
print("Output:")
print(json.dumps(output, indent=4))