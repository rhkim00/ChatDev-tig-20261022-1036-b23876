def calculate_partner_shares(): 
    # Initial investments 
    kirk_initial_investment = 72000 
    martin_initial_investment = 63000 

    # Withdrawals and additional investments 
    kirk_withdrawal = 3000 
    martin_withdrawal = 1800 
    kirk_additional_investment = 1200 

    # Total profits 
    total_profits = 37080 

    # Calculate total investment for each partner 
    kirk_total_investment = kirk_initial_investment - kirk_withdrawal + kirk_additional_investment 
    martin_total_investment = martin_initial_investment - martin_withdrawal 

    # Calculate interest 
    interest_rate = 0.06 
    kirk_interest = kirk_total_investment * interest_rate 
    martin_interest = martin_total_investment * interest_rate 

    # Calculate remaining profits 
    remaining_profits = total_profits - (kirk_interest + martin_interest) 

    # Calculate shares 
    kirk_share = remaining_profits * (1/3) 
    martin_share = remaining_profits * (2/3) 

    # Calculate final shares including interest 
    kirk_final_share = kirk_interest + kirk_share 
    martin_final_share = martin_interest + martin_share 

    # Print results
    print("Kirk's total investment: $", kirk_total_investment)
    print("Martin's total investment: $", martin_total_investment)
    print("Kirk's share of total profits: $", round(kirk_final_share, 3)) 
    print("Martin's share of total profits: $", round(martin_final_share, 3))

    # Return results as JSON 
    return { 
        "action": "calculate_partner_shares", 
        "result": { 
            "Kirk's share of total profits": round(kirk_final_share, 3), 
            "Martin's share of total profits": round(martin_final_share, 3) 
        } 
    } 

# Run the function 
result = calculate_partner_shares() 
print(result)