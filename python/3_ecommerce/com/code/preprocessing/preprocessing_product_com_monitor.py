#%% load dataset
item = 'Monitor' #Headphones

import pandas as pd
df = pd.read_json('./output/product_output_com_' + item +'_1.jsonl')
df.head()

# %% initial check with data 

# number of unique items: 
# Monitor - 5553/7452
print('number of unique items:',len(set(df.name)),'of',len(df.name))
print('missing values in all items:')
print(df.isnull().sum()/len(set(df.name)))

# check missing values:
# Monitor - rating/review:1309, price:1747
print(df.isnull().sum()) 

# drop unnecessary columns 
df_dropped = df_dropped.drop(['col_name'], axis=1)

# drop rows containing 75% NaN values 
perc = 75.0 
min_count =  int(((100-perc)/100)*df.shape[1] + 1)
mod_df = df.dropna( axis=0, 
                    thresh=min_count)

print('number of unique items after 1st removal:',len(set(mod_df.name)), 'of',len(mod_df.name))

# add column 'prod_type'
#df.loc[:, 'prod_type'] = item

