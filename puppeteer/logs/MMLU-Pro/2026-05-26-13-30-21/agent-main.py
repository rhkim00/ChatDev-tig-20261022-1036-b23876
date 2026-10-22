def calculate_discount_rate(original_price, discounted_price):
    discount_rate = ((original_price - discounted_price) / original_price) * 100
    print(f"Original Price: ${original_price}")
    print(f"Discounted Price: ${discounted_price}")
    print(f"Discount Rate Calculation: (({original_price} - {discounted_price}) / {original_price}) * 100")
    return discount_rate

original_price = 280
discounted_price = 196

discount_rate = calculate_discount_rate(original_price, discounted_price)
print(f"The discount rate is {discount_rate}%")