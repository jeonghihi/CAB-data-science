---
layout: post
title: 'daily-log'
date: "2021-01-25"
---


- CAB settings
- dir: Users\Jeong\CAB\test

# week1
## 2021-01-25

## Task1
1. prepare settings (for windows)
- install "anaconda" 
- install "visual studio code"
- install "git"

2. prepare directory (at github & laptop)
- create repository "test" on github ("/username_on_github/test.git" ; "git link")
- create a directory on laptop ("C:\Users\test")

3. Authentification (to allow access from laptop to repo at github)
- Press *"control + R"* to open cmd prompt
- go to the directory on laptop
```
cd "C:\Users\test"
```
- clone (copy and paste) the repo from github to laptop

```
    git clone "git link"
```
or
```
    git init
    git remote add origin "git link"
    git config user.name "__"
    git config user.email "__"
    git clone "git link"
```

- difference between *git clone* and git remote add* : https://stackoverflow.com/questions/4855561/difference-between-git-remote-add-and-git-clone


4. open directory on visual studio code
- click the directory (where you cloned repo)

## Task2
- assignments (first 5): https://dsft.code-data-ai.com/python-workshops/

- install python extension in VisualStudioCode, e.g. markdown preview


## 2021-01-26
Todo:
- data types, operators

> spike
- what is programming: a set of instructions to communicate with the system
- what is variable: object that can vary. 
  - e.g. "var = 5" : "var" is assigned to "5" 
  - Left Hand Side (LHS) is assigned by Right Hand Side(RHS); LHS is not constant but is varying. 

- data type, operators
	- integer division operator
	- numeric, boolean, list, strings, tuple
	- assignment (=), comparison between values (==)

- variable(object)s in python: https://www.golinuxcloud.com/python-type-of-variable/

## 2021-01-27
Todo:
- loops, conditionals, functions
- understand basic concepts (e.g. list, set, dict, tuple, string, int, float, boolean) (conditions & loops) (functions)
- assignments (week1-int-3&4)

> spike: loops & functions
- set is an unordered list and does not allow duplicates. (> key to assignments)
- loops
	- when you use while loop, be careful to have 'if - break'
	- using "if  + elif + else " is more efficient than using "if + if + if"
- functions 
	- ask 'specific task/instructions' (for this, we need to assign "values" to "variables")
	- returns/print a value (for this, we need to have "return" in the end of function)
	- elements : arguments -> formula/functions -> output
    - e.g.
    ```python  
    # function with one argument
    def sample(x): 
        print (['Input is ' + x ]

    sample('name')

    # function with two arguments    
    def sample(x, y): 
        output = (x+y)*2
	    return output

    # if default value for "y" is assigned in the function, this function will work even when you only entered one argument
    def sample2(x, y=0): 
        output = (x+y)*2
	    return output
    ```
- function - arguments: https://www.w3schools.com/python/gloss_python_function_arguments.asp
    

### 2021-01-28
Todo:
- assignments (intermediate 5-10)
- assignment (intermediate 3,6)

[x] solved the issue with github authentication issue between visual studio code and github

> - https://stackoverflow.com/questions/52533318/how-to-solve-the-requested-url-returned-error-403-in-git-repository#53129341
> - https://stackoverflow.com/questions/15381198/remove-credentials-from-git

[x] solved assignments-int-5-10
[x] transforming answers using 'for-loop' to 'list comprehension' (int-2,4,5)

> - https://www.programiz.com/python-programming/list-comprehension

### 2021-01-28
[x] solve assignments-int-3,6
[x] review assignments (w. Ottavia)
- use a clear terms (variable names) for the other readers (including future yourself)
- remember to keep things in simple and direct: instead of using multiple lines of for-loops, think first. There might be a basic concept that can be useful, but you are missing.

[-] exercises in book ch.1-5

# week2
### 2021-02-01-Mon
[x] update answers for assignments

[x] spike - numpy (week2-task1)
  - A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. 
  - When you operate on multiple arrays, always be careful to have same length of arrays.

      ```python
      # The number of dimensions : the rank of the array : a number of row
      # THe size of the array : shape 

      a = np.array([1,2,3,4,5,6]) 
      # one dimensional array (1-D) made of one row and six columns
      b = np.array([[1,2,3],[4,5,6]]) 
      # two dimensional array (2-D) made of two rows and two columns
      c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 
      # three dimensional array (3-D)
      
      # check a structure of given array: 
      a.shape # (6,)
      b.shape # (2,3)
      c.shape # (2,2,3)
      
      # find '6' in array a, b, c 
      a[5]
      b[1][2]
      c[0][1][2]

      # element by element operation (e.g, np.add()) is efficient way of handling data. 
      a = [1,1,1]
      b = [2,2,2]
      c = np.add(a,b)

      ```


