#The Andrews plot (or Andrews curve) helps visualize if there are inherent groupings of the numerical features based on a given stratifying variable. Andrews curves are a projection of multivariate data
#into a 2D space: each observation is represented by a curve. If two curves are close to each other, then the corresponding observations are also close.

andrews_curves(df, 'cyl', colormap='Set1')

# decorations
plt.title('Andrews Curves of mtcars')
plt.xlim(-3, 3)
plt.grid(alpha=0.3)
plt.show()
#https://www.geeksforgeeks.org/how-to-plot-andrews-curves-using-pandas-in-python/
