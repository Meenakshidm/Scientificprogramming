import pandas as pd

# Data Cleaning: Check for missing values and handle them appropriately.
# Ensure that the Date column is in the correct datetime format.
# Create a new column called Revenue if it’s missing, using Quantity × Price.

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url) 

# Check for missing values
missing_values = df.isnull().sum()

# Handle missing values (e.g., filling or dropping), Drop rows with missing values
# df = df.dropna()  

# Ensure the order_date and ship_date columns are in datetime format
for column in ['order_date', 'ship_date']:
    if column in df.columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')
        # Check for invalid date entries after conversion
        invalid_dates = df[column].isnull().sum()
        print(f"Invalid entries in {column}: {invalid_dates}")
    else:
        print(f"{column} column not found")

# Check and create a 'revenue' column if it's missing 
if 'revenue' not in df.columns:
    # Ensure both 'quantity' and 'price' columns exist
    if {'quantity', 'price'}.issubset(df.columns):
        df['revenue'] = df['quantity'] * df['price']
        revenue_status = "'Revenue' column created successfully."
    else:
        revenue_status = "Required columns ('quantity' and 'price') for 'Revenue' calculation are missing."
else:
    revenue_status = "'Revenue' column already exists."


print("\nMissing values in the dataset:")
print(missing_values)
print("\nNumber of invalid dates after conversion:", invalid_dates)
print(revenue_status) 