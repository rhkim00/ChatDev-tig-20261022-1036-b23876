def calculate_insurance_payment(policy_value, house_value, loss, coinsurance_clause):
    # Calculate the minimum value required by the coinsurance clause
    min_value = (house_value / 100) * coinsurance_clause
    print("Minimum value required by coinsurance clause:", min_value)
    
    # Check if the policy value meets the minimum requirement
    if policy_value < min_value:
        print("Policy value does not meet the minimum requirement.")
        return "Error"
    
    # Calculate the insurance payment
    payment = (loss / house_value) * policy_value
    print("Calculated insurance payment:", payment)
    
    return payment

# Given values
policy_value = 36000
house_value = 45000
loss = 10500
coinsurance_clause = 80

# Calculate the insurance payment
payment = calculate_insurance_payment(policy_value, house_value, loss, coinsurance_clause)

if payment is not "Error":
    print("The insurance company will pay: $", round(payment, 2))