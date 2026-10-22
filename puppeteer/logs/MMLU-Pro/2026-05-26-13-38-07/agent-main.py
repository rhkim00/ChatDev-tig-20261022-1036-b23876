import json

def calculate_compound_interest(principal, rate, years, compounding_frequency):
    # Convert the interest rate from percentage to decimal
    rate = rate / 100
    print(f"Interest rate (decimal): {rate}")

    # Calculate the compound interest
    amount = principal * (1 + rate/compounding_frequency)**(compounding_frequency*years)
    print(f"Amount after {years} years: {amount}")

    return amount

def run_python():
    principal = 30000
    rate = 1.8
    years = 6
    compounding_frequency = 1  # Compounded annually

    amount = calculate_compound_interest(principal, rate, years, compounding_frequency)
    print(f"Principal amount: {principal}")
    print(f"Interest rate: {rate}%")
    print(f"Number of years: {years}")
    print(f"Compounding frequency: {compounding_frequency}")

    result = {
        "action": "run_python",
        "parameter": f"calculate_compound_interest({principal}, {rate}, {years}, {compounding_frequency})",
        "result": amount
    }

    return json.dumps(result)

print(run_python())