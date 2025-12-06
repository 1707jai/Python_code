import numpy as np 

arr=np.arange(1,101)

def is_prime(n):
    if n <= 1:
        return False
    for d in range(2 , int (np.sqrt(n))+1):
        if n % d == 0:
            return False
    return True

prime =np.array([x for x in arr if is_prime(x)])

print("prime number form 1 to 100 ")
print(prime)