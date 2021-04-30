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

## task1-exercises-numpy
- source: https://medium.com/python-in-plain-english/100-numpy-exercises-for-data-science-1d1bb221e7cd

```python
# 1. import numpy packages
import numpy as np

# 2. numpy version and the configuration
print (np.__version__) #1.19.2
np.show_config() # shows libarary_dirs, define_macros, include_dirs

# 3. Create a null vector of size 10 
Z = np.zeros(10)
print(Z) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# 4. find the memory size of any array
Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize)) # 800 bytes

# 5. get the document of numpy "add" function from cmd
# %run `python -c "import numpy; numpy.info(numpy.add)"`

# 6. create a null vector of size 10 + fifth value is 1
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 7. a vector with values ranging from 10 to 49
Z = np.arange(10,50)

# 7.2. a vector with values ranging from 10 to 49 with spacing 4
Z = np.arange(10,50,4)

# 8. reverse a vetor
Z = np.arange(50)
Z = Z[::-1]
print(Z)

# 9. Create a 3x3 matrix with values ranging from 0 to 8
Z = np.arange(9).reshape((3, 3))
print(Z)
# an exemple code in the given link was wrong

# 10. Find indices of non-zero elements from [1,2,0,0,4,0] 
nz = np.nonzero([1,2,0,0,4,0])
print(nz) #array([0, 1, 4], dtype=int64)

```

# pandas
- tutorial: https://dsft.code-data-ai.com/pandas-dataframe/
- useful source: https://pandas.pydata.org/docs/user_guide/index.html#user-guide

## load & preprocessing dataset: run these before starting assignments below
```python
# load dataset
import pandas as pd
data_source = 'https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
df = pd.read_csv(data_source)

# check data structure and column names
df.head() 

# check datatypes
df.dtypes 

# replace wrong data values in columns
## wrong Genre names
df.replace(['Comdy','comedy','Romence','romance'],['Comedy','Comedy','Romance','Romance'], inplace=True)

## wrong values in int64 column (Worldwide Gross)
world_gross_string = df["Worldwide Gross"].str.replace('$', '')
world_gross_number = pd.to_numeric(world_gross_string)
world_gross_number
df["Worldwide Gross"] = world_gross_number

# convert datatypes
df = df.astype({'Film': 'string', 'Genre': 'string','Lead Studio': 'string', 'Worldwide Gross': 'int64','Profitability': 'int64' })

# check errors in values of (potential) index column 
df.Genre.value_counts()

# change column names
columns = df.columns[:].tolist()
columns_new = [item.replace(' ', '_') for item in columns]
columns_new
df.columns = columns_new

# check empty values
df.isnull().value_counts()

# check duplicates in rows
df[df.duplicated()]

# remove duplicates and save as df_new
df.drop_duplicates(keep='first', inplace=True)


```

# first five assignments 

```python
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



## Show the movies with more than 70% Audience Score & greater than $350 Worldwide Gross.
```python
df[(df['Audience_score_%'] > 70 ) & (df['Worldwide_Gross'] > 350)]
```

## Show the movies  produced by Disney with more than 70% Audience Score & greater than $350 Worldwide Gross .
```python
df[(df['Lead_Studio'] == 'Disney') & (df['Audience_score_%'] > 70 ) & (df['Worldwide_Gross'] > 350)]
```

## Count of Animation movies with more than 70% Audience Score. (Hint: use the count() function)
```python
df_ani = df[df['Genre'] == 'Animation']
df_ani_70 = df_ani[df_ani['Audience_score_%'] > 70 ]
df_ani_70.count()[0]

## A2 - another answer
df[(df["Genre"] == "Animation") & (df["Audience_score_%"] > 70)]

```

## Show the list of top 5 movies based on profitability.
```python
first_five = df.sort_values(by = 'Profitability', ascending = False ).head(5)
first_five_movies = first_five["Film"]
first_five_movies
```

## Show the top 5 Comedy movies approved by the audience. (hint : Audience Score)
```python
df[df["Genre"] == "Comedy"].sort_values(by=["Audience_score_%"], ascending=False).head(5)
```

## Which Genre is favored the most by the Audience ?
```python
# A1 - first answer - too complicated
# calculate the average of audience scores per genre
df_Audience_score_ave_Genre = pd.DataFrame(df.groupby('Genre')['Audience_score_%'].mean())
df_Audience_score_ave_Genre.rename(columns = {'Audience_score_%':'Audience_Score_Ave_Genre_%'}, inplace = True)
df_Audience_score_ave_Genre['Audience_Score_Ave_Genre_%'].astype('int64')
df_Audience_score_ave_Genre['Genre'] = df_Audience_score_ave_Genre.index
df_Audience_score_ave_Genre

