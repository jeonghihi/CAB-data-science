---
# title : "python-module1-week2-assignments"
# date : "2021-02-05"
# tags : [python, exemple, stats]
---

- source: https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%201/Week%202/Task3-email.md

- presentation: 8-12 slides (final: ) 3-4 slides (small presentation: 15th Feb.)


- consider the customer's deadline than internal team deadline
- predict the proper price

# Task
- follow the guidelines and reply to Mark's email as you progress with the project.

1. load the dataset

2. understand the composition of red wine and white wine
- red wine: 
- white wine: 

3. combine two dataframes into one "wines" 
 
```python
  # load dataset
import pandas as pd
import numpy as np
red_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep= ';')
white_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep= ';')

red_wine.dtypes
red_wine.astype('int64').dtypes
red_wine.head()

white_wine.dtypes
white_wine.astype('int64').dtypes
white_wine.head()

# add a column 'wine_type' to dataframe 'red_wine' and 'white_wine'

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

wines['wine_type'] = wines['wine_type'].replace(np.nan, 'red')
wines

# wines['wine_type'] = wines['wine_type'].replace(wines['wine_type'] = np.nan, 'red')
# wines.loc[wines.wine_type = np.nan].fillna('red')
# wines.fillna(method='WORD', inplace=True)
# wines.fillna(0, inplace=True)
# wines[wines['wine_type'] != 'white']

# wines['ID'] = wines.index
# wines['wine_type'] = wines[wines.isna().any(axis=1)].replace(np.nan,'red')
# wines['wine_type'] = wines['ID'].map(wines_red.set_index('ID')['wine_type'])

  ```

4. score the quality of wine
- Wines with a quality score of 3, 4, and 5 are low quality;
- score of 6 and 7 are medium quality;
- score of 8 and 9 are high quality wines.







---

# Email

## customer (BlueBery Winery)
- a start-up company
- is trying to enter the business with a good amount of analytics & research on domain knowledge. 
- wine-maker (not distributior, not seller) 

- they want to build a Wine Quality Analytics system which can help them determine the quality of wines produced based on ingredients & composition.
- companies should start with preliminary quality research on either market / wine quality.

- companies trust data and machine learning to come to a decision instead of expert recommendation / analysis.

- From a Sales & Marketing perspective, put a proper price tag for a bottle of wine.
  - > there should be no mismatch between quality and price of the product which is one of the major factors contributing to 'Customer Satisfaction'.
  
- many other factors that contribute to the quality.
  - The age of a bottle of wine : 
    - time changes the taste of the fruit flavors in a wine as well as 
    - time reduces the acidity and tannin in a wine
    - As the acidity and tannin are reduced, the wine becomes rounder and smoother.
- The analysis should not restrict to the technical specifications but include the business / domain aspects 
- help BlueBerry Winery with Business Decisions
-  