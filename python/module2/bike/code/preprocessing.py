# ========== packages
import pandas as pd
import numpy as np

# ========== load dataset
df = pd.read_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module2\bike\data\202101-capitalbikeshare-tripdata.csv', sep= ',')

# check basic features of dataset
df.dtypes
df.describe() 
df.columns 
df.info  # 100070 rows x 13 columns

# check missing values in any rows and remove those rows
nan_values = df[df.isna().any(axis=1)] #[14851 rows x 13 columns]
df1 = df.dropna() #[85219 rows x 13 columns]

# convert dtypes
# dteday : from object(String) to timestamp (;datetime object)

# season,holiday,weekday : integers > categoricals 
df1.astype({'started_at': 'datetime64[ns]', 'ended_at':'datetime64[ns]'})

# ========== create final dataset (lastweek.csv)

df1.started_at = pd.to_datetime(df1.started_at)
df1 = df1[df1['started_at'] >'2021-01-25']
df1.index = df1.started_at
df1 = df1.sort_index()

df1['day'] = df1['started_at'].dt.date
df1['hour'] = df1['started_at'].dt.hour

df2 = df1.groupby(by = ['day', 'hour', 'member_casual']).count()['ride_id'].reset_index()
df2.columns = ['day', 'hour', 'member_type', 'count']

df2
df2.to_csv('last_week.csv')

# ========== load final dataset (lastweek.csv)
hdf = pd.read_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module2\bike\data\last_week.csv', sep=",")

# add columns (weekdays)
# source: https://stackabuse.com/converting-strings-to-datetime-in-python/
# source2: https://www.tutorialsrack.com/articles/323/how-to-find-the-day-of-the-week-for-a-given-date-in-python

# ===== how function can reduce the line of codes
# ver1 
sns.histplot(df1)
sns.histplot(df2)

# ver2
################
#generate plot #
################

function plot(x):
    sns.histplot(x)
