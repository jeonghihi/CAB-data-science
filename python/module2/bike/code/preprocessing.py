
# ========== packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import calendar as cal

import datetime
from dateutil.parser import parse 

#%%
# convert raw data from website to dataframe and save it as csvfile

filepath1 = '../data/raw/2013Q1-capitalbikeshare-tripdata.csv'
filepath2 = '../data/raw/2013Q2-capitalbikeshare-tripdata.csv'
filepath3 = '../data/raw/2013Q3-capitalbikeshare-tripdata.csv'
filepath4 = '../data/raw/2013Q4-capitalbikeshare-tripdata.csv'

raw_df1 = pd.read_csv(filepath1, sep=",", engine="python")
raw_df1.head()
raw_df2 = pd.read_csv(filepath2, sep=",", engine="python")
raw_df2.head()
raw_df3 = pd.read_csv(filepath3, sep=",", engine="python")
raw_df3.head()
raw_df4 = pd.read_csv(filepath4, sep=",", engine="python")
raw_df4.head()

df = pd.concat([raw_df1, raw_df2, raw_df3, raw_df4], axis=0)
print(df.shape)

df.head()
#%%
print('hi')
#%%
#====== function1


def raw_to_df(df):
    df['Member type'] = pd.Categorical(df['Member type'], categories=
      ['Member','Casual'],
      ordered=True)

    df.index = df.loc[:,'Start date']
    df = df.sort_index()

    df['Start date'] = pd.to_datetime(df['Start date'], format="%Y/%m/%d")
    df['End date'] = pd.to_datetime(df['End date'])

    df['day'] = df['Start date'].dt.date
    df['hour'] = df['Start date'].dt.hour

    ## merge day-hour to use it as index
    df.day = df.day.astype('str')
    df.hour = df.hour.astype('str')
    df['hour'] = df['hour'].apply(lambda x : '{0:0>2}'.format(x))

    df.loc[:,'timestamp'] = df['day'] + ' ' + df['hour']
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H")
    print("{}".format(df['timestamp'][5]))

    df.rename(columns = {'Member type':'member_type','Start date':'started_at', 'End date':'ended_at', 'Start station':'start_station', 'End station':'end_station'}, inplace = True) 
    df.head()
    df1 = df.copy()
    return df1


# function2


def merge_df1_hour(df):
    # merge date + hour (converting to last_week.csv)

    df2 = df.groupby(by = ['day', 'hour', 'member_type']).count()['Bike number'].reset_index()
    df2.columns = ['day', 'hour', 'member_type', 'count']
    df2['day'] = pd.to_datetime(df2['day'], format="%Y-%m-%d")
    #df2['hour'] = pd.to_datetime(df2['hour'])

    df2.head(5)

    df2.day = df2.day.astype('str')
    df2.hour = df2.hour.astype('str')

    df2['hour'] = df2['hour'].apply(lambda x : '{0:0>2}'.format(x))
    df2.loc[:,'timestamp'] = df2['day'] + ' ' + df2['hour']
    df2.timestamp = pd.to_datetime(df2.timestamp, format="%Y-%m-%d %H")

    print("{}".format(df2['timestamp'][5]))

    df2.index = df2.timestamp
    df2 = df2.sort_index()
    df2.head()

    # separate dataframe
    df2['time_ind'] = df2['timestamp']
    df2 = df2.drop('timestamp',1)
    df2_casual = df2[df2["member_type"] == 'Casual']
    df2_member = df2[df2["member_type"] == 'Member']

    df2_casual.head()

        # merge using time_ind
    df2_merged = pd.merge(df2_casual, df2_member, on= ['time_ind','day','hour'], how='outer')

    # reorder
    df2_merged = df2_merged[['day', 'hour', 'time_ind', 'member_type_x', 'count_x', 'member_type_y', 'count_y']]
    print(df2_merged.head(5))

    df2_merged.columns = ['day', 'hour', 'time_ind', 'member_type_x', 'casual', 'member_type_y', 'member']
    df2_merged.drop(columns = ['member_type_x', 'member_type_y'], inplace=True)

    # handle NaN values in count (replace 0 with 0.001)
    df2_merged['casual'] = df2_merged['casual'].astype('str')
    df2_merged['member'] = df2_merged['member'].astype('str')
    df2_merged.dtypes

    df2_merged['member'] = df2_merged['member'].replace('nan', '0.001')
    df2_merged['casual'] = df2_merged['casual'].replace('nan', '0.001')

    df2_merged['casual'] = df2_merged['casual'].astype('float64')
    df2_merged['member'] = df2_merged['member'].astype('float64')
    df2_merged.dtypes

    df2_merged['total_count'] = df2_merged['casual'] + df2_merged['member']
    df2_merged.head()

    # check NaN values (in the original dataset these numbers would be 0)
    df2_merged[df2_merged['total_count'] <= 1]


    # add weekday column (for visualization / weekend grouping )
    weekdays = []

    for item in range(len(df2_merged)):
      date_time_obj = df2_merged['time_ind'][item]
      weekday = cal.day_name[date_time_obj.weekday()]
      weekdays.append(weekday)

    df2_merged['weekdays'] = weekdays

    df2_merged['daytype'] = df2_merged['weekdays']

    weekend = ['Saturday', 'Sunday']

    #df2_merged = df2_merged[df2_merged['daytype'].isin(weekend)]
    df2_merged['daytype'] = df2_merged['daytype'].apply(lambda value: 'weekend'
          if value in weekend else 'weekday')

    # change datatype into category

    df2_merged['daytype'] = pd.Categorical(df2_merged['daytype'], categories=['weekday', 'weekend'])
    df2_merged['weekdays'] = pd.Categorical(df2_merged['weekdays'], categories=
      ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
      ordered=True)
    out = df2_merged.copy()
    return out
#%%

df1 = raw_to_df(df)
df1.head()

df2_merged = merge_df1_hour(df1)
df2_merged.head()

df2_merged.to_csv('../data/preprocessed/2014-df.csv', sep=",")

#%%
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
