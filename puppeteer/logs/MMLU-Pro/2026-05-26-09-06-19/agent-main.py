fixed_cost = 140000
cost_per_item = 0.75
selling_price = 1.25

items_to_break_even = fixed_cost / (selling_price - cost_per_item)
sales_revenue = items_to_break_even * selling_price

print(f'Fixed cost: ${fixed_cost}')
print(f'Cost per item: ${cost_per_item}')
print(f'Selling price: ${selling_price}')
print(f'Items to break even: {int(items_to_break_even)}')
print(f'Sales revenue at break even point: ${int(sales_revenue)}')