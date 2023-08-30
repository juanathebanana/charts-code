#Ridgeline plots (Joy plots) allow the density curves of different groups to overlap: they are a great way to visualize the
#distribution of a large number of groups
#in relation to each other. It looks pleasing to the eye and conveys just 
#the right information clearly. It can be easily built using the joypy package which is based on matplotlib and pandas.

fig, axes = joypy.joyplot(mpg, column=['hwy', 'cty'], by="class", 
                          ylim='own', 
                          figsize=(8, 6))

# Decoration
plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=20)
plt.show()

#https://www.analyticsvidhya.com/blog/2021/06/ridgeline-plots-visualize-data-with-a-joy/
