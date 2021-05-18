# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ### Importing relevant libraries and mounting Drive. 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from google.colab import drive


# %%
# drive.mount('/content/drive/')

# %% [markdown]
# ### Importing the dataset.
# 

# %%
#Created a dataframe for each product category that was joined to a final dataframe called "products". 

categories= ['headphones', 'keyboard', 'monitor', 'dslr_camera', 'laptop', 'mouse', 'processor','smartphone']

paths= ['/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/Headphones_summary.csv', 
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/Keyboard_summary.csv', 
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/Monitor_summary.csv', 
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/dslr_camera_summary.csv',
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/laptop_summary.csv',
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/mouse_summary.csv',
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/Processor_summary.csv',
        '/content/drive/MyDrive/CODEAcademy, DataScience- PINK EICHHOERNCHEN/e-commerce/search_output/Product_Summary_csv_files/smartphones_summary(updated).csv'] 

empty= []

products= pd.DataFrame(empty)

for i in range(0,len(paths)):
  df= pd.read_csv(paths[i])
  products= products.append(df, ignore_index=True)

products.head(20)

#%%
import pandas as pd
# > make this for-loop as function
#%% function

def create_data_frame(path, *therest):
    for i in range(0,len(paths)):
        df= pd.read_csv(paths[i])
    products= products.append(df, ignore_index=True)

    return products

#%%
source_dir = '../python/3_ecommerce/com/output/search_output'
filenames_list = []

for filenames in os.walk(source_dir):
    print(filenames)
    for filename in filenames:
        print(filename)
        filenames_list.append(filename)

filenames_list
#%%
products = create_data_frame(path_list)
# %%
products.shape

# %% [markdown]
# ### Cleaning process. 

# %%
#Checking how many missing values were in the dataframe. 

products.isnull().sum()


# %%
#Merging "ASIN" and "product_type" columns together with their duplicate.

products['ASIN']= products['ASIN'].fillna(products['asin'])
products['product_type']= products['product_type'].fillna(products['prod_type'])


# %%
#Confirming that the new "ASIN" and "product_type" columns have no missing values. 
products.isnull().sum()


# %%
#Dropped unnecessary or duplicated columns

products.drop(columns=['asin', 'prod_type', 'Unnamed: 0'], inplace= True)
products.head()


# %%
#Reformatted 'product_type' column
products['product_type']= products['product_type'].replace('dslr camera', 'dslr_camera').apply(lambda x: x.lower())

#Reformatted 'rating' column 
products['rating'] = products['rating'].replace(['None','Non'],np.NaN)

#Reformatted 'review_count' column 
products['review_count'] = products['review_count'].replace(['None','Non'],0)
products.review_count.fillna(0, inplace=True)

#Reformatted 'price' column
products['price'] = products['price'].astype('str').apply(lambda x: x.replace('$', '').replace(',','') if '$' or ',' in x else x) 
products['price'] = products['price'].replace(['None','Non'],np.NaN)


# %%
#Converted column types
products= products.astype({'rating': 'float', 'review_count': 'int', 'price': 'float'})


# %%
products.shape


# %%
#Created a 'duplicated' dataframe with the rows whose value in the 'ASIN' column were duplicated
duplicated= products[products['ASIN'].duplicated(keep= 'last')][['ASIN']]
duplicated['sponsored']= 1

#Removed duplicated values from the 'ASIN' column. Decided to keep last occurence. 
print('Number of rows before removing duplicated ASIN:', products.shape[0])
products.drop_duplicates(subset= 'ASIN', keep='last', inplace= True)
print('Number of rows after removing duplicated ASIN:', products.shape[0])
print('\n')

#Joined the products dataframe together with the duplicated dataframe. 
products= products.join(duplicated.set_index('ASIN'), on='ASIN', rsuffix='_duplicated')

#Replaced missing values in the 'sponsored' column of the products dataframe with the one from the 'duplicated' dataframe, and the remaining missing values with zero (0)
products['sponsored']= products['sponsored'].fillna(products['sponsored_duplicated'])
products['sponsored']= products['sponsored'].fillna(0)

#Dropped irrelevant column
products= products.drop(columns= ['sponsored_duplicated'])

print(products.isnull().sum())


# %%
#Top 10 products sorting by rating and then review count

for i in categories: 
  print(i.upper())
  print('Amount of products that have a 5.0 rating:', products[(products['product_type']==i) & (products['rating']==5.0)].loc[:,].shape[0])
  print('\n')
  print('Top 10 products based on rating and review_count:')
  df= products[products['product_type']==i].sort_values(by=['rating', 'review_count'], ascending= False).head(10).loc[:,['title', 'rating', 'review_count']]
  df.index = range(1, 11)
  print(df)
  name = '/content/drive/MyDrive/CODE Data Science/Project3-E-Commerce/Top-10-Products/Top-ten-products_by_rating_' + i + '.csv'
  df.to_csv(name)
  print('\n')


# %%
#Top 10 products sorting by review count and then rating

for i in categories: 
  print(i.upper())
  print('\n')
  print('Top 10 products based on review_count:')
  df= products[products['product_type']==i].sort_values(by=['review_count', 'rating'], ascending= False).head(10).loc[:,['title', 'rating', 'review_count']]
  df.index = range(1, 11)
  print(df)
  name = '/content/drive/MyDrive/CODE Data Science/Project3-E-Commerce/Top-10-Products/Top-ten-products_by_review_count_' + i + '.csv'
  df.to_csv(name)
  print('\n')


# %%
products.groupby(['product_type', 'sponsored'])[['rating','review_count', 'price']].mean()


# %%
products[products['product_type']=='mouse'].loc[:,['price', 'rating', 'review_count', 'sponsored']].corr()


