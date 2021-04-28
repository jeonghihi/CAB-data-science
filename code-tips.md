---
# title : "python-code-tips"
# date : "2021-03-09"
# tags : [python, exemple, stats]
---

# essential python libraries

## data cleaning/transformation
pandas
numpy
## modeling
sklearn

## visualization
seaborn
matplotlib

[] markdown formatting
  - https://daringfireball.net/projects/markdown/syntax#html
  - TOC 
    - https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents/33433098#33433098
    - https://stackoverflow.com/questions/21151450/how-can-i-add-a-table-of-contents-to-a-jupyter-jupyterlab-notebook

[] figure
  - subplots : https://stackoverflow.com/questions/55767312/how-to-position-suptitle
  - stacked barplot (plt) : https://www.weirdgeek.com/2018/11/plotting-stacked-bar-graph/, https://www.python-graph-gallery.com/13-percent-stacked-barplot, https://stackoverflow.com/questions/63906653/how-to-add-annotations-to-stack-percentage-barplot-in-matplotlib

  - stacked barplot (seaborn) : https://randyzwitch.com/creating-stacked-bar-chart-seaborn/, https://stackoverflow.com/questions/50160788/annotate-stacked-barplot-matplotlib-and-pandas

  - barplot - color scale by rank : https://stackoverflow.com/questions/36271302/changing-color-scale-in-seaborn-bar-plot
  - barplot (seaborn) - annotation : https://stackoverflow.com/questions/39519609/annotate-bars-with-values-on-pandas-on-seaborn-factorplot-bar-plot

  - multiple plots (seaborn) : https://towardsdatascience.com/a-step-by-step-guide-for-creating-advanced-python-data-visualizations-with-seaborn-matplotlib-1579d6a1a7d0
  - subplots 
    - https://towardsdatascience.com/a-step-by-step-guide-for-creating-advanced-python-data-visualizations-with-seaborn-matplotlib-1579d6a1a7d0
    - https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html

  - nice visualizations: https://drawingfromdata.com/seaborn/matplotlib/visualization/rotate-axis-labels-matplotlib-seaborn.html


[] pandas
  - multiple group by: https://www.statology.org/pandas-groupby-aggregate-multiple-columns/
  - drop column pandas : https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe
  - reshape tables : https://pandas.pydata.org/docs/user_guide/reshaping.html
  - sql: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html?highlight=read_sql#pandas.read_sql
  - 
# code crumbs

## string transformation 
- https://www.askpython.com/python/string/python-remove-spaces-from-string

- https://stackoverflow.com/questions/15129567/csv-writer-writing-each-character-of-word-in-separate-column-cell

```python
#%% split text string: partition vs. split
my_test = "url/dp/string1/string2" # / = %2F
left_text = my_text.partition(r"/dp/")[0]
mid_text = my_text.partition(r"/dp/")[1]
right_text = my_text.partition(r"/dp/")[2]
```

## write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
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

# datetime 
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
    
df_fun_stock.info()


# based on value_counts() in one specific column 
https://stackoverflow.com/questions/17709270/create-column-of-value-counts-in-pandas-dataframe#17709453

# difference between timedata
https://www.plus2net.com/python/pandas-dt-timedelta64.php

# stacked barchart with timeseries data
https://stackoverflow.com/questions/42044299/stacked-histogram-with-time-series-data-with-gnuplot


# bike project - df2 (customized dataset) - add index column for later processing
```python
time_list = []
for row in range(df2.shape[0]):
    time_ind = str("{}{}{}".format(df2['day'][row], '-',df2['hour'][row]))
    time_list.append(time_ind)

df2['time_ind'] = time_list
```

# convert all numbers in timedelta data into second scale 
```python
import numpy as np
temp = df1['duration'][1]
a = np.timedelta64(temp,'s')
a.astype("timedelta64[s]")
a
```

# change hour to datetime
for i in range(0,len(df2)):
  temp = datetime.datetime.strptime(str(df2.iloc[i][1]).replace('.0',''),'%H')
  df2.iloc[i,1] = temp.strftime('%I%p')

# convert dict.keys to column names
- from: preprocessing_product_detail.py
- keys to cols  (error: col_list is made from duplicates of all products)

```python
for item in data_new:
    col_list = [] 
    val_list = []
    if item is not None:
        for feature in item_dict:
            col = list(feature.keys())[0]
            val = list(feature.values())[0]
            col_list.append(col)
            val_list.append(val)
    else:
        None
    print(col_list)
    print(val_list)

    item_df = pd.DataFrame(val_list,columns = col_list)
    print(item_df.head())

# create dataframe (product_info)        
pt= pd.DataFrame([['NaN']*len(col_list)], columns=col_list)
pt
```