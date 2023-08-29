df.loc[['Italy', 'Germany'], years].transpose()
df_ig.plot(kind='box')

plt.title("title")
plt.ylabel("ylbael")

plt.show()


#https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/


##sns

g = sns.boxplot(data=tips, x="day", y="tip_pct")
g.set(xlabel="Day", ylabel="Tip %");

g = sns.boxplot(data=tips, x="day", y="tip_pct",
               hue="sex",
               palette=['m', 'g'])
g.set(xlabel="Day", ylabel="Tip %");
#https://seaborn.pydata.org/generated/seaborn.boxplot.html
#The function catplot() can also be used to generate categorical estimate plots such as bar or count plots (kind="count").
sns.catplot(data=tips, kind="box", x="day", y="tip_pct", hue="sex");

sns.catplot(data=tips, kind="violin", x="day", y="tip_pct", hue="sex", inner="quartile");

sns.catplot(
    x="alive",
    col="deck",
    col_wrap=4,
    data=titanic[titanic.deck.notnull()],
    kind="count",
    height=2.5,
    aspect=0.8,
    palette="tab20",
)

plt.show()
#https://seaborn.pydata.org/generated/seaborn.catplot.html
