# Regula Falsi Method - 
from math import log
def f (x):
    return x**3-2*x-5

a = int(input("enter the initial  "))
b = int(input("enter the initial  "))
n = int(input("no of iteration  "))
i = 1
while i<=n:
    r = (a*f(b)-b*f(a))/(f(b)-f(a))
    if f(r)>0:
        print(f'Iteration{i}: approximation:',r)
        i+=1
        b = r
    elif f (r)<0:
        print(f'Iteration{i}: approximation:',r)
        i+=1
        a = r