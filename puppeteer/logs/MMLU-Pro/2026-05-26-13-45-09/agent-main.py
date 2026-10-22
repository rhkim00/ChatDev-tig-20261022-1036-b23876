invoice_amount = 7000
discount_percentage = 2
discount_days = 10
payment_days = 13

if payment_days <= discount_days:
    print("Invoice Amount:", invoice_amount)
    print("Discount Percentage:", discount_percentage)
    print("Discount Days:", discount_days)
    print("Payment Days:", payment_days)
    
    discount = (invoice_amount * discount_percentage) / 100
    print("Discount:", discount)
    print("Amount Paid:", invoice_amount - discount)
    
else:
    print("Amount Paid:", invoice_amount)