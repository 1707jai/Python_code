import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

print(np.vstack((a,b)))  #vstack


print("\n",np.hstack((a,b)))  #hstack


#concatenate


A=[[1,2],[3,4]]
B=[[5,6],[7,8]]


print("\n",np.concatenate((a,b),axis=0))

print("\n",np.concatenate((A,B),axis=1))