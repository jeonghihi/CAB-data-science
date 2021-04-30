#%%
# load necessary libraries
import pandas as pd 
import numpy as np

# ========commonly used libraries for classification in machine learning
import matplotlib.pyplot as plt
#import model_evaluation_utils as meu
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

#%%
# ======================================== prepare dataset
red_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep= ';')
white_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep= ';')

red_wine.astype('int64').dtypes
white_wine.astype('int64').dtypes

## create a new variable 'wine_type'
red_wine['wine_type'] = 'red'

# bucket wine quality scores into qualitative quality labels
red_wine['quality_label'] = red_wine['quality'].apply(lambda value: 'low'
if value <= 5 else 'medium'
if value <= 7 else 'high')
red_wine

red_wine['quality_label'] = pd.Categorical(red_wine['quality_label'],
categories=['low', 'medium', 'high'])
red_wine['quality_label'].dtype

# create a new variable 'wine_type'
white_wine['wine_type'] = 'white'

# bucket wine quality scores into qualitative quality labels

white_wine['quality_label'] = white_wine['quality'].apply(lambda value: 'low'
if value <= 5 else 'medium'
if value <= 7 else 'high')

white_wine['quality_label'] = pd.Categorical(white_wine['quality_label'],
categories=['low', 'medium', 'high'])

white_wine

# combine two dataframe (red_wine) & (white_wine)
wines = pd.concat([red_wine, white_wine])

# re-shuffle records just to randomize data points
wines = wines.sample(frac=1, random_state=42).reset_index(drop=True)
wines

# ======================================== wine type prediction
# wtp = wine type prediction

# code source: https://nickmccullum.com/python-machine-learning/decision-trees-random-forests-python/
# data info: wtp_train_X, wtp_test_X, wtp_train_y, wtp_test_y

#Train the decision tree model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(wtp_train_X, wtp_train_y)

tp_rf_predictions = model.predict(wtp_test_X)

#Measure the performance of the decision tree model
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print(classification_report(wtp_test_y, tp_rf_predictions, target_names=['red', 'white']))
print(confusion_matrix(wtp_test_y, tp_rf_predictions))

#Train the random forests model
from sklearn.ensemble import RandomForestClassifier

random_forest_model = RandomForestClassifier()
random_forest_model.fit(wtp_train_X, wtp_train_y)
tp_rf_predictions = random_forest_model.predict(wtp_test_X)

#Measure the performance of the random forest model

print(classification_report(wtp_test_y, tp_rf_predictions, target_names=['red', 'white']))
print(confusion_matrix(wtp_test_y, tp_rf_predictions))
# %%
