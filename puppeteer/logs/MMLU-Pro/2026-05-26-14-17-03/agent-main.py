def calculate_markup(cost, selling_price):
    markup = ((selling_price - cost) / cost) * 100
    return markup

# Given values
floor_goods_cost = 200
floor_goods_selling_price = 250
total_purchase_cost = 1500

# Calculate markup on floor goods
markup_floor_goods = calculate_markup(floor_goods_cost, floor_goods_selling_price)
print(f"Markup percentage on floor goods is: {markup_floor_goods:.2f}%")

# Calculate remaining purchase cost
remaining_purchase_cost = total_purchase_cost - floor_goods_cost
print(f"Remaining purchase cost after floor goods: ${remaining_purchase_cost}")

# Calculate required markup on remaining purchase
required_markup = calculate_markup(remaining_purchase_cost, total_purchase_cost - floor_goods_cost) * 100
print(f"Required markup percentage on balance of purchases is: {required_markup:.2f}%")