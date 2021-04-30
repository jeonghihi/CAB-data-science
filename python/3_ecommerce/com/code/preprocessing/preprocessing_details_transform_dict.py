import pandas as pd 

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

    