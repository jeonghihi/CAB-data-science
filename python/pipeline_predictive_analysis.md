---
# title : "pipeline-predictive-analysis"
# date : "2021-04-29"
# tags : [piepeline, analysis, dataanalysis]
---

#- [Table of Contents](#)
  - [Set up environment](#set-up-environment)
  - [Data acquisition](#data-acquisition)
  - [Data preparation](#data-preparation)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Data transformation](#data-transformation)
  - [Model building](#model-building)
  - [Model evaluation](#model-evaluation)
  - [Conclusion (Interpretation of findings)](#conclusion-interpretation-of-findings)
  
## Set up environment
- Load packages

## Data acquisition
- Import Data

## Data preparation

### Exploratory Data Analysis (EDA)
- Features of dataset (e.g. check linear separability, convexity, sparsity)
- Statistical analysis (e.g. mean, min/max, standard deviation)
- Data visualization (e.g. check distribution of data values)
- Clustering
- Data quality check (e.g. anomaly detection)

### Data transformation 
- Data cleaning
  - impute missing values 
  - impute anomalies (e.g. reduce redundancy - duplicates in rows/columns, label of columns, datatype)

- Feature engineering
  - Encoding variables 
    - categorical features: ordinal/categorical data (e.g. one-hot encoder)
    - numeric features: standardization/normalization (e.g. standard scaler), log-transformation

## Model building
- Split Data
- Standardization/normalization

- Model predictions with train Data 
  - Compare algorithms and decide the final model
  - [Supervised learning models](1)
    - Logistic Regression (LR)
    - Decision Trees (DT)
    - Ensemble Methods (Bagging, AdaBoost, Random Forest, Gradient Boosting)
    - K-Nearest Neighbors (KNN)
    - Linear Discriminant Analysis (LDA)
    - Support Vector Machines (SVM)
    - Gaussian Naive Bayes (GaussianNB)
    - Stochastic Gradient Descent (SGDC)

- Model predictions with test Data

## Model evaluation
- Evaluation metrics
  - Regression problems: Mean Absolute Error, Mean Squared Error, Root Mean Squared Error)
  - Classification problems: Classification accuracy 

## Conclusion 
- Interpretation of findings
- Suggestions for model improvements

---
[1] : https://scikit-learn.org/stable/supervised_learning.html
