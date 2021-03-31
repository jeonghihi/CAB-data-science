#%% load dataset
import pandas as pd 
df = pd.read_json('search_output_smartphone.jsonl')
df.head()
#%%
# add column 'prod_type'
df.loc[:, 'prod_type'] = 'smartphone'

# %% check missing values (less than 5%)
print(df.isnull().sum())
# rating97,price26 (total 446> 260)

# missing values in rating
len(set(df.title))

#%% clean data (german res): monitor

for i in range(len(df.rating)):
    try:
        df.loc[i,'rating'] = df.loc[i,'rating'][:3].replace(',','.')
    except:
        continue
        #print('Sorry lets move on')

for i in range(len(df.review_count)):
    try:
        df.loc[i,'review_count'] = df.loc[i,'review_count'].replace(',','')
    except:
        continue

for i in range(len(df.price)):
    try:
        df.loc[i,'price'] = df.loc[i,'price'].replace('€','')
    except:
        continue

#%% clean data (english res): smartphone
for i in range(len(df.rating)):
    try:
        df.loc[i,'rating'] = df.loc[i,'rating'][:3]
    except:
        continue
        #print('Sorry lets move on')

for i in range(len(df.review_count)):
    try:
        df.loc[i,'review_count'] = df.loc[i,'review_count'].replace(',','')
    except:
        continue

for i in range(len(df.price)):
    try:
        df.loc[i,'price'] = df.loc[i,'price'].replace('€','')
    except:
        continue
#%% data type
df.rating = df.rating.astype('float')
df.review_count = df.review_count.astype('float')


# %% save preprocessed data
df.to_csv('summary_monitor.csv', index= None)
# %%
