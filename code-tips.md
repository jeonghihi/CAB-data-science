---
# title : "python-code-tips"
# date : "2021-03-09"
# tags : [python, exemple, stats]
---


[] markdown formatting
  - https://daringfireball.net/projects/markdown/syntax#html
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

# code crumbs

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
