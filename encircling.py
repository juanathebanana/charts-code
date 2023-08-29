from matplotlib import patches
from scipy.spatial import ConvexHull

fig = plt.figure(figsize=(10, 8))
sns.scatterplot(x='area', y='poptotal', data=midwest, hue='state')

plt.xlim(0, 0.1)
plt.ylim(0, 5e5)


def encircle(x, y, ax=None, **kw):
    if not ax:
        ax = plt.gca()
    p = np.c_[x, y] # similar to R's cbind()
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)

# Select data to be encircled
midwest_encircle_data = midwest.query('poptotal > 350000 & poptotal < 5e5 & area > 0.01 & area < 0.1')
# equivalent:
# cond = (midwest.poptotal > 350000) & (midwest.poptotal < 5e5) & (midwest.area > 0.01) & (midwest.area < 0.1)
# midwest_encircle_data = midwest.loc[cond, :]

# Draw polygon surrounding vertices    
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="k", fc="gold", alpha=0.1)

# Decorations
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Scatterplot with encircling", fontsize=20)
plt.legend(fontsize=12)    
plt.show()   

#https://stackoverflow.com/questions/44575681/how-do-i-encircle-different-data-sets-in-scatter-plot
https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html
