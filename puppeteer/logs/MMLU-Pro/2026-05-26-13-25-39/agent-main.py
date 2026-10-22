def calculate_principal():
    # Given values
    interest_rate = 0.06  # 6% interest rate
    interest_charge = 36  # Interest charge on the loan
    days = 90  # Loan duration in days

    print("Interest Rate: ", interest_rate)
    print("Interest Charge: $", interest_charge)
    print("Loan Duration (days): ", days)

    # Calculate principal using the formula: Interest = Principal * Rate * Time
    principal = interest_charge / (interest_rate * (days / 365))

    return principal

principal = calculate_principal()
print("The principal of the loan is: $", round(principal, 2))