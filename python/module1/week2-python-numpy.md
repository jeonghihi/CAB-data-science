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

df['Genre'].replace['Comdy','comedy','romance','Romence'],['Comedy','Comedy','Romance','Romance'],inplace=True)

## Can you print the first 10 records.
df.loc[:9] 
#df.head(10)

# What are the data types of the columns.
df.dtypes

# Count of Animation movies. (Hint: use the count() function)
df_ani = df[df['Genre'] == 'Animation']
df_ani.count()[0]
# other answers: df.Genre.value_counts()['Animation']

# Show the Comedy movies in the year 2007.
df_comedy_2007 = df[(df['Genre'] == 'Comedy') & (df['Year'] == 2007)]
df_comedy_2007

# Count of Animation movies with more than 70% Audience Score.
df_ani = df[df['Genre'] == 'Animation']
df_ani_70 = df_ani[df_ani['Audience score %'] > 70 ]
df_ani_70.count()[0]

# another answer: 
    # df_ani = df[(df['Genre'] == 'Animation']) & (df['Audience score %'] > 70)]
    # df_ani.count()[0]

# Show the list of top 5 movies based on profitability.
df.sort_values(by = 'Profitability', ascending = False ).head(5)

# Show the top 5 Comedy movies approved by the audience. (hint : Audience Score)
df[df["Genre" == "Comedy"]].sort_values(by = 'Audience score %', ascending = False ).head(5)

```

## task1-ecercises-numpy
- source: https://medium.com/python-in-plain-english/100-numpy-exercises-for-data-science-1d1bb221e7cd

```python
### 1. 

```

# pandas
- tutorial: https://dsft.code-data-ai.com/pandas-dataframe/

## Show the movies with more than 70% Audience Score & greater than $350 Worldwide Gross.
```python
df_world_gross_string = df['Worldwide Gross'].str.replace('$','')
df_world_gross_number = pd.to_numeric(df_world_gross_string)
df['Worldwide Gross'] = df_world_gross_number

df[(df['Audience score %'] > 70 ) & (df['Worldwide Gross' > 350])]
```

## Show the movies  produced by Disney with more than 70% Audience Score & greater than $350 Worldwide Gross .
```python
df[(df['Lead Studio'] == 'Disney') & (df['Audience score %'] > 70 ) & (df['Worldwide Gross' > 350])]
```

## Count of Animation movies with more than 70% Audience Score. (Hint: use the count() function)
```python
df_ani = df[df['Genre'] == 'Animation']
df_ani_70 = df_ani[df_ani['Audience score %'] > 70 ]
df_ani_70.count()[0]
```

## Show the list of top 5 movies based on profitability.
```python
df.sort_values(by = 'Profitability', ascending = False ).head(5)
```

## Show the top 5 Comedy movies approved by the audience. (hint : Audience Score)
```python
df.sort_values(by = 'Audience score %', ascending = False ).head(5)
```

## Which Genre is favored the most by the Audience ?

```python
df.count()[0]
df_ani_70.count()[0]

# calculate the mean of audience scores for each genre
df_audience_score_ave_genre = df.groupby('Genre')['Audience score %'].mean()
df_audience_score_ave_genre.tail(1)

```


# Top 5 movie names by Rotten Tomato Score. ======== ing
```python
# show index of top 5 movies : df.sort_values(by = 'Rotten Tomatoes %', ascending = False ).head(5).index

# append indexes of top 5 movies to a list
list_rot_5_index =  df.sort_values(by = 'Rotten Tomatoes %', ascending = False ).head(5).index.values
names_rotten_top5 = []

    # print names using the list of indexes
for item in list_rot_5_index:
  row = df.iloc[[item],:]['Film'].astype('string')
  names_rotten_top5.append(row)

names_rotten_top5

## another answer
sorted_five = df.sort_values(by = 'Rotten Tomatoes %', ascending = False ).head(5)
sorted_five_film = sorted["Film"]

```

# Top 3 high gross Romance movies produced by Disney after 2008

# How many Lead Studios are present in the dataframe ? (Hint: use the function value_counts() which applies to category)

# Top 5 profitable movies produced by Disney after 2008 (measured by Profitability index)

# Most & Least Frequent lead studio in the dataset in terms of occurances.

# Most and Least profitable Lead Studio. (Take an average of all Profitability measures grouped by Lead studios)

# Top 5 lead studios with audience score greater than 70%.

# Count of least Frequent Genre with Rotten Tomato score more than 50%.

# Ranking of Fox studio for Comedy movies based on Audience Score.

# Count of each genre of movies produced by Independent. (use groupby() )

```
