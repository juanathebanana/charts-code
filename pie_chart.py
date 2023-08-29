df['Total'].plot(kind='pie',
                            autopct='%1.1f%%', # add and format percentages
                            startangle=90,
                            labels=None, # turn off text labels
                            pctdistance=1.1, # move percentages outside
                            figsize=(15, 6)
                           )

plt.axis('equal') # force equal axes so the pie chart looks like a circle
plt.legend(labels=df_continents.index, loc='upper left')
plt.show()

#https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
