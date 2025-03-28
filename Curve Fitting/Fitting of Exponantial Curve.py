import numpy as np 
import math 
import sympy as smp
from sympy import symbols ,Eq,solve
import matplotlib.pyplot as plt
from datetime import datetime as dt

# Fitting of Exponential Curve - 

def f(a,b,p):
    return b*math.e**((a)*p)

a = symbols("a")
b = symbols("b0")


x = np.array([1,2,3,4,5,6])
Y = np.array ([1.6,4.5,13.8,40.8,125,300])
n = len(x)
y = np.zeros(n)
y =  [math.log(i) for i in Y]

# print(y)


q1= np.zeros(n)

print("Number of data points = ",n)

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
print("b0 =",b)
b = math.e**b
print("b =",b)
print("The best fit of exponantial curve is y =(,",b,")e^(",a,")x")


for i in range(n):
    q1[i] = f(b,a,x[i])
    
print(q1)
print(x)

plt.scatter(x, Y, label= "stars", color= "red", 
            marker= "o", s=50)
plt.plot(x,q1,color='g', linewidth =1)
plt.title("Curve plotted using  the given points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()