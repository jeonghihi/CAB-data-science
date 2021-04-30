---
# title : "python-module1-week1-assignments"
# date : "2021-01-25"
# tags : [python, exemple]
---


- QnA source: https://dsft.code-data-ai.com/python-workshops/

# Beginner

#Q1: write a function that returns the age of customers
```python
#A1 - before review

def current_age(list_years):
    current_age = []
    
    for year in list_years:
        age = 2021 - year
        current_age.append(age)
        
    return current_age

list_years = [1999, 1995, 2005, 2010, 2007, 2006, 1994, 1996, 1979, 2008]
print (current_age(list_years))

#A2 - after review
def current_age2(list_years):
    current_age = []
    [current_age.append(2021 - x) for x in list_years] 
    return current_age

def current_age3(list_years):
    out = [(2021 - x) for x in list_years] 
    return out

```

#Q2: write a function that removes the outliers (the oldest and youngest person’s age) and return the new list with age of 8 persons (in this case which contains data for 10 customers initially).

```python
##A1
def age_middle(list_ages):
    res = [] 
    for i in list_ages:
        if min(list_ages) < i < max(list_ages) :
            res.append(i)
    return res

#A2
def age_middle2(list_ages):
    out = [i for i in list_ages if min(list_ages) < i < max(list_ages)]
    return out

list_ages = [20, 24, 14, 9, 12, 13, 25, 23, 40, 11]
age_middle(list_ages)
```

#Q3: write a function that takes these 2 lists as input and returns the common age values.
```python
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

##A3
def comm_age3(a,b):
    return [i for i in a if i in b]

a = [15, 13, 16, 18, 19, 10, 12 ]
b = [7, 13, 15, 20, 19, 18, 10, 16]
#out =  [15,13,16,18,19,10]

```

#Q4: write a function that takes the list with duplicate values as input and return the list with unique age values. 

```python
##A1
def unique_age(list_ages):
    res = [] 

    for i in list_ages: 
        if i not in res: 
            res.append(i) 
    return res

unique_age(list_ages)

##A2
def unique_age2(list_ages):
    [res.append(x) for x in list_ages if x not in res] 
    return res

##A3
def unique_age2(list_ages):
    res = list(set(list_ages))
    return res
    

list_ages = [15, 13, 16, 18, 19, 15, 10]
```

#Q5: write a function that takes an input list and value of age to find as input and return true or false if the age value is present or not.

```python
#A1 - before review (By accident, I changed the questions)
def target_age(target_ages):    
    for age in target_ages:
        if age in list_ages:
            return True
        else:
            return False
            
list_ages = [15,13,16,18,19,15,10]
target_ages = [15, 28]

target_age(list_ages,target_ages)

# A2 - after review
def target_age(list_numbers, number):    
        if number in list_numbers:
            return True
        return False
            

list_numbers = [15,13,16,18,19,15,10]
number = 15

target_age(list_numbers,number)
target_age([15,13,16,18,19,15,10], 28)

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

    print(out[0])


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

def array_diff3(a,b):
    return [i for i in a if i not in b]

input: a = [1,2], b = [1]
# output: [2]
input: a = [1,2,2], b = [2]
# output: [1]
```

#Q3: Return a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

```python

def print_names(namelist):
    n = len(namelist)
    res = []
    for x in range(n):
        my_dic = namelist[x]
        my_key = 'name'
        val = my_dic[my_key]
    
        if n == 1:
            res.append(val)
        elif n == 2:
            if x < n-1:
                res.append(val)
            if x == n-1:
                res.append('& ' + str(val))   
        else:
            if x < n-2:
                res.append(str(val) + ',')
            elif x == n-2:
                res.append(str(val))
            elif x == n-1:
                res.append('& ' + str(val))  
            else:
                break 
    output = str(' '.join(res))
    return output


namelist = ([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
namelist = ([ {'name': 'Bart'}, {'name': 'Lisa'} ])
namelist = ([ {'name': 'Bart'} ])
namelist = ([])

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
#A1 - before review
def find_it(numbers):
    res = [] 
    for num in numbers:
        val = numbers.count(num)
        if (val % 2) != 0:
            res.append(num)
            return res 
            
#A2 - after review
def find_it2(numbers):
    return list(set([num for num in numbers if numbers.count(num) % 2 != 0]))

numbers = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
# ouput = [5]
```

