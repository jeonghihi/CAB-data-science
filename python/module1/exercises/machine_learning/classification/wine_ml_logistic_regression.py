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

# =======load dataset & preprocessing for classification
from sklearn.linear_model import LogisticRegression

# labelencoder : convert categorical variables to numeric values (wine_type, wine_quality)
wines.columns

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
wines.iloc[:, -1] = labelencoder.fit_transform(wines.iloc[:, -1]) #high:0, low:1, middle:2 

# remove dependant variable for dataset-split-train-test
wines_features = wines.drop(columns=['quality', 'wine_type'])
wines_feature_names = wines_features.columns

wines_type_labels = np.array(wines['wine_type'])
wines_quality_labels = np.array(wines['quality_label'])

X = wines_features.drop(columns=['quality_label'])
y = wines_features['quality_label']
#y = wines_features['wine_type']


# =======standardization
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
#scaler = MinMaxScaler()
scaler = StandardScaler()
X = np.array(X)
scaler.fit(X)
X = scaler.transform(X)

# =======split dataset 
wtp_train_X, wtp_test_X, wtp_train_y, wtp_test_y = train_test_split(X,y, test_size=0.3, random_state=42)
print(Counter(wtp_train_y), Counter(wtp_test_y))
print('Features:', list(wines_feature_names))

# define parameters of the logisitic regression model 
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
verbose=0, warm_start=False)

# =======train a model : fit the Logistic Regression classifier
wtp_lr = LogisticRegression()
wtp_lr.fit(wtp_train_X, wtp_train_y)
wtp_lr.score(wtp_test_X, wtp_test_y)

# =======predict the wine type and evaluate the performance
wtp_lr_predictions = wtp_lr.predict(wtp_test_X)
#print(classification_report(wtp_test_y,wtp_lr_predictions, target_names=['red', 'white']))
print(classification_report(wtp_test_y,wtp_lr_predictions))

### classification report
    # macro average (averaging the unweighted mean per label), 
    # weighted average (averaging the support-weighted mean per label)
    # sample average (only for multilabel classification). 

# =======select the best model based on kappa score
from sklearn.metrics import cohen_kappa_score as kappa
kappa(wtp_lr_predictions, wtp_test_y) # 0.401119052307472

# ======= preprocessing: feature selection
# source: https://stackoverflow.com/questions/32860849/classification-pca-and-logistic-regression-using-sklearn
# source: https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

pca = PCA(n_components=2)
cls = LogisticRegression() 

pipe = Pipeline([('pca', pca), ('logistic', cls)])
pipe.fit(wtp_train_X, wtp_train_y)
predictions = pipe.predict(wtp_test_X)

print(classification_report(wtp_test_y,predictions))
kappa(predictions, wtp_test_y) # 0.1532474824097192
