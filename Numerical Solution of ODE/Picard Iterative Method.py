import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Step 1: Define the Picard Iterative Method

def picard_iteration(x_vals, max_iter=3):
    # Initial guess y0(x) = 0
    y_vals = np.zeros_like(x_vals)
    
    # Picard Iterations
    for n in range(1, max_iter+1):
        y_new = np.zeros_like(x_vals)
        for i, x in enumerate(x_vals):
            # Integral term from 0 to x
            integral_term = np.trapz((x_vals[:i+1]**2 + y_vals[:i+1]**2)[:i+1], x_vals[:i+1])
            y_new[i] = integral_term
        y_vals = y_new
    return y_vals

# Step 2: Define the Exact Solution using Numerical Integration (Solve IVP)
def exact_solution(t, y):
    return t**2 + y**2

# Solve the IVP using solve_ivp for the exact solution
x_exact_vals = np.linspace(0, 0.2, 100)
sol_exact = solve_ivp(exact_solution, [0, 0.2], [0], t_eval=x_exact_vals, method='RK45')
y_exact_vals = sol_exact.y[0]

# Step 3: Define the x-values for plotting and apply Picard Method
x_vals = np.linspace(0, 0.2, 10)  # x-values from 0 to 0.2
y_picard_vals = picard_iteration(x_vals, max_iter=3)

# Step 4: Plot the exact solution and numerical solution

plt.figure(figsize=(10, 6))
plt.plot(x_exact_vals, y_exact_vals, label="Exact Solution", color="blue", linewidth=2, linestyle="--")
plt.plot(x_vals, y_picard_vals, label="Picard Approximation (3 Iterations)", marker="o", color="red")
plt.xlabel("x", fontsize=12, family="Times New Roman")
plt.ylabel("y(x)", fontsize=12, family="Times New Roman")
plt.title("Exact vs Picard Approximation for y' = x^2 + y^2", fontsize=14, family="Times New Roman")
plt.legend(fontsize=10, family="Times New Roman")
plt.grid(True)

# Save the plot with 500 DPI
plt.savefig("picard_exact_comparison.png", dpi=500, bbox_inches="tight")
plt.show()

# Print the values at x = 0.2 for both solutions
print(f"Exact solution at x=0.2: {y_exact_vals[-1]}")
print(f"Picard approximation at x=0.2: {y_picard_vals[-1]}")