[x] pandas questions 

[-] exercises in book ch.3-5


### 2021-02-02-Tue
[-] pandas - find errors on tutorial page
    - typos in dataset: Comedy - Comdy/comedy, Romance  -romance/Romence/Romance 
    - duplicated rows:2
    - wrong values (string) in int64 column (Worldwide Gross)
    - there is no Romance movies produced by Disney
    - blanks in column names
    - there are only two studios with averaged audience score greater than 70%
[-] solve top 20 questions among 100 numpy questions
[-] exercises in book ch.3-5

- functins/methods are with (), 
- dataframes/values are indexed with []

[x] spike - pandas exercises (w.Ottavia) (week2-task1)
  - df['film'].map(type) //display the type of objects in column 'film'
  - df['film'] = df['film'].astype("string") //convert the type of objects in column 'film' into 'string' 
  - df['Genre'].replace['Comdy','comedy','romance','Romence'],['Comedy','Comedy','Romance','Romance'],inplace=True) //replace elements
  - df.drop.duplicates()
  - df.isnull().value_counts()

### 2021-02-03-Wed
[-] solve top 20 questions among 100 numpy questions
[x] complete pandas exercises
[x] spike - statistics (week2-task2)
- what is difference between mathematics and statistics
  - mathematics calculates the values based on the principles.
    - Statistics consider the situations, e.g. probabilities, as in real life. 
    - Statistics shows a characteristic of a sample (given context/population).
    
- probability
  - Probability exists between 0 and 1
  - Uncertanty and variation

- descriptive statistics
    ```python
    import numpy as np
    val = np.array([10,20,30])

    # Measure of Frequency (Count, Percent, Frequency)
        len(val) # Count: how many items exist in the list "val"
        # Percentage: the proportion of items in the list "val"
        # Frequency: how many times items occurs in the list "val"

        # Distribution: how each item is distributed in the list "val", histogram will show how the distribution of items in the list. e.g., standard distribution

    # Measure of Central tendency (Mean, Median, Mode)
        np.mean(val) #mean is average of a given set of data
        np.median(val) #median is the middle value in a data set.
        import statistics
        statistics.mode(val) #mode is a list of numbers refers to the integers that occur most frequently. 

    # Measure of Variation (Range, Variance, Standard Deviation)
        np.range() # range is a difference between lowest and highest value.
        # variance is the sum of squares of differences between all numbers in the data and their mean.
        # standard deviation is square root of variance. It measures the extent to which data varies from the mean.
    
    # useful source for understnading the concepts: https://www.geeksforgeeks.org/mathematics-mean-variance-and-standard-deviation/
    ```

