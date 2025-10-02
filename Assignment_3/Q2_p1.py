import control
import numpy as np

A = np.pi* (0.15/2)**2
R1 = 12e6 # MPas/m^3
R2 = 105e6 # MPas/m^3
C = 4.5e-3*1e-6 #m^3/MPa
m = 8 #kg

n1 = A/(R1*C)
d2 = (R1+R2)/(R1*R2*C)
d3 = A**2/(m*C)

P = control.tf([n1,0],[1,d2,d3])

T = 0.01
Pd = P.sample(T, method='zoh')

print(Pd)