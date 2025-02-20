# Plot monthly temperature trends using sns.lineplot().
# Show the relationship between humidity and temperature with a scatter plot. 


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/I752598/Downloads/weather_data.csv")

# Convert Date_Time to datetime format for easier manipulation
df['Date_Time'] = pd.to_datetime(df['Date_Time'])

# Extract month from Date_Time for monthly trends
df['Month'] = df['Date_Time'].dt.month

# Group by month and calculate average temperature
monthly_avg_temp = df.groupby('Month')['Temperature_C'].mean().reset_index()

# Plot monthly temperature trends
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_avg_temp, x='Month', y='Temperature_C', marker='o')
plt.title('Monthly Temperature Trends')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.xticks(range(1, 13))  # Ensure all months (1 to 12) are shown
plt.grid(True)
plt.show()

# Plot the relationship between humidity and temperature
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Temperature_C', y='Humidity_pct', alpha=0.6)
plt.title('Relationship between Humidity and Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.show()
