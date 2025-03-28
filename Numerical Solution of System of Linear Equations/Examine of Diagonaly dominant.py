import numpy as np
import time
from datetime import datetime as dt

# Diagonaly dominant - approach - 1 

# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# A = np.array([[0,3,-2],[2,10,1],[1,-2,8]])
def DD(A): 
    for i in range(0,len(A)):
        sum = 0 
        for j in range(0,len(A)):
                sum = sum+abs(A[i][j])
        sum = sum - abs(A[i][i])
        # print(sum)

        if abs(A[i][i])<=sum:
            return False
    return True
A = np.array([[15,3,-2],[2,10,1],[1,-2,8]])
if(DD(A)):
    print("yes")
else:
     print("no")
     
     
# Diagonal Dominant approach - 2 


A = np.array([[15,2,3],[4,55,6],[7,8,94]]) 
for i in range(0,len(A)):
    sum = 0 
    for j in range(0,len(A)):
        if i!=j:
            sum = sum+A[i][j]
    
if A[i][i]> sum:
    print("DD")
    
else:
    print("NDD")
