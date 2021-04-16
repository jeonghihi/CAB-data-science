import pandas as pd
import numpy as np 


df_test = pd.DataFrame([1,2,3], columns = ['index_nr']) 

########################## working final - search overlap and remove columns

df = df_test.copy()
df_new = df.copy()
df_new = df.replace(np.nan, '', regex=True) 

cols = sorted(list(df.columns))


col_dict_list = []
cols_to_merge = []
cols_uni = []

for col in cols:
    overlapping_cols = [col for col in cols if "_" in col]
    if col in overlapping_cols:
        col_origin = col.partition("_")[0]
        col_variations = col
        # save info as dict
        if col_origin not in cols_to_merge:
            cols_to_merge.append(col_origin)
            col_dict = {}
            col_dict.setdefault(col_origin,[])
            col_dict[col_origin].append(col_variations)
            if col_dict not in col_dict_list:
                col_dict_list.append(col_dict)
        else:
            col_dict = [item_dict for item_dict in col_dict_list if col_origin in list(item_dict)[:]]
            col_dict = col_dict[0]
            #print(col_dict)
            col_dict[col_origin].append(col_variations)
            #print(col_dict)
            #print(col_origin)
    else:
        cols_uni.append(col)

for col in cols_to_merge:
    col_dict = [item_dict for item_dict in col_dict_list if col in list(item_dict)[:]]
    my_dict_keys = list(col_dict[0].values())[:][0]
    print(my_dict_keys)
    
    for item in my_dict_keys:
        print(col)
        print(item)
        try:
            df[col] = df_new[col] + df_new[item]
            df.drop(columns=item, inplace=True)
        except:
            df[col] = []
            df[col] = df_new[item]
            continue
        
        print('dict_replaced')
 ##########################################



df_test = pd.DataFrame([1,2,3], columns = ['index_nr']) 

# check overlapping columns
cols = sorted(list(df_test.columns))
#'ASIN', 'ASIN_3',  'ASIN_4',
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

# source: https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
cols = ['info_1', 'info_2', 'info_5', 'type_1', 'type_2','ASIN']
col_dict_list = []
cols_to_merge = []
cols_uni = []

for col in cols:
    overlapping_cols = [col for col in cols if "_" in col]
    if col in overlapping_cols:
        col_origin = col.partition("_")[0]
        col_variations = col
        # save info as dict
        if col_origin not in cols_to_merge:
            cols_to_merge.append(col_origin)
            col_dict = {}
            col_dict.setdefault(col_origin,[])
            col_dict[col_origin].append(col_variations)
            if col_dict not in col_dict_list:
                col_dict_list.append(col_dict)
        else:
            col_dict = [item_dict for item_dict in col_dict_list if col_origin in list(item_dict)[:]]
            col_dict = col_dict[0]
            #print(col_dict)
            col_dict[col_origin].append(col_variations)
            #print(col_dict)
            #print(col_origin)
    else:
        cols_uni.append(col)


######### trials ###########


# merge columns
test12_concat = pd.concat([test1, test2], axis=1)
# concat() makes two columns with same name

test12_join = test1.join(test2, lsuffix="_1", rsuffix="_2")
# join() makes two columns with suffix

test12_merge = pd.merge(test1, test2, how = "outer")
# merge() makes one column, by adding rows instead of merging two columns with same name based on the original index

test12_merge2 = pd.merge(test1, test2, how = "outer", left_index=True, right_index=True)
# same as test12_join

test12_merge3 = pd.merge(test1, test2, how = "outer", left_on=test1.index)
# this doesn't work because test1 and test2 have different size 

test12_append = test1.append(test2)
# this replace the string values from test1 with nan values from test2

test12_combine = test1.copy()
test12_combine['Color_fin'] = test1['Color'].combine_first(test2['Color'])

# merge method2: = pd.concat(test1, test4), axis=1) 
# but when I used pd.merge (index is reset; original index is lost)
# and couldn't find how to remove overlapping columns after concatenation, e.g. 'Brand' 



# method1
df1: merge/join non overlapping columns
df2: additional dataframe with overlapping columns

compare overlapping column in two df 
if the value is not None, 
take it as a value for target_column

test12_merge = pd.merge(test1,test2, how = "outer", left_index=True, right_index=True)
test123_merge = pd.merge(test12_merge,test3, how = "outer", left_index=True, right_index=True)

intersection1 = list(set(list(test1.columns)) & set(list(test2.columns)))

# merge values in those columns
df_temp = df.replace(np.nan, '', regex=True)
df["ASIN"] = df_temp["ASIN"] + df_temp["ASIN_3"] + df_temp["ASIN_4"]