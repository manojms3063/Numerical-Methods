import numpy as np
import sympy as smp
from sympy import symbols,diff
import math

# # tylor series method 


x = smp.symbols('x')
y = smp.symbols('y')

dydx = -2*x*y
f = smp.lambdify([x,y],dydx)

d2ydx2 = -2*y + 4*x**2 * y 
df = smp.lambdify([x,y],d2ydx2)
# print(d2ydx2)

h = 0.2 
# h = float(input("Enter Step Size (h) = "))
a = 0
# a = float(input("Enter start point (a) = "))
b = 1
# b = float(input("Enter end point (b) = "))
x0 = 0
# x0 = float(input("Enter inital value (x0) = "))
y0 = 1
# y0 = float(input("Enter inital value (y0) = "))
r = 2
# r = float(input("Enter the value where the value to be find (r) = "))
 
n = int((b-a)/h)
print(n)
x=np.empty(n+1)
x[0] = x0
y=np.empty(n+1)
y[0] = y0

i = 1
while i < n:
    y[i] = f(x[i],y[i]) + h * f(x[i],y[i]) + (h**2 / 2) * df(x[i],y[i])
    x[i]=x[i-1]+h
    i+=1

print(x)
print(y)

m = np.where(x==r)[0]
print(f"y({b})=",y[m])