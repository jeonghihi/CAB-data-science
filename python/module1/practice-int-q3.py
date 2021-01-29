# === Q3 ===================================================

namelist = ([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
namelist = ([ {'name': 'Bart'}, {'name': 'Lisa'} ])
namelist = ([ {'name': 'Bart'} ])

n = len(namelist)
res = []

for x in range(0, n):
    my_dic = namelist[x]
    my_key = 'name'
    val = my_dic[my_key]

    if n == 1:
        res.append(val)

    if n == 2:
        while x < n-1:
            res.append(val)

        if x == n-1:
            out1 = str(val)
            con1 = '& ' 
            res.append(out1 + con1)   

if x == n:
    break

    if n > 2:
        while x < n-1:
            out1 = str(val)
            con1 = ', '
            res.append(out1 + con1)

        if x == n-1:
            out1 = str(val)
            con1 = '& ' 
            res.append(con1 + out1)  
            break   

return str(','.join(res))

output = str(','.join(res))
output 



    
# === old

    if n = 2:
        while x < n-1:
            out = val
            res.append(out)
            x = x + 1
        if x = n-1:
            out = str(val)
            con1 = '& ' 
            res.append(con1 + out)
        output = str()

output


# === old
    if n > 2:
        while x < n-1:
            out = val
            res.append(out)
            x = x + 1
        if x = n-1:
            out = str(val)
            con1 = ',& ' 
            res.append(con1 + out)

    if n = 2:
        out = str(my_dic[my_key])
        con2 = '& '
        res.append(con2 + out)

    if n < 2:
        out = my_dic[my_key]
        res.append(out)

    ''.join(res)

# returns ‘Bart, Lisa & Maggie‘


# Q3-A2:
for k,v in namelist.items():
    if k == 'names'
        print(v)


# === Q 6  ===================================================
# 2021-01-26-16.30 ~ 17.00 (not done)

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

if the amount of X and O is same, or if  there is no X or O
give true

if data.count['x'] == data.count['o']
    print('True')



#
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