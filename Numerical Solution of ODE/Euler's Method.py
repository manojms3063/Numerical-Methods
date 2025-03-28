import numpy as np
import sympy as smp
from sympy import symbols,diff
import math

# Euler's method

# Problem 1 

import numpy as np
import matplotlib.pyplot as plt
import sympy as smp

# Define symbols for x and y
x, y = smp.symbols('x y')

# The ODE: y' = x^2 + y^2
dydx = x**2 + y**2

# Create a lambda function to evaluate dydx for specific values of x and y
f = smp.lambdify([x, y], dydx)

# Step size
h = 0.1

# Interval values (start and end)
x0 = 0  # initial value of x
y0 = 1  # initial value of y
b = 4   # end point
n = 4 
# n = int((b - x0) / h)  # number of steps

# Initialize arrays for x and y values
x_values = np.empty(n + 1)
y_values = np.empty(n + 1)

# Initial conditions
x_values[0] = x0
y_values[0] = y0

# Apply Euler's method
for i in range(n):
    y_values[i + 1] = y_values[i] + h * f(x_values[i], y_values[i])  # Update y
    x_values[i + 1] = x_values[i] + h  # Update x

# Plot the numerical solution using Euler's method
plt.figure(figsize=(8, 4.5), dpi=500)
plt.plot(x_values, y_values, label='Euler Method (Numerical)', marker='o', color='blue')

# Add titles and labels to the graph
plt.title("Numerical Solution for y' = t^2 + y^2 with y(0) = 1", fontsize=16, family='Times New Roman')
plt.xlabel('t', fontsize=12, family='Times New Roman')
plt.ylabel('y(x)', fontsize=12, family='Times New Roman')
plt.grid()
# plt.legend(fontsize=12, family='Times New Roman')

# Show the plot
plt.show()

# Printing the numerical values of x and y
print('t values:', x_values)
print('y values:', y_values)


#------------------------------------------------------------------------------
# Problem 2 

import numpy as np
import matplotlib.pyplot as plt

# Define the ODE: y' = 2 - e^(-4t) - 2y
def f(t, y):
    return 2 - np.exp(-4*t) - 2*y

# Exact solution: y(t) = 1 + (1/2)e^(-4t) - (1/2)e^(-2t)
def exact_solution(t):
    return 1 + 0.5 * np.exp(-4*t) - 0.5 * np.exp(-2*t)

# Initial condition
t0 = 0  # start point
y0 = 1  # initial value y(0) = 1

# Step size
h = 0.1

# Time points where we want to approximate the solution
t_values = np.arange(t0, 0.6, h)  # from 0 to 0.5 (inclusive)

# Initialize arrays to store the numerical and exact solutions
y_values_numerical = np.zeros(len(t_values))
y_values_exact = np.zeros(len(t_values))

# Set the initial value for the numerical solution
y_values_numerical[0] = y0

# Apply Euler's method
for i in range(1, len(t_values)):
    y_values_numerical[i] = y_values_numerical[i-1] + h * f(t_values[i-1], y_values_numerical[i-1])

# Compute exact solution for comparison
for i in range(len(t_values)):
    y_values_exact[i] = exact_solution(t_values[i])

# Plotting the results
plt.figure(figsize=(8, 5), dpi=500)
plt.plot(t_values, y_values_numerical, label='Euler Method (Numerical)', marker='o', color='blue')
plt.plot(t_values, y_values_exact, label='Exact Solution', color='red', linestyle='--')

# Add titles and labels
plt.title("Euler's Method vs Exact Solution", fontsize=16, family='Times New Roman')
plt.xlabel('t', fontsize=12, family='Times New Roman')
plt.ylabel('y(t)', fontsize=12, family='Times New Roman')
plt.legend()
plt.grid()
# Show the plot
plt.show()

# Print the results
print("t-values:", t_values)
print("Numerical solution values:", y_values_numerical)
print("Exact solution values:", y_values_exact)

# Calculate and print errors
errors = np.abs(y_values_numerical - y_values_exact)
print("Errors:", errors)




