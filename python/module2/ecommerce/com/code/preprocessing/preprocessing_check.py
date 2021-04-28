# %% 
import pandas as pd 
import numpy as np

# %%

item = 'monitor'

df_details_fin = pd.read_csv('./output/product_output/' + item +'_details.csv', index_col = 0)
df_add_fin = pd.read_csv('./output/product_output/' + item +'_add.csv', index_col = 0)

df_details_fin["ASIN"] = df_details_fin["ASIN"].apply(lambda a: str(a).rstrip())    # Apply rstrip function

# %%
# df_join = df_details_fin.join(df_add_fin, how='outer', lsuffix="_1", rsuffix="_2")

df_details_fin_temp = df_details_fin.fillna('').astype(str)
df_add_fin_temp = df_add_fin.fillna('').astype(str)

try:
    test_merged2 = pd.concat([df_add_fin_temp, df_details_fin_temp], axis=1, verify_integrity=True)
except ValueError as e:
    print('ValueError', e)

same_cols = ['ASIN', 'seller', 'seller_link', 'batteries', 'date_first_available',
            'discontinued_by_mfg', 'product_dimensions', 'link_to_all_reviews']

df_merge = pd.merge(df_details_fin_temp, df_add_fin_temp, on= same_cols, how='outer')

df_merge2 = df_merge.sort_values('ASIN').drop_duplicates(subset=['freq_bought_info','customer_reviews'])
df_merge_new = df_merge2.replace('', np.nan, regex=True)

test = df_merge_new.copy()

temp = df_merge_new.reset_index()

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

drop_cols = ['seller2', 'seller_link2','Package_Dimensions']
df_merge_fin = temp.drop(columns = drop_cols)

df_merge_fin_col_new = []

for item in list(df_merge_fin.columns):
    item = item.lower()
    df_merge_fin_col_new.append(item)

#%%
df_merge_fin.columns = ['index',
 'ASIN',
 'product_name',
 'seller',
 'seller_link',
 'batteries',
 'batteries_required?',
 'date_first_available',
 'discontinued_by_mfg',
 'item_model_number',
 'package_dimensions',
 'product_dimensions',
 'freq_bought',
 'freq_bought_link',
 'link_to_all_reviews',
 'brand',
 'freq_bought_info',
 'customer_reviews',
 'manufacturer',
 'customer_reviews_detail',
 'best_seller_rank',
 'batteries_Required?',
 'Screen_Resolution',
 'Size',
 'Standing_screen_display_size',
 'color',
 'computer_memory_Type',
 'department',
 'graphics_coprocessor',
 'hardware_platform',
 'product_weight',
 'Item_model_number',
 'Language',
 'Manufacturer_Part_Number',
 'Material_Type',
 'Max_Screen_Resolution',
 'Number_of_Items',
 'Number_of_USB_2.0_Ports',
 'Number_of_USB_3.0_Ports',
 'Operating_System',
 'Power_Source',
 'Processor_Brand',
 'Processor_Count',
 'RAM',
 'Series',
 'Voltage',
 'Wireless_Type',
 'info']

col_order = ['index',
 'ASIN',
 'product_name',
 'package_dimensions',
 'product_dimensions',
 'product_weight',
 'freq_bought_info',
 'freq_bought_link',
 'freq_bought',
 'link_to_all_reviews',
 'date_first_available',
 'discontinued_by_mfg',
 'customer_reviews',
 'customer_reviews_detail',
 'seller',
 'seller_link',
 'best_seller_rank',
 'department',
 'brand',
 'manufacturer',
 'Size',
 'color',
 'batteries',
 'batteries_required?',
 'item_model_number',
 'batteries_Required?',
 'Screen_Resolution',
 'Standing_screen_display_size',
 'computer_memory_Type',
 'graphics_coprocessor',
 'hardware_platform',
 'Item_model_number',
 'Language',
 'Manufacturer_Part_Number',
 'Material_Type',
 'Max_Screen_Resolution',
 'Number_of_Items',
 'Number_of_USB_2.0_Ports',
 'Number_of_USB_3.0_Ports',
 'Operating_System',
 'Power_Source',
 'Processor_Brand',
 'Processor_Count',
 'RAM',
 'Series',
 'Voltage',
 'Wireless_Type',
 'info']


df_merge_fin = df_merge_fin[col_order]

for i in range(len(df_merge_fin)):
    if type(df_merge_fin.loc[i,'freq_bought_info']) is str:
        try:
            df_merge_fin.loc[i,'freq_bought_info'] = df_merge_fin.loc[i,'freq_bought_info'][32:]
        except:
            pass
    else:
        print('none:',i)
        continue

df_merge_fin.to_csv('./output/product_output/monitor_detail_fin.csv')

# %% fin check

item = 'monitor'
df = pd.read_csv('./output/product_output/monitor_detail_fin.csv', index_col=0)

# %%
