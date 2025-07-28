import pandas as pd  # Importing pandas

# Reading the dataset from your specified path
movies = pd.read_csv("C:/Users/kotha/OneDrive/Desktop/datasceince/movies.csv")

# Displaying the first five rows of the dataframe
print(movies.head())  # Using print() to ensure the output is displayed

import pandas as pd
from matplotlib import pyplot as plt

# Read your dataset
movies = pd.read_csv("C:/Users/kotha/OneDrive/Desktop/datasceince/movies.csv")

# Plot the movieId column
movies['movieId'].plot(kind='hist', bins=20, title='movieId')

# Hide the top and right spines
plt.gca().spines[['top', 'right']].set_visible(False)

# Display the plot
plt.show()  # This will display the graph in VS Code

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

# Read your dataset
movies = pd.read_csv("C:/Users/kotha/OneDrive/Desktop/datasceince/movies.csv")

def _plot_series(df, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    
    # Count occurrences of 'movieId' and sort
    counted = (df['movieId']
                .value_counts()
                .reset_index(name='counts')
                .rename({'index': 'movieId'}, axis=1)
                .sort_values('movieId', ascending=True))
    
    xs = counted['movieId']
    ys = counted['counts']
    
    # Plot the data
    plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')

# Sort the movies DataFrame by 'movieId'
df_sorted = movies.sort_values('movieId', ascending=True)

# Plot the series
_plot_series(df_sorted, 'Movie Counts')

# Despine and label
sns.despine(fig=fig, ax=ax)
plt.xlabel('movieId')
plt.ylabel('count()')

# Show the plot
plt.show()  # This ensures the plot is displayed
print('plt.show')