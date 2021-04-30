#%% load dataset

import pandas as pd
df = pd.read_json('../../output/search/search_output_monitor.jsonl')
df.head()

# %% initial check with data 
# check missing values: rating/review:19, price:13
print(df.isnull().sum()) 

# number of unique items: 186
len(set(df.title)) 

# add column 'prod_type'
df.loc[:, 'prod_type'] = 'monitor'

#%% clean data-rating and price 

def clean(df):
    # clean strings
    for i in range(len(df)):
        df_temp = df.fillna("NaN")
        try:
            char_to_replace = {',': '.',
                            '€': 'euro'}
            for key, value in char_to_replace.items():
                df_temp.loc[i,'rating'] = df_temp.loc[i,'rating'][:3].replace(key,value)
                df_temp.loc[i,'price'] = df_temp.loc[i,'price'].replace(key,value)
        except:
            continue
        #print('Sorry lets move on')

    # change data type: rating/review_count as float, title/utl as string
    string_cols = ['title', 'url', 'prod_type']
    float_cols = ['rating', 'review_count']
    for col in string_cols:
        df_temp[col] = df_temp[col].astype('string')
    for col in float_cols:   
        df_temp[col] = df_temp[col].astype('float')

    df = df_temp
    return df

df_cleaned = clean(df)
#%% get ASIN 
# source: https://stackoverflow.com/questions/8162021/analyzing-string-input-until-it-reaches-a-certain-letter-on-python

def get_asin(df_cleaned):
    temp_asin = df_cleaned
    temp_url = temp_asin.loc[:,'url']
    temp_url_df = pd.DataFrame(temp_url)

    for row in range(len(temp_url_df)):
        my_text = temp_url_df.loc[row, 'url'] 
        division_tag1 = str(r"%2Fdp%2F")
        division_tag2 = str('/dp/')
        if division_tag1 in my_text:
            right_text = my_text.partition(division_tag1)[2] 
        else:
            right_text = my_text.partition(division_tag2)[2] 
        temp_url_df.loc[row, 'right_text'] = right_text
        
        my_text2 = temp_url_df.loc[row, 'right_text'] 
        division_tag1 = str(r"%2F")
        division_tag2 = str('/')
        if division_tag1 in my_text2:
            target_text = my_text2.partition(division_tag1)[0] 
        else:
            target_text = my_text2.partition(division_tag2)[0] 
        temp_url_df.loc[row, 'ASIN'] = target_text
        temp_url_df = temp_url_df[['url','ASIN']]

    print(temp_url_df.head())
    out_df = df_cleaned.merge(temp_url_df, on='url')

    return out_df 

df_asin = get_asin(df_cleaned)

#%% check all values are valid

print(df_asin.dtypes)
print(df_asin.isnull().sum())

# %% save preprocessed data
df_asin.to_csv('../../output/summary/summary_monitor.csv', index= None)
# %%
