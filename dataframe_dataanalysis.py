import pandas as pd

# Data Analysis: Find the total revenue generated.
# Identify the top 5 products by total revenue.
# Find the customer who placed the most orders. 

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)

# Calculate the total revenue generated
total_revenue = df['sales'].sum() 

# Identify the top 5 products by total revenue
top_5_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(5) 

# Find the customer who placed the most orders
most_orders_customer = df['customer'].value_counts().idxmax()
most_orders_count = df['customer'].value_counts().max() 

print(f"Total Revenue Generated: ${total_revenue:,.2f}")
print("\nTop 5 Products by Total Revenue:")
print(top_5_products)
print(f"\nCustomer with the Most Orders: {most_orders_customer} (Total Orders: {most_orders_count})")
