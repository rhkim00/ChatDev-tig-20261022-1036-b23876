def calculate_radio_price():
    # Given information
    original_price = 38.00
    excise_tax_rate = 0.03
    sales_tax_rate = 0.04
    down_payment = 10.00
    payment_amount = 11.60
    num_payments = 3

    # Calculate total taxes
    excise_tax = original_price * excise_tax_rate
    sales_tax = original_price * sales_tax_rate
    total_taxes = excise_tax + sales_tax

    # Calculate cash price
    cash_price = original_price + total_taxes

    # Calculate total installment price
    total_installment_price = down_payment + (num_payments * payment_amount)

    # Calculate installment price
    installment_price = total_installment_price - (total_taxes - excise_tax)

    # Print the calculated values
    print("Cash price: $", round(cash_price, 2))
    print("Installment price: $", round(installment_price, 2))

    # Return the results as a dictionary
    return {
        "cash_price": round(cash_price, 2),
        "installment_price": round(installment_price, 2)
    }

# Run the function and print the results
result = calculate_radio_price()
print(result)