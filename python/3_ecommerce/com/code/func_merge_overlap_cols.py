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


######### trials with different methods to combine/merge columns###########
#%%
# ref: https://www.journaldev.com/33320/pandas-concat-examples
# ref: https://queirozf.com/entries/pandas-dataframe-union-and-concat-examples

import pandas as pd 
import numpy as np 

#test1
d1 = {"Name": ["Jia", "Lisa"], "ID": [1, 2], "Date" : [np.nan,'2021-04-10'], "Type" : ['A', 'B'], "Age" : [34, 27]}
d2 = {"Name": ["Alex","Max",''], "ID": [1, 3, 4], "Date": ['2021-04-10','','2021-04-09'], "Type": ['B','O','AB'], "Age" : [28, 20, 25]}

df1 = pd.DataFrame(d1, index={1, 2})
df2 = pd.DataFrame(d2, index={1, 3, 4})

#test2 

df_1 = pd.DataFrame(
	[['Tom', 68, 84, 78, 96],
	['Lina', 74, 56, 88, 85],
	['Jin', 77, 73, 82, 87]],
	columns=['name', 'physics', 'chemistry','algebra','calculus'])

df_2 = pd.DataFrame(
	[['Ameli', 72, 67, 91, 83],
	['Lin', 78, 69, 87, 92]],
	columns=['name', 'physics', 'algebra','history','literature'])	

#concatenate dataframes
df = pd.concat([df_1, df_2], sort=False)
#reset index
df.reset_index(drop=True, inplace=True)
#print dataframe 
print(df)

#%%

#  concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
#            keys=None, levels=None, names=None, verify_integrity=False,
#            sort=None, copy=True)

# concatenate dataframes with 
    # same indexes
    # similar columns
    # while keeping the duplicates 


# merge columns
df12_concat = pd.concat([df1, df2], axis=1)
# concat() makes two columns with same name

df12_join = df1.join(df2, lsuffix="_1", rsuffix="_2")
# join() makes two columns with suffix

df12_merge = pd.merge(df1, df2, how = "outer")
# merge() makes one column, by adding rows instead of merging two columns with same name based on the original index

df12_merge2 = pd.merge(df1, df2, how = "outer", left_index=True, right_index=True)
# same as df12_join

df12_merge3 = pd.merge(df1, df2, how = "outer", left_on=df1.index)
# this doesn't work because df1 and df2 have different size 

df12_append = df1.append(df2)
# this replace the string values from df1 with nan values from df2

df12_combine = df1.copy()
df12_combine['Color_fin'] = df1['Color'].combine_first(df2['Color'])

# merge method2: = pd.concat(df1, test4), axis=1) 
# but when I used pd.merge (index is reset; original index is lost)
# and couldn't find how to remove overlapping columns after concatenation, e.g. 'Brand' 

# merge method1
# df1: merge/join non overlapping columns
# df2: additional dataframe with overlapping columns

# compare overlapping column in two df 
# if the value is not None, 
# take it as a value for target_column

# df12_merge = pd.merge(df1,df2, how = "outer", left_index=True, right_index=True)
# df123_merge = pd.merge(df12_merge,test3, how = "outer", left_index=True, right_index=True)

# intersection1 = list(set(list(df1.columns)) & set(list(df2.columns)))

## merge values in those columns
# df_temp = df.replace(np.nan, '', regex=True)
# df["ASIN"] = df_temp["ASIN"] + df_temp["ASIN_3"] + df_temp["ASIN_4"]