#Task: Visualize the frequency 


#example in which we have to transpose the data. He have to select the number of bins(interval)
df.loc[countries, years].transpose().plot.hist(figsize=(10, 6),
                                              bins=15,
                                              alpha=0.7,
                                              # stacked=True,
                                              color=['darksalmon', 'darkblue', 'limegreen'])

plt.title("Immigration 1980-2013")
plt.xlabel("# of immigrants")
plt.ylabel("# of years")
plt.show()

#https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/


"""
another example using for
"""
energy_sources = [
    'Traditional biofuels (terrawatt-hours)', 
    'Wind (Terawatt-hours)', 
    'Solar PV (Terawatt-hours)', 
    'Hydropower (TWh)'
]

for source in energy_sources:
    plt.figure(figsize=(8, 6))
    plt.hist(df[source], bins=10, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'Histogram of {source}')
    plt.xlabel('Energy in TWh')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
