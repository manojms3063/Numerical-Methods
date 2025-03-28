import numpy as np
import sympy as smp
from sympy import symbols,diff
import math


# Modified Euler's method


x=symbols('x')
y=symbols('y')
dydx = 1 +y**2
f = smp.lambdify([x,y],dydx)  
h = 0.1
# h = float(input("Enter Step Size (h) = "))
a = 0
# a = float(input("Enter start point (a) = "))
b = 1
# b = float(input("Enter end point (b) = "))
x0 = 0
# x0 = float(input("Enter inital value (x0) = "))
y0 = 0
# y0 = float(input("Enter inital value (y0) = "))
r = 0.2
# r = float(input("Enter the value where the value to be find (r) = "))

n=int((b-a)/h)

x=np.empty(n+1)
y=np.empty(n+1)
x[0]=x0 
y[0]=y0 

for i in range(n):
    y[i+1] = y[i]+h*f(x[i],y[i])
    x[i+1] = x[i]+h
    
print(f"y{i+1}* = ", y)

j = 2
while j <n:
    y[j+1] = y[j] + (h/2)*(f(x[j],y[j])+ f(x[j+1],y[j+1]))
    x[j+1] = x[j]+h
    j+=1 

print("x=",x)
print("y= ", y)
m = np.where(x==0.2)[0]
# print(m)
print(f"y({r}) = ",y[m])