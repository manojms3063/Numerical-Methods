import numpy as np
import sympy as smp
from sympy import symbols,diff
import math


# Runge Kutta  4th Order (1st order linear ODE)

x=symbols('x')
y=symbols('y')

dydx = x+y
fxy = smp.lambdify([x,y],dydx)  
h = 2
# h = float(input("Enter Step Size (h) = "))
a = 0
# a = float(input("Enter start point (a) = "))
b = 2
# b = float(input("Enter end point (b) = "))
x0 = 0
# x0 = float(input("Enter inital value (x0) = "))
y0 = 0
# y0 = float(input("Enter inital value (y0) = "))
r = 2
# r = float(input("Enter the value where the value to be find (r) = "))



n = int((b-a)/h)
print(n)
y=np.empty(n+1)
x=np.empty(n+1)
d=np.empty(5)

x[0]=x0
y[0]=y0

i=0

while i<n:

    d[1] = h*fxy(x[i],y[i])
    d[2] = h*fxy(x[i]+h/2 , y[i]+d[1]/2)
    d[3] = h*fxy(x[i]+h/2 , y[i]+d[2]/2)
    d[4] = h*fxy(x[i]+h , y[i]+d[3])

    y[i+1]=y[i]+(1/6)*(d[1]+2*d[2]+2*d[3]+d[4])        

    x[i+1]=x[i]+h
    i+=1
print(d[1])
print(d[2])
print(d[3])
print(d[4])
print('x=',x)
print('y=',y)

m = np.where(x==r)[0]
print(f"y({r})=",y[m]) 