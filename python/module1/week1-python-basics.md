---
# title : data-science-module1-week1-assignments
# date :
---


- source: https://dsft.code-data-ai.com/python-workshops/

# beginner

#Q1: write a function that returns the age of customers
```python
input = [1999, 1995, 2005, 2010, 2007, 2006, 1994, 1996, 1979, 2008]

def current_age(input):
    current_age = []
    
    for x in input:
        age = 2021 - x
        current_age.append(age)
        
    print(current_age)

```

#Q2: write a function that removes the outliers (the oldest and youngest person’s age) and return the new list with age of 8 persons (in this case which contains data for 10 customers initially).

```python
##A1
input = [20, 24, 14, 9, 12, 13, 25, 23, 40, 11]

def age_middle(input):
    res = [] 
    for i in input:
        if min(input) < i < max(input) :
            res.append(i)
    print(res)

age_middle(input)
```

#Q3: write a function that takes these 2 lists as input and returns the common age values.
```python

a = [15, 13, 16, 18, 19, 10, 12 ]
b = [7, 13, 15, 20, 19, 18, 10, 16]

##A1
def comm_age(a,b):
    out = set(a) & set(b)
    print(out)

##A2
def comm_age2(a,b):
    res = []

    for i in a:
            if i in b:
                res.append(i)
    print(res) 
```

#Q4: write a function that takes the list with duplicate values as input and return the list with unique age values. 

```python
input = [15, 13, 16, 18, 19, 15, 10]

##A1
def unique_age(input):
    res = [] 

    for i in input: 
        if i not in res: 
            res.append(i) 
    print(res)

unique_age(input)

##A2
def unique_age2(input):
    [res.append(x) for x in input if x not in res] 
    print(res)

##A3
def unique_age2(input):
    out = set(input)
    print(list(out))
    
```

#Q5: write a function that takes an input list and value of age to find as input and return true or false if the age value is present or not.

```python
input_list = [15,13,16,18,19,15,10]
input = [15, 28]

def target_age(input):    
    for i in tar_age:
        if i in input_list:
            print('True')
        else:
            print('False')
            
target_age(input)

```
