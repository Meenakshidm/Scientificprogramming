import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Generate synthetic data
data = pd.DataFrame({
    'Time': range(100),
    'Value': np.sin(np.linspace(0, 10, 100)) + np.random.normal(scale=0.1, size=100)
})

# Ensure we're working with a copy of the DataFrame to avoid SettingWithCopyWarning
data = data.copy()

# Add lagged features
data['Lag_1'] = data['Value'].shift(1)
data['Lag_2'] = data['Value'].shift(2)

# Drop rows with missing values
data.dropna(inplace=True)

# Train-test split
X = data[['Lag_1', 'Lag_2']]  # Features: Lag_1 and Lag_2
y = data['Value']  # Target: Value

# Splitting into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict and evaluate the model
y_pred = rf.predict(X_test)

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)

# Print the result
print("Mean Absolute Error:", mae)
