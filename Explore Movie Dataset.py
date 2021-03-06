#!/usr/bin/env python
# coding: utf-8

# ## 探索电影数据集
# 
# 在这个项目中，你将尝试使用所学的知识，使用 `NumPy`、`Pandas`、`matplotlib`、`seaborn` 库中的函数，来对电影数据集进行探索。
# 
# 下载数据集：
# [TMDb电影数据](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/explore+dataset/tmdb-movies.csv)
# 

# 
# 数据集各列名称的含义：
# <table>
# <thead><tr><th>列名称</th><th>id</th><th>imdb_id</th><th>popularity</th><th>budget</th><th>revenue</th><th>original_title</th><th>cast</th><th>homepage</th><th>director</th><th>tagline</th><th>keywords</th><th>overview</th><th>runtime</th><th>genres</th><th>production_companies</th><th>release_date</th><th>vote_count</th><th>vote_average</th><th>release_year</th><th>budget_adj</th><th>revenue_adj</th></tr></thead><tbody>
#  <tr><td>含义</td><td>编号</td><td>IMDB 编号</td><td>知名度</td><td>预算</td><td>票房</td><td>名称</td><td>主演</td><td>网站</td><td>导演</td><td>宣传词</td><td>关键词</td><td>简介</td><td>时常</td><td>类别</td><td>发行公司</td><td>发行日期</td><td>投票总数</td><td>投票均值</td><td>发行年份</td><td>预算（调整后）</td><td>票房（调整后）</td></tr>
# </tbody></table>
# 

# **请注意，你需要提交该报告导出的 `.html`、`.ipynb` 以及 `.py` 文件。**

# 
# 
# ---
# 
# ---
# 
# ## 第一节 数据的导入与处理
# 
# 在这一部分，你需要编写代码，使用 Pandas 读取数据，并进行预处理。

# 
# **任务1.1：** 导入库以及数据
# 
# 1. 载入需要的库 `NumPy`、`Pandas`、`matplotlib`、`seaborn`。
# 2. 利用 `Pandas` 库，读取 `tmdb-movies.csv` 中的数据，保存为 `movie_data`。
# 
# 提示：记得使用 notebook 中的魔法指令 `%matplotlib inline`，否则会导致你接下来无法打印出图像。

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')
movie_data = pd.read_csv('./tmdb-movies.csv')
movie_data


# ---
# 
# **任务1.2: ** 了解数据
# 
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
# 
# 1. 获取数据表的行列，并打印。
# 2. 使用 `.head()`、`.tail()`、`.sample()` 方法，观察、了解数据表的情况。
# 3. 使用 `.dtypes` 属性，来查看各列数据的数据类型。
# 4. 使用 `isnull()` 配合 `.any()` 等方法，来查看各列是否存在空值。
# 5. 使用 `.describe()` 方法，看看数据表中数值型的数据是怎么分布的。
# 
# 

# In[2]:


print('rows: {}, columns: {}'.format(*movie_data.shape))

# movie_data.head(5)
# movie_data.tail(5)
# movie_data.sample(5)

for col in movie_data.keys():
    sr = movie_data[col]
    print('{} - {} - {}'.format(col, sr.dtypes, sr.isnull().any()))

movie_data.describe()


# ---
# 
# **任务1.3: ** 清理数据
# 
# 在真实的工作场景中，数据处理往往是最为费时费力的环节。但是幸运的是，我们提供给大家的 tmdb 数据集非常的「干净」，不需要大家做特别多的数据清洗以及处理工作。在这一步中，你的核心的工作主要是对数据表中的空值进行处理。你可以使用 `.fillna()` 来填补空值，当然也可以使用 `.dropna()` 来丢弃数据表中包含空值的某些行或者列。
# 
# 任务：使用适当的方法来清理空值，并将得到的数据保存。

# In[3]:


# print(movie_data.dropna(axis=0, inplace=True))
movie_data.fillna(0, inplace=True)
print(movie_data.shape)
movie_data.isnull().any()


