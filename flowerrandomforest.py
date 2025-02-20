# Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix   

iris = load_iris()

# Convert to a pandas DataFrame for easier manipulation
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target  # Adding the target column with labels 

# Mapping target integers to class names for readability
data['target_name'] = data['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("First 5 rows of the dataset:")
print(data.head()) 

# Visualizing the distribution of the target variable
sns.countplot(x='target_name', data=data)
plt.title("Distribution of Target Classes")
plt.show()

X = data[iris.feature_names]  # Features
y = data['target']            # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
rf.fit(X_train, y_train) 

# Make predictions on the test data
y_pred = rf.predict(X_test)

# Confusion Matrix: Shows how well the model predicts each class
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Feature Importance: Identifies which features are most important in making predictions
# Random Forest provides a built-in feature to calculate feature importance
importance = rf.feature_importances_

# Display feature importance
print("\nFeature Importance:")
for feature, importance_score in zip(iris.feature_names, importance):
    print(f"{feature}: {importance_score:.4f}")


# Visualize feature importance
sns.barplot(x=importance, y=iris.feature_names)
plt.title("Feature Importance in Random Forest")
plt.show() 