print(df_Audience_score_ave_Genre.sort_values(by = 'Audience_Score_Ave_Genre_%', ascending = False ).head(1).index.values)
#out: ['Fantasy']

## A2 - after spike - use only necessary values
genre_studios = df.groupby('Genre')['Audience_score_%'].mean()
genre_studios.sort_values().tail(1)
#out: ['Fantasy']

```

# Top 5 movie names by Rotten Tomato Score.
```python
# show index of top 5 movies : df.sort_values(by = 'Rotten Tomatoes %', ascending = False ).head(5).index

## A1 - before spike
# append indexes of top 5 movies to a list
list_rot_5_index =  df.sort_values(by = 'Rotten_Tomatoes_%', ascending = False ).head(5).index.values
names_rotten_top5 = []

    # print names using the list of indexes
for item in list_rot_5_index:
  row = df.iloc[[item],:]['Film'].astype('string')
  names_rotten_top5.append(row)

names_rotten_top5

## A2 - after spike
df.sort_values(by = 'Rotten_Tomatoes_%', ascending = False ).head(5)['Film']

## A3 - after spike
sorted_five = df.sort_values(by = 'Rotten_Tomatoes_%', ascending = False ).head(5)
sorted_five_film = sorted_five["Film"]

```

# Top 3 high gross Romance movies produced by Disney after 2008 
```python
df_disney = df[df['Lead_Studio'] == 'Disney']
df_disney_2008 = df_disney[df_disney['Year'] > 2008]
df_disney_2008.sort_values(by='Worldwide_Gross', ascending = False ).head(3)
#there is no Romance movies produced by Disney
```

# How many Lead Studios are present in the dataframe ? (Hint: use the function value_counts() which applies to category)
```python
df.Lead_Studio.value_counts().size
#values in colum names should not have blanks
```

# Top 5 profitable movies produced by Disney after 2008 (measured by Profitability index)
```python
df_disney = df[df['Lead_Studio'] == 'Disney']
df_disney.sort_values(by='Profitability', ascending = False ).head(5)['Film']
```

# Most & Least Frequent lead studio in the dataset in terms of occurances.
```python
df.Lead_Studio.value_counts().nlargest(1)
df.Lead_Studio.value_counts().nsmallest(2)
```

# Most and Least profitable Lead Studio. (Take an average of all Profitability measures grouped by Lead studios)
```python
# A1 - before spike
# calculate average of Profitability per Lead studio
df_Profitability_ave_Studio = pd.DataFrame(df.groupby('Lead_Studio')['Profitability'].mean())
df_Profitability_ave_Studio.rename(columns = {'Profitability':'Profitability_Studio'}, inplace = True)
df_Profitability_ave_Studio['Profitability_Studio'].astype('int64')
df_Profitability_ave_Studio['Lead_Studio'] = df_Profitability_ave_Studio.index
df_Profitability_ave_Studio

#most profitable lead studio
print(df_Profitability_ave_Studio.sort_values(by='Profitability_Studio', ascending = False ).head(1).index.values)
# Summit

#least profitable lead studio
print(df_Profitability_ave_Studio.sort_values(by='Profitability_Studio', ascending = False ).tail(1).index.values)
# The Weinstein Company'

## A2 - after spike - use only necessary values
prof_studios = df.groupby('Lead_Studio')['Profitability'].mean()
prof_studios.sort_values().head(1)
prof_studios.sort_values().tail(1)
```

# Top 5 lead studios with audience score greater than 70%.
```python
# A1 - before spike
# calculate average of audience score per Lead studio
df_AudienceScore_ave_Studio = pd.DataFrame(df.groupby('Lead_Studio')['Audience_score_%'].mean())
df_AudienceScore_ave_Studio.rename(columns = {'Audience_score_%':'Audience_Score_Ave_Studio_%'}, inplace = True)
df_AudienceScore_ave_Studio['Audience_Score_Ave_Studio_%'].astype('int64')
df_AudienceScore_ave_Studio['Lead_Studio'] = df_AudienceScore_ave_Studio.index
df_AudienceScore_ave_Studio