[x] questions 1-3 (source: https://dsft.code-data-ai.com/stats-1/)
[x] concept of percentile / outlier  

### 2021-02-04-Thu
Todo:
[x] solve top 10 questions among 100 numpy questions
[x] solve last 2 questions (pandas)
[x] statistics basics - mean, median, standard deviation, normal distribution, discrete/continuous variable

[x] had a problem with importing library (pandas) in visual studio code, and solved this by entering two lines of codes in cmd
  ```python
  cd C:\Users\Anaconda3\lib\site-packages (#a directory where pandas is installed)
  python -m pip install --upgrade pandas
  # - solution source: https://github.com/boy1dr/SpleeterGui/issues/69

  ```
## 2021-02-05-Fri
Todo:
[] solve 11-20 questions among 100 numpy questions
[x] statistics basics (summary) + R exemple
[x] pandas basic functions
[x] project1-wine- preprocessing dataset, concatenating dataframes, changing NaN to value

# week3
## 2021-02-08-Mon
Todo:
[-] read paper for wine project
[] solve 11-20 questions among 100 numpy questions
[] pandas cheetsheet
[-] matplotlib - data visualization
[x] spike - data exploration

```python
y = lambda x: 'low' if value <= 5 else 'medium' if value <= 7 else 'high'

z = lambda x, y: x + y if x%2 == 0 else x + y + 2
z(5,6) 
#out: 13

[x for x in list if x >5]

# anatomy of a figure
[]image

```
-  what is difference between list comprehension and lambda function:
- > https://dev.to/suvhotta/python-lambda-and-list-comprehension-5128
-  lambda used inside list comprehension
- > https://stackoverflow.com/questions/10070477/lambdas-inside-list-comprehensions
- ? can we use 'df.apply.lambda[]'  to fill NaN in column wine_type 

- how to transform datatype pandas
https://stackoverflow.com/questions/34844711/convert-entire-pandas-dataframe-to-integers-in-pandas-0-17-0

## 2021-02-09-Tue
Todo:
[] read paper for wine project
[] matplotlib - 5 visualizations comparing white/red wine: quality, acidity, alcohol + explanations
[] pandas cheetsheet

## 2021-02-10-Wed
```python
import seaborn as sns
sns.histplot(data=wines, x = "alcohol", hue="wine_type", multiple="stack");
sns.histplot(data=wines, x = "alcohol", hue="wine_type", multiple="dodge");

# ? how can we display proportion of three acidity types (Yaxis, three groups indexed by color) within 6 quality level (Xaxis), per wine_type (X axis 1st level) > catplot (x, y, hue = 'quality_label')
sns.catplot(x = wine type, y = quality label, data = wines, kind="count");
sns.pairplot ( data, hue = "wine_type") > shows the relationship between two variables (x/y)
sns.scatterplot ( data, hue = "wine_type", style = "time")
sns.boxplot(x = wine type, y = , data = wines, hue = quality)

fig = g.get_figure()
fig.savefig('filename.png', dpi=600)
```

## 2021-02-11-Thu
[x] seaborn - setting up for the grid, position is different for each plot type 
[x] wine-5 plots using seaborn - violin, pairplot (grid), lmplot

```python

# multiple plots in one view
https://towardsdatascience.com/clearing-the-confusion-once-and-for-all-fig-ax-plt-subplots-b122bb7783ca

# position of multiple subplots
https://stackoverflow.com/questions/56788245/is-there-a-restriction-on-catplot-with-subplot
https://stackoverflow.com/questions/35042255/how-to-plot-multiple-seaborn-jointplot-in-subplot

```
[x] basic guideline for presenation
- cover page - topic words
- background and goal: why we choose this dataset, what do we want to tell
- agenda (Catch phrase) for single big ideas/insights
- max.2 plots per slide
- steps of analysis
- total max. 5-6 slides


## 2021-02-12-Fri
[x] wine- presentation
[x] summary of codes for plots (ipnyb)
[-] cheetsheet for pandas 

# week4
## 2021-02-15-Mon
[-] spike - basic concepts in machine learning : supervised vs. unsupervised, scikit-learn
[-] understand basic concepts and methods
- [-] read machine learning handbook ch.5
- [-] try code exemple

## 2021-02-16-Tue
[x] spike - cross validation
[-] understand basic concepts and methods
- [x] read machine learning handbook ch.5
- [-] try code exemple

## 2021-02-17-Wed
[-] understand basic concepts and methods
- [x] summarized notes for basic concepts and methods
- [x] try code exemple:  modelling - logistic regression : https://towardsdatascience.com/understanding-logistic-regression-step-by-step-704a78be7e0a
- [x] try code exemple:  modelling - classification - k-nearest neighbors, random forest
- [-] try code exemple:  modelling - regression - k-nearest neighbors, random forest
 
[-] wine project 
  - [x] predict the quality of white wine using all variables
  - predict the quality of white wine using top 3/4 critical variables 
  - compare which classifier method shows high accuracy: https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/


## 2021-02-17-Thu
[-] wine project 
  - predict the quality of white wine using top 3/4 critical variables 
    - feature selection methods: VIF, PCA
      - https://www.reneshbedre.com/blog/logistic-regression.html
  - [x] compare which classifier method shows high accuracy: https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/

[x] spike - accuracy and kappa
  - one hot encoding: transforming categorical variables into using dummy variables ('dummify')
    - https://towardsdatascience.com/one-hot-encoding-multicollinearity-and-the-dummy-variable-trap-b5840be3c41a
  - Recall, precision, Accuracy
    - Recall: the ability of a classifier to find all positive instances. For each class it is defined as the ratio of true positives to the sum of true positives and false negatives.
    - ?Recall: TP/TP+FN: how many correct answers you made from all target (positive/negative) datapoints 
    - Precision: the ability of a classifier not to label an instance positive that is actually negative. For each class, it is defined as the ratio of true positives to the sum of a true positive and false positive.
    - ?Precision: TP /TP+FP : how many correct answers you made from all datapoints


    - Accuracy: 
      - confusion matrix gives information about TP, TF, NP, NF 
        - confusion matrix: https://en.wikipedia.org/wiki/Confusion_matrix
        - https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
        - how to plot confusion matrix: https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html#sphx-glr-auto-examples-miscellaneous-plot-display-object-visualization-py
    - Classification report
      - F1 score: a weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0.
      - Support: the number of actual occurrences of the class in the specified dataset. Imbalanced support in the training data may indicate structural weaknesses in the reported scores of the classifier and could indicate the need for stratified sampling or rebalancing. Support doesn’t change between models but instead diagnoses the evaluation proces
    - You can use F1-score for performance (accuracy considering precision and recall)
  - when there is a missing value in one variable(column), calculate the median of corresponding values in other column(index)

## 2021-02-18-Fri
[] wine project
  - [x] preprocessing : standardization/normalization 
  - predict the quality of white wine using top 3/4 critical variables 
    - feature selection methods: VIF, PCA
      - https://www.reneshbedre.com/blog/logistic-regression.html
  - compare which classifier method shows high accuracy: https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/

[] 11.30 - spike/new mentor
  - labelencoder: wine type (category: string > numeric)
  - imbalanced dataset (White >>>> Red)
    - randomundersampler (same size of W/R wine)
  - 
[-] new mentor - decision tree and random forest

# week5
## 2021-02-22-Mon
[] wine project
  - predict the quality of white wine using top 3/4 critical variables 
    - [x] feature selection methods: VIF, PCA
      - https://www.reneshbedre.com/blog/logistic-regression.html
  - compare which classifier method shows high accuracy: https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/

[] spike - feature selection, KNN, decision tree (base for random forest)
  - preprocessing: label encoder, feature engineering, minmax/standard scaler
  - criteria of the model selection: pick the one when both accuracy and kappa score are high.
  - decision tree
    - f1: root node, child node, and leaf node (max_depth: 2 / the value of max_features is greater than the value of max_depth)
    - every split decreases the impurity (informatino gain increase)

## 2021-02-23-Tue
[] wine project
  - [x] predict the quality of white wine using random forest
  - [x] extract top 3-5 critical variables using random forest/SelectFromModel

[] predictive modeling methods
  - baggin methods
  - boosting methods
    - try other algorithms like KNN, SVM similarly for Wine Quality Prediction like you did for Wine Type prediction.

## 2021-02-24-Wed
[] wine project
  - preprocessing - price dataset: impute missing values
  -  
## 2021-02-25-Thu
[] wine project
  - modelling - red wine (quality, price)
  - feature importance - red wine (quality)
  - compare algorithms - red wine (quality)
  - 
## 2021-02-26-Fri
[] wine project
  - visualization - red wine, white wine : predicted vs. actual price
    - 
  - wordcloud(?)

# week 6
## 2021-03-01-Mon
[-] technical report
  - technical report about basic concepts in machine learning: https://ficw.fsu.edu/sites/g/files/upcbnu1106/files/pdf-files/TR%20Data%20and%20Statistics%20121115.pdf
  - guidelines for technical report
  > http://stat.cmu.edu/~brian/701/notes/paper-structure.pdf
  > https://www.aresearchguide.com/writing-a-technical-report.html

  - examples of technical report (detailed versions)
    - I think the index/table of contents section in these reports might be useful for having an idea about the general frame of technical report in data anlysis.
    > https://www.nrel.gov/docs/fy18osti/68913.pdf
    > https://www.researchgate.net/publication/342068999_Company_Data_Analysis_Summary_Safety_AI_technical_report
    > https://www.who.int/ncds/surveillance/steps/Part4.pdf
[] code review
  - write codes for wine project in complete one document: connecting wine quality dataset and price dataset

## 2021-03-02-Tue
[-] technical report
[-] code review

## 2021-03-03-Wed
[x] bike project
  - preprocessing
  - visualization: daily demand during one week
[x] spike - basic - json data

## 2021-03-04-Thu
[x] bike project
  - visualization: weekday/weekend demand

## 2021-03-05-Fri
[x] technical report - data preprocessing, transformation for ML analysis
[] spike - technical report
  - version info (ver, author, date, modification)
  - dataset features (e.g., class imbalance)
  - code snippet
  - STAR methods for each section: situation, task, action, result
[] spike - code review
  - initial write - header: author, version, description, project 

# week7
## 2021-03-09-Tue
[-] bike project
  - reply to email: general pattern of bike demand for users.
    - exploartory analysis : visualization using custom dataset (h/d/membertype/count)
  - statistic models for detailed analysis

## 2021-03-10-Wed
[x] bike project
  - preprocessing - timeseries dataset
  - visualization - timeseries using datetime(index)
  - ? how to convert values of duration from datetime dtype to numeric

## 2021-03-11-Thu
[x] bike proejct
  - modeling - regression - custom dataset 
  - research - timeseries : add more relevant infos (e.g., rider types ~ duration/length of trips, frequent route of trips ~ weather ~ location of stations?)
[] ML background
  - summary - bagging vs. boosting algorithms for RF model

## 2021-03-12-Fri
[x] bike project
  - modeling - regression - UCI dataset (2011+2012, 2011)
  - draft for presentation
