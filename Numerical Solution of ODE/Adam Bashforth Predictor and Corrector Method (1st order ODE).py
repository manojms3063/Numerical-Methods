import numpy as np
import sympy as smp
from sympy import symbols,diff
import math

# Adam Bashforth Predictor and Corrector Method (1st order ODE)

x = symbols("x")
y = symbols("y")
dydx = x-y**2
f = smp.lambdify([x,y],dydx)

a = 0
b = 0.8
x0 = 0
y0 = 0
r = 0.8
h = float((b-a)/4)
y1 = 0.02
y2 = 0.0795
y3 = 0.176

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
y4 = y[3]+h/24*(55*dy[3]-59*dy[2]+37*dy[1]-9*dy[0])
print("P(y4)=",y4)
dy4 = f(x[4],y4)
# print("P(dy4)=",dy4)

#milne corrector formula - 
y4 = y[3]+h/24*(9*dy4+19*dy[3]-5*dy[2]+dy[1])
print("C(y4)=",y4)