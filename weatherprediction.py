import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt  

df = pd.read_csv("/Users/I752598/Downloads/weather_data.csv")

# Preprocessing: Handle missing values
df = df.dropna()

# Define features (X) and target (y)
X = df.drop(columns=['Temperature_C', 'Location', 'Date_Time']) 
y = df['Temperature_C']  # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Initialize the Random Forest Regressor with fewer trees and limited jobs
model = RandomForestRegressor(n_estimators=10, random_state=42, n_jobs=2)

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test) 

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")

# Plot: Actual vs Predicted Temperatures
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='blue', label='Predictions')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2, label='Perfect Prediction')
plt.title('Random Forest Regressor: Actual vs Predicted Temperature')
plt.xlabel('Actual Temperature (°C)')
plt.ylabel('Predicted Temperature (°C)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show() 


