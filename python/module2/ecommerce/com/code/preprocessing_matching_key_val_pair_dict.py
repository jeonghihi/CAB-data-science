
#====== find a value matching to the key/value of dictionary that was made from correct pairs ---

# search the correct key for values paired with the wrong key (e.g. {'Maker: Other', 'Model:Clio'})
from collections import defaultdict

# create a dictionary from correct key-value pairs

list_car_brand_dict = []

for row in range(len(temp)):
  try:
    item_key = temp.loc[row,'maker']
    item_val = temp.loc[row,'model']
    temp_dict = {item_key : item_val}
    if item_key != 'Other':
      if temp_dict not in list_car_brand_dict:
        list_car_brand_dict.append(temp_dict)
  except:
    pass

car_dict = defaultdict(list)
for myd in list_car_brand_dict:
    for k, v in myd.items():
        car_dict[k].append(v)
print(car_dict)

# check which values are wrong
temp = df_inv2[df_inv2['maker'] == 'Other']
temp.head()

# replace wrong keys (values in the column 'maker') with correct key (based on car_dict)
df_inv2['maker'] = df_inv2['model'].apply(lambda x: ''.join(str(element) for element in [key for key,val in car_dict.items() if any(x in s for s in val)]))
df_inv2.head()

# check if the replacement was succesful

temp = df_inv2[df_inv2['maker'] == 'Other']
print('models with maker == Other:',len(temp))

temp = df_inv2[df_inv2['model'] == 'Clio']
print('makers of model == Clio:',set(temp.maker.values))

#%% trials 
# dict - reference: https://stackoverflow.com/questions/17340922/how-to-search-if-dictionary-value-contains-certain-string-with-python, https://stackoverflow.com/questions/11533274/how-can-i-combine-dictionaries-with-the-same-keys
# setdefault - reference: https://www.programiz.com/python-programming/methods/dictionary/setdefault

# search correct keys 
key_missing_items = ['Clio']
key_found_items = []
car_dict 

for item in key_missing_items:
  target = item
  key_correct = [key for key,val in car_dict.items() if any(target in s for s in val)][0]
  key_found_items.append({key_correct:target})

key_found_items

# update the dictionary : add items with corrected values
# using setdefault
