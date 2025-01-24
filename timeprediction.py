import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer 

mtcars = sns.load_dataset("mpg") 

# Display all columns
pd.set_option('display.max_columns', None)

print(mtcars)

print(mtcars.head()) 

# Use "horsepower" as the predictor and "mpg" as the target variable
X = mtcars[["horsepower"]]
y = mtcars["mpg"]

# Check for and impute missing values in "horsepower"
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Drop rows where the target variable 'mpg' is missing
mtcars = mtcars.dropna(subset=["mpg"])
X = mtcars[["horsepower"]]
X = imputer.fit_transform(X)
y = mtcars["mpg"]

# Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)

# Random Forest Regression
rf_reg = RandomForestRegressor(n_estimators=100, random_state=0)
rf_reg.fit(X_train, y_train)

# Predictions
y_pred_linear = linear_reg.predict(X_test)
y_pred_rf = rf_reg.predict(X_test)

# Calculate Mean Squared Error (MSE) and R-squared (R²)
mse_linear = mean_squared_error(y_test, y_pred_linear)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_linear = r2_score(y_test, y_pred_linear)
r2_rf = r2_score(y_test, y_pred_rf)

print("Linear Regression:")
print("MSE: ", mse_linear)
print("R²: ", r2_linear)

print("\nRandom Forest Regression:")
print("MSE: ", mse_rf)
print("R²: ", r2_rf)

# Plot predictions
plt.scatter(y_test, y_pred_linear, label='Linear Regression', color='r')
plt.scatter(y_test, y_pred_rf, label='Random Forest Regression', color='g')
plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.legend()
plt.title("Model Comparison: Linear vs. Random Forest Regression")
plt.show()


