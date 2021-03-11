---
# title : "python-module1-week4-5-machine-learning"
# date : "2021-02-15"
# tags : [python, exemple, machinelearning]
---

# what is machine learning:
- human learning 
- : keep [trying tasks using different methods, getting resources, going through failure/success, with/out people, to achieve the goal (quality: joy/satisfaction, quantity: money)] based on motivation.
- : tend to search/select and utilize the resources with 'good' quality for effective learning (understand questions and solve it with less time/effort) ~ motivation. In this sense, humean learning is a kind of problem-solving and this applies similarly to the machine learning (but we, human, get more than just an answer for the question while learning something).

- machine learning 
- : trying tasks using different methods, gettting resources, going through failure/success, to achieve the goal (quantity: prediction with high accuracy)
- : machines have no intention, so technician should give them good resources ('good data') and the direction to go ('goal/target'). => basic principle of supervised learning
- : we teach the machine to learn a mapping function from input to output (i.e. function approximation) and predictive modelling is one way of teaching the machine. (??todiscuss)

- Remember - If you feed machines a rotten tomato, they will give you something else harmful instead of warm soup. 

- resource: 
  - machine learning handbook with exemples: https://jakevdp.github.io/PythonDataScienceHandbook/05.01-what-is-machine-learning.html
  - basic algorithms with python exemples https://www.analyticsvidhya.com/blog/2017/09/common-machine-learning-algorithms/

- When you do machine learning, it means you build models that understand a dataset; models that can explain the relationship between data values (numerical/categorical/..variable/parameters) in the given dataset and predict how their interaction influences each other within the dataset or the third data in a new dataset. 
- The dataset could be 2-dimensional, 3 or 4-dimensional depending on the number of variables (parameters)
  - 2D(number of coffee -> the length of working hours)
  - 3D(number of coffee, the quality of sleep last night-> length of working hours)
  - 4D(number of coffee, the quality of sleep last night, number of browser tabs -> length of working hours)

- Types of machine learning: supervised vs. unsupervised

# supervised learning vs. unsupervised learning
- In supervised learning, models explain data by predicting a dependant variable "label" (e.g. wine_label; red/white, wine_price; 5~20euros) based on independent variables (e.g. features of wine; alcohol, pH, acidity).
- In unsupervised learning: models explain data by predict a variable without any label (no target/goal, no guide).
- In semi-supervised learning, samll part of dataa is labelled (only incomplete labels are available).
 
## supervised learning
- Learning from labelled data. "let the machine find the solution for a given dataset and apply them to a new data"
  - using classification/regression.
    - classification : predict discrete labels - categorical variable. e.g., weather (sunny/cloudy/rainny/stormy), wine_label (red/white), whether you will enter the club or not (yes/no)
    - regression : predict continuous labels. e.g, weather (degree), wine_price (between 2~30euros~), price of falafel (euros)
    - difference between classification and regression : https://machinelearningmastery.com/classification-versus-regression-in-machine-learning/

> - common machine learning methods: 
> https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/ (2020)
>https://towardsdatascience.com/10-machine-learning-methods-that-every-data-scientist-should-know-3cc96e0eeee9 (2019)
>https://www.analyticsvidhya.com/blog/2017/09/common-machine-learning-algorithms/ (2017)

> - brief intro about ML methods with use cases (2018): https://www.soa.org/globalassets/assets/files/e-business/pd/events/2018/equity-based-insurance/2018-ebig-presentation-articial-intelligence.pdf
> - simple exemple/description for basic machine learning methods: https://towardsdatascience.com/machine-learning-types-and-algorithms-d8b79545a6ec

## unsupervised elarning
- Learning from unlabelled data. "let the dataset speak for itself"
  - how? like human have been developing themselves by anyhow 
    - _did we discover/develop our abilities/skills or those abilities emerged from experiences and came to our hands?_ 
  - using clustering/dimensionality reduction. 
    - details about these methods (see you later)

# supervised learning methods - classification
  - Classification refers to a method of predictive modelling where a discrete value (class/category) is predicted for a given example of input data. 
  - Types of classification algorithms: 
    - binary, multi-class, multi-label, imbalanced classification 
      - resource: https://machinelearningmastery.com/types-of-classification-in-machine-learning/
    - logistic regression, naive bayes, decision tree, k-nearest eighbours, random forest, kernel approximation
      - https://data-flair.training/blogs/machine-learning-classification-algorithms/

  - What is given (dataset):
    - For a dataset with 2-dimension, there are two features for each data point, which is represented by (x,y) positions and two classes for the label of data point.
    - The position of one data point will decided by value of two features on x,y axis. 
    - The label of one data point would be a discrete value (either "white" or "red").
  - What is assumed (how the dataset is structured):
    - two groups(labels) can be separated by a straight line; same group of data point will be in the same side. The location and orientation of the line is described based on the optimal values of model parameters and those values learned from the dataset (from training set).    
  - What do we do: 
    - training: building a model with training sets (fitting a model to find the optimal line) using classification algorithms 
    - generalization: After the training, the model applies the learned rule to the new,unlabeled dataset to predict whether the data point in new dataset belongs to one of labels "white" or "red".
    - evaluate the performance of the model based on its accuracy (accuracy is a popular metric, but not perfect).

