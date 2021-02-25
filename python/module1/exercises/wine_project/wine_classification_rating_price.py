#%%
# load libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 

# ======================================== prepare dataset
# load dataset
wine_sales_data = pd.read_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module1\exercises\wine_project\data\wine_sales_data.csv', sep= ',')
# check basic features of dataset
wine_sales_data.dtypes
wine_sales_data.describe() 
wine_sales_data.columns
wine_sales_data.info #[150930 rows x 11 columns]

# filter the unnecessary data - include: 'country'(portugal), 'province'(vinho verde), 'price', 'points', 'variety' (wine type) 
target_reg = ['portugal', 'Vinho Verde']
my_df = wine_sales_data[wine_sales_data['province'].isin(target_reg)]
my_df2 = my_df.drop(columns=['description','region_1','region_2']) #396 rows

# check missing values in price, points
print (len(my_df2[my_df2['price'].isna()| my_df2['points'].isna()])) #output: 86 rows (out of 396)

# check null data and replace nan to alternative values
# Impute the values using scikit-learn SimpleImpute Class
from sklearn.impute import SimpleImputer
imp = SimpleImputer( strategy='most_frequent')
imp.fit(my_df2)
imputed_df = imp.transform(my_df2)
# save as new df
my_df3 = pd.DataFrame(imputed_df)
col_names = list(my_df2.columns.values)
my_df3.columns = col_names
print (len(my_df3[my_df3['price'].isna()| my_df3['points'].isna()])) #output: 0

# check the distribution of values in each variable
# import seaborn as sns 
# sns.histplot(data=my_df3, x="price")

# Remove Price outliers (hint: Take price between 25 and 75 percentile).
# source: https://stackoverflow.com/questions/35827863/remove-outliers-in-pandas-dataframe-using-percentiles
target_cols = ['price'] 

Q1 = my_df3['price'].quantile(0.25) #9
Q3 = my_df3['price'].quantile(0.75) #12
IQR = Q3 - Q1

my_df4 = my_df3[~((my_df3[target_cols] < (Q1 - 1.5 * IQR)) |(my_df3[target_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]
my_df4 #359 rows

# ?? -> high quality (dv) / high quality (iv) -> high price (dv) 

# Cut rating into 7 levels or 3 levels based on the levels of wine quality you have used in the dataset. 
# For each rating, check the price range (min_price, max_price) and mean_price/median_price.
my_df4['rating'] = pd.cut(my_df4['points'], 3, labels=["low","medium","high"])
# Categories (3, interval[float64]): [(79.989, 83.667] < (83.667, 87.333] < (87.333, 91.0]]
my_df4.iloc[:,-1]

# Now we have a dataframe with rating and price 
# where rating is equivalent to quality of the product and price is a dependent variable.
# try to estimate the price of wines you have analysed and provide suggestions on 'Pricing'.

# goal: predict price (estimates) from rating (quality labels - created based on points in the dataset)
# how: using random forest classification
# step: standardize, split dataset, train a model (DV: price, IV: rating, variety using onehotencoder) 
#? can we use "designation, winery information?" "variety includes information about wine type"

#? what about random forest regressor
# https://stackoverflow.com/questions/29996435/getting-random-forest-prediction-accuracy-for-a-continuous-variable-in-r
# https://www.geeksforgeeks.org/random-forest-regression-in-python/
