import numpy as np
import statistics as stats

baked_food = np.array([200,300,150,130,200,280,170,188])

print(np.mean(baked_food))
print(np.median(baked_food))
print(stats.mode(baked_food))
print(np.std(baked_food))

tobacco_consumption = [30,50,10,30,50,40]
deaths = [100,120,70,100,120,112]

print(np.corrcoef([tobacco_consumption, deaths]))
