# Numerical Methods in Python

This repository contains Python implementations of various **Numerical Methods** used in mathematical and engineering applications. These methods help solve interpolation problems, numerical integration, solving ODEs, solving systems of linear equations, root-finding techniques, and curve fitting.

## 1. Interpolation
Interpolation is a method to estimate values between known data points.

### **Lagrange's Interpolation**
Formula:
$P(x) = \sum_{i=0}^{n} y_i \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$

### **Newton's Forward Difference Interpolation**
Formula:
$P(x) = y_0 + \Delta y_0 \frac{(x - x_0)}{h} + \frac{\Delta^2 y_0}{2!} \frac{(x - x_0)(x - x_1)}{h^2} + \dots$

### **Newton's Backward Difference Interpolation**
Formula:
$P(x) = y_n + \nabla y_n \frac{(x - x_n)}{h} + \frac{\nabla^2 y_n}{2!} \frac{(x - x_n)(x - x_{n-1})}{h^2} + \dots$

### **Newton's Divided Difference Interpolation**
Formula:
$P(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \dots$

---

## 2. Numerical Integration
Methods to approximate the integral of a function.

### **Trapezoidal Rule**
Formula:
$\int_a^b f(x)dx \approx \frac{h}{2} [f(a) + 2 \sum f(x_i) + f(b)]$

### **Simpson's 1/3 Rule**
Formula:
$\int_a^b f(x)dx \approx \frac{h}{3} [f(a) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \dots + f(b)]$

### **Simpson's 3/8 Rule**
Formula:
$\int_a^b f(x)dx \approx \frac{3h}{8} [f(a) + 3f(x_1) + 3f(x_2) + 2f(x_3) + 3f(x_4) + \dots + f(b)]$

---

## 3. Numerical Solution of ODEs
### **Euler's Method**
Formula:
$y_{n+1} = y_n + h f(x_n, y_n)$

### **Modified Euler's Method**
Formula:
$y^* = y_n + h f(x_n, y_n)$
$y_{n+1} = y_n + \frac{h}{2} [ f(x_n, y_n) + f(x_{n+1}, y^*) ]$

### **Taylor Series Method**
Formula:
$y_{n+1} = y_n + h f(x_n, y_n) + \frac{h^2}{2} f'(x_n, y_n)$

### **Runge-Kutta 2nd Order (RK2)**
Formula:
$k_1 = h f(x_n, y_n)$
$k_2 = h f(x_n + h, y_n + k_1)$
$y_{n+1} = y_n + \frac{1}{2} (k_1 + k_2)$

### **Runge-Kutta 4th Order (RK4)**
Formula:
$k_1 = h f(x_n, y_n)$
$k_2 = h f(x_n + \frac{h}{2}, y_n + \frac{k_1}{2})$
$k_3 = h f(x_n + \frac{h}{2}, y_n + \frac{k_2}{2})$
$k_4 = h f(x_n + h, y_n + k_3)$
$y_{n+1} = y_n + \frac{1}{6} (k_1 + 2k_2 + 2k_3 + k_4)$

### **Runge-Kutta 4th Order for 2nd Order ODEs**
Solving second-order ODEs of the form:
$\frac{dy}{dx} = f(x, y, z), \quad \frac{dz}{dx} = g(x, y, z)$

### **Milne's Predictor-Corrector Method**
Predictor:
$y_{n+1} = y_{n-3} + \frac{4h}{3} (2 f_{n-1} - f_{n-2} + 2 f_n)$
Corrector:
$y_{n+1} = y_{n-1} + \frac{h}{3} (f_{n-1} + 4 f_n + f_{n+1})$

### **Adams-Bashforth Method**
A multi-step method using past function evaluations.

---

## 4. Numerical Solution of System of Linear Equations
### **Checking for Diagonal Dominance**
A matrix is diagonally dominant if:
$|a_{ii}| \geq \sum_{j \neq i} |a_{ij}| \quad \forall i$

### **Gauss Elimination Method**
A systematic method to reduce a system of equations to an upper triangular form.

### **Gauss-Seidel Method**
Iterative method using:
$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j<i} a_{ij} x_j^{(k+1)} - \sum_{j>i} a_{ij} x_j^{(k)} \right)$

### **Jacobi Iteration Method**
Iterative method using:
$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$

---

## 5. Methods of Root Finding
### **Bisection Method**
If $ f(a)f(b) < 0 $, the root lies in the interval $(a, b)$ and is given by:
$c = \frac{a + b}{2}$

### **Secant Method**
$x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}$

### **Regula Falsi Method**
$x_{n+1} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$

### **Newton-Raphson Method**
$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

### **Newton-Raphson for Multiple Roots**
$x_{n+1} = x_n - \frac{f(x_n) f'(x_n)}{(f'(x_n))^2 - f(x_n) f''(x_n)}$

---

## 6. Curve Fitting
### **Straight Line Fit**
$y = ax + b$

### **Parabolic Fit**
$y = ax^2 + bx + c$

### **Exponential Fit**
$y = a e^{bx}$

---
