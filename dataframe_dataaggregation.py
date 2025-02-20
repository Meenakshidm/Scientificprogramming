import pandas as pd

# Data Aggregation: Group data by Product and calculate the total quantity sold for each product.
# Group data by Date to show daily revenue trends.

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)

# Data Aggregation: Group data by Product and calculate total quantity sold for each product
total_quantity_by_product = df.groupby('product_name')['quantity'].sum().reset_index()

# Group data by Date to show daily revenue trends
df['order_date'] = pd.to_datetime(df['order_date'])
daily_revenue = df.groupby('order_date')['sales'].sum().reset_index()


print("\nTotal Quantity Sold by Product:")
print(total_quantity_by_product.head(10))

print("\nDaily Revenue Trends:")
print(daily_revenue.head(10)) 

