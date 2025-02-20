# Join the movies dataset with a dataset containing country information to analyze which country produces the most profitable movies.
# Create a new column, Profit = Revenue - Budget, and rank movies by profit.
# Use groupby to find the most profitable genres.

import pandas as pd  

df = pd.read_csv("/Users/I752598/Downloads/movie_dataset.csv")
df2 = pd.read_csv("/Users/I752598/Downloads/netflix_titles.csv")

# Merge the datasets on the 'title' column
merged_df = pd.merge(df, df2, how='left', on='title')

# Create a new column 'Profit' as the difference between 'Revenue' and 'Budget'
merged_df['Profit'] = merged_df['revenue'] - merged_df['budget']

# Rank movies by profit in descending order
merged_df['Profit_Rank'] = merged_df['Profit'].rank(ascending=False)

# Group by 'country' to find the total profit by country
country_profit = merged_df.groupby('country')['Profit'].sum().sort_values(ascending=False)

# Group by 'genres' to find the total profit by genre
genre_profit = merged_df.groupby('genres')['Profit'].sum().sort_values(ascending=False)

# Display the results
print("Top 5 Countries by Total Profit:")
print(country_profit.head())

print("\nTop 5 Genres by Total Profit:")
print(genre_profit.head())

print("\nTop 10 Most Profitable Movies:")
print(merged_df[['title', 'Profit', 'Profit_Rank']].sort_values('Profit', ascending=False).head(10))

