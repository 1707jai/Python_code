import numpy as np

arr=np.array([20,40,60,80 ])

print(np.cumsum(arr)) #cumulative sum
print(np.cumprod(arr)) #cumulative product


a= [100,150,199,200,250,130]
b=[10,50,30,40,30,10]

price=np.array(a)
quantity=np.array(b)

print(price,"\n",quantity,"\n")

c=(np.cumprod([price,quantity],axis = 0)) 

print(c[1].sum())

print("-----------------------------------")