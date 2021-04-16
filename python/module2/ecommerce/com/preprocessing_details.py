#%% load dataset (search_output, product_output)
import pandas as pd
import numpy as np

item = 'Headphones'

s = pd.read_json('./output/search_output/' + item +'_summary.jsonl')
p = pd.read_json('./output/product_output/' + item +'_details.jsonl')
p2 = pd.read_json('./output/product_output/' + item +'_add.jsonl')

# %% check columns
s.head()
p.head()
print('columns in product_summary:',s.columns)
print('columns in product_details:',p.columns)

# column names in three datasets
product_df_names = ['product_overview','product_tech_spec','product_tech_spec2','product_info', 'customer_reviews_detail'] 
product_df_names2 = [x for x in list(p.columns) if x not in product_df_names] 
p2.columns 

# %% Main - (run the function 'trans_dict.py' before continuing)
exec(open("preprocessing_details_transform_dict.py").read())

#%% ==================================== clean df1

col_list1 = product_df_names
df_all = []

for item in col_list1:
    data = p[item]
    print(item)
    df = trans_dict(data)
    df[['type']] = [item] * len(df)
    df_all.append(df)

# Headphones: 
# product_df_names = ['product_overview','product_tech_spec','product_tech_spec2','product_info', 'freq_bought_2_info','customer_reviews_detail'] 
# product_overview, Items with non value: 1452
# product_tech_spec, Items with non value: 7137
# product_tech_spec2, Items with non value: 7450
# product_info, Items with non value: 206
# customer_reviews_detail, Items with non value: 1

# check non-values in each dataframe
for i in range(len(df_all)):
    print(i)
    print(df_all[i].type[0])
    df_all[i].info()

# check name of each dataframe - each df has 'nametag' in the column 'type'
for i in range(len(df_all)):
    print(i, df_all[i].type[0])

df_product_overview = df_all[0]
df_product_tech_spec = df_all[1]
df_product_tech_spec2 = df_all[2]
df_product_info = df_all[3]
df_customer_reviews_detail = df_all[4]

# display all columns: pd.set_option('display.max_columns', None)
#%% continue - clean df1

# ============ merge df with suffixes for overlapping columns, 
# ============ while keeping the original index (n=7663)
test12_join = df_product_overview.join(df_product_tech_spec, lsuffix="_1", rsuffix="_2")
test123_join = test12_join.join(df_product_tech_spec2, lsuffix="_3", rsuffix="_4")
test1234_join = test123_join.join(df_product_info, lsuffix="_5", rsuffix="_6")

df_join = test1234_join.drop(columns=['info_5','info_6','type_5','type_6'])

# select target columns
target_cols = ['ASIN','Best Sellers Rank','Brand Name','Product Dimensions','Package Dimensions','Item Weight','Date First Available','Is Discontinued By Manufacturer','Item model number','Batteries','Date First Available','Batteries Required?','Wireless Type','Color','Brand']
my_list = list(df_join.columns)
cols_keep = []
cols_etc = []

for item in my_list:
    try:
        template = item.partition("_")[0]
        #print(template)
        if template in target_cols:
            if item not in cols_keep:
                cols_keep.append(item)
        else:
            cols_etc.append(item)
    except:
        pass

# ============ reorder columns and remove unnecessary columns
df1 = df_join
df1.columns 

df1_new = df1[sorted(list(df1.columns))]
df_filtered = df1_new.drop(columns=cols_etc)

# ============ merge values in overlapping columns
# check overlapping columns
cols = sorted(list(df_filtered.columns))
cols_to_merge = []
cols_to_be_merged = [] 

for col in cols:
    overlapping_cols = [col for col in cols if "_" in col]
    for col in overlapping_cols:
        col_origin = col.partition("_")[0]
        col_variations = col
        if col_origin not in cols_to_merge:
            cols_to_merge.append(col_origin)
        if col_variations not in cols_to_be_merged:
            cols_to_be_merged.append(col_variations)

# merge cols one by one
df_filtered_temp = df_filtered.replace(np.nan, '', regex=True)
df_filtered["ASIN"] = df_filtered_temp["ASIN"] +" "+ df_filtered_temp["ASIN_3"] +" "+ df_filtered_temp["ASIN_4"]
df_filtered["ASIN"] = df_filtered['ASIN'].apply(lambda a: str(a)[:10])
df_filtered["ASIN"] = df_filtered["ASIN"].replace(r'^\s*$', np.nan, regex=True)

df_filtered["Brand Name_5"] = df_filtered_temp["Brand Name_5"] +" "+ df_filtered_temp["Brand Name_6"]
df_filtered["Brand_1"] = df_filtered_temp["Brand_1"] +" "+ df_filtered_temp["Brand_2"] +" "+ df_filtered_temp["Brand_5"] +" "+ df_filtered_temp["Brand_6"]

