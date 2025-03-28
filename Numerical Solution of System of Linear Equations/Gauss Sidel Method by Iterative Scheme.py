import numpy as np
import time
from datetime import datetime as dt



#Gauss Sidel by Iterative Scheme 
A=np.array([[15,3,-2],[2,10,1],[1,-2,8]],dtype=np.float64)
B=np.array([[85],[51],[5]],dtype=np.float64)
L=np.empty([len(A),len(A)])
U=np.empty([len(A),len(A)])
D=np.empty([len(A),len(A)])
t_i=time.time()

for i in range(len(A)):
    for j in range(len(A)):
        if i>j:
            L[i][j]=A[i][j]
        elif i<j:
            U[i][j]=A[i][j]
        elif (i==j):
            D[i][j]=A[i][j]
        else:
            L[i][j]=0
            U[i][j]=0
            D[i][j]=0
# print("D\n",D)
H=-np.dot(np.linalg.inv(D),(L+U))
C=np.dot(np.linalg.inv(D),B)
# print("H\n",H)
# print("C\n",C)
x0=np.array([[0],[0],[0]])
i=0
n=10
while i<n:
    x1=np.dot(H,x0)+C
    print(f'\niteration {i+1}:\n',x1)
    x0=x1
    i+=1
t_f=time.time()
print('\ncost of computation:',t_f-t_i)