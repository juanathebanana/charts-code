#If you want to see how the items are varying based on a single metric and
#visualize the order and amount of this variance, the diverging bars is a great tool.
#It helps to quickly differentiate the performance of groups in your data and is quite intuitive and instantly conveys the point.

plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)

# decorate
plt.yticks(df.index, df.cars, fontsize=8)
plt.grid(linestyle='--', alpha=0.5)
plt.gca().set(xlabel='Mileage',
              ylabel='Model',
              title='Diverging Bars')
plt.show()


#https://www.geeksforgeeks.org/diverging-bar-chart-using-python/
