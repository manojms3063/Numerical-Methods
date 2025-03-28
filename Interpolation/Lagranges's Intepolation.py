from datetime import datetime as dt

import numpy as np
import sympy as smp
from sympy import symbols,simplify
import math   

# lagrange
x = np.array([0,1,2,4,5])
y = np.array([0,16,48,88,0])
a=symbols('a')
i=0
n=len(x)
b=0
t_i = dt.now()
while i < n-1:
    p=1
    j=0
    while j < n-1:
    # for j in range(n):
        if i!=j:
            p=p*(a-x[j])/(x[i]-x[j])
        j+=1
    b+=y[i]*p
    i+=1
    poly= smp.lambdify(a,b)
t_f = dt.now()
print('The cost of computation is:\n',t_f-t_i)
print(f'poly:\n',poly)
print('The interpolating polynomial is : \n',simplify(b), '\nThe value of the function is:\n',poly(3))
