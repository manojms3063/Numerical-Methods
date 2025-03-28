import numpy as np
import sympy as smp
from sympy import symbols,diff
import math

# Runge Kutta 4th Order Method ( 2nd Order Linear ODE)


x=symbols('x')
y=symbols('y')
z=symbols("z")

dydx= (x+y)/z
f = smp.lambdify([x,y,z],dydx)   
dzdx = (x*y) + z
g = smp.lambdify([x,y,z],dzdx) 
h = 0.1
# h = float(input("Enter Step Size (h) = "))
a = 0
# a = float(input("Enter start point (a) = "))
b = 0.6
# b = float(input("Enter end point (b) = "))
x0 = 0.5
# x0 = float(input("Enter inital value (x0) = "))
y0 = 1.5
# y0 = float(input("Enter inital value (y0) = "))
z0 = 1.5
# z0 = float(input("Enter inital value (z0) = "))
r = 0.6
# r = float(input("Enter the value where the value to be find (r) = "))
 
n = int((b-a)/h)

y=np.empty(n+1)
x=np.empty(n+1)
z=np.empty(n+1)
x[0] = x0
y[0] = y0
z[0] = z0


k=np.empty(5)
l = np.empty(5)
i = 0
while i<n:

    k[1] = h*f(x[i],y[i],z[i])
    l[1] = h*g(x[i],y[i],z[i])
    
    k[2] = h*f(x[i]+h/2,y[i]+k[1]/2,z[i]+l[1]/2)
    l[2] = h*g(x[i]+h/2,y[i]+l[1]/2,z[i]+l[1]/2)
    
    k[3] = h*f(x[i]+h/2,y[i]+k[2]/2,z[i]+l[2]/2)
    l[3] = h*g(x[i]+h/2,y[i]+l[2]/2,z[i]+l[2]/2)
    
    k[4] = h*f(x[i]+h,y[i]+k[3],z[i]+l[3])
    l[4] = h*g(x[i]+h,y[i]+l[3],z[i]+l[3])
    
    y[i+1]=y[i]+(1/6)*(k[1]+2*k[2]+2*k[3]+k[4])
    z[i+1]=z[i]+(1/6)*(l[1]+2*l[2]+2*l[3]+l[4])        
    x[i+1]=x[i]+h
    i+=1

print('x=',x)
print('y=',y)
print('z=',z)

m = np.where(x==r)[0]
print(f"y({b})=",y[m])
print(f"z({b})=",z[m])