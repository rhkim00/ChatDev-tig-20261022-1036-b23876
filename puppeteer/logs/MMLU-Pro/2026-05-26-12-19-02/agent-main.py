import math

def calculate_stock_value(current_dividend, growth_rate, years, final_growth_rate, expected_rate_of_return):
    print("Calculating stock value...")
    
    present_value = 0
    for year in range(years):
        dividend = current_dividend * (1 + growth_rate) ** (year + 1)
        present_value += dividend / (expected_rate_of_return - growth_rate)
    
    present_value += current_dividend * (1 + growth_rate) ** years / (expected_rate_of_return - final_growth_rate)
    
    print("Stock value calculation completed.")
    return present_value

current_dividend = 12
growth_rate = 0.20
years = 4
final_growth_rate = 0.08
expected_rate_of_return = 0.15

stock_value = calculate_stock_value(current_dividend, growth_rate, years, final_growth_rate, expected_rate_of_return)

print('The fair value of the stock is:', stock_value)