# %% 
import pandas as pd 
import numpy as np

# %%

item = 'headphones'

df_details_fin = pd.read_csv('./output/product_output/' + item +'_details.csv', index_col = 0)
df_add_fin = pd.read_csv('./output/product_output/' + item +'_add.csv', index_col = 0)


# %%
df_details_fin["ASIN"] = df_details_fin["ASIN"].apply(lambda a: str(a).rstrip())    # Apply rstrip function
# df_join = df_details_fin.join(df_add_fin, how='outer', lsuffix="_1", rsuffix="_2")

df_details_fin.isna().sum()
df_add_fin.isna().sum()

df_details_fin_temp = df_details_fin.fillna('').astype(str)
df_add_fin_temp = df_add_fin.fillna('').astype(str)

try:
    test_merged2 = pd.concat([df_add_fin_temp, df_details_fin_temp], axis=1, verify_integrity=True)
except ValueError as e:
    print('ValueError', e)

same_cols = ['ASIN', 'seller', 'seller_link', 'link_to_all_reviews']

df_merge = pd.merge(df_details_fin_temp, df_add_fin_temp, on= same_cols, how='outer')

df_merge2 = df_merge.sort_values('ASIN')
df_merge3 = df_merge2.replace('', np.nan, regex=True)
df_merge4 = df_merge3.loc[df_merge3['ASIN'].notnull()]

df_merge5 = df_merge4.sort_values('ASIN').drop_duplicates(subset=['freq_bought','ratings'])

test = df_merge5.copy()
temp = df_merge5.reset_index()

for i in range(len(temp)):
    if temp.loc[i,:] is not None:
        if type(temp['seller'][i]) is float:
            try:
                temp.loc[i,'seller'] = temp.loc[i, 'seller2'] 
            except:
                pass
    else:
        temp.loc[i,'seller2']
        continue

for i in range(len(temp)):
    if temp.loc[i,:] is not None:
        if type(temp['seller_link'][i]) is float:
            try:
                temp.loc[i,'seller_link'] = temp.loc[i, 'seller_link2'] 
            except:
                pass
    else:
        temp.loc[i,'seller_link2']
        continue

drop_cols = ['seller2', 'seller_link2']
df_merge_fin = temp.drop(columns = drop_cols)

#%%
df_merge_fin.columns = ['index', 'ASIN', 'product_name', 'item_model_nr', 'package_dimensions',
       'product_dimensions', 'batteries', 'date_first_available',
       'discontinued_by_mfg', 'seller', 'seller_link', 'freq_bought',
       'rating_details', 'link_to_all_reviews', 'ratings',
       'best_sellers_rank']

col_order = ['index', 'ASIN', 'product_name', 'item_model_nr', 'package_dimensions',
       'product_dimensions', 'best_sellers_rank', 'ratings', 'rating_details', 
       'batteries', 'date_first_available', 'discontinued_by_mfg', 
       'seller', 'seller_link', 'freq_bought','link_to_all_reviews'
       ]

df_merge_fin = df_merge_fin[col_order]

#df_merge_fin.to_csv('./output/product_output/headphones_detail_fin.csv')


# %%

df_new = df_merge_fin.drop(columns = 'index')
df_new.head()

#%%
# try:
try:
    df_new['ratings'] = df_new['ratings'].apply(lambda x: str(x).split(' ')[0])
    df_new['product_dimensions'] = df_new['product_dimensions'].apply(lambda a: str(a).replace('inches','')) 
    df_new['seller'] = df_new['seller'].apply(lambda x: str(x).replace('Visit the', ''))
    df_new['seller'] = df_new['seller'].apply(lambda x: str(x).replace('Store', '').rstrip())
except:
    pass

df_new.head()
#%%
df_temp = df_new.replace('nan','')
df_temp2 = df_temp.replace('', np.nan, regex=True)
df_temp2.head()

df_temp3 = df_temp2.loc[df_temp2['ASIN'].notnull()]

df_temp3.to_csv('./output/product_output/headphones_details_fin.csv')
