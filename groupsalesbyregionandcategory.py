# Use the Superstore Dataset to analyze sales by region and product category. Group sales by Region and Category.
# Create a pivot table for monthly sales trends.
# Handle missing sales data using fillna().

import pandas as pd

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)

# Convert the 'order_date' column to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

# 1. Grouping Sales by Region and Product Category
pivot_region_category = df.pivot_table(
    values='sales', 
    index='region', 
    columns='category', 
    aggfunc='sum', 
    fill_value=0
) 

# 2. Monthly Sales Trends
df['month'] = df['order_date'].dt.to_period('M')  # Extract month and year as period (e.g., '2021-01')
pivot_monthly_sales = df.pivot_table(
    values='sales', 
    index='month', 
    aggfunc='sum', 
    fill_value=0
)

print("Sales by Region and Category:")
print(pivot_region_category)
print("\nMonthly Sales Trends:")
print(pivot_monthly_sales)




