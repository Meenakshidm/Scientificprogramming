
# Missing Data Challenge
# Scenario: Simulate missing data by randomly replacing 10% of values in the Superstore dataset's Sales column with NaN.
# Objective:
# Fill missing values using the mean or median.
# Use mean and compare results.
# Visualize the impact of missing data on regional sales performance.

import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)

# Step 1: Simulate missing data in the 'Sales' column
np.random.seed(42)  # Set seed for reproducibility
missing_indices = df.sample(frac=0.1).index  # Randomly select 10% of rows
df.loc[missing_indices, 'sales'] = np.nan  # Replace 'sales' values with NaN 

# Check the number of missing values
print("\nNumber of missing values in the 'Sales' column after simulation:")
print(df['sales'].isna().sum()) 

# Step 2: Fill missing values with the mean
sales_mean = df['sales'].mean()  # Calculate the mean of the 'Sales' column
df['sales_filled_mean'] = df['sales'].fillna(sales_mean)  # Fill missing values with the mean 

# Step 3: Analyze regional sales performance
# Regional sales before filling missing values
regional_sales_before = df.groupby('region')['sales'].sum()

# Regional sales after filling missing values with the mean
regional_sales_after = df.groupby('region')['sales_filled_mean'].sum()

# Step 4: Visualize the impact of missing data
plt.figure(figsize=(10, 6))
x = regional_sales_before.index

# Bar chart for regional sales before and after filling missing values
plt.bar(x, regional_sales_before, alpha=0.7, label='Before Filling Missing Data', color='blue')
plt.bar(x, regional_sales_after, alpha=0.7, label='After Filling Missing Data (Mean)', color='orange', width=0.4)

plt.title("Impact of Missing Data on Regional Sales Performance")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 

# Step 5: Print regional sales for comparison
print("\nRegional Sales Before Filling Missing Data:")
print(regional_sales_before)

print("\nRegional Sales After Filling Missing Data (Mean):")
print(regional_sales_after)



