# Newtons backward interpolation 

import numpy as np
import sympy as smp
from sympy import symbols,simplify
import math 

# def u_cal(u,n):
#     prod = 1
#     for i in range(n+1):
#         prod = prod*(u-i)
#     return prod
# peogram of fatorial notation 
# here we can alos use this formula - 
def u_cal(u,n):
    prod = 1
    
    for i in range(1,n):
        prod = prod*(u+i-1)
    return prod

x = np.array([1891,1901,1911,1921,1931])
y = np.array([46,66,81,93,101]) 
n = len(x)
h = x[1]-x[0]
# n = int(input("Enter number of Data Point (n) = "))
# x = np.empty(n)
# y = np.empty(n)

# x[0] = float(input("Enter initial term of x data (x0) = "))
# h = float(input("Enter step size of x data (h) = "))

# for i in range(1,n):
    # x[i] = x[i-1]+h
    
# print("x = ",x)    
# for i in range(0,n):
    # y[i]= float(input(f"Y values y{i+1} = "))
# print("y= f(x) =",y)    
# 
# p = float(input("enter the interpolating value (x) = "))
p = 1930
u = symbols('u')
dy = np.zeros([n,n+1])

for k in range(n):
    dy[k][0] = dy[k][0]+x[k]
    dy[k][1]= dy[k][1]+y[k]
print(dy)

j =2
while j<n+1:
    i = n-1
    a=j-1
    while i>a-1:
        dy[i][j] = dy[i][j-1]-dy[i-1][j-1]
        i-=1
    a-=1
    j+=1        
print(dy)  

# for j in range(2,n+1):
    # sum = dy[0][j]
    
sum = dy[n-1][1]   
for i in range(2,n+1):
        sum = sum+(u_cal(u,i)*dy[n-1][i])/math.factorial(i-1)

poly = smp.lambdify(u,sum)  
print("sum=",sum)
u=(p-x[n-1])/h
print("u =",u) 
print("The value of interpolation for",p,"is",poly(u))
print("Interpolating polunomial is", simplify(sum))
