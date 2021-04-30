# ======================================== wine type prediction
# wtp = wine type prediction


# labelencoder : convert categorical variables to numeric values (wine_type, wine_quality)


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

# -------------------------------------
# LR
# r_wq_train_X, r_wq_test_X, r_wq_train_y, r_wq_test_y

# define parameters of the logisitic regression model 
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
verbose=0, warm_start=False)

# =======train a model : fit the Logistic Regression classifier
wq_lr = LogisticRegression()
wq_lr.fit(r_wq_train_X, r_wq_train_y)
wq_lr.score(r_wq_test_X, r_wq_test_y)

# =======predict the wine type and evaluate the performance
r_wq_lr_predictions = wq_lr.predict(r_wq_test_X)
print(classification_report(r_wq_test_y,r_wq_lr_predictions))

print('accuracy score:' + str(accuracy_score(r_wq_test_y,r_wq_lr_predictions))) #0.6375
print ('kappa score:' + str(cohen_kappa_score(r_wq_test_y, r_wq_lr_predictions))) #0.2703

# RF
random_forest_model = RandomForestClassifier()
random_forest_model.fit(r_wq_train_X, r_wq_train_y)
r_wq_rf_predictions = random_forest_model.predict(r_wq_test_X)

#Measure the performance of the random forest model
print(classification_report(r_wq_test_y, r_wq_rf_predictions))
print(confusion_matrix(r_wq_test_y, r_wq_rf_predictions))

print('accuracy score:' + str(accuracy_score(r_wq_test_y,r_wq_rf_predictions))) #0.8291
print ('kappa score:' + str(cohen_kappa_score(r_wq_test_y, r_wq_rf_predictions))) #0.6603


#--------------- price prediction ------------------------ #

# ============ wine price prediction


# load filtered dataset
df = pd.read_csv("/content/sample_data/ML/wines_sales_prep.csv", sep=",")

# re-shuffle records just to randomize data points
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.head(10)

# set IV and DV for modelling
df_feature = df.loc[:,('points')] #,'rating_n'
df_feature_names = 'points'
df_price = np.array(df['price_bin_n'])

X = df_feature
y = df_price

# =======split dataset 
wpr_train_X, wpr_test_X, wpr_train_y, wpr_test_y = train_test_split(X,y, test_size=0.3, random_state=42)
print(Counter(wpr_train_y), Counter(wpr_test_y))
# Counter({2: 130, 1: 53, 0: 37}) Counter({2: 65, 1: 17, 0: 13}) #high:0, low:1, middle:2 
print('IV:', df_feature_names, '/ DV: high:0, low:1, middle:2' )