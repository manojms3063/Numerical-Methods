from datetime import datetime as dt
import time

#NUMERICAL INTEGRAL 

import numpy as np
import math 
import sympy as smp

# Trapizoidal Rule 

# x = smp.symbols('x')
# dydx = math.sin(x)
# f = smp.lambdify([x],dydx)  

a = 0
b = math.pi/2
n = 6
x0 = 0
h = (b-a)/n

def f(x):
    return math.sin(x)
y = np.empty(n+1)
y[0]=f(a)
y[n]=f(b)
t_i=dt.now()
i=1
sum = h*(y[0]+y[n])/2
while i<n:
    y[i] = f(x0+i*h)
    sum =  sum + h*y[i]
    i+=1
print(y)
print(sum)
t_f=dt.now()
print('\ncost of computation:',t_f-t_i)