df_filtered['Batteries_3'] = df_filtered_temp['Batteries_3'] +" "+  df_filtered_temp['Batteries_4']
df_filtered['Date First Available_3'] = df_filtered_temp['Date First Available_3'] +" "+  df_filtered_temp['Date First Available_4']
df_filtered['Is Discontinued By Manufacturer_3'] = df_filtered_temp['Is Discontinued By Manufacturer_3'] +" "+  df_filtered_temp['Is Discontinued By Manufacturer_4']
df_filtered['Item Weight_1'] = df_filtered_temp['Item Weight_1'] +" "+  df_filtered_temp['Item Weight_2'] +" "+  df_filtered_temp['Item Weight_5'] +" "+  df_filtered_temp['Item Weight_6']
df_filtered['Product Dimensions_3'] = df_filtered_temp['Product Dimensions_3'] +" "+  df_filtered_temp['Product Dimensions_4']
df_filtered['Package Dimensions_3'] = df_filtered_temp['Package Dimensions_3'] +" "+  df_filtered_temp['Package Dimensions_4']

# remove merged columns
df_dropped = df_filtered.drop(columns = cols_to_be_merged)
df_dropped = df_dropped.drop(columns='Best Sellers Rank') # this info will be available from other df

df1_fin = df_dropped
print(df1_fin.head())
print(df1_fin.info())
df1_fin.shape
# select rows with values in each dataframe
# df_dropped_nan = df_dropped.loc[df_dropped['ASIN'] == None,:]

#%% ==================================== clean - df2
product_df_names2

# 2 dataset
col_list2 = product_df_names2

df_list2 = []

for item in product_df_names2:
    key = item
    val = p[item]
    series_dict = {key: val}
    series_df = pd.concat(series_dict, axis=1)
    df_list2.append(series_df)
    
# combine all df in df_list 
df_list2_all = pd.concat(df_list2, axis=1)

for i in range(len(df_list2_all['freq_bought_2_info'])):
    try:
        df_list2_all['freq_bought_2_info'][i] = [df_list2_all['freq_bought_2_info'][i][1]]
    except:
        print('none value:',i)
        continue

col_drop = ['best_seller_rank','link_to_all_reviews2','freq_bought','freq_bought_link']
df_list2_all = df_list2_all.drop(columns = col_drop)

df_list2_all.columns = ['name', 'seller', 'seller_link', 'seller2', 'seller_link2','freq_bought', 'rating_details', 'link_to_all_reviews']
col_order = ['name', 'freq_bought', 'rating_details', 'link_to_all_reviews', 'seller', 'seller_link', 'seller2', 'seller_link2']
df_list2_fin = df_list2_all[col_order]

df2_fin = df_list2_fin

print(df2_fin.head())
print(df2_fin.info())
df2_fin.shape

#%% clean df3
col_list3 = list(p2.columns)

p2_origin = p2.copy()
#p2 = p2_origin

# include only necessary val from this col: ['seller_link_new']
# p2['seller_link_new'][0] = [p2['seller_link_new'][0][1]]
for i in range(len(p2['seller_link_new'])):
    try:
        p2['seller_link_new'][i] = [p2['seller_link_new'][i][1]]
    except:
        print('none value:',i)
        continue

# do not need to do anything with these cols
# ['asin'], ['product_info'], ['link_to_all_reviews'],['link_to_all_reviews2']

# merge dictionaries as df
df_list3 = []

for item in col_list3:
    key = item
    val = p2[item]
    series_dict = {key: val}
    series_df = pd.concat(series_dict, axis=1)
    df_list3.append(series_df)
    
# combine all df in df_list 
df_list3_all = pd.concat(df_list3, axis=1)

# from col(product_info), extract only 'Customer Reviews' and 'Best Sellers Rank'
temp = trans_dict(df_list3_all['product_info'])
temp2 = temp[['Customer Reviews', 'Best Sellers Rank']]
df_list3_new = pd.concat([df_list3_all, temp2], axis=1)

# from col(seller_link_new), seller and link in column separately
seller_df = pd.DataFrame([], columns=['seller','seller_link'])
temp = df_list3_all['seller_link_new']
for i in range(len(temp)):
    if temp[i] is not None:
        try:
            seller_df.loc[i,'seller'] = temp[1][0]['info']
            seller_df.loc[i,'seller_link'] = temp[1][0]['value']            
        except:
            pass
    else:
        seller_df.loc[i,'seller'] = None
        seller_df.loc[i,'seller_link'] = None        
        print('none values',i)

df_list3_new2 = pd.concat([df_list3_new, seller_df], axis=1)

