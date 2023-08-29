dfi.plot(kind='bar',
          color='darkslategray',
          figsize=(10, 6))

plt.xlabel('Year')
plt.ylabel('# of immigrants')
plt.title('Icelandic immigrants to Canada, 1980-2013', size=18)
plt.ylim(0, 90)

plt.annotate('',
            xy=(32, 75),
            xytext=(28, 75),
            xycoords='data',
            arrowprops=dict(arrowstyle='<->', color='firebrick', lw=2))

plt.text(30, 78, "Financial crisis", horizontalalignment="center")

plt.show()

#With pandas' plot() syntax, we'll use kind='bar' or kind='barh' for vertical and horizontal bar charts, respectively.
#https://www.analyticsvidhya.com/blog/2021/08/understanding-bar-plots-in-python-beginners-guide-to-data-visualization/
