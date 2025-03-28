import numpy as np
import time
from datetime import datetime as dt


# Jacobi Itteration method 

a = np.array([[15,3,-2],[2,10,1],[1,-2,8]],dtype= np.float64)
b = np.array([[15,3,-2],[2,10,1],[1,-2,8]],dtype= np.float64)
c = np.array([[15,3,-2],[2,10,1],[1,-2,8]],dtype= np.float64)
B = np.array([[85],[51],[5]],dtype= np.float64)
t_i = dt.now()
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i<j:
            a[i][j] = 0
        elif i==j: 
            a[i][i]= 0 
L = a
print("L=", L)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i>j:
            b[i][j] = 0
        elif i==j: 
            b[i][i]= 0 
U = b
print("U=", U)

for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i!=j:
            c[i][j]=0
D = c
print("D=", D)

LPU = L+U
print(LPU)
Di = np.linalg.inv(D)

H = -(np.dot(Di,LPU))
print(H)

C = np.dot(Di,B)
print(C)
X0 = np.array([[0],[0],[0]])
i = 0
n = 10
while i<n:
    X1= np.dot(H,X0)+C
    print(f"Itteration {i+1}: \n ",X1)
    i+=1
    X0 = X1
t_f = dt.now()

print("Cost= ",t_f-t_i)