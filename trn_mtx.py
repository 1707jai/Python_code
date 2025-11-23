import numpy as np 

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

#transpose with using .T function

transpose = arr.swapaxes(0,1)
print(transpose)

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n",arr1)

new=arr1.reshape(-1)
print(new)