import pandas as pd
#columns and index are not Python lists, but it is easy to convert them to lists! for this we can use this code
#df is the dataframe took in consideration
df.columns.tolist()
#To view the dimensions of the dataframe, we use the shape instance variable.
df.shape
#delete columns that we don't need
df.drop(['col1','col2','col3','Type','Coverage'], axis=1, inplace=True)

#rename columns
rename_dict = {'OdName':'Country', # old: new
               'AreaName':'Continent',
               'RegName':'Region'}

df.rename(columns=rename_dict, inplace=True)


#how to create a new column with computations
col_list = [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]#here we select columns that have numbers 
df['Sum'] = df[col_list].sum(axis=1)#here there is the sum

#Quick check to see how many null elements are in the dataset, by column:
df.isnull().sum()

"""
Row selection

There are two alternative ways to select rows:

    by label, df.loc[label]
    by position, df.iloc[index]
"""

#useful for computations
df.set_index('column_we_want as_index', inplace=True)

#tranpose
df.transpose()

#sorting
df.sort_values(by='total', ascending=False, axis=0, inplace=True)#



##BASIC PLOT
df.plot(kind='line', color="darkred") # kind="line" by default

plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")



#We can annotate  using plt.text or plt.annotate

plt.annotate('texe', xy=(2010, 6000), xytext=(2000, 5000),
             arrowprops=dict(color='black', shrink=0.01, width=0.1), 
             fontsize=11, color='black', horizontalalignment='center')
plt.show()
