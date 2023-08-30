n_categories = df.shape[0]
# create labels as "class name (class count)"
labels = df.apply(lambda x: f'{x[0]} ({x[1]})', axis=1)
sizes = df['counts'].tolist()
# create n_categories unique colors
colors = [plt.cm.Spectral(i/(n_categories-1)) for i in range(n_categories)]

# draw plot
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# decorate
plt.title("Treemap of Vehicle Class")
plt.axis("off")
plt.show()

#https://www.geeksforgeeks.org/treemaps-in-python-using-squarify/
