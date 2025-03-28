import numpy as np
import sympy as smp
from sympy import symbols,diff
import math


# Milne Predictor and Corrector Method (1st order ODE)

x = symbols("x")
y = symbols("y")
dydx = x*y + y**2
f = smp.lambdify([x,y],dydx)

a = 0
b = 0.4
x0 = 0
y0 = 1
r = 0.4
h = float((b-a)/4)
print(h)
y1 = 1.1169
y2 = 1.2774
y3 = 1.5041

y = np.array([y0,y1,y2,y3])
print("y=",y)
x = np.empty(5)

for i in range(5):
    x[i] = x0 + i*h
print("x=",x)

dy = np.empty(4)

for i in range(4):
    dy[i] = f(x[i],y[i])
print("dy = ",dy)

#milne predictor formula - 
y4 = y[0]+4*h/3*(2*dy[1]-dy[2]+2*dy[3])
print("P(y4)=",y4)
dy4 = f(x[4],y4)
# print("P(dy4)=",dy4)|

#milne corrector formula - 
y4 = y[2]+h/3*(dy[2]+4*dy[3]+dy4)
print("C(y4)=",y4)
