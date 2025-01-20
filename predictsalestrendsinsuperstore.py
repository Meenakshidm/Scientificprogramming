import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error  

url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/refs/heads/main/superstore_dataset.csv"
df = pd.read_csv(url) 

# Clean up column names (remove any leading/trailing spaces)
df.columns = df.columns.str.strip()

# Convert 'order_date' column to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Handle missing values (if any)
df = df.dropna(subset=['order_date', 'sales', 'quantity', 'discount'])

# Extract features (Month, Year, Day) from 'order_date'
df['Month'] = df['order_date'].dt.month
df['Year'] = df['order_date'].dt.year
df['Day'] = df['order_date'].dt.day

# Debugging: Print the column names to check the available columns
print(df.columns)

# Step 3: Feature Selection (selecting relevant columns)
X = df[['Month', 'Year', 'quantity', 'discount']]  # Features
y = df['sales']  # Target variable 

# Step 4: Train-Test Split (80% for training, 20% for testing) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Model Training (Linear Regression)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train) 

# Step 6: Make Predictions
y_pred = lr_model.predict(X_test) 

# Step 7: Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Updated Visualization: Scatter Plot with Linear Regression Line
plt.figure(figsize=(18, 6))

# Plot for Linear Regression
plt.subplot(1, 3, 1)
plt.scatter(y_test, y_pred, alpha=0.7, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
plt.title('Linear Regression: Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.grid(True)

plt.tight_layout()
plt.show() 


