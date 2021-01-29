---
# title : "python-module1-week1-assignments"
# date : "2021-01-25"
# tags : [python, exemple]
---


- QnA source: https://dsft.code-data-ai.com/python-workshops/

# Beginner

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


# Intermediate

#Q1: Write a method that takes the array as an argument and returns this “outlier” N.

```python
input = [2, 4, 6, 8, 10, 3]

def out_odd_or_even(input):
    list_odd = []
    list_even = []
    
    for i in input:
        num = i  
        if (num % 2) == 0:
            list_even.append(i)      
        else: 
            list_odd.append(i)
    
    if len(list_odd) < len(list_even):
        out = list_odd
    else:
        out = list_even

    print(out)


def out_odd_or_even2(input):
    odd = []
    even = []
    grouping = [odd.append(i) if (i % 2) == 0 else even.append(i) for i in input]
    out = [odd if len(odd)<len(even) else even]
    return out

## don't know how to unwrap double-list: change the output from [[3]] to [3] 

```

#Q2: implement a difference function, which subtracts one list from another and returns the result.


```python
def array_diff1(a,b):
    res = []

    for i in a:
        if i not in b:
            res.append(i)
    return res 


def array_diff2(a,b):
    return list(set(a) - set(b))
    # return list(set(a).difference(set(b)))

input: a = [1,2], b = [1]
# output: [2]
input: a = [1,2,2], b = [2]
# output: [1]
```

#Q3: *on going*

```python

```

#Q4: create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
```python
def filter_list1(input):
    keep = []

    for index in input:
        if type(index) is int: 
            keep.append(index)
    return keep


def filter_list2(input):
    return [i for i in input if type(i) == int]

input = [1,2,'a','b'] 
# output = [1,2]
input = [1,'a','b',0,15]
# output = [1,0,15]
input = [1,2,'aasf','1','123',123]
# output = [1,2,123]

```

#Q5: Given an array, find the int that appears an odd number of times.
```python
def find_it(input):
    numbers = set(input)
    res = [] 
    for num in numbers:
        val = input.count(num)
        if (val % 2) != 0:
            res.append(num)
    return res


def find_it2(input):
    return [num for num in numbers if input.count(num) % 2 != 0]

input = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
# ouput = [5]
```

#Q6:  *on going*
```python

```

#Q7: 
```python
def validate_pin(input):
    if len(input) == 4 or len(input) == 6:
        if input.isdigit():
            print ('True')
        else:
            print ('False')
    else: 
        print('False')

input = "1234"
# True
input = "12345"
# False
input = "a234"
# False
```

#Q8: given a string of words, return the length of the shortest word(s).
```python
def find_word_short(input):
    string = input.split(' ')
    res = []
    for word in string:
        count_letters = len(word) 
        res.append(count_letters)
    return min(res)
    
input = 'Friday i am in love'
#output = 2

# related: 
# - https://stackoverflow.com/questions/2932511/letter-count-on-a-string
```

#Q9: write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
```python
def missing_letters(input):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = ''.join(input).casefold()
    
    for i in range(0,len(alphabet)-1):
        if alphabet[i] == string[0]:
            part = alphabet[i:i+len(string)+1]
            target = str(part)
            missing = []
            for i in target:
                while i not in string:
                    missing.append(i)
                    break

            return missing

input = ['a','b','c','d','f'] 
# output = 'e'

input = ['O','Q','R','S']
# output = 'P'

# find a string starting with a given letter in another string
# : string1[i].startswith(string2[0]) 

# related: 
# - (https://stackoverflow.com/questions/2970520/string-count-with-overlapping-occurrences) 
# - (https://stackoverflow.com/questions/55265024/missing-letters-method-with-python)
```

#Q10: Make a program that filters a list of strings and returns a list with only your friends name in it. If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he /she is not.

```python
def find_friends(input):
    friends = []
    for i in range(0, len(input)):
        val = input[i] 
        if len(val) == 4:
            friends.append(val)
    return friends 

input = ['Ryan', 'Kieran', 'Jason', 'Yous']
# output = ['Ryan', 'Yous']

```

### Other related tips:
- a structure of list comprehension: [ <RETURNED_VALUE>  <OUTER_LOOP1>  <INNER_LOOP2>  <INNER_LOOP3> ... <OPTIONAL_IF> ]
- https://stackoverflow.com/questions/1198777/double-iteration-in-list-comprehension
- 
    ```python
    c=[111, 222, 333]
    b=[11, 22, 33]
    a=[1, 2, 3]

    print(
    [
        (i, j, k)                            # <RETURNED_VALUE> 
        for i in a for j in b for k in c     # in order: loop1, loop2, loop3
        if i < 2 and j < 20 and k < 200      # <OPTIONAL_IF>
    ]
    )
    [(1, 11, 111)]
    ```
- examples of list comprehension: https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
- sets: https://www.datacamp.com/community/tutorials/sets-in-python, https://www.quora.com/What-is-Python-set-union, https://www.python-course.eu/sets_frozensets.php
- visualizations: https://python-graph-gallery.com/ 