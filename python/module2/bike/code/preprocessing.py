# load dataset
import pandas as pd
import numpy as np

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

