#%%

import sys
import pandas as pd
from pandas.io.parsers import read_csv
import numpy as np
import matplotlib.pyplot as plt
import os
import glob


#%%
x_axis ='Province_State' 

plt.close('All')
df= pd.read_csv("/Users/shabnam/Documents/DataScienceTest/DataSciencePython/csse_covid_19_daily_reports_us/01-01-2021.csv")

data= df.drop(columns = ["Hospitalization_Rate"])
##Compdf= data[['Province_State', 'Confirmed']]
##Compdf.plot.bar(x=x_axis)
print(df.columns)   ## this gives header
print(df.head(3))   ## this gives first 3 rows

# %%
## to gathger all of the cvs files from a folder
path = "/Users/shabnam/Documents/DataScienceTest/DataSciencePython/csse_covid_19_daily_reports_us"
csv_files = glob.glob(os.path.join(path, "*.csv"))
##print(csv_files)
# %%
## here we read each csv file and plot, then close and go to next one
for i in csv_files:
    dt = pd.read_csv(i)
    dt.plot.bar(x="Province_State", y="Confirmed")

# %%
## here we want one data frame for each file and keep them open. if you run parts of this script, you have to run line 23, 24 first to get the cvs_files 
dict_df= dict()
for i in csv_files:
    dict_df[i] = pd.read_csv(i)
    ##dict_df[i].plot.bar(x="Province_State", y="Confirmed")

## now want to query the dataframe. per each state want the confirmed cases per day and then plot them
## dict_df contains all of the dataframes, so have to first pick each dataframe and then find the column "confirmed"
sum= 0 
for struct in dict_df:
    Wrow= dict_df[struct].query('Province_State == "South Carolina"')
    ##print(type(Wrow))
    sum = sum + Wrow['Confirmed'].values[0]
print(sum)
   
# %%
