# Function to draw line segment
def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mpl.lines.Line2D([p1[0], p2[0]], [p1[1], p2[1]], color=color)
    ax.add_line(l)
    return l

fig, ax = plt.subplots(1, 1, figsize=(10, 10), facecolor='#f7f7f7') # facecolor = figure background color

# points
ax.scatter(x=df['pct_2013'], y=df['index'], s=50, color='#0e668b', alpha=0.7) # darker blue
ax.scatter(x=df['pct_2014'], y=df['index'], s=50, color='#a3c4dc', alpha=0.7) # lighter blue

# line Segments
for i, p1, p2 in zip(df['index'], df['pct_2013'], df['pct_2014']):
    newline([p1, i], [p2, i], 'skyblue')

# vertical lines
styles = dict(color='black', alpha=1, linewidth=1, linestyles='dotted')
for xx in np.linspace(0.05, 0.20, num=4, endpoint=True):
    ax.vlines(x=xx, ymin=0, ymax=26, **styles)

# decorations
ax.set_facecolor('#f7f7f7') # facecolor = axes background color
ax.set_title("Pct Change - 2013 vs 2014", fontsize=22)
ax.set(xlim=(0, .25), ylim=(-1, 27), ylabel='')
ax.set_xticks([.05, .1, .15, .20])
ax.set_xticklabels(['5%', '10%', '15%', '20%'])
ax.set_yticks(df['index'])
ax.set_yticklabels(df.Area)
plt.show()
#https://plotly.com/python/dumbbell-plots/