# ---
# 
# ---
# 
# ## 第二节 根据指定要求读取数据
# 
# 
# 相比 Excel 等数据分析软件，Pandas 的一大特长在于，能够轻松地基于复杂的逻辑选择合适的数据。因此，如何根据指定的要求，从数据表当获取适当的数据，是使用 Pandas 中非常重要的技能，也是本节重点考察大家的内容。
# 
# 

# ---
# 
# **任务2.1: ** 简单读取
# 
# 1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
# 2. 读取数据表中前1～20行以及48、49行的数据。
# 3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
# 
# 要求：每一个语句只能用一行代码实现。

# In[4]:


# movie_data[['id', 'popularity', 'budget', 'runtime', 'vote_average']]
# movie_data.loc[0:19].append(movie_data.loc[48:49])
movie_data_part_cols = movie_data[['id', 'popularity', 'budget', 'runtime', 'vote_average']]
movie_data_part_cols.loc[0:19].append(movie_data_part_cols.loc[47:48])
movie_data.loc[49:59][['popularity']]


# ---
# 
# **任务2.2: **逻辑读取（Logical Indexing）
# 
# 1. 读取数据表中 **`popularity` 大于5** 的所有数据。
# 2. 读取数据表中 **`popularity` 大于5** 的所有数据且**发行年份在1996年之后**的所有数据。
# 
# 提示：Pandas 中的逻辑运算符如 `&`、`|`，分别代表`且`以及`或`。
# 
# 要求：请使用 Logical Indexing实现。

# In[5]:


movie_data[movie_data['popularity'] > 5]
movie_data[(movie_data['popularity'] > 5) & (movie_data['release_year'] > 1996)]


# ---
# 
# **任务2.3: **分组读取
# 
# 1. 对 `release_year` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `revenue` 的均值。
# 2. 对 `director` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `popularity` 的均值，从高到低排列。
# 
# 要求：使用 `Groupby` 命令实现。

# In[6]:


movie_data.groupby(['release_year']).revenue.agg('mean')
movie_data.groupby(['director']).agg({'popularity': 'mean'}).sort_values(by="popularity", ascending=False)


# ---
# 
# ---
# 
# ## 第三节 绘图与可视化
# 
# 接着你要尝试对你的数据进行图像的绘制以及可视化。这一节最重要的是，你能够选择合适的图像，对特定的可视化目标进行可视化。所谓可视化的目标，是你希望从可视化的过程中，观察到怎样的信息以及变化。例如，观察票房随着时间的变化、哪个导演最受欢迎等。
# 
# <table>
# <thead><tr><th>可视化的目标</th><th>可以使用的图像</th></tr></thead><tbody>
#  <tr><td>表示某一属性数据的分布</td><td>饼图、直方图、散点图</td></tr>
#  <tr><td>表示某一属性数据随着某一个变量变化</td><td>条形图、折线图、热力图</td></tr>
#  <tr><td>比较多个属性的数据之间的关系</td><td>散点图、小提琴图、堆积条形图、堆积折线图</td></tr>
# </tbody></table>
# 
# 在这个部分，你需要根据题目中问题，选择适当的可视化图像进行绘制，并进行相应的分析。对于选做题，他们具有一定的难度，你可以尝试挑战一下～

# **任务3.1：**对 `popularity` 最高的20名电影绘制其 `popularity` 值。

# In[7]:


# movie_data[['id', 'popularity']].head(100)
sorted_movie_data = movie_data.sort_values('popularity', ascending=False).head(20)
sorted_movie_data
# max_popularity = sorted_movie_data['popularity'].max()
# bins_edge = np.arange(0, max_popularity + 1, 1)
# sb.distplot(sorted_movie_data['popularity'])
# plt.bar(sorted_movie_data['original_title'], sorted_movie_data['popularity'])
plt.barh(sorted_movie_data['original_title'], sorted_movie_data['popularity'])
plt.xlabel('popularity')
plt.ylabel('original_title')
plt.title('popularity top 20')


