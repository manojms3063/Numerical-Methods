import numpy as np
import time
from datetime import datetime as dt

#Gaussian Elimination 
t_i=time.time()

def gauss_el(a,b):
    n = len(b)
    m = n-1
    i = 0
    j = i-1
    X = np.zeros(n)
    new_line = "\n"
    agm = np.concatenate((a,b),axis = 1,dtype=np.float64)
    sol = np.empty([len(agm),1])
    #Augmented matrix 
    
    print(f"the intial augmented matrix is :{new_line}{agm}")
    print("solving for the upper triangular matrix")
    
    while i<n:
        if agm[i][j] == 0.0:
            print("divide by zero error")
            return

        for j in range(i+1,n):
            sf = agm[j][i]/agm[i][i]
            agm[j]=agm[j]-(sf*agm[i])
            print(agm)
        i+=1

    for i in range(n-1,-1,-1):
        X[i]=agm[i][n]

        for j in range(i+1,n):
            X[i] = X[i]-agm[i,j]*X[j]
        X[i]  = X[i]/agm[i,i]
    print("the following X - vector matrix solve the above agm matrix")
    for answer in range(n):
        print(f"{answer} is {X[answer]}")

A = np.array([[3,-1,-2,-1],[1,-2,0,-1],[2,2,1,2],[1,0,0,-2]],dtype= np.float64)
B = np.array([[3],[2],[7],[0]],dtype= np.float64)
gauss_el(A,B)
t_f=time.time()
print('\ncost of computation:',t_f-t_i)