df_AudienceScore_ave_Studio.sort_values(by='Audience_Score_Ave_Studio_%', ascending = False )
df_AudienceScore_Studio_top = df_AudienceScore_ave_Studio[df_AudienceScore_ave_Studio['Audience_Score_Ave_Studio_%']>70]
df_AudienceScore_Studio_top
#there are only two studios with averaged audience score greater than 70%: Disney, Summit

# A2 - after spike
aud_score_studios = df.groupby('Lead_Studio')['Audience_score_%'].mean()
aud_score_studios.sort_values()

```

# Count of least Frequent Genre with Rotten Tomato score more than 50%.
```python
# calculate average of rotten tomato score per genre
df_RottenTScore_ave_Genre = pd.DataFrame(df.groupby('Genre')['Rotten_Tomatoes_%'].mean())
df_RottenTScore_ave_Genre.rename(columns = {'Rotten_Tomatoes_%':'RottenTScore_ave_Genre_%'}, inplace = True)
df_RottenTScore_ave_Genre['RottenTScore_ave_Genre_%'].astype('int64')
df_RottenTScore_ave_Genre['Genre'] = df_RottenTScore_ave_Genre.index
df_RottenTScore_ave_Genre

# filter data (score over 50)
df_RottenTScore_ave_Genre_over50 = df_RottenTScore_ave_Genre[df_RottenTScore_ave_Genre['RottenTScore_ave_Genre_%']>50]
#Drama, Fantasy, Animation: genres with Rotten Tomato score more than 50%

# print the count of genres (with the name of Genre)
dic_genre_counts = df['Genre'].value_counts().to_dict()
[[str(item) + str(dic_genre_counts[item])] for item in df_RottenTScore_ave_Genre_over50['Genre']]

```

# Ranking of Fox studio for Comedy movies based on Audience Score.
```python
## A1 - calculating average and re-order
df_comedy = df[df['Genre'] == 'Comedy']
df_comedy.sort_values(by='Lead_Studio', ascending = False)

df_audscore_comedy_per_studio = pd.DataFrame(df_comedy.groupby('Lead_Studio')['Audience_score_%'].mean())
df_audscore_comedy_per_studio.rename(columns = {'Audience_score_%':'Audience_Score_comedy_Ave_Studio_%'}, inplace = True)
df_audscore_comedy_per_studio['Audience_Score_comedy_Ave_Studio_%'].astype('int64')
df_audscore_comedy_per_studio['Lead_Studio'] = df_audscore_comedy_per_studio.index

df_res = df_comedy.join(df_audscore_comedy_per_studio.set_index('Lead_Studio'), on = 'Lead_Studio')
df_res.sort_values(by='Audience_Score_comedy_Ave_Studio_%', ascending = False)

# Ranking of Fox: 1st (highest average of audience score, within Comedy genre, among all Lead studio)
# how to concatenate two df using one overlapping column as an index : df_new = df1.join(df2.set_index('Lead_Studio'), on='Lead_Studio')

## A2 - apply .rank (could not solve using rank function)
df.sort_values(by=['Lead_Studio'], ascending = False)

df.groupby('Lead_Studio')['Audience_score_%'].rank(pct=True).sort_values(by='Film', ascending = False )  #not working?

df_comedy = df[df['Genre'] == 'Comedy']
df_comedy.sort_values(by='Lead_Studio_Rank_AudScore', ascending = False ) 

## A3 - within fox studio, rank of comedy movies based on audience score
default_rank = df[(df["Lead_Studio"] == "Fox") & (df["Genre"] == "Comedy")]["Audience_score_%"].rank(ascending = False)
df["defaul_rank"] = default_rank

sort_values(by='Film', ascending = False )

```

# Count of each genre of movies produced by Independent. (use groupby() )
```python
df_Ind = df[df['Lead_Studio'] == 'Independent']
df_Ind.groupby('Genre').count()
# another way: df_Ind.set_index(["Genre", "Film"]).count(level="Genre")


```