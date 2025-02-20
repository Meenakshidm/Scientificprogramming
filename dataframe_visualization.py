import pandas as pd
import matplotlib.pyplot as plt

# Visualization: Plot a bar chart showing the top 5 products by revenue.
# Create a line graph to visualize daily revenue trends.

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)

# Data Aggregation: Group data by Product and calculate total quantity sold for each product 
total_quantity_by_product = df.groupby('product_name')['quantity'].sum().reset_index()

# Group data by Date to show daily revenue trends
df['order_date'] = pd.to_datetime(df['order_date'])
daily_revenue = df.groupby('order_date')['sales'].sum().reset_index()  

# Visualization: Top 5 products by revenue
top_products_by_revenue = df.groupby('product_name')['sales'].sum().reset_index()
top_products_by_revenue = top_products_by_revenue.sort_values(by='sales', ascending=False).head(5) 

plt.figure(figsize=(10, 6))
plt.bar(top_products_by_revenue['product_name'], top_products_by_revenue['sales'], color='skyblue') 
plt.title('Top 5 Products by Revenue')
plt.xlabel('Product Name')
plt.ylabel('Revenue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()  

# Visualization: Daily revenue trends
plt.figure(figsize=(12, 6))
plt.plot(daily_revenue['order_date'], daily_revenue['sales'], color='green')
plt.title('Daily Revenue Trends')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nTotal Quantity Sold by Product:")
print(total_quantity_by_product.head(10))

print("\nDaily Revenue Trends:")
print(daily_revenue.head()) 
