import numpy as np
import time
from datetime import datetime as dt

# Gauss Sidel Method - 
a = np.array([[2,1,1],[3,5,2],[2,1,4]],dtype= np.float64)
b = np.array([5,15,8],dtype= np.float64)

x = np.array([0,0,0],dtype= np.float64)
t_i=time.time()
for k in range(0,10):
    for i in range(0,len(a)):
        p = b[i]
        for j in range(0,len(a)):
            if i!=j:
                p = p-a[i][j]*x[j]
        x[i] = p/a[i][i]
    
    print(x)
t_f=time.time()
print('\ncost of computation:',t_f-t_i)