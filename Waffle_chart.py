from pywaffle import Waffle
#Waffle charts show the compositions of groups in a larger population. Here we directly use the `pywaffle` package.

# data
df_raw = mpg.copy()

# compute the number of elements belonging to each "class"
df = df_raw.groupby("class").size().reset_index(name="counts")
# get the class labels
labels = df['class'].tolist()

fig = plt.figure(FigureClass=Waffle,
                 rows=10,
                 columns=10,
                 values=df.counts,
                 labels=labels,
                 legend={'bbox_to_anchor': (1, 1)},
                 title={"label": "# Vehicles by Class", 
                        "loc": "center", 
                        "fontsize": 18},
                 figsize=(6, 6),
                )

#pywaffle allows you to add multiple 
#waffle charts as subplots to the same figure.
#In this case, you need to merge the parameters for each plot as 
#dict values and pass them to the argument plots. The keys of this dict are integers describing 
#the position of the subplot, in the format 312, standing for nrow, ncol, index.



# Prepare distinct data frames to hold data for the different waffles
# By Class
df1 = df_raw.groupby('class').size().reset_index(name='counts')

# By Cylinders
df2 = df_raw.groupby('cyl').size().reset_index(name='counts')

# Draw Plot and Decorate
fig = plt.figure(
    FigureClass=Waffle,
    plots={
        211: {
            'values': df1.counts,
            'labels': df1['class'].tolist(),
            'legend': {'bbox_to_anchor': (1, 1), 'fontsize': 12, 'title':'Class'},
            'title': {'label': '# Vehicles by Class', 'loc': 'center', 'fontsize':18},
        },
        212: {
            'values': df2.counts,
            'labels': df2['cyl'].tolist(),
            'legend': {'bbox_to_anchor': (1, 1), 'fontsize': 12, 'title':'Cyl'},
            'title': {'label': '# Vehicles by Cyl', 'loc': 'center', 'fontsize':18},
        },
    },
    rows=10,
    columns=10,
    # cmap_name="Accent",
    figsize=(10, 10)
)
#https://python-charts.com/part-whole/waffle-chart-matplotlib/
