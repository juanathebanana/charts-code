sns.jointplot(x="x", y="y", data=df)
#Assigning a `hue` variable will add conditional colors to the plots and an automatic legend:
iris = sns.load_dataset("iris")

sns.jointplot(data=iris, x="petal_length", y="petal_width",
              hue="species")


#https://seaborn.pydata.org/generated/seaborn.jointplot.html
