corr = cars.corr(method='pearson', numeric_only=True)#change car

fig, ax = plt.subplots(figsize=(8, 6))

# step 0: create heatmap
im = ax.imshow(corr, cmap='RdYlGn')
fig.colorbar(im, orientation='vertical', fraction=0.05)

# # step 1: set labels
ax.set_xticks(np.arange(len(corr)), labels=corr.columns)
ax.set_yticks(np.arange(len(corr)), labels=corr.columns)
ax.set_xticklabels(ax.get_xticklabels(), rotation=65, ha='right', fontsize=15)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=15)

# step 2: add text annotations
from itertools import product
seq = range(len(corr))
for i, j in product(seq, seq): # itertools' product avoids writing a nested for loop
    text = ax.text(i, j, f"{corr.iloc[i, j]:.2f}",
                   ha="center", va="center",
                   size="small")

plt.tight_layout()
plt.show()

#With seaborn, it is much easier to create a heatmap with annotations:
plt.figure(figsize=(8, 6))

sns.heatmap(corr, annot=True)
plt.tight_layout()
plt.show()

#better 
fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(corr, annot=True, ax=ax,
            vmin=-1,
            vmax=1,
            cmap='RdYlGn', # sns.diverging_palette(20, 220, n=200), # 'RdYlGn'
            square=True)


# optional:
ax.set_xticklabels(ax.get_xticklabels(), rotation=65, ha='right', fontsize=15)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, va='center', fontsize=15)

plt.tight_layout()
plt.show()


#If you are interested in plotting a diagonal correlogram, you can leverage
#the argument mask of sns.heatmap(), which accepts a boolean array
#specifiyng which cells should be hidden from the visualization. For example, you may want to hide the upper triangular portion of corr:
# create a mask for the upper triangular portion of corr
mask = np.triu(np.ones_like(corr, dtype=bool))


fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(corr, annot=True, ax=ax,
            vmin=-1,
            vmax=1,
            cmap='RdYlGn',
            mask=mask,
            square=True)


# optional:
ax.set_xticklabels(ax.get_xticklabels(), rotation=65, ha='right', fontsize=15)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, va='center', fontsize=15)

plt.tight_layout()
plt.show()

#https://seaborn.pydata.org/generated/seaborn.heatmap.html
