# === Q3 ===================================================
namelist = ([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
namelist = ([ {'name': 'Bart'}, {'name': 'Lisa'} ])
namelist = ([ {'name': 'Bart'} ])
namelist = ([])

def list_names(input):
    n = len(input)
    res = []
    for x in range(0, n):
        my_dic = input[x]
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

# Is there a more efficient way? if I want to use 'while-break', how could the codes be written?
# Q3-A2 (on going):
names = []
res = []
for i in range(0,len(namelist)):
    name = namelist[i]['name']
    names.append(name)

if len(names) < 2:   
    res = names    
    output = str(' '.join(res))

elif len(names) == 2:
    res = names
    output = str('&'.join(res))

else: 
    for i in names:
        ...


# Q6 : if the amount of X and O is same, or if  there is no X or O, give true
# 2021-01-26-16.30 ~ 17.00 (not done)
# 2021-01-29-11:50 (done?)

input = 'ooxx'

def XO(input):
    import re 

    string = input.casefold()
    if len(re.findall('x', string)) == len(re.findall('o', string)):
        out = print('true')
    else:
        out = print('false')
    return out

XO(input)




# === old ================================================
input = 'ooxx'
# output = true

data = 'ooxXm'
data_all = []
data_part = []

for i in range(0,len(data)):
    data = data.casefold()
    val = data[i]
    data_all.append(val)
    if val not in data_part: 
        data_part.append(val) 

data_all
data_part


# write a method that takes an array of consecutive (increasing) letters 
# as input and that returns the missing letter in the array.

def count_letters(word, char):
    count = 0
    for c in word:
        count += (char == c)
    return count

def count_substring(string, sub_string):
    count = 0
    for pos in range(len(string)):
        if string[pos:].startswith(sub_string):
            count += 1
    return count