import numpy as np
from scipy import stats

arr = np.random.randint(0,100,50)
print(" Orignal Array : \n",arr)

mean_val=np.mean(arr)
median_val=np.median(arr)
std_val=np.std(arr)

print("\n mean :",mean_val)
print("\nmedian ",median_val)
print("\n Standard deviation ",std_val)

filtered =arr[arr >mean_val]
print("\n values greater than mean :\n ",filtered)

sorted_desc= np.sort(filtered)[::-1]
print("\n sorted in descending order ;\n",sorted_desc)