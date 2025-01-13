# Create a pie chart to display the percentage of movies by genre.
# Plot a scatterplot showing the relationship between budget and revenue, and use color coding to distinguish genres.
# Generate a word cloud for movie titles in the most profitable genre.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("/Users/I752598/Downloads/movie_dataset.csv")

# Fill missing values for relevant columns
df['genres'] = df['genres'].fillna('Unknown')
df['budget'] = df['budget'].fillna(0)
df['revenue'] = df['revenue'].fillna(0)
df['title'] = df['title'].fillna('Unknown')

# Split genres into individual entries 
all_genres = df['genres'].str.split('|').explode()

# Create a pie chart for genre percentages
genre_counts = all_genres.value_counts()
plt.figure(figsize=(8, 8))
genre_counts.plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Percentage of Movies by Genre')
plt.ylabel('')  # Remove y-axis label
plt.show()

# Scatterplot: Relationship between budget and revenue, color-coded by genres
# Select the first genre for simplicity (since movies may belong to multiple genres)
df['main_genre'] = df['genres'].str.split('|').str[0]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='budget', y='revenue', hue='main_genre', alpha=0.7, palette='tab10')
plt.title('Relationship between Budget and Revenue by Genre')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show() 

# Word Cloud for movie titles in the most profitable genre 
# Calculate profit and find the most profitable genre
df['profit'] = df['revenue'] - df['budget']
most_profitable_genre = df.groupby('main_genre')['profit'].mean().idxmax()

# Filter movies in the most profitable genre
profitable_genre_titles = df[df['main_genre'] == most_profitable_genre]['title'].dropna()

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(profitable_genre_titles))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(f'Word Cloud for Movie Titles in the Most Profitable Genre: {most_profitable_genre}')
plt.show()
