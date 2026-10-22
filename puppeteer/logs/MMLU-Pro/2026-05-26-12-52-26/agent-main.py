# Define the insurance rates for Class A and Class B towns
class_a_rate = 0.0005  # 0.05%
class_b_rate = 0.001  # 0.1%

# Define the insurance amount
insurance_amount = 24000

# Calculate the insurance premium for Class A town
class_a_premium = insurance_amount * class_a_rate
print(f"The insurance premium for Class A town is: ${class_a_premium:.2f}")

# Calculate the insurance premium for Class B town
class_b_premium = insurance_amount * class_b_rate
print(f"The insurance premium for Class B town is: ${class_b_premium:.2f}")

# Calculate the difference in insurance premiums
difference = class_b_premium - class_a_premium
print(f"The difference in insurance premiums is: ${difference:.2f}")