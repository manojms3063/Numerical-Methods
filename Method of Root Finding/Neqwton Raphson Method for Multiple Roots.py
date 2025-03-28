# Neqwton Raphson Method for Multiple Roots 
# from math import sin
# from math import cos
import sympy as smp
x = smp.symbols('x')
X = smp.symbols('X')
def f(x):
    return x**2-2*x+1
a = int(input("Enter the initial value : "))
z = int(input("Enter no. of Significance degit : "))
m = int(input("enter the Multiplicity Factor : " ))
e = 10**(-z)
# i =  1
dfdx = smp.diff(f(x),x)
df = smp.lambdify(x,dfdx) 
h = f(a)/df(a)
if df(a)!=0:
    i = 0
    while abs(h)>= e:
        if df(a)!=0:
            h = f(a)/df(a)
            r = a-m*h
            print(f'iteration {i+1}:',r)
            x = r
            i+=1
            a = r
print(f'The root of {f(x)} =',r)