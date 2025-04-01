'''
This script performs Ridge and Lasso regression on a dataset containing sales, PBT, and PAT data from 2016 to 2023.

Author: Vinit Shah
Date: 25/03/2024
'''

# Sales - 2024 - 245315
# PBT - 2024 - 61997
# PAT - 2024 - 46099

# --------------- Ridge & Lasso Regression ----------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import GridSearchCV

# Dataset (Excluding 2024)
data = {
    'Year': [2016, 2017, 2018, 2019, 2021, 2022, 2023],
    'Sales': [108646, 117966, 126746, 150774, 167311, 195772, 228907],
    'PBT': [31675, 34513, 34092, 41563, 44978, 51687, 56907], 
    'PAT': [24291, 26357, 25880, 31562, 43760, 38449, 42303]   
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Prepare data for training
X = df[['Year', 'PBT', 'PAT']]
y = df['Sales']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Define alpha range for stability
alphas = np.logspace(0, 3, 20)

# GridSearchCV with proper cross-validation
ridge = GridSearchCV(Ridge(max_iter=50000, tol=1e-3), param_grid={'alpha': alphas}, cv=3)
lasso = GridSearchCV(Lasso(max_iter=50000, tol=1e-3), param_grid={'alpha': alphas}, cv=3)

# Train models
ridge.fit(X_scaled, y)
lasso.fit(X_scaled, y)

# Best alpha values
best_alpha_ridge = ridge.best_params_['alpha']
best_alpha_lasso = lasso.best_params_['alpha']

# Final models with best alphas
ridge_model = Ridge(alpha=best_alpha_ridge, max_iter=50000, tol=1e-3)
lasso_model = Lasso(alpha=best_alpha_lasso, max_iter=50000, tol=1e-3)

ridge_model.fit(X_scaled, y)
lasso_model.fit(X_scaled, y)

# Predict sales for 2024
test_data_2024 = np.array([[2024, 61997, 46099]])  # Using actual 2024 PBT & PAT
test_data_2024_scaled = scaler.transform(test_data_2024)

ridge_pred = ridge_model.predict(test_data_2024_scaled)
lasso_pred = lasso_model.predict(test_data_2024_scaled)

print(f"Predicted Sales for 2024 (Ridge): {ridge_pred[0]:.2f}")
print(f"Predicted Sales for 2024 (Lasso): {lasso_pred[0]:.2f}")
print(f"Actual Sales for 2024: 245315.00")

# Model evaluation
def evaluate_model(y_true, y_pred, model_name):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    print(f"{model_name} - MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}")

evaluate_model(y, ridge_model.predict(X_scaled), "Ridge Regression")
evaluate_model(y, lasso_model.predict(X_scaled), "Lasso Regression")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Year'], y=df['Sales'], color='blue', label='Actual Sales')
plt.plot(df['Year'], ridge_model.predict(X_scaled), color='red', linestyle='dashed', label='Ridge Prediction')
plt.plot(df['Year'], lasso_model.predict(X_scaled), color='green', linestyle='dotted', label='Lasso Prediction')
plt.scatter(2024, ridge_pred, color='red', marker='x', s=100, label='Ridge 2024 Prediction')
plt.scatter(2024, lasso_pred, color='green', marker='x', s=100, label='Lasso 2024 Prediction')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Prediction for 2024 using Ridge & Lasso Regression')
plt.legend()
plt.grid()
plt.show()
