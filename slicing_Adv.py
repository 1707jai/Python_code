import numpy as np

arr1=np.arange(1,17).reshape(4,4)
print("\n")
print(arr1)

print("\n",arr1[1, :])  #print 2nd row

print("\n",arr1[ : ,2])  #print 3rd column

print("\n",arr1[2: , :]) #print last 2 row

print("\n",arr1[:, :2])  #print last 2 column

print("\n",arr1[ ::-1 , :]) # reverse rows 

print("\n",arr1[ :, ::-1 ]) # reverse columns

print("\n",arr1[1:3,1:3])  # print 2*2 block from middle 


arr2=np.arange(1,17).reshape(4,4)

print("\n",arr2[ 0, : ]) #print 1rd row 

print("\n",arr2[ :, 0])  #print 3rd row

print("\n",arr2[ 2, :]) #print 2nd row

print("\n",arr2[:, 0]) #print 1 column

print("\n",arr2[:, 2]) #print 3rd column

print("\n",arr2[2:, :]) #print last 2nd row

print("\n",arr2[::-1 , ::-1]) #reverse whole matrix

print("\t","\n",arr2[arr2 % 2!= 0]) #odd in whole matrix

print("\t","\n",arr2[arr2 % 2!= 0])  #even in whole matrix