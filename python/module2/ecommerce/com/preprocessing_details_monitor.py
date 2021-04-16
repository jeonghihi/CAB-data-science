#%% load dataset (search_output, product_output)
import pandas as pd
import numpy as np

item = 'Monitor' #'Headphones'

s = pd.read_json('./output/search_output/' + item +'_summary.jsonl')
p = pd.read_json('./output/product_output/' + item +'_details.jsonl')
p2 = pd.read_json('./output/product_output/' + item +'_add.jsonl')

# %% check columns
s.head()
p.head()
print('columns in product_summary:',s.columns)
print('columns in product_details:',p.columns)

# column names in three datasets
product_df_names = ['product_overview','product_tech_spec','product_tech_spec2','product_info'] 
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

#%%
# check name of each dataframe - each df has 'nametag' in the column 'type'
for i in range(len(df_all)):
    print(i, df_all[i].type[0])

df_product_overview = df_all[0]
df_product_tech_spec = df_all[1]
df_product_tech_spec2 = df_all[2]
df_product_info = df_all[3]

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

# for i in range(len(df_list2_all['freq_bought_2_info'])):
#     try:
#         df_list2_all['freq_bought_2_info'][i] = [df_list2_all['freq_bought_2_info'][i][1]]
#     except:
#         print('none value:',i)
#         continue

col_drop = ['link_to_all_reviews2']
df_list2_all = df_list2_all.drop(columns = col_drop)

df_list2_all.columns = ['product_name', 'seller', 'seller_link', 'seller2', 'seller_link2','freq_bought', 'freq_bought_link', 'link_to_all_reviews']
col_order = ['product_name', 'seller', 'seller_link', 'seller2', 'seller_link2','freq_bought', 'freq_bought_link', 'link_to_all_reviews']
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
temp_ordered = temp[sorted(list(temp.columns))]

# remove columns with NaN more than 95%
temp_dropped = temp_ordered.loc[:, temp_ordered.isnull().mean() <= .99]

df_list3_new = pd.concat([df_list3_all, temp_dropped], axis=1)


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

df_list3_new2_col = []
for item in list(df_list3_new2.columns):
    item = item.lower()
    new = item.replace(" ","_")
    df_list3_new2_col.append(new)

df_list3_new2.columns = df_list3_new2_col
df_list3_new2.columns = ['ASIN', 'freq_bought_info', 'customer_reviews',
       'customer_reviews_detail', 'best_seller_rank', 'link_to_all_reviews',
       'asin', 'batteries', 'batteries_Required?', 'brand', 'brand_name',
       'color', 'colour', 'computer_memory_Type', 'date_first_available',
       'department', 'graphics_coprocessor', 'hardware_platform',
       'discontinued_by_mfg', 'product_dimensions',
       'product_weight', 'Item_model_number', 'Language', 'manufacturer',
       'Manufacturer_Part_Number', 'Material_Type', 'Max_Screen_Resolution',
       'Number_of_Items', 'Number_of_USB_2.0_Ports', 'Number_of_USB_3.0_Ports',
       'Operating_System', 'Package_Dimensions', 'Power_Source',
       'Processor_Brand', 'Processor_Count', 'product_dimensions', 'RAM',
       'Screen_Resolution', 'Series', 'Size', 'Standing_screen_display_size',
       'Voltage', 'Wireless_Type', 'info', 'seller', 'seller_link']

col_order = ['ASIN', 'asin', 'brand', 'brand_name','seller', 'seller_link',
        'freq_bought_info', 'customer_reviews','manufacturer', 'discontinued_by_mfg',
       'customer_reviews_detail', 'best_seller_rank', 'link_to_all_reviews',
       'batteries', 'batteries_Required?', 'Screen_Resolution',
       'Size', 'Standing_screen_display_size',
       'color', 'colour', 'computer_memory_Type', 'date_first_available',
       'department', 'graphics_coprocessor', 'hardware_platform',
       'Package_Dimensions', 'product_dimensions','product_weight', 
       'Item_model_number', 'Language', 
       'Manufacturer_Part_Number', 'Material_Type', 'Max_Screen_Resolution',
       'Number_of_Items', 'Number_of_USB_2.0_Ports', 'Number_of_USB_3.0_Ports',
       'Operating_System', 'Power_Source',
       'Processor_Brand', 'Processor_Count', 'product_dimensions', 'RAM',
       'Series', 'Voltage', 'Wireless_Type', 'info']

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
df_details.columns = ['ASIN', 'Batteries', 'Batteries Required?', 'Date First Available',
       'Is Discontinued By Manufacturer', 'Item model number',
       'Package Dimensions', 'Product Dimensions', 'product_name', 'seller',
       'seller_link', 'seller2', 'seller_link2', 'freq_bought',
       'freq_bought_link', 'link_to_all_reviews']

temp = []
for item in list(df_details.columns):
    item = item.lower()
    new = item.replace(" ","_")
    temp.append(new)

df_details.columns = temp

df_details.columns = ['ASIN', 'batteries', 'batteries_required?', 'date_first_available',
       'discontinued_by_mfg  ', 'item_model_number',
       'package_dimensions', 'product_dimensions', 'product_name', 'seller',
       'seller_link', 'seller2', 'seller_link2', 'freq_bought',
       'freq_bought_link', 'link_to_all_reviews']

col_order = ['ASIN', 'product_name', 'seller', 'seller_link', 'seller2', 'seller_link2',
       'batteries', 'batteries_required?', 'date_first_available',
       'discontinued_by_mfg  ', 'item_model_number',
       'package_dimensions', 'product_dimensions', 'freq_bought',
       'freq_bought_link', 'link_to_all_reviews']

df_details = df_details[col_order]

df_add = df3_fin

# save as csvfile
item = 'Monitor'

df_details.to_csv('./output/product_output/' + item +'_details.csv')
df_add.to_csv('./output/product_output/' + item +'_add.csv')