# ---
# **任务3.2：**分析电影净利润（票房-成本）随着年份变化的情况，并简单进行分析。

# In[24]:


# profit_by_year = movie_data.groupby(['release_year']).agg({'budget': 'sum', 'revenue': 'sum'}).sort_values('release_year')

# plt.plot(year_sorted_movie_data['release_year'], year_sorted_movie_data['revenue']  - year_sorted_movie_data['budget'])
# print(profit_by_year.head(1))
# print(profit_by_year.tail(1))
# plt.plot(profit_by_year[['budget', 'revenue']])

# plt.errorbar(profit_by_year.index, profit_by_year['budget'])
# plt.errorbar(profit_by_year.index, profit_by_year['revenue'], yerr=profit_by_year['revenue']-profit_by_year['budget'], fmt='-o')

# plt.plot(profit_by_year['revenue']-profit_by_year['budget'])

movie_data['profits'] = movie_data['revenue_adj'] - movie_data['budget_adj']
profits_by_year = movie_data.groupby('release_year')['profits'].mean()

plt.subplot(1, 2, 1)
plt.errorbar(x=profits_by_year.index, y=movie_data.groupby('release_year')['budget_adj'].sum())
plt.errorbar(x=profits_by_year.index, y=movie_data.groupby('release_year')['revenue_adj'].sum())
plt.xlabel('release_year')
plt.ylabel('sum of budget & revenue')

plt.subplot(1, 2, 2)
plt.errorbar(x=profits_by_year.index, y=profits_by_year)
plt.xlabel('release_year')
plt.ylabel('mean of profits')


# ---
# 
# **[选做]任务3.3：**选择最多产的10位导演（电影数量最多的），绘制他们排行前3的三部电影的票房情况，并简要进行分析。

# In[25]:


# directors = movie_data[movie_data['director'] != 0].groupby(['director']).agg({'original_title': 'count'}).sort_values('original_title', ascending=False).index[0:10]

# for director in directors:
    #print(movie_data[movie_data['director'] == director].sort_values('revenue', ascending=False)[0:3][['director', 'original_title', 'revenue']])

director_data = movie_data[['director', 'original_title', 'revenue']]
# Get Most Prolific Directors 
top10_directors = director_data.groupby('director').count()['original_title'].nlargest(10).index
top10_table = director_data[director_data['director'].isin(top10_directors)]
# Rearrange Table for Plotting
top10_table = top10_table.sort_values(['director','revenue'], ascending=[False,False])   .set_index(['director','original_title']) 
# Plot Highest Revenues
top10_table.groupby(level=0).head(3).unstack()   .plot(kind='bar',stacked=True, legend=False, rot=30, figsize=(10,5))
plt.ylabel('revenue')
plt.title("Top 10 prolific directors with 3 movies of highest revenues")
    


# ---
# 
# **[选做]任务3.4：**分析1968年~2015年六月电影的数量的变化。

# In[27]:


films_by_year = movie_data[(movie_data['release_year'] > 1967) & (movie_data['release_year'] < 2016)]
plt.plot(films_by_year.groupby('release_year').agg({'original_title': 'count'}).sort_values('release_year'))


# ---
# 
# **[选做]任务3.5：**分析1968年~2015年六月电影 `Comedy` 和 `Drama` 两类电影的数量的变化。

# In[36]:


c_d_films = films_by_year[(films_by_year['genres'].str.contains('Comedy')) | (films_by_year['genres'].str.contains('Drama'))]

# c_d_films.groupby(['release_year', 'genres']).agg({'original_title': 'count'}).sort_values('release_year')
c_d_films.groupby(['release_year', 'genres']).count()['original_title']


# > 注意: 当你写完了所有的代码，并且回答了所有的问题。你就可以把你的 iPython Notebook 导出成 HTML 文件。你可以在菜单栏，这样导出**File -> Download as -> HTML (.html)、Python (.py)** 把导出的 HTML、python文件 和这个 iPython notebook 一起提交给审阅者。
