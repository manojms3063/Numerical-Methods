#Secant Method - 
from math import log
def f (x):
    return x**3-2*x-5

a = int(input("enter the initial  "))
b = int(input("enter the initial  "))
n = int(input("no of iteration  "))
i = 1
while i<=n:
    r = b-((b-a)*f(b)/(f(b)-f(a)))
    print(f'Iteration{i}: approximation:',r)
    a = b
    b = r
    i = i+1