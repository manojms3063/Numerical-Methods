from datetime import datetime as dt
import time

#NUMERICAL INTEGRAL 

import numpy as np
import math 
import sympy as smp

# # # simpson's 3/8

a = 0
b = 1
n = 6
x0 = a
h = (b-a)/n

def f(x):
    return 1/(1+x)
y = np.empty(n+1)
y[0]=f(a)
y[n]=f(b)
i=1
sum = y[0] + y[n]
p=0
q=0
t_i=dt.now()
while i<n:
    y[i] = f(x0+i*h)
    if i%3==0:
        p+=2*(y[i])
    else:
        q+=3*(y[i])
    i+=1

print(y)
sum =  (3*h/8)*(sum + p+q)
print(f"\nthe value of the given integral by Simpson's is \n {sum}")
t_f=dt.now()
print('\ncost of computation:',t_f-t_i)
