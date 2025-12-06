import numpy as np

arr=np.ones((6,6),dtype=int) # only for digit 1
print(arr)
print("\n")

#only for different digit for whole matrix 

arr1 =np.full((6,6),17,dtype=int)
print(arr1)

print("\n")
#this one is for random element in matrix 

arr2 = np.random.randint(0,101,(6,6))
print(arr2)