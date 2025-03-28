# Bisection method
import math
# from datetime import datetime
def f(x):
    return x**3-2*x-5
# x*(math.log(x))-1.2
    # return 3*math.sin(x)-2*x+5
    # return x**2+1
a = float(input("enter a : "))
b = float(input("enter b : "))
z = float(input(" enter the significant digit:"))
E=10**(-z)
n = (math.log(abs(b-a)/E))/math.log(2)
n= math.ceil(n)

print("number of Iteration = " , n)
# t_i = datetime.now()
i=0
while i<n:
    r = (a+b)/2
    if f(a)>0 and f(b)<0:
        if f(r)<0:
            b = r
            print(f'Iteration{i+1}: approximation:',r)        
        elif f(r)>0:
            a = r
            print(f'Iteration{i+1}: approximation:',r) 
    elif f(a)<0 and f(b)>0:
        if f(r)<0:
            a = r
            print(f'Iteration{i+1}: approximation:',r)        
        elif f(r)>0:
            b = r
            print(f'Iteration{i+1}: approximation:',r) 
    i+=1
# t_f = datetime.now()
# print(r)
# print("The cost of computtation = ",t_i-t_f)