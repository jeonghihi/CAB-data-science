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
wine_sales_data = pd.read_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module1\exercises\wine_project\data\wine_sales_data.csv', sep= ',', index_col=[0])
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
my_df4['price_bin'] = pd.cut(my_df4['price'], 3, labels=["low","medium","high"])
# Categories (3, interval[float64]): [(79.989, 83.667] < (83.667, 87.333] < (87.333, 91.0]]
my_df4.iloc[:,-1]

# Now we have a dataframe with rating and price 
# where rating is equivalent to quality of the product and price is a dependent variable.
# try to estimate the price of wines you have analysed and provide suggestions on 'Pricing'.

# goal: predict price (estimates) from rating (quality labels - created based on points in the dataset)
# how: using random forest classification
# step: standardize, split dataset, train a model (DV: price, IV: rating, variety using onehotencoder) 

# transform dtypes
my_df4 = my_df4.astype({'price': 'int64', 'points': 'int64'})

# distribution of each ratings
my_df4.rating.value_counts() # high: 115, low: 37, mid:207
my_df4.price_bin.value_counts() #high 55, low:83, medium:221
# > we need to apply RandomOverSampling to balance minority class (low label)
# source: https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/


# convert categorical variables to numeric values (rating)
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
my_df4['rating_n'] = labelencoder.fit_transform(my_df4.iloc[:, -2]) #high:0, low:1, middle:2 
my_df4['price_bin_n'] = labelencoder.fit_transform(my_df4.iloc[:, -2]) #high:0, low:1, middle:2 
#=============? can we use "winery (13 types)" for giving different weights to prediction (KNN)
# my_df4.winery.value_counts() 

#=============use "variety for categorizing wine type"
my_df4['variety'].value_counts()

wine_type = pd.read_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module1\exercises\wine_project\data\wines_sales_type.csv',sep=",")
wine_white_names = list(wine_type[wine_type['wine_type'] == 'white']['wine_variety'].values)
wine_red_names = list(wine_type[wine_type['wine_type'] == 'red']['wine_variety'].values)
wine_rose_names = list(wine_type[wine_type['wine_type'] == 'rose']['wine_variety'].values)

my_df4['wine_type'] = ""
my_df4['wine_type'] = np.where(my_df4['variety'].isin(wine_red_names), 'red', my_df4.wine_type)
my_df4['wine_type'] = np.where(my_df4['variety'].isin(wine_white_names), 'white', my_df4.wine_type)
my_df4['wine_type'] = np.where(my_df4['variety'].isin(wine_rose_names), 'rose', my_df4.wine_type)

# filter items which are not red or white wine
my_df_fin = my_df4[my_df4.wine_type != 'rose'] #315rows

# final dataset save as csv
my_df_fin.to_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module1\exercises\wine_project\data\wines_sales_prep.csv') 

##=============? what about random forest regressor
# https://stackoverflow.com/questions/29996435/getting-random-forest-prediction-accuracy-for-a-continuous-variable-in-r
# https://www.geeksforgeeks.org/random-forest-regression-in-python/


#============= TRAIN AND PREDICT

# re-shuffle records just to randomize data points
my_df4 = my_df4.sample(frac=1, random_state=42).reset_index(drop=True)

# set IV and DV for modelling
my_df4_feature = my_df4.loc[:,('points')] #,'rating_n'
my_df4_feature_names = my_df4_feature.columns
my_df4_price = np.array(my_df4['price_bin_n'])
#? which one is better for predicting price (continuous) using rating values (3category) than using points (continuous)?
#? if we predict price (continuous) from points (continous), is it better? but then we cannot use dataset1 with winetype/quality

X = my_df4_feature
y = my_df4_price

# =======split dataset 
wpr_train_X, wpr_test_X, wpr_train_y, wpr_test_y = train_test_split(X,y, test_size=0.3, random_state=42)
print(Counter(wpr_train_y), Counter(wpr_test_y))
# Counter({2: 151, 1: 62, 0: 38}) Counter({2: 70, 1: 21, 0: 17}) #high:0, low:1, middle:2 
print('Features:', list(my_df4_feature_names))

# standardization
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
#scaler = MinMaxScaler()
sc = StandardScaler()
X = np.array(X)

sc.fit_transform(wpr_train_X)
sc.transform(wpr_test_X)
# data info: wpr_train_X, wpr_test_X, wpr_train_y, wpr_test_y

#============ modelling: random forest - train and predict
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(wpr_train_X, wpr_train_y)
rf.score(wpr_test_X, wpr_test_y) #0.6481481481481481

wpr_rf_predictions = rf.predict(wpr_test_X)

#============ modelling: random forest - performance
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print(classification_report(wpr_test_y, wpr_rf_predictions, target_names=['high', 'medium','low']))
print(confusion_matrix(wpr_test_y, wpr_rf_predictions))

#============ modelling: logistic regression - train and predict
from sklearn.linear_model import LogisticRegression
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
verbose=0, warm_start=False)

wpr_lr = LogisticRegression()
wpr_lr.fit(wpr_train_X, wpr_train_y)
wpr_lr.score(wpr_test_X, wpr_test_y) #0.6481481481481481

wpr_lr_predictions = wpr_lr.predict(wpr_test_X)

#============ modelling: logistic regression - performance
print(classification_report(wpr_test_y, wpr_lr_predictions, target_names=['high', 'medium','low']))
print(confusion_matrix(wpr_test_y, wpr_lr_predictions))

accuracy_score(wpr_test_y,wpr_lr_predictions)
accuracy_score(wpr_test_y,wpr_rf_predictions)