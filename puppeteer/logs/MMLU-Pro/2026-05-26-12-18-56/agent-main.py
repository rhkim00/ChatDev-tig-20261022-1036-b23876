import datetime

# Define the variables
draft_date = datetime.date(2023, 7, 11)
discount_date = datetime.date(2023, 8, 2)
face_value = 544.20
discount_rate = 0.04
discount_term = 3 / 12  # Convert months to years
discount_rate_2 = 0.05
collection_fee = 0.125 / 100  # Convert 1/8% to decimal

# Calculate the discount
discount = face_value * discount_rate * discount_term
print(f"The discount is: ${discount:.2f}")

# Calculate the proceeds before collection fee
proceeds_before_fee = face_value - (face_value * discount_rate_2) - discount
print(f"The proceeds before collection fee are: ${proceeds_before_fee:.2f}")

# Calculate the proceeds after collection fee
proceeds = proceeds_before_fee - (proceeds_before_fee * collection_fee)
print(f"The proceeds after collection fee are: ${proceeds:.2f}")