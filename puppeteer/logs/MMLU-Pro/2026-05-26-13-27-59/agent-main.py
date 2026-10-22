PMT = 1000
r = 0.05
n = 12
t = 5

FV = PMT * (((1 + r/n)**(n*t)) - 1) / (r/n)

print("PMT:", PMT)
print("r:", r)
print("n:", n)
print("t:", t)
print("Future Value (FV):", FV)