# supervised learning methods - regression
  - Regression refers to a method of predictive modelling where a continous value (integer/floating point) is predicted for a given example of input data. 
  - Types of regression algorithms: 
    - Linear regression, support vector machine, random forest regression 
  
  - What is given (dataset):
    - For a 2-dimension dataset, there are two features for each data point, which is represented by (x,y) positions and describe the position of each data point (z).
    - The position of data point could be indexed/represented on the third dimension.
    - The label of one data point would be a continous integer/floating value. 
  - What is assumed (how the dataset is structured):
    - the label (continous value) of data point is predicted by a line; The location and orientation of the line is described based on the optimal values of model parameters and those values learned from the dataset (from training set).  
  - What we do:
    - training: building a model with training sets (fitting a model to find the optimal line) using regression algorithms.
    - generalization: After the training, the model applies the learned rule to the new,unlabeled dataset to predict whether the data point in new dataset is explained by the fitted line.
    - evaluate the performance of the model based on the unexplained variance of fitted models. 
      - e.g., Root Mean Sqaured Error (RMSE)
      - ??todisucss - ROC curve (https://www.mygreatlearning.com/blog/roc-curve/)
      - resource: https://www.ritchieng.com/machine-learning-evaluate-linear-regression-model/
 

# how to evaluate the performance of classification models
  - There are multiple metrics for evaluation of models. 
    - resource: https://www.ritchieng.com/machine-learning-evaluate-classification-model/
  - how these metrics are implemented in python modules: https://scikit-learn.org/stable/modules/model_evaluation.html
  - 
## Cross validation
- Cross validation is a method used to evaluate/estimate the algorithm.
- Underfitting can result from high bias, low variance : prediction line cannot explain for the whole data (both train and test data), which means many E - errors (unexplained part)
  - predict train (bad score) and test (bad score)
- Overfitting can : prediction line can explain for the trained data, not for test data
  - predict train (good score) and test (bad score)
- Best fit : find a balance between under-and over-fitting
- resource: https://towardsdatascience.com/cross-validation-explained-evaluating-estimator-performance-e51e5430ff85


_below this : needs to be updated_
# unsupervised learning methods - clustering 
- Models that detect and identify distinct groups in the data

# unsupervised learning methods - dimensionality reduction
- Models that detect and identify lower-dimensional structure in higher-dimensional data

# Questions to be answered
- Q1. LR why is it called regression ?
- Q2. random_state in LR what it means ?


#### ??quetions
- what is difference between machine learning and predictive modelling? https://www.educba.com/machine-learning-vs-predictive-modelling/
- cross-validation: Is there a way to classify untrained data as the third answer (cloudly) when only two target answers (categorization: sunny vs. rainny) are given in the model
- useful figures for understanding the general idea/concepts in machine learning
  - : https://www.researchgate.net/publication/324250573/figure/fig1/AS:612417880981504@1523023209051/Fundamental-steps-of-supervised-machine-learning-for-image-based-species-identification_W640.jpg

## preprocessing
- standardization and normalization
  - resource: https://www.machinecurve.com/index.php/2020/11/19/how-to-normalize-or-standardize-a-dataset-in-python/
- when to use which one
  - use min-max normalization if you want to normalize the data while keeping some differences in scales (because units remain different)
  - use standardization if you want to make scales comparable (through standard deviations)

- feature scaling
  - for sparse data, use MaxAbsScaler
  - difference between fit and fit_transform
    - source: https://datascience.stackexchange.com/questions/12321/whats-the-difference-between-fit-and-fit-transform-in-scikit-learn-models
    - source: https://stackoverflow.com/questions/23838056/what-is-the-difference-between-transform-and-fit-transform-in-sklearn/50904741#50904741
    - to set customized fit order: https://stackoverflow.com/questions/51308994/python-sklearn-determine-the-encoding-order-of-labelencoder

- how to check if the data matrix is sparse
  ```python
  import scipy
  my_matrix = wtp_features
  scipy.sparse.issparse(my_matrix)
  ```

## feature selection
- multicollinearity (VIF)
- dimension reduction by PCA
- recursive feature elimination (RFE)
- fitting models with all variables and removing insignificant variables
- Chi-squared test etc.
- ? do we need to apply different feature selection method for different algorithm?
  - https://stackoverflow.com/questions/46285960/feature-selection-from-sklearn-logisitc-regression