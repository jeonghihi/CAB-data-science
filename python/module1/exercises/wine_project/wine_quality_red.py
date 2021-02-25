
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

#load dataset
wines = pd.read_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module1\exercises\wine_project\data\wines_prep.csv', sep= ',', index_col=[0])

wines_red = wines[wines['wine_type'] == 'red'] #1599 rows

# =======preprocessing : categorical DV (string to numeric) 
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
wines_red['wine_quality_N'] = labelencoder.fit_transform(wines_red['quality_label']) #high:0, low:1, medium:2

wines_red.head(10)
wines_red.to_csv(r'C:\Users\Jeong\CAB\CAB-data-science\python\module1\exercises\wine_project\data\wines_red.csv')

# =======preprocessing : prepare dataset for classification
w_features = wines_red.iloc[:,:-4]
w_feature_names = w_features.columns

# set IV and DV
X = w_features
y = wines_red['quality_label']
#y = w_features['wine_type']

# split dataset for predicting wine quality
r_wq_train_X, r_wq_test_X, r_wq_train_y, r_wq_test_y = train_test_split(X, y, test_size=0.3, random_state=42)
print(Counter(r_wq_train_y), Counter(r_wq_test_y))
#Counter({'medium': 590, 'low': 514, 'high': 15}) Counter({'medium': 247, 'low': 230, 'high': 3})
print('Features:', list(w_feature_names))

# standardization
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

#scaler = MinMaxScaler()
sc = StandardScaler()
X = np.array(X)

sc.fit_transform(r_wq_train_X)
sc.transform(r_wq_test_X)

# ================= comparison algorithms for predicting red wine quality
# r_wq_train_X, r_wq_test_X, r_wq_train_y, r_wq_test_y

# Compare Algorithms
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# load dataset
# set IV and DV
X = w_features
Y = wines_red['quality_label']

# prepare configuration for cross validation test harness
seed = 10
# prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('KNN', KNeighborsClassifier(n_neighbors = 20)))
models.append(('RF', RandomForestClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('SVM', SVC()))

# evaluate each model in turn - wine_quality
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=42, shuffle=True)
	cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
 
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

#=========== feature importance
# https://stackoverflow.com/questions/44101458/random-forest-feature-importance-chart-using-python
