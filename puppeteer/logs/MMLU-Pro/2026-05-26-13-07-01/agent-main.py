def calculate_financing_charge(total_cost, down_payment, monthly_payment, num_payments):
    # Total amount paid
    total_amount_paid = down_payment + (monthly_payment * num_payments)
    print('Total amount paid: $', total_amount_paid)

    # Financing charge
    financing_charge = total_cost - total_amount_paid
    print('Financing charge: $', financing_charge)

    return financing_charge

print('The financing charge is: $', calculate_financing_charge(250, 25, 20, 12))