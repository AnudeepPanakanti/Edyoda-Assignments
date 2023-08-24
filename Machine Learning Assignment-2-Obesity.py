#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv('Obesity_data.csv')

# Select relevant features for the model
features = ['age_range', 'income_range', 'location', 'education', 'gender', 'class_level']
X = data[features]
y = data['obesity_percentage']

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X, columns=['age_range', 'income_range', 'location', 'education', 'gender', 'class_level'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

