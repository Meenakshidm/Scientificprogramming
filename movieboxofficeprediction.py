import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/Users/I752598/Downloads/movie_dataset.csv")

# Handle missing values in columns
df = df.dropna(subset=['budget', 'genres', 'director', 'revenue'])

# Extract the 'budget' as numerical and preprocess categorical columns
df['budget'] = pd.to_numeric(df['budget'], errors='coerce') 

# Use LabelEncoder to convert 'director' (since it's a single value) to numerical
label_encoder_director = LabelEncoder()
df['director'] = label_encoder_director.fit_transform(df['director'])

# For 'genres', we'll assume it's a string of comma-separated genres, so we'll split and encode, # Handle NaN in 'genres' if any
df['genres'] = df['genres'].fillna('')  
label_encoder_genres = LabelEncoder()
df['genres'] = label_encoder_genres.fit_transform(df['genres'])

# Select relevant features (budget, genres, director) and target variable (revenue)
X = df[['budget', 'genres', 'director']]  # Features
y = df['revenue']  # Target variable 

# Step 3: Train-Test Split (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Decision Tree Regressor model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate the Model using R-squared and Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared: {r2}")

# Step 7: Forecast future box office revenue (for new data)
# Assuming we have new data in a similar format (e.g., a budget of 100 million, genre index 3, director index 5)
new_data = pd.DataFrame({'budget': [100000000], 'genres': [3], 'director': [5]})
predicted_revenue = model.predict(new_data)

print(f"Predicted Box Office Revenue for new data: {predicted_revenue[0]}")

# Step 8: Visualize Actual vs Predicted Values
plt.figure(figsize=(10, 5))

# Scatter plot of actual vs predicted values
plt.subplot(1, 1, 1)
plt.scatter(y_test, y_pred, alpha=0.7, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2, label='Perfect Prediction')
plt.title('Decision Tree Regressor: Actual vs Predicted Revenue')
plt.xlabel('Actual Revenue')
plt.ylabel('Predicted Revenue')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show() 

