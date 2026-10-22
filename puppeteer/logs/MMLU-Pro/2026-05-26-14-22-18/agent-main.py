def calculate_payment(principal, annual_interest_rate, years, monthly_payment):
    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = years * 12
    remaining_balance = principal
    prepayment_penalty = 0
    total_amount = 0

    for _ in range(number_of_payments):
        interest = remaining_balance * monthly_interest_rate
        remaining_balance -= monthly_payment
        remaining_balance += interest
        if remaining_balance < 0:
            prepayment_penalty = remaining_balance
            remaining_balance = 0
        total_amount += monthly_payment

    print('Monthly payment: $', round(monthly_payment, 2))
    print('Remaining balance after', years, 'years: $', round(remaining_balance, 2))
    print('Prepayment penalty: $', round(prepayment_penalty, 2))
    print('Total amount Mr. Tencer has to pay: $', round(total_amount, 2))

principal = 10000
annual_interest_rate = 0.06
years = 10
monthly_payment = 111.02
calculate_payment(principal, annual_interest_rate, years, monthly_payment)