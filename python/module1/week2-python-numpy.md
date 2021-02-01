---
# title : "python-module1-week2-assignments"
# date : "2021-02-01"
# tags : [python, exemple]
---

# 2021-02-01-week2

## task1-assignments-numpy
- tutorial : https://cs231n.github.io/python-numpy-tutorial/#numpy

- assignments : https://github.com/CodeAcademyBerlin/Data-Science/blob/master/Module%201/Week%202/Task1.md
- answer: https://colab.research.google.com/drive/1iEWrGrnDA0JVVaDBzVT_b7KQx46UWwCH?usp=sharing

```python

import pandas as pd
data_source = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'

df = pd.read_csv(data_source)
df

## Can you print the first 10 records.
df.loc[:9] 
#df.head(10)

# What are the data types of the columns.

df.dtypes

# Count of Animation movies. (Hint: use the count() function)
df_ani = df[df['Genre'] == 'Animation']
df_ani

df_ani.count()[0]

# Show the Comedy movies in the year 2007.
out = df[(df['Genre'] == 'Comedy') & (df['Year'] == 2007)]
out

# Count of Animation movies with more than 70% Audience Score.
df_ani = df[df['Genre'] == 'Animation']
df_ani_70 = df_ani[df_ani['Audience score %'] > 70 ]
df_ani_70

# Show the list of top 5 movies based on profitability.
df.sort_values(by = 'Profitability', ascending = False ).head(5)

# Show the top 5 Comedy movies approved by the audience. (hint : Audience Score)
df.sort_values(by = 'Audience score %', ascending = False ).head(5)

```

## task1-ecercises-numpy
- source: https://medium.com/python-in-plain-english/100-numpy-exercises-for-data-science-1d1bb221e7cd


# pandas
- tutorial: https://dsft.code-data-ai.com/pandas-dataframe/
