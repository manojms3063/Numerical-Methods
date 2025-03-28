import numpy as np 
import math 
import sympy as smp
from sympy import symbols ,Eq,solve
import matplotlib.pyplot as plt
from datetime import datetime as dt

# straight line Fitting 

def f(a,b,p):
    return a*p + b

a = symbols("a")
b = symbols("b")

    
x = np.array([1,2,3,4,6,8])
y = np.array ([2.4,3.1,3.5,4.2,5,6])
n = len(x)
q1= np.zeros(n)

print("Number of data points = ",n)
t_i=dt.now()
Ex = sum(x)
print("Ex=",Ex)
Ey = sum(y)
print("Ey =", Ey)
Exy = np.dot(x,y)
print("Exy=",Exy)
Ex2 =np.dot(x,x)
print("Ex2 =",Ex2)

eq1 = Eq((a*Ex+b*n),Ey)
eq2 = Eq((a*Ex2+b*Ex),Exy)
print(eq1) 
print(eq2) 
m = solve((eq1, eq2), (a, b))
# print(m)
a = m[a]
b = m[b]
print("a =", a)
print("b =",b)
print("The best fit straight line is y = (",a,") x +(",b,")")
t_f=dt.now()
print('\ncost of computation:',t_f-t_i)

for i in range(n):
    q1[i] = f(a,b,x[i])
    
print(q1)
print(x)

plt.scatter(x, y, label= "stars", color= "red", 
            marker= "o", s=50)
plt.plot(x,q1,color='g', linewidth =1)
plt.title("Curve plotted using  the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()