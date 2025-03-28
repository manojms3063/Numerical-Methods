import numpy as np
import sympy as smp
from sympy import symbols,diff
import math

# Runge Kutta  2nd Order (1st order Linear ODE)

x=symbols('x')
y=symbols('y')

dydx = (x-y)/2
fxy = smp.lambdify([x,y],dydx)  
h = 0.1
# h = float(input("Enter Step Size (h) = "))
a = 0
# a = float(input("Enter start point (a) = "))
b = 0.2
# b = float(input("Enter end point (b) = "))
x0 = 0
# x0 = float(input("Enter inital value (x0) = "))
y0 = 1
# y0 = float(input("Enter inital value (y0) = "))
r = 0.2
# r = float(input("Enter the value where the value to be find (r) = "))

n = int((b-a)/h)
y=np.empty(n+1)
x=np.empty(n+1)
d=np.empty(3)
x[0]=x0
y[0]=y0

i=0

while i<n:
    d[1] = h*fxy(x[i],y[i])
    d[2] = h*fxy(x[i]+h,y[i]+d[1])

    y[i+1]=y[i]+(1/2)*(d[1]+d[2])        
    x[i+1]=x[i]+h
    i+=1
print('x=',x)
print('y=',y)
m = np.where(x==r)[0]
print(f"y({r})=",y[m]) 