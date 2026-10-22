import numpy as np

S0 = 0.5
r = 0.03
sigma = 0.2
alpha = -1
T = 1

mu = r - 0.5 * sigma**2
expected_S1 = S0 * np.exp((mu + 0.5 * sigma**2) * T)
print('Expected value of the stock price at time 1:', expected_S1)

time_0_price = expected_S1 ** alpha * np.exp(-r * T)
print('Time-0 price of the contingent claim:', time_0_price)