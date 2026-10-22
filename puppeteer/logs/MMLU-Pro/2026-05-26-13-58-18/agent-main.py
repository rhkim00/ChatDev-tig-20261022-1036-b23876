import math

def calculate_annuity_payout():
    # Savings phase parameters
    savings_per_quarter = 1000
    savings_duration_years = 30
    savings_interest_rate = 0.06
    savings_compounding_frequency = 4

    # Annuity payout phase parameters
    payout_duration_years = 25
    payout_interest_rate = 0.048
    payout_compounding_frequency = 12

    # Calculate total savings
    total_savings = 0
    for year in range(savings_duration_years):
        for quarter in range(4):
            total_savings += savings_per_quarter * (1 + savings_interest_rate / savings_compounding_frequency) ** (quarter * savings_duration_years * savings_compounding_frequency + year * savings_compounding_frequency)
    
    print(f"Total savings accumulated: ${total_savings}")

    # Calculate monthly annuity payout
    monthly_payout = total_savings * (payout_interest_rate / payout_compounding_frequency) / ((1 + payout_interest_rate / payout_compounding_frequency) ** (payout_duration_years * payout_compounding_frequency) - 1)

    print(f"Monthly annuity payout calculated: ${monthly_payout}")

    return round(monthly_payout, 2)

# Execute the function
monthly_payout = calculate_annuity_payout()
print(f"The monthly retirement annuity payout is: ${monthly_payout}")