#Q6:if the amount of X and O is same, or if  there is no X or O, give true
```python
# 2021-01-26-16.30 ~ 17.00 (not done)
# 2021-01-29-11:50 (solved)
import re 
random_string = 'ooxx'

def XO(random_string):
    string = random_string.casefold()
    if len(re.findall('x', string)) == len(re.findall('o', string)):
        return True
    return False

# show results
XO(random_string)

# how to connect two functions
def feedback(random_string):
    if XO(random_string) == True:
        return ("It is true")
    return ("It is false")

```

#Q7: 
```python
#A1 - before review
def validate_pin(list_numbers):
    if len(list_numbers) == 4 or len(list_numbers) == 6:
        if list_numbers.isdigit():
            print ('True')
        else:
            print ('False')
    else: 
        print('False')

#A2 - after review
def validate_pin(list_numbers):
    if (len(list_numbers) == 4 or len(list_numbers) == 6) and list_numbers.isdigit():
        return True 

    return False

list_numbers = "1234"
# True
list_numbers = "12345"
# False
list_numbers = "a234"
# False
```

#Q8: given a string of words, return the length of the shortest word(s).
```python
#A1 - before review
def find_word_short(list_words):
    string = list_words.split(' ')
    res = []
    for word in string:
        count_letters = len(word) 
        res.append(count_letters)
    return min(res)
    
#A2 - after review
def find_word_short(list_words):
    string = list_words.split(' ')
    res = [len(word) for word in string]
    
    return min(res)
    
list_words = 'Friday i am in love'
find_word_short(list_words)

# related: 
# - https://stackoverflow.com/questions/2932511/letter-count-on-a-string
```

#Q9: write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
```python
#A1
def missing_letters(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = ''.join(s).casefold()
    missing_letter = []

    for i in range(0,len(alphabet)-1):
        if alphabet[i] == string[0]:
            string_to_compare = str(alphabet[i:i+len(string)+1])            
            for i in string_to_compare:
                while i not in string:
                    missing_letter.append(i)
                    break
    return missing_letter

# A2 - sample answer
import string
def find_missing_letter(s):
  alp_lower = list(string.ascii_lowercase)
  alp_upper = list(string.ascii_uppercase)
  
  s1 = ''.join(s)
  
  if s1.isupper():
    x = set(alp_upper[alp_upper.index(s[0]):alp_upper.index(s[-1])+1]) - set(s)
    return x.pop()
  else: 
    x = set(alp_lower[alp_lower.index(s[0]):alp_lower.index(s[-1]) + 1]) - set(s)
    return x.pop()


s = ['a','b','c','d','f'] 
# output = 'e'

s = ['O','Q','R','S']
# output = 'P'

# find a string starting with a given letter in another string
# : string1[i].startswith(string2[0]) 

# related: 
# - (https://stackoverflow.com/questions/2970520/string-count-with-overlapping-occurrences) 
# - (https://stackoverflow.com/questions/55265024/missing-letters-method-with-python)
```

#Q10: Make a program that filters a list of strings and returns a list with only your friends name in it. If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he /she is not.

```python
#A1
def find_friends(list_friends):
    friends = []
    for i in range(len(list_friends)):
        if len(list_friends[i]) == 4:
            friends.append(list_friends[i])
    return friends 

#A2 
def find_friends(list_friends):
    return [friend for friend in list_friends if len(friend) == 4]
    

list_friends = ['Ryan', 'Kieran', 'Jason', 'Yous']
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