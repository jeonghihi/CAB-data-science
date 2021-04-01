#%% 
import yaml

# make dict with keys, values
prod_dict_feature = ['css', 'xpath', 'type']
prod_dict_val_title = ['a-size-medium a-color-base a-text-normal', 'null', 'Text']
prod_dict_val_url = ['a-link-normal a-text-normal', 'null', 'Link']
prod_dict_val_price = ['span.a-price-whole', 'null', 'Text']

prod_dict_feature2 = ['css', 'xpath', 'type', 'attribute']
prod_dict_val_review = ['div.a-row.a-size-small span:nth-of-type(1)', 'null', 'Attribute', 'aria-label']
prod_dict_val_rating = ['div.a-row.a-size-small span:nth-of-type(2)', 'null', 'Attribute', 'aria-label']

#title: .s-line-clamp-2
#review: a-size-base

c_title = dict(zip(prod_dict_feature, prod_dict_val_title))
c_url = dict(zip(prod_dict_feature, prod_dict_val_url))
c_rating = dict(zip(prod_dict_feature2, prod_dict_val_rating))
c_review = dict(zip(prod_dict_feature2, prod_dict_val_review))
c_price = dict(zip(prod_dict_feature, prod_dict_val_price))

product_dict = {'title':c_title, 'url':c_url, 'rating':c_rating, 'review_count':c_review, 'price':c_price}
product_index = {'css': 20, 'xpath': 2, 'multiple': 3, 'type': 100, 'children': product_dict}

dict_file = {'products': product_index}

for p_id, p_info in product_dict.items():
    print("\nProduct Info:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])

# check keys in dict: list(child)[:] 
# check keys in dict: next(iter(bla))
# check values in dict: [child.values()]

output_dir = r'C:\Users\Jeong\Anaconda3\envs\CAB\CAB-data-science\CAB-data-science\python\module2\ecommerce\pipe/'
output_file = output_dir + 'search.yml'
with open(output_file, 'w+') as f:
    documents = yaml.dump(dict_file, f)

f.close()

# why the structure of dict_file is different from sample?