import numpy as np 
arr=np.array([10,20,30,40,50,60,70,80,90,100])
           #print numbers from 10 to 60 only

 
  #first four elements slice
print(arr[:4])

  #last three elements slice
print(arr[-3:])

  #index 2 to 6 slice
print(arr[2:7])

  #alternate values
print(arr[::2])

arr1=np.arange(1,21)
print(arr1)

# slice last 5 elements from first 10 elements. 
print(arr1[:10][-5:])

#reverse array by slicing 
print(arr1[::-1])

#select every 3rd number
print(arr1[::3]) 

arr2=np.arange(1,17).reshape(4,4)
print(arr2)

#slice 2nd row
print("\n",arr2[1])

#slice 3nd column
print(arr2[:,3])

#slice 2 * 2 BLOCK

print(arr2[1:3 , 1:3])