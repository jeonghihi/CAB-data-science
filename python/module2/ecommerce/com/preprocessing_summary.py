#%% load dataset

import pandas as pd
item = 'Headphones' #Monitor
df = pd.read_json('./output/search_output/' + item + '_summary.jsonl')
df.head()

# %% initial check with data 
# check missing values:
# Monitor - rating/review:1309, price:1747
# Headphones - rating/review:311, price:488
print(df.isnull().sum()) 

# number of unique items: 
# Monitor - 5553 of 7452
# Headphones - 5688 of 7470
print(len(set(df.title)))
print(df.isnull().sum()/len(set(df.title)))

# add column 'prod_type'
df.loc[:, 'prod_type'] = 'headphones'

#%% clean data-rating and price 

def clean(df):
    # clean strings
    #for i in range(len(df)):
    df_temp = df.fillna("NaN")
    df_temp['rating'] = df['rating'].apply(lambda a: str(a)[:3])
    df_temp['price'] = df['price'].apply(lambda a: str(a).replace('$',''))
    df_temp['review_count'] = df['review_count'].apply(lambda a: str(a).replace(',',''))  
        #df_temp.loc[i,'price'] = df.loc[i,'price'].replace(',','')
        #print('Sorry lets move on')
    df_temp = df_temp.replace("NaN",'')
    df_cleaned = df_temp
    return df_cleaned
    
#%%
df_cleaned = clean(df)

# s['rating'] = s['rating'].map(lambda x: x.strip('')[0:3])
# s[['review_count']] = s[['review_count']].fillna(value= '0')
# s['review_count'] = s['review_count'].replace(',','', regex=True)

# s['price'] = s['price'].replace(',','', regex=True)
# s.price = s.price.astype('float')

print(df_cleaned.isnull().sum())
# %% save preprocessed data
df_cleaned.columns = ['title', 'url', 'rating', 'review_count', 'price', 'ASIN', 'prod_type']
df_cleaned = df_cleaned[['ASIN', 'title', 'price', 'rating', 'review_count', 'url', 'prod_type']]

df_cleaned.to_csv('./output/summary_headphones_com.csv', index= None)

#%% =================== other functions ===================
def convert_dtype(df):
    df_temp = df
    # change data type: rating/review_count as float, title/utl as string
    string_cols = ['title', 'url', 'prod_type', 'asin']
    float_cols = ['rating', 'review_count', 'price']
    for col in string_cols:
        df_temp[col] = df_temp[col].astype('string')
    for col in float_cols:   
        df_temp[col] = df_temp[col].astype('float')

    df_typed = df_temp
    return df_typed

#%% get ASIN from url
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
