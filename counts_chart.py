# create a working copy of the original data
df = mpg.copy()
df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')
df_counts.head()

plt.figure(figsize=(8, 6))    
sns.stripplot(x="cty", y="hwy", data=df_counts, sizes=df_counts.counts.values*5)

plt.title('Counts Plot - Size of circle is bigger as more points overlap')
plt.show()

plt.figure(figsize=(8, 6))    
sns.stripplot(x="cty", y="hwy", data=df, jitter=0.3, alpha=0.7, size=8)

plt.title('Use jittered plots to avoid overlapping of points')
plt.show()

#https://seaborn.pydata.org/generated/seaborn.stripplot.html
