import pandas as pd

# Data Loading: Load the CSV file into a Pandas DataFrame.
# Display the first 10 rows and basic statistics of the dataset using .head() and .describe().

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url)

first_10_rows = df.head(25)

basic_statistics = df.describe()

print("First 10 rows of the dataset:")
print(first_10_rows)
print("\nBasic Statistics of the dataset:")
print(basic_statistics) 