# remove unnecessary cols and reorder cols
col_drop = ['seller_link_new', 'product_info', 'link_to_all_reviews2']
df_list3_new2 = df_list3_new2.drop(columns = col_drop)

df_list3_new2.columns = ['ASIN', 'link_to_all_reviews', 'ratings', 'best_sellers_rank', 'seller', 'seller_link']
col_order = ['ASIN','seller','seller_link','ratings','best_sellers_rank','link_to_all_reviews']

df_list3_fin = df_list3_new2[col_order]

df3_fin = df_list3_fin
print(df3_fin.head())
print(df3_fin.info())
df3_fin.shape

#%% ============================================= check final df

df1_fin.head()
df2_fin.head()
df3_fin.head()

df_details = pd.concat([df1_fin, df2_fin], axis=1)
df_details.columns = ['ASIN', 'batteries', 'date_first_available',
       'discontinued_by_mfg', 'item_model_nr',
       'package_dimensions', 'product_dimensions', 'product_name', 'freq_bought',
       'rating_details', 'link_to_all_reviews', 'seller', 'seller_link',
       'seller2', 'seller_link2']

col_order = ['ASIN', 'product_name', 'item_model_nr', 'package_dimensions', 'product_dimensions',
        'batteries', 'date_first_available', 'discontinued_by_mfg', 
        'seller', 'seller_link','seller2', 'seller_link2',
        'freq_bought','rating_details', 'link_to_all_reviews'
        ]
df_details = df_details[col_order]

df_add = df3_fin

# save as csvfile
item = ''
item = 'Headphones'

df_details.to_csv('./output/product_output/' + item +'_details.csv')
df_add.to_csv('./output/product_output/' + item +'_add.csv')



#%% ================ pieces of codes ================
# more cleaning details

df_temp['rating'] = df['rating'].apply(lambda a: str(a)[:3])
# convert ounces to pounds
def oz2lb(my_val_ounce):
    my_val_pounds = my_val_ounce / 16
    print (my_val_ounce, 'Ounces =', my_val_pounds, 'Pounds')
    return my_val_pounds

test = test_df[:3]
my_pound = oz2lb(my_val_ounce)
test['Item Weight'] = test['Item Weight'].apply(lambda a: str(a).replace('ounces','/16'))
test['Item Weight'] = test['Item Weight'].apply(lambda a: str(a).replace('ounces/16',''))


# remove columns with NaN more than 95%
test1234_dropped = test1234_merged.loc[:, test1234_merged.isnull().mean() <= .95]
test1234_dropped.shape

# target csv formatting
sample_list = ['ASIN','Best Sellers Rank','Product Dimensions','Package Dimensions','Item Weight','Date First Available','Is Discontinued By Manufacturer','Item model number','Batteries','Card Description','Voltage','Series','National Stock Number','Chipset Brand','Date First Available','Batteries Required?','Wireless Type','Standing screen display size','Max Screen Resolution','Part Number','Item Package Quantity','Color','Brand','Number of USB 3.0 Ports','Memory Speed','Graphics Coprocessor','Computer Memory Type','Number of USB 2.0 Ports','Average Battery Life (in hours)','Graphics Card','Ram Size','Processor Count']


#remove duplicated words
string1 = "calvin klein design dress calvin klein"
words = string1.split()
print(" ".join(sorted(set(words), key=words.index)))


# select rows with values in each dataframe
df_new = df.loc[df['info'] != 'NaN',:]


# merge columns with different names, but same type of values
# source: https://stackoverflow.com/questions/11858472/string-concatenation-of-two-pandas-columns
# first convert NaN float to string
test_df = temp_merge2_dropped.copy()
test_df['Product Dimensions'].astype(str)
test_df['Package Dimensions'].astype(str)
test_df['Item Dimensions  LxWxH'].astype(str)
test_df['Item Weight'].astype(str)

# merge
test_df["Item Dimensions"] = test_df.agg('{0[Product Dimensions]};{0[Package Dimensions]};{0[Item Dimensions  LxWxH]};{0[Item Weight]}'.format, axis=1)
test_df["Item Dimensions"] = test_df["Item Dimensions"].apply(lambda a: str(a).replace('nan',''))


# check overlapping columns between dataframes using intersection
test1 = df_product_overview
test4 = df_product_info
test_merge1 = test1.append([test4])
test_merge1.columns 
intersection1 = list(set(list(test1.columns)) & set(list(test4.columns)))

# keep only overlapping columns across dataframes
temp_merge2_dropped = temp_merge2.drop(columns = [col for col in temp_merge2 if col not in intersection])

# check many overlapping columns
try:
    test_merged2 = pd.concat([test1, test2, test3, test4], axis=1, verify_integrity=True)
