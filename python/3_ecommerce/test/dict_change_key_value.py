#%%
import pandas as pd
temp = pd.read_csv('temp_dict.csv')

temp['product_summary']
temp_0_list = temp['product_summary'][0]
temp_product_summary_0_dict = temp_0_list[0]
# %%
# method1
# source: https://stackoverflow.com/questions/20817747/replace-value-of-dictionary-with-key-from-another-dictionary
# source: https://stackoverflow.com/questions/30418481/error-dict-object-has-no-attribute-iteritems

d0 = temp_product_summary_0_dict
d1 = {v:k for k,v in d0.items()}

d2 = {v:d1[k] for k,v in d1.items()}

# method2 
temp_product_summary_0_dict.keys() 
temp_product_summary_0_dict.values()

# dict values into list
temp_product_summary_0_dict_keys = list(temp_product_summary_0_dict)[:]
temp_product_summary_0_dict_values = list(temp_product_summary_0_dict.values())[:]

# replace with new_dict
temp_product_summary_0_dict_new = dict(zip(temp_product_summary_0_dict_values,temp_product_summary_0_dict_keys))

#%% dictionary - dataframe tips
# https://appdividend.com/2020/03/06/python-how-to-add-append-key-value-pairs-in-dictionary/
# https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe