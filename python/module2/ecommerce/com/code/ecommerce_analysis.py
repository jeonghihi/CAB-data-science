# %% packages
# ========== packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
# %% 
# load dataset
filepath = './output/product_summary.csv'
df = pd.read_csv(filepath, sep=",", engine="python")
print(df.columns)
df.head()

# %%
# check and transform data types in the dataset

# df.review_count.astype('int64').dtypes

df['product_type'] = pd.Categorical(df['product_type'], categories=
      ['Keyboard', 'Laptop', 'Mouse', 'Processor', 'dslr camera', 'headphones', 'monitor', 'smartphone'],
      ordered=True)
# bucket wine quality scores into qualitative quality labels
df['rating_label'] = df['rating'].apply(lambda value: 'low'
if value <= 2 else 'medium'
if value <= 4 else 'high')

df['rating_label'] = pd.Categorical(df['rating_label'],
categories=['low', 'medium', 'high'])
df['rating_label'].dtype

df['sponsored_type'] = df['sponsored'].apply(lambda value: 'yes'
if value == 1 else 'No')

df['sponsored_type'] = pd.Categorical(df['sponsored_type'],
categories=['yes', 'no'])


# %% basic statistics1: prices
data = df.groupby(['product_type'])[['price']].mean()

# plot
f, ax = plt.subplots(figsize=(8, 5))

#fig = plt.gcf()
#figsize=(8,5)
g = sns.barplot(x='price', y=data.index, data=data) #bar or box

# label & title
plt.xlabel("Mean price ($)", size=14)
plt.ylabel("Product types", size=14)
_, xlabels = plt.xticks()
_, ylabels = plt.yticks()

g.set_xticklabels(xlabels, size=14)
g.set_yticklabels(ylabels, size=12)

for i in range(0,8):
    g.text(data['price'][i]+.5, i, str(round(data['price'][i],2)), fontsize = 12)
    
plt.title("The mean prices of products in 8 elctronic categories", size=18,  fontweight = 'bold')

# Add a legend and informative axis label
ax.legend(ncol=2, loc="upper right", frameon=True)
plt.show()

plt.savefig("./output/fig/mean_price_per_category.png", format='png',dpi=300)


# %% 
# distribution of product items in 8 categories 
df.product_type.value_counts().plot(kind = 'bar')

s = sns.scatterplot(x=list(set(df.product_type.values)), y=df.rating.value_counts(), data=df)
# work ----------- https://izziswift.com/scatter-plots-in-pandas-pyplot-how-to-plot-by-category/


# %% detail statistics: proportion of ratings_label (low,med,high) in each 8 categories

# distribution of prices 
df_stat_price_per_category = df.groupby(['product_type'])[['price']].describe()
df_stat_rating_per_category = df.groupby(['product_type'])[['rating']]
df_stat_review_per_category = df.groupby(['product_type'])[['review_count']].describe()

#pie(total.iloc[[0]], startangle=90, colors=colors, wedgeprops={'edgecolor': 'black'}, autopct='%1.f%%', explode=explode, shadow=True)


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 8), constrained_layout = True)

#fig.tight_layout(h_pad=60)
pie_labels = list(df_stat_price_per_category.index)

theme = plt.get_cmap('bwr')

# color: https://stackoverflow.com/questions/16006572/plotting-different-colors-in-matplotlib

pie_price = df.groupby("product_type")["price"].sum()
ax[0].pie(pie_price, autopct='%1.1f%%', shadow=True,radius=2.0, textprops={'fontsize': 14}, startangle=90, colors = cs)
#define subplot titles
ax[0].set_title('distribution of price', size = 16, pad=60, fontweight='bold') # plt.subplots_adjust(top=0.8) 

pie_rating = df.groupby("product_type")["rating"].sum()
ax[1].pie(pie_rating, autopct='%1.1f%%', shadow=True,radius=2.0, textprops={'fontsize': 14}, startangle=90, colors = cs)
#define subplot titles
ax[1].set_title('distribution of rating', size = 16, pad=60, fontweight='bold')

pie_review = df.groupby("product_type")["review_count"].sum()
ax[2].pie(pie_review, autopct='%1.1f%%', shadow=True,radius=2.0, textprops={'fontsize': 14}, startangle=90, colors = cs)
#define subplot titles
ax[2].set_title('distribution of review counts', size = 16, pad=60, fontweight='bold')

fig.legend(loc="lower center", ncol=4, labels=pie_labels, fontsize='medium') #manual legend loc: bbox_to_anchor=(0.5, 0., 0.5, 0.5), 

plt.show()

# %% basic statistics1: rating & review counts
# how many reviews x each rating value  

# %% figures


# distribution of prices in 8 categories 
plt.figure(figsize=(8,5))
data = df.groupby(['product_type'])[['price']].count()
sns.boxplot(x=data.values, y=data, data = data, palette = 'rainbow')
# https://stackoverflow.com/questions/59826098/seaborn-plot-pandas-dataframe-by-multiple-groupby

#sns.boxplot(x='product_type', y='price', data = df, palette = 'rainbow')
plt.title( 'The distribution of price in 8 categories ' )

plt.suptitle('')
plt.show()


# %% distribution of ratings in 8 categories
fig, ax = plt.subplots(2,4, figsize=(12, 6))
ax[0,0].hist( df[df['product_type'] == 'Keyboard']['rating'], 30)
ax[0,1].hist( df[df['product_type'] == 'Laptop']['rating'], 30)
ax[0,2].hist( df[df['product_type'] == 'Mouse']['rating'], 30)
ax[0,3].hist( df[df['product_type'] == 'Processor']['rating'], 30)
ax[1,0].hist( df[df['product_type'] == 'dslr camera']['rating'], 30)
ax[1,1].hist( df[df['product_type'] == 'headphones']['rating'], 30)
ax[1,2].hist( df[df['product_type'] == 'monitor']['rating'], 30)
ax[1,3].hist( df[df['product_type'] == 'smartphone']['rating'], 30)

# stacked hist: https://towardsdatascience.com/customer-reviews-identify-your-strengths-and-weaknesses-with-the-help-of-web-scraping-data-b87a3636ef55


# distribution of ratings for products in 8 categories - stacked barplots
# x = product_type
# y = count()
# color = rating
sns.barplot(x = df.product_type, y = df.rating_label.value_counts().values,
            order = ['medium', 'high','low'])