# load necessary libraries
import pandas as pd 
import numpy as np

# ========commonly used libraries for classification in machine learning
import matplotlib.pyplot as plt
import model_evaluation_utils as meu
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report


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

# ===========================k-nearest neighbors classifier
# source1: https://pythonbasics.org/k-nearest-neighbors/
# source2: https://nickmccullum.com/python-machine-learning/k-nearest-neighbors-python/

# =======load dataset
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# =======check dataset for classification
wtp_features = wines.iloc[:,:-3]
wtp_feature_names = wtp_features.columns
wtp_class_labels = np.array(wines['wine_type'])

wtp_train_X, wtp_test_X, wtp_train_y, wtp_test_y = train_test_split(wtp_features,wtp_class_labels, test_size=0.3, random_state=42)

print(Counter(wtp_train_y), Counter(wtp_test_y))
print('Features:', list(wtp_feature_names))

# =======preprocessing
# Define the scaler
wtp_ss = StandardScaler().fit(wtp_train_X)
# Scale the train set
wtp_train_SX = wtp_ss.transform(wtp_train_X)
# Scale the test set
wtp_test_SX = wtp_ss.transform(wtp_test_X)


# simple version of k-nearest neighbors model
# =======train a model : fit a k-nearest neighbor model to the data
K = 3 
tp_knn = KNeighborsClassifier(n_neighbors = K)
tp_knn.fit(wtp_train_SX, wtp_train_y)
print(tp_knn)

# =======predict the wine type and evaluate the performance
tp_knn_predictions = tp_knn.predict(wtp_test_SX)

# check accuracy of model
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print(classification_report(wtp_test_y, tp_knn_predictions, target_names=['red', 'white']))

# another version of k-nearest neighbors model: choosing an optimal K-value using elbow method

error_rates = []

for i in np.arange(1, 101):
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(wtp_train_SX, wtp_train_y)
    new_predictions = new_model.predict(wtp_test_SX)
    error_rates.append(np.mean(new_predictions != wtp_test_y))

plt.plot(error_rates)

# K should be 20 for highest accuracy.