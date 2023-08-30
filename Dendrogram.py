#A Dendrogram groups similar points together based on a given distance metric and organizes them in tree like links based on the point’s similarity.
hc = shc.linkage(df[['Murder', 'Assault', 'UrbanPop', 'Rape']], method='ward')

# plot dendrogram
plt.figure(figsize=(8, 6))
dend = shc.dendrogram(hc,
                      labels=df.State.values,
                      color_threshold=100)
plt.title("USArrests Dendograms")
# plt.xticks(fontsize=10)
plt.show()

#https://plotly.com/python/dendrogram/
