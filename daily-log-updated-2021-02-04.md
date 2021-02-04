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
    ```
    cd C:\Users\Anaconda3\lib\site-packages (#a directory where pandas is installed)
    python -m pip install --upgrade pandas
    # - solution source: https://github.com/boy1dr/SpleeterGui/issues/69

    ```
### 2021-02-05-Fri
Todo:
[] solve 11-20 questions among 100 numpy questions
[] statistics basics (summary) + R exemple
[] pandas basic functions