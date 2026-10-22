def calculate_stock_turn_rate(cost_price, selling_price, opening_inventory, closing_inventory, sales):
    # Calculate cost of goods sold
    cost_of_goods_sold = (sales * cost_price) / selling_price
    print("Cost of Goods Sold:", cost_of_goods_sold)
    
    # Calculate stock turn rate at cost
    stock_turn_rate_cost = (opening_inventory + closing_inventory) / 2 / (cost_of_goods_sold / (opening_inventory + closing_inventory))
    print("Stock Turn Rate (at Cost):", stock_turn_rate_cost)
    
    # Calculate stock turn rate at selling price
    stock_turn_rate_selling_price = (opening_inventory + closing_inventory) / 2 / (sales / (opening_inventory + closing_inventory))
    print("Stock Turn Rate (at Selling Price):", stock_turn_rate_selling_price)
    
    # Calculate stock turn rate in units
    stock_turn_rate_units = sales / (opening_inventory + closing_inventory)
    print("Stock Turn Rate (in Units):", stock_turn_rate_units)
    
    return stock_turn_rate_cost, stock_turn_rate_selling_price, stock_turn_rate_units

# Given data
cost_price_initial = 60000 / 90000
selling_price_initial = 80000 / 90000
opening_inventory_initial = 90000
cost_price_final = 90000 / 70000
selling_price_final = 120000 / 70000
closing_inventory_final = 70000
sales = 360000

# Calculate stock turn rates
stock_turn_rate_cost, stock_turn_rate_selling_price, stock_turn_rate_units = calculate_stock_turn_rate(cost_price_initial, selling_price_initial, opening_inventory_initial, closing_inventory_final, sales)

# Return results as JSON
print("{{\"Stock Turn Rate (at Cost)\":", stock_turn_rate_cost, ", \"Stock Turn Rate (at Selling Price)\":", stock_turn_rate_selling_price, ", \"Stock Turn Rate (in Units)\":", stock_turn_rate_units, "}}")