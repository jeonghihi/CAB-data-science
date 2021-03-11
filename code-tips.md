---
# title : "python-code-tips"
# date : "2021-03-09"
# tags : [python, exemple, stats]
---


[] markdown formatting
  - https://daringfireball.net/projects/markdown/syntax#html
[] figure
  - subplots : https://stackoverflow.com/questions/55767312/how-to-position-suptitle
[] pandas
  - multiple group by: https://www.statology.org/pandas-groupby-aggregate-multiple-columns/


# code crumbs

# write a method that takes an array of consecutive (increasing) letters 
# as input and that returns the missing letter in the array.
```python
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
```

# pandas - questions : could not solve last two questions
```
df2 = df.join(df_AudienceScore_ave_Studio.set_index('Lead_Studio'), on='Lead_Studio')
```