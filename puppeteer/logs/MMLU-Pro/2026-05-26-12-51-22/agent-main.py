price = 69.75
discount_percentage = 5
state_sales_tax_percentage = 3
city_sales_tax_percentage = 4

# Calculate discount
discount = (price / 100) * discount_percentage
price_after_discount = price - discount

print("Discount amount: $", round(discount, 2))
print("Price after discount: $", round(price_after_discount, 2))

# Calculate sales tax
state_sales_tax = (price_after_discount / 100) * state_sales_tax_percentage
city_sales_tax = (price_after_discount / 100) * city_sales_tax_percentage
total_sales_tax = state_sales_tax + city_sales_tax

print("State sales tax: $", round(state_sales_tax, 2))
print("City sales tax: $", round(city_sales_tax, 2))
print("Total sales tax: $", round(total_sales_tax, 2))

# Calculate total price
total_price = price_after_discount + total_sales_tax

print("The total price Jim paid for the cleaner is: $", round(total_price, 2))