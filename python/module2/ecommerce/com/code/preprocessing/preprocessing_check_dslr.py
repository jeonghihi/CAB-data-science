# %% 
import pandas as pd 
import numpy as np


# %%
item = 'dslr_camera'
df = pd.read_csv('./output/product_output/' + item +'_details.csv', index_col = 0)

#%%
print(df.info())
df.head()
# all none-values are numpy NaN

# %%
item = 'monitor_detail_fin'
df = pd.read_csv('./output/product_output/' + item +'.csv', index_col = 0)

# %%
df_new = df.drop(columns = 'index')
df_new.head()

#%% with monitor
# try:
try:
    df_new['product_weight'] = df_new['product_weight'].apply(lambda x: str(x).replace('pounds',''))
    df_new['product_dimensions'] = df_new['product_dimensions'].apply(lambda a: str(a).replace('inches','')) 
    df_new['customer_reviews_detail'] = df_new['customer_reviews_detail'].apply(lambda x: str(x).replace('0%', ''))
except:
    pass

df_new.head()

#%% with headphones
# try:
try:
    df_new['ratings'] = df_new['ratings'].apply(lambda x: str(x).split(' ')[0])
    df_new['product_dimensions'] = df_new['product_dimensions'].apply(lambda a: str(a).replace('inches','')) 
    df_new['seller'] = df_new['seller'].apply(lambda x: str(x).replace('Visit the', ''))
    df_new['seller'] = df_new['seller'].apply(lambda x: str(x).replace('Store', '').rstrip())
except:
    pass

df_new.head()
#%% headphones / monitor
df_temp = df_new.replace('nan','')
df_temp2 = df_temp.replace('', np.nan, regex=True)
df_temp2.head()

df_temp3 = df_temp2.loc[df_temp2['ASIN'].notnull()]


# %%
# df_temp3.to_csv('./output/product_output/headphones_details_fin.csv', index_col = 0)
df_temp3.to_csv('./output/product_output/monitor_details_fin.csv')