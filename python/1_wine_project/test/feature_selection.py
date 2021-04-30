feature_selection.py

#----------test

#1
# https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%201/Week%204/Task4.md
# feature selection by data type : https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/

r_wq_dt_feature_importances = DT.feature_importances_
w_feature_names, r_wq_dt_feature_scores = zip(*sorted(zip(w_feature_names,r_wq_dt_feature_importances), key=lambda x: x[1]))
y_position = list(range(len(w_feature_names)))
plt.barh(y_position, r_wq_dt_feature_scores, height=0.6, align='center')
plt.yticks(y_position , w_feature_names)
plt.xlabel('Relative Importance')
plt.ylabel('Feature')
t = plt.title('Feature Importances for Decision Tree (red wine)')

#2 red wine - random forest - feature importance
rf = RandomForestClassifier()
r_feature_imp = pd.Series(rf.feature_importances_,index=r_wines_feature_names).sort_values(ascending=False)
print(r_feature_imp)

# Creating a bar plot : feature importance
sns.barplot(x=r_feature_imp, y=r_feature_imp.index)
# Add labels to your graph
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Important Features in predicting good red wine")
plt.legend()
plt.show()

# white wine - random forest - feature importance
w_feature_imp = pd.Series(rf.feature_importances_,index=rw_features_names).sort_values(ascending=False)
w_feature_imp

w_feature_df = pd.DataFrame(w_feature_imp, columns = ["feature_importance"])
w_feature_df_top5 = list(w_feature_df.head(5).index)
w_feature_df["top5"] = w_feature_df["feature_importance"].index.isin(w_feature_df_top5)
w_feature_df.head(10)

# Creating a bar plot

sns.barplot(x=w_feature_df['feature_importance'][:], y=w_feature_df['feature_importance'], hue="top5", data = w_feature_df)
# Add labels to your graph

plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title("Important Features in predicting good white wine")
plt.legend()
plt.show()


#=========== feature importance
# https://stackoverflow.com/questions/44101458/random-forest-feature-importance-chart-using-python

#3
# classification feature selection
# source: https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/

# ANOVA feature selection for numeric input and categorical output
from sklearn.datasets import make_classification
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
# generate dataset

# define feature selection
fs = SelectKBest(score_func=f_classif, k=2)
# apply feature selection
X_selected = fs.fit_transform(X, y)
print(X_selected.shape) #(1599, 2)


#4

# ------------------- another feature selection ======not working


# source: https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/

# pearson's correlation feature selection for numeric input and numeric output
from sklearn.datasets import make_regression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

# get independent and dependent variables 
w_features = wines_red.iloc[:,:-4]
w_feature_names = w_features.columns

X = w_features
Y = wines_red[['quality']]

# to get intercept -- this is optional
# X = sm.add_constant(X)

# define feature selection
fs = SelectKBest(score_func=f_regression, k=5)
# apply feature selection
X_selected = fs.fit_transform(X, Y)
print(X_selected.shape)

#----------- modeling with selected features -----------

## random forest with selected festures: alcohol, sulphates, volatile acidity - red wine

# calculate class weight
import numpy as np
from sklearn.utils.class_weight import compute_class_weight

# set IV and DV
X = rw_features[['alcohol','sulphates', 'volatile acidity','total sulfur dioxide','density']]
Y = wines_red['quality_label']
r3_feature_names = list(X.columns)

# split dataset for predicting wine quality
r3_wq_train_X, r3_wq_test_X, r3_wq_train_y, r3_wq_test_y = train_test_split(X, Y, test_size=0.3, random_state=42)
print(Counter(r3_wq_train_y), Counter(r3_wq_test_y))
#Counter({'medium': 590, 'low': 514, 'high': 15}) Counter({'medium': 247, 'low': 230, 'high': 3})
print('Features:', list(r3_feature_names))

# standardization
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

#scaler = MinMaxScaler()
sc = StandardScaler()
X = np.array(X)

sc.fit_transform(r3_wq_train_X)
sc.transform(r3_wq_test_X)

#--------------
# r_wq_train_X, r_wq_test_X, r_wq_train_y, r_wq_test_y

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(r3_wq_train_X, r3_wq_train_y)
r3_wq_rf_predictions = rf.predict(r3_wq_test_X)

#Measure the performance of the random forest model

print(classification_report(r3_wq_test_y, r3_wq_rf_predictions))
print(confusion_matrix(r3_wq_test_y, r3_wq_rf_predictions))
print('accuracy score:' + str(accuracy_score(r3_wq_test_y,r3_wq_rf_predictions))) #0.8229
print ('kappa score:' + str(cohen_kappa_score(r3_wq_test_y, r3_wq_rf_predictions))) #0.6486


#------------------
# r_wq_train_X, r_wq_test_X, r_wq_train_y, r_wq_test_y

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 8, metric = 'minkowski', p = 2) #p = 2 : euclidean_distance
knn.fit(r_wq_train_X, r_wq_train_y)
r_wq_knn_predictions = knn.predict(r_wq_test_X)

print(classification_report(r_wq_test_y, r_wq_knn_predictions))
print(confusion_matrix(r_wq_test_y, r_wq_knn_predictions))
print('accuracy score:' + str(accuracy_score(r_wq_test_y,r_wq_knn_predictions))) #0.5416
print ('kappa score:' + str(cohen_kappa_score(r_wq_test_y, r_wq_knn_predictions))) #0.0900

#---------------------
# find the optimal number of K

# another version of k-nearest neighbors model: choosing an optimal K-value using elbow method
error_rates = []

for i in np.arange(1, 15): #first tried with 101 and found lowest point around 10-15
    new_model = KNeighborsClassifier(n_neighbors = i)
    new_model.fit(r_wq_train_X, r_wq_train_y)
    new_predictions = new_model.predict(r_wq_test_X)
    error_rates.append(np.mean(new_predictions != r_wq_test_y))

plt.plot(error_rates)
#- error rates tend to be minimized with a K value of approximately 8. 
# This means that 8 is a suitable choice for K that balances both simplicity and predictive power.

#----------------------------
# r_wq_train_X, r_wq_test_X, r_wq_train_y, r_wq_test_y

from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(r_wq_train_X, r_wq_train_y)

r_wq_dt_predictions = DT.predict(r_wq_test_X)

#Measure the performance of DT
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print(classification_report(r_wq_test_y, r_wq_dt_predictions))
print(confusion_matrix(r_wq_test_y, r_wq_dt_predictions))
print('accuracy score:' + str(accuracy_score(r_wq_test_y,r_wq_dt_predictions))) #0.7520
print ('kappa score:' + str(cohen_kappa_score(r_wq_test_y, r_wq_dt_predictions))) #0.5099