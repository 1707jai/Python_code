import numpy as np 
import pandas as pd
from scipy import stats 
from scipy.stats import ttest_rel
import matplotlib.pyplot as plt

months =["jan","feb","march","april","may","june","july","aug","sep","oct","nov","dec"]
regions=["north","west","south","east","west","north","west","south","east","north","south","west"]

before_ad=[1234,2567,3890,4123,5345,6789,7098,8341,9123,10000,846,6790]
ad_expense=[2140,2355,2678,2890,3055,3210,3388,3560,3725,3880,3955,3990]
after_ad=[5280,13000,8120,9455,11023,13045,15210,16789,17840,18990,19325,19980]

data ={
    "months":months,
    "regions": regions,
    "before_ad":before_ad,
    "ad_expense":ad_expense,
    "after_ad":after_ad
}

df = pd.DataFrame(data)
#print(df)

t_stat,p_value=ttest_rel(df["before_ad"],df["after_ad"])

print(t_stat)
print(p_value)
print(df.dtypes)