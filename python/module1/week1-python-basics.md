---
# title : data-science-module1-week1-assignments
# date :
---


- source: https://dsft.code-data-ai.com/python-workshops/

# beginner
#Q1
list_year = [1999, 1995, 2005, 2010, 2007, 2006, 1994, 1996, 1979, 2008]
out_year = []

for x in list_year:
    age = 2021 - x
    out_year.append(age)

print(out_year)
# Q1-answer: 


#Q2
list_year = [20, 24, 14, 9, 12, 13, 25, 23, 40, 11]
res = [] 

for i in list_year:
    out_old = max(list_year)
    out_young = min(list_year)
    if out_young < i < out_old:
        res.append(i)

print(res) 
# Q2-answer: [20, 24, 14, 12, 13, 25, 23, 11]


list_year = [20, 24, 14, 9, 12, 13, 25, 23, 40, 11]
res = [] 

for i in list_year:
    if min(list_year) < i < max(list_year) :
        res.append(i)

print(res) 


# Q3
sample_list1 = [15, 13, 16, 18, 19, 10, 12 ]
sample_list2 = [7, 13, 15, 20, 19, 18, 10, 16]

# Q3-A1
out = set(sample_list1) & set(sample_list2)
out 

# Q3-A2
res = []

for i in sample_list1:
    if i in sample_list2:
        res.append(i)
     
print(res) 
# Q3-answer:[15, 13, 16, 18, 19, 10]


# Q4
sample_list = [15, 13, 16, 18, 19, 15, 10]
res = [] 

for i in sample_list: 
    if i not in res: 
        res.append(i) 
        
print(res)
# Q4-answer: [15, 13, 16, 18, 19, 10]
## another one line code: [res.append(x) for x in test_list if x not in res] 

# Q5
list_input =  [15,13,16,18,19,15,10]
tar_age = [15, 28]

for i in tar_age:
    if i in list_input:
        print('True')
    else:
        print('False')
    
# Q5-answer: 15 (true), 28 (false)
