import numpy as np
from scipy import stats

arr = np.array([[10,20,30,40],[50,60,70,80],[20,40,60,80]])
#print(np.shape(arr))
#print(np.size(arr))
#print(np.ndim(arr))
#print(arr.dtype)
#print(np.array(arr**2))# element wise square 
#print(np.array(arr**3))# element wise cube 

# standard maths  functions 

#print(np.array(arr.sum()))

print(np.array(arr.mean()))#mean

print(stats.mode(arr,axis=1,keepdims= True))#mode
#print(stats.mode(arr))

print(np.median(arr))# median

print(np.std(arr)) #standard deviation 

print(np.var(arr))# variance 