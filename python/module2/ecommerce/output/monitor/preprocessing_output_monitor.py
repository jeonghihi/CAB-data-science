#%% load dataset
import pandas as pd 
df = pd.read_json('search_output_monitor.jsonl')
df.head()

# add column 'prod_type'
df.loc[:, 'prod_type'] = 'monitor'

# %% check missing values 
print(df.isnull().sum())

# missing values in rating
len(set(df.title))

#%% clean data 

for i in range(len(df.rating)):
    try:
        df.loc[i,'rating'] = df.loc[i,'rating'][:3].replace(',','.')
    except:
        continue
        #print('Sorry lets move on')

# data type
df.rating = df.rating.astype('float')


# %% save preprocessed data
df.to_csv('summary_monitor.csv', index= None)
# %%
