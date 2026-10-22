def calculate_monthly_earnings(yearly_earnings):
    monthly_earnings = yearly_earnings / 12
    print(f"Yearly earnings: ${yearly_earnings}")
    print(f"Monthly earnings: ${monthly_earnings:.2f}")
    return monthly_earnings

yearly_earnings = 5400
monthly_earnings = calculate_monthly_earnings(yearly_earnings)
print(f"The Wilsons receive ${monthly_earnings:.2f} each month.")