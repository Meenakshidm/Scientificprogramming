# Visualize the distribution of movie ratings using sns.histplot().
# Create a bar plot for top genres by average rating.
# Use a heatmap to show correlations in movie features.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv("/Users/I752598/Downloads/movie_dataset.csv") 

# 1. Distribution Plot of Movie Ratings
plt.figure(figsize=(8, 6))
sns.histplot(df['vote_average'], kde=True, color='skyblue', bins=15)
plt.title("Distribution of Movie Ratings with KDE")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show() 

# 2. Horizontal Bar Plot for Top Genres by Average Rating
# Split genres into individual rows
genres = df['genres'].str.split('|', expand=True).stack().reset_index(level=1, drop=True)
genres.name = 'genre'

# Create a new DataFrame that aligns genres with the corresponding ratings
df_genres = df[['vote_average']].join(genres)

# Check the intermediate dataframe
print(df_genres.head())

# Calculate average rating for each genre
avg_genre_rating = df_genres.groupby('genre')['vote_average'].mean().sort_values(ascending=False)

# Plot horizontal bar plot for top 5 genres by average rating
plt.figure(figsize=(10, 6))
avg_genre_rating.head(5).plot(kind='barh', color='lightcoral')
plt.title("Top Genres by Average Rating (Horizontal)")
plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.show() 

# 3. Heatmap for Correlations in Numerical Features
# Select numerical features
movie_features = df[['budget', 'revenue', 'runtime', 'vote_average', 'vote_count']]

# Drop rows with missing values
movie_features = movie_features.dropna()

# Compute the correlation matrix
corr_matrix = movie_features.corr()

# Plot the heatmap with a color map
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=0.5, annot_kws={"size": 12})
plt.title("Correlation Heatmap of Movie Features with Viridis")
plt.show()
