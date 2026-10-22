def calculate_balance_due(invoice_amount, partial_payment, discount_rate):
    # Calculate the discount
    discount = partial_payment * (discount_rate / 100)
    print(f'Discount calculated: ${discount:.2f}')

    # Calculate the balance due
    balance_due = invoice_amount - partial_payment + discount
    print(f'Balance due calculated: ${balance_due:.2f}')

    return balance_due, discount

invoice_amount = 190.55
partial_payment = 90.00
discount_rate = 2

balance_due, discount = calculate_balance_due(invoice_amount, partial_payment, discount_rate)

print(f'Balance due: ${balance_due:.2f}')
print(f'Discount: ${discount:.2f}')

result = {'balance_due': round(balance_due, 2), 'discount': round(discount, 2)}

print(result)