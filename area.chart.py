"""
 area chart (also called stacked line plot), simply using `kind='area'` within pandas `plot()`. in pandas basic we use line
"""

df.plot(kind="area", stacked=False, # by default area charts are stacked
            alpha=0.25, # by default alpha=0.5
            figsize=(15, 8)) # increasing the figsize is another workaround for improving the legend location

plt.title("title", size=20)
plt.xlabel("x label" name)
plt.ylabel("# y label ")
plt.show()

"""
another way to do it 
"""

ax = df.plot(kind="area", stacked=False,
                 alpha=0.25,
                 figsize=(15, 8))

ax.set_title("title", size=20)
ax.set_xlabel("x lanel name")
ax.set_ylabel("y label name")
plt.show()

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.area.html
