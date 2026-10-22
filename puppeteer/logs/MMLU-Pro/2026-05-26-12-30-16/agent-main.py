import numpy as np

P = 20
A = 0

Q = (20 - P)*(1 + 0.1*A - 0.01*A**2)
print("Q =", Q)

C = 10*Q + 15 + A
print("C =", C)

Q_opt = Q.subs({P: 20, A: 0})
print("Q_opt =", Q_opt)