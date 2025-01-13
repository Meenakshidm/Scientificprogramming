# Create a pie chart to display the percentage of movies by genre.
# Plot a scatterplot showing the relationship between budget and revenue, and use color coding to distinguish genres.
# Generate a word cloud for movie titles in the most profitable genre.


import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in tips dataset
tips = sns.load_dataset('tips')

# 1. Violin plot to show tip distributions by time of day
plt.figure(figsize=(8, 6))
sns.violinplot(data=tips, x='time', y='tip', palette='muted') 
plt.title('Tip Distributions by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Tip Amount')
plt.show()

# 2. Bar graph to show average tip percentages by day
# Calculate tip percentage
tips['tip_percentage'] = (tips['tip'] / tips['total_bill']) * 100

# Group by day and calculate mean tip percentage
avg_tip_percentage = tips.groupby('day')['tip_percentage'].mean().reset_index()


# Plot the bar graph
plt.figure(figsize=(8, 6))
sns.barplot(data=avg_tip_percentage, x='day', y='tip_percentage', palette='pastel')
plt.title('Average Tip Percentage by Day')
plt.xlabel('Day')
plt.ylabel('Tip Percentage (%)')
plt.ylim(0, avg_tip_percentage['tip_percentage'].max() + 2)  # Adjust y-axis range
plt.show()

# 3. Scatterplot comparing total bill and tip amounts with a regression line
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', style='time', palette='cool', alpha=0.7)
sns.regplot(data=tips, x='total_bill', y='tip', scatter=False, color='blue', line_kws={"lw": 2})
plt.title('Total Bill vs. Tip Amounts with Regression Line')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.legend(title='Time of Day')
plt.show()
