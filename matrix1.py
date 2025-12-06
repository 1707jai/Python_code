import numpy as np

                #create array and and replace all even numebr with 0
                #and all odd number with 1
                 

#create 5*5 matrix from 1 to 25
arr=np.arange(1,26).reshape(5,5)

#replace even number with 0 
arr[arr%2 == 0]=0

#replace odd number with 1
arr[arr%2 == 1]=1

print(arr)
