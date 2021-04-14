#%% load dataset (search_output, product_output)
import pandas as pd

item = 'Headphones' #Headphones

#%%
s = pd.read_json('./output/search_output/' + item +'_summary.jsonl')
p = pd.read_json('./output/product_output/' + item +'_details.jsonl')

# %%
s.head()
p.head()
print('columns in product_summary:',s.columns)
print('columns in product_details:',p.columns)

# %% Main - (run the function 'trans_dict' below before running this cell)

product_df_names = ['product_overview','product_tech_spec','product_tech_spec2','product_info', 'customer_reviews_detail'] 
product_df_names2 = [x for x in list(p.columns) if x not in product_df_names] 

df_all = []

for item in product_df_names:
    data = p[item]
    print(item)
    df = trans_dict(data)
    df[['type']] = [item] * len(df)
    df_all.append(df)
#%%
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

# display all columns: pd.set_option('display.max_columns', None)

#%% function - clean df

# check name of each dataframe - each df has 'nametag' in the column 'type'
for i in range(len(df_all)):
    print(i, df_all[i].type[0])

df_product_overview = df_all[0]
df_product_tech_spec = df_all[1]
df_product_tech_spec2 = df_all[2]
df_product_info = df_all[3]
df_customer_reviews_detail = df_all[4]

# merge df
# merge dataframes by using append() to keep the original index (n=7663)
test1 = df_product_overview
test2 = df_product_tech_spec
test3 = df_product_tech_spec2
test4 = df_product_info

test12_merged = test1.append(test2)
test123_merged = test12_merged.append(test3)
test1234_merged = test123_merged.append(test4)

test1_new = test1.join(test2, lsuffix="_left", rsuffix="_right")

# merge columns
test1_new['Brand_left'] = test1_new['Brand_left'].combine_first(test1_new['Brand_right'])

test12_new = pd.concat([test1, test2], axis=1)
# merge method2: = pd.concat(test1, test4), axis=1) 
# but when I used pd.merge (index is reset; original index is lost)
# and couldn't find how to remove overlapping columns after concatenation, e.g. 'Brand' 
test1234_merged[['index']] = test1234_merged.index


# remove columns with NaN more than 95%
test1234_dropped = test1234_merged.loc[:, test1234_merged.isnull().mean() <= .95]
test1234_dropped.shape

# target csv formatting
sample_list = ['ASIN','Best Sellers Rank','Product Dimensions','Package Dimensions','Item Weight','Date First Available','Is Discontinued By Manufacturer','Item model number','Batteries','Card Description','Voltage','Series','National Stock Number','Chipset Brand','Date First Available','Batteries Required?','Wireless Type','Standing screen display size','Max Screen Resolution','Part Number','Item Package Quantity','Color','Brand','Number of USB 3.0 Ports','Memory Speed','Graphics Coprocessor','Computer Memory Type','Number of USB 2.0 Ports','Average Battery Life (in hours)','Graphics Card','Ram Size','Processor Count']


#%%

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
# remove merged cols
test_df_new = test_df.drop(columns = ['Product Dimensions', 'Package Dimensions', 'Item Dimensions  LxWxH', 'Item Weight'])

# remove columns with NaN more than 80%
temp_merge2_dropped2 = temp_merge2_dropped.loc[:, temp_merge2_dropped.isnull().mean() <= .8]

temp_merge2_dropped2.shape

test = temp_merge2_dropped2[:3]
my_pound = oz2lb(my_val_ounce)
test['Item Weight'] = test['Item Weight'].apply(lambda a: str(a).replace('ounces','/16'))
test['Item Weight'] = test['Item Weight'].apply(lambda a: str(a).replace('ounces/16',''))

df_temp['rating'] = df['rating'].apply(lambda a: str(a)[:3])


# cleaning details
# convert ounces to pounds
def oz2lb(my_val_ounce):
    my_val_pounds = my_val_ounce / 16
    print (my_val_ounce, 'Ounces =', my_val_pounds, 'Pounds')
    return my_val_pounds

#%% function: trans_dict 


def trans_dict(my_data):
    data_new = [] 
    data_none = []

    # transform dict
    for i in range(len(my_data)):
        #if my_data[i] is not None:
        try:    #temp = data.copy()
            product_info_list = []
            for target in my_data[i]:
                data_item_key = target['info']
                data_item_val = target['value']
                data_dict_new = {data_item_key : data_item_val}
                product_info_list.append(data_dict_new)
            #data_new_val = product_info_dict
            #temp[i] = data_new_val
            data_new.append(product_info_list)
        except:
#            print('none value in raw:',i)
            data_none.append(str(i))
#            data_new.append([x for x in my_data[i] if x.strip()])
            pass
#            product_info_list = []
            data_dict_new = {'info': 'NaN'}
            data_new.append(product_info_list)
            product_info_list.append(data_dict_new)
    print('Items with non value:',len(data_none))
    print(len(my_data))
    print(len(data_new))
    #print(data_none)

    # create my_df from each item dictionary after unwrapping from a list
    for i in range(len(data_new)):
        if data_new[i] is not None:
            try:
                my_dict_list = data_new[i]
                my_dict_fin = {}
                for d in my_dict_list:
                    my_dict_fin.update(d)
                data_new[i] = my_dict_fin
            except:
                continue

        data_dict = data_new      

    # merge all item dictionaries into one dataframe
    my_df = pd.DataFrame.from_dict(data_dict)
    print(len(my_df.isnull().sum()))

    return my_df


#%% ================ pieces of codes ================


# select rows with values in each dataframe
temp_df_product_tech_spec_new = df_product_tech_spec.loc[df_product_tech_spec['info'] != 'NaN',:]
temp_df_product_tech_spec2_new = df_product_tech_spec2.loc[df_product_tech_spec2['info'] != 'NaN',:]


# check overlapping columns between dataframes using intersection
test1 = df_product_overview
test4 = df_product_info
test_merge1 = test1.append([test4])
test_merge1.columns 
intersection1 = list(set(list(test1.columns)) & set(list(test4.columns)))

# keep only overlapping columns across dataframes
temp_merge2_dropped = temp_merge2.drop(columns = [col for col in temp_merge2 if col not in intersection])


# so many overlapping columns
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