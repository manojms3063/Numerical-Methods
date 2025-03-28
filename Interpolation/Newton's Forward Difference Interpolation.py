from datetime import datetime as dt

# Newtons Forward Interpolation 
import numpy as np
import sympy as smp
from sympy import symbols,simplify
import math 

# # def u_cal(u,n):
# #     prod = 1
# #     for i in range(n-1):
# #         prod = prod*(u-i)
# #     return prod
# # Program of fatorial notation 
# # here we can also use this formula -
 
def u_cal(u,n):
    prod = 1
    for i in range(1,n):
        prod = prod*(u-i+1)
    return prod

# x = np.array([80,85,90,95,100])
# y = np.array([5026,5674,6362,7088,7854])  
 
x = np.array ([1891,1901,1911,1921,1941])
y = np.array ([46,66,81,93,101])
n = len(x)
h = 10

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
p = 1895
# p = float(input("enter the interpolating value (x) = "))

u = symbols('u')
dy = np.zeros([len(x),len(x)+1])
for k in range(len(x)):
    # dy[k][0] = dy[k][0]+x[k]
    # dy[k][1]= dy[k][1]+y[k]
    dy[k][0] = x[k]
    dy[k][1]= y[k]
print(dy)
t_i=dt.now()
a = len(x)-1
j =2 
while j<len(x)+1:
    i = 0 
    while i<a:
        dy[i][j] = dy[i+1][j-1]-dy[i][j-1]
        i+=1
    a-=1
    j+=1        
print(dy)  

# for j in range(1,n+2):
    # sum = dy[0][j]
    

sum = dy[0][1]
# print(m)
for i in range(2,n+1):
    sum = sum + (u_cal(u,i)*dy[0][i])/math.factorial(i-1)
t_f=dt.now()
print('\ncost of computation:',t_f-t_i)
 
poly = smp.lambdify(u,sum)  
u =(p-x[0])/h
print(sum)
print("u =",u) 
print("The value of interpolation for",p,"is",poly(u))
print(f"sum = {sum}")
print("Interpolating polunomial is", simplify(sum))