except ValueError as e:
    print('ValueError', e)

# merge overlapping columns in 'df_product_details_merged'
len(test_merged.columns) # total columns: 322
len(set(test_merged.columns)) # unique columns: 193

# get the list of overlapping cols
uni_cols = []
for i in list(test_merged.columns):
    if i not in uni_cols:
        uni_cols.append(i)
len(uni_cols) #193

test_merged["Brand_fin"] = test_merged.agg('{0[Brand]};{0[Brand]};{0[Brand]};{0[Brand]}'.format, axis=1)
test_df["Item Dimensions"] = test_df["Item Dimensions"].apply(lambda a: str(a).replace('nan',''))

sample = test_merged['Brand']
# merge string values: sample = sample.apply(''.join, axis=1)
sample_new = sample.Brand.combine_first(sample.Brand)

combine_first(sample.Brand)

test_merged["Brand_fin"] = test_merged["Brand"].fillna(0)

test_merged_yesOverlap = test_merged.drop(columns = [col for col in test_merged if col not in uni_cols])
test_merged_nonOverlap = test_merged.drop(columns = [col for col in test_merged if col in uni_cols])


#%%
# select rows with no NaN
df_all_2 = []

for df in df_all:
    temp = df.copy()
    temp_new = temp.loc[temp['info'] != 'NaN',:]
    df_all_2.append(temp_new)


# merge string values after completing NaN as float 0 
df["Item Dimensions"] = df["Product Dimensions"].fillna(0) + df["Package Dimensions"].fillna(0) + df['Item Dimensions  LxWxH'].fillna(0)
df["Item Dimensions"].replace(0, np.nan, inplace=True)

# drop rows containing 99% NaN values 
perc = 99.0 
min_count =  int(((100-perc)/100)*df.shape[1] + 1)
mod_df = df.dropna( axis=0, 
                    thresh=min_count)

# 2 # transform dict
data = p['product_info']
data_new = [] 

for i in range(len(data)):
    try:
        #temp = data.copy()
        product_info_list = []
        for target in data[i]:
            data_item_key = target['info']
            data_item_val = target['value']
            data_dict_new = {data_item_key : data_item_val}
            product_info_list.append(data_dict_new)
        #data_new_val = product_info_dict
        #temp[i] = data_new_val
        data_new.append(product_info_list)
    except:
        continue

print(data_new)

# change column (product_overview) into one df 

# how to search key in the nested dict
# https://codereview.stackexchange.com/questions/201754/getting-a-keys-value-in-a-nested-dictionary
# https://www.geeksforgeeks.org/python-extract-selective-keys-values-including-nested-keys/
# https://stackoverflow.com/questions/7681301/search-for-a-key-in-a-nested-python-dictionary
# https://stackoverflow.com/questions/14692690/access-nested-dictionary-items-via-a-list-of-keys
# https://thispointer.com/python-how-to-check-if-a-key-exists-in-dictionary/

#search key for one/two level nested dict
# https://stackoverflow.com/questions/29339859/how-do-i-traverse-nested-dictionaries-python


# 3 # create my_df from each item dictionary within a list
# convert a list of multiple dictionaries into a single dict
# source: https://stackoverflow.com/questions/3494906/how-do-i-merge-a-list-of-dicts-into-a-single-dict
# source: https://stackoverflow.com/questions/58557213/how-to-convert-this-nested-dictionary-into-one-single-dictionary-in-python-3

for i in range(len(data_new)):
    my_dict_list = data_new[i]

    my_dict_fin = {}
    for d in my_dict_list:
        my_dict_fin.update(d)

    data_new[i] = my_dict_fin
    data_dict = data_new

print(data_dict)

# merge all item dictionaries into dataframe
my_df = pd.DataFrame.from_dict(data_new)
my_df.isnull().sum()

# check if all procedure is done correctly: 
len(data) == len(my_df) #True

#%% ================ test trials ================
product_info_dict = {}


temp = {val : key for key, val in product_info_dict.items()}
res = {val : key for key, val in temp.items()}
print(res)


result = {}

for key, value in product_info_dict.items():
    if value not in result.values():
        result[key] = value


product_info_dict = set(product_info_dict)
data[i] = product_info_dict

# search key/value within nested dict
def find_by_key(data, target):
    for k, v in data.items():
        if k == target:
            return v
        elif isinstance(v, dict):
            return find_by_key(v, target)
        elif isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    return find_by_key(i, target)

find_by_key(data, "info")

#  have a set of columns which cover all the columns of different products
my_l = []
for i in range(p.shape[0]):
    try:
        cols = [d['info'] for d in p.product_info[i]]
        my_l = list(set().union(cols,my_l))
    except:
        continue
    #when cols is NA
product_product_info_cols = my_l