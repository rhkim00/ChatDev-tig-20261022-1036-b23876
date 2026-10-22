import math

def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate/n) ** (n*time)

def main():
    principal = 2000
    rate1 = 0.04
    time1 = 3
    n1 = 4
    rate2 = 0.05
    time2 = 2
    n2 = 2

    balance1 = calculate_compound_interest(principal, rate1, time1, n1)
    balance2 = calculate_compound_interest(balance1, rate2, time2, n2)

    interest = balance2 - principal

    print(f"Balance after first period: ${balance1:.6f}")
    print(f"Final balance: ${balance2:.6f}")
    print(f"Interest earned: ${interest:.6f}")

if __name__ == "__main__":
    main()