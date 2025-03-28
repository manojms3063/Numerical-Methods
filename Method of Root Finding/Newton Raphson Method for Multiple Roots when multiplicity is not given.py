#Newton Raphson Method for Multiple Roots when multiplicity is not given
import sympy as smp
x = smp.symbols('x')
X = smp.symbols('X')
def f(x):
    return x**2-2*x+1
a = int(input("Enter the initial value : "))
z = int(input("Enter no. of Significance degit : "))
e = 10**(-z)
# i =  1
dfdx = smp.diff(f(x),x)
dfdx2 = smp.diff(f(x),x,2)
df = smp.lambdify(x,dfdx)
df2 = smp.lambdify(x,dfdx2)  
h = f(a)/df(a)
if df(a)!=0:
    i = 0
    while abs(h)>= e:
        if df(a)!=0:
            r = a - ((f(a)*df(a))/((df(a))*2-f(a)*df2(a)))
            print(f'iteration {i+1}:',r)
            x = r
            i+=1
            a = r
print(f'The root of {f(x)} =',r)