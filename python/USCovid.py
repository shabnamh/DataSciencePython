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
Compdf= data[['Province_State', 'Confirmed']]
Compdf.plot.bar(x=x_axis)
print(df.columns)   ## this gives header
print(df.head(3))   ## this gives first 3 rows

# %%
##THIS SECTION IS REQUIRED IN ALL OF THE NEXT PARTS SINCE IT IS FOR GATHERING THE DATA FROM THE FOLDER
## to gather all of the cvs files from a folder
path = "/Users/shabnam/Documents/DataScienceTest/DataSciencePython/csse_covid_19_daily_reports_us"
csv_files = glob.glob(os.path.join(path, "*.csv"))
##print(csv_files)
# %%
##NEXTQUESTION
## here we read each csv file and plot, then close and go to next one
for i in csv_files:
    dt = pd.read_csv(i)
    dt.plot.bar(x="Province_State", y="Confirmed")

# %%
##NEXTQUESTION
#NEED THIS SECTION FOR THE REST OF THE QUESTIONS
## here we want one dataframe for each file and keep them open. if you run parts of this script, you have to run line 23, 24 first to get the cvs_files 
dict_df= dict()
for i in csv_files:
    dict_df[i] = pd.read_csv(i)
    ##dict_df[i].plot.bar(x="Province_State", y="Confirmed")

# %%
##NEXT TASK WITH THE DATAFRAME
## now want to query the dataframe. for one state, we want the confirmed cases per day and then plot them
## dict_df contains all of the dataframes, so have to first pick each dataframe and then find the column "confirmed"
sum= 0 
for struct in dict_df:
    Wrow= dict_df[struct].query('Province_State == "South Carolina"')
    ##print(type(Wrow))
    sum = sum + Wrow['Confirmed'].values[0]
print(sum)

## note confirmed type was arrey, so in order to get the value as integer had to use the above code   
# %%
##NEXT QUESTION
## want to define a ftn to get the sum for one state and then use it in a for loop to get the sum for all of the states

def StateConfirmed (StName):
    sum = 0
    for struct in dict_df:
        WR= dict_df[struct].query('Province_State == "' + str(StName) +'"')
        sum = sum + WR['Confirmed'].values[0]
    print(sum) 

StateConfirmed("South Carolina")   
## now we have a for loop to get the confirmed amount, now need to get all of the states and then have a for loop to get the confirmmed amount for all of them
# %%
dt1= pd.read_csv(csv_files[1])
states= dt1['Province_State']
print(states)
print(type(states))

# %%
for st in states:
    print (st)
    StateConfirmed(st)
    #print(st , StateConfirmed(st))

# NEXT QUESTION
# Now we see that numbers are not right, so we want to find the number of cases per day. Each day data is yesterday data + new cases , so have to subtract two data frames to find the new cases. However, the first day does not need this!
# Have to adjust the StateConfirmed ftn to get the correct number and then use the loop tp get it fot all of the states
# Need to set the initial value as day 1 and then subtract the next day value and keep it as the new value
# the first date we have is 04-12-2020
# %%
# This function prints the date and number of new cases per state
# NOTE:Had to modify the date since the logged date is always one day after the actually measured day
def UpDStateConfirmed (StName):
    df1= pd.read_csv("/Users/shabnam/Documents/DataScienceTest/DataSciencePython/csse_covid_19_daily_reports_us/04-12-2020.csv")
    sum = df1.query('Province_State == "' + str(StName) +'"')['Confirmed'].values[0]
    for struct in dict_df:
        WR= dict_df[struct].query('Province_State == "' + str(StName) +'"')['Confirmed'].values[0]
        D = dict_df[struct].query('Province_State == "' + str(StName) +'"')['Last_Update'].values[0]
        D = datetime.datetime.strptime(D, "%Y-%m-%d %H:%M:%S")
        if D.day-1 == 0 and D.month > 1:
            D = datetime.date(D.year,D.month-1,30) 
        elif D.day-1 == 0 and D.month == 1:
            D = datetime.date(D.year-1,12,30)
        else:
            D = datetime.date(D.year,D.month,D.day-1)
        NCase = WR - sum
        if NCase <= 0:
            print(D, "No new case")
        else:
            print(D, NCase)
        sum= sum + NCase
    
# %%
UpDStateConfirmed("South Carolina")     

# %%
for st in states:
    print (st)
    UpDStateConfirmed("' + str(StName) +'")
# %%
