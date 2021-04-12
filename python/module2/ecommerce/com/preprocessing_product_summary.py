#%% load dataset (search_output, product_output)
item = 'Monitor' #Headphones

import pandas as pd
#%%
s = pd.read_json('./output/search_output/' + item +'_summary.jsonl')
p = pd.read_json('./output/product_output/' + item +'_details.jsonl')

# %%
s.head()
p.head()
print('columns in product_summary:',s.columns)
print('columns in product_details:',p.columns)
#%%
p.columns

# change column (product_overview) into one df 

# how to search key in the nested dict
# https://codereview.stackexchange.com/questions/201754/getting-a-keys-value-in-a-nested-dictionary
# https://www.geeksforgeeks.org/python-extract-selective-keys-values-including-nested-keys/
# https://stackoverflow.com/questions/7681301/search-for-a-key-in-a-nested-python-dictionary
# https://stackoverflow.com/questions/14692690/access-nested-dictionary-items-via-a-list-of-keys
# https://thispointer.com/python-how-to-check-if-a-key-exists-in-dictionary/

#search key for one/two level nested dict
# https://stackoverflow.com/questions/29339859/how-do-i-traverse-nested-dictionaries-python



# dict key values as a list (cols)
cols = []
for item in p['product_overview']:
    if item is not None:
        for i in item:
            try:
                if i['info'] not in cols:
                    cols.append(i['info'])
            except:
                continue

#  have a set of columns which cover all the columns of different products
l = []
for i in range(p.shape[0]):
    try:
        cols = [d['info'] for d in p.product_info[i]]
        l = list(set().union(cols,l))
    except:
        continue
    #when cols is NA
product_product_info_cols = l