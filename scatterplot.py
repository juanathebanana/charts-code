df.plot(kind='scatter', x='year', y='total')


#https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html
#https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/

#sns
sns.scatterplot(tips, x="total_bill", y="tip")
#Seaborn supports statistical estimation, for example of linear regression lines:
sns.lmplot(tips, x="total_bill", y="tip");
#Stratification by a third variable is supported by the argument `hue`:
sns.scatterplot(tips, x="total_bill", y="tip", hue="time");
sns.lmplot(tips, x="total_bill", y="tip", hue="time", col="smoker");
#https://seaborn.pydata.org/generated/seaborn.scatterplot.html
