# #newton raphson method
from math import sin
from math import cos
import sympy as smp
x = smp.symbols('x')
X = smp.symbols('X')
def f(x):
    return 2*x**3-2*x-5
a = float(input("Enter the initial value :"))
z = int(input("Enter no. of Significance degit : "))
e = 10**(-z)
# i =  1
dfdx = smp.diff(f(x),x)
df = smp.lambdify(x,dfdx) 
h = f(a)/df(a)
if df(a)!=0:
    i = 0
    while abs(h)>= e:
        h = f(a)/df(a)
        r = a-h
        print(f'iteration {i+1}',r)
        x = r
        i+=1
        a = r
    print(f'Root  =',r)

# '''the difference in the use of library change the number of iteration required for the results.
# Lambdify library considers the integer value of the derivative which reduces the number of iterations whereas subs command takes float value to find accurate results, increasing the number of iterations.'''
