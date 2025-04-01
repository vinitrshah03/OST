'''
This script attempts to predicts the sales for the year 2024 using polynomial regression.

Author: Vinit Shah
Date: 18/03/2024
'''
# Sales - 2024 - 245315
# PBT - 2024 - 61997
# PAT - 2024 - 46099

# ----------------- Polynomial Regression -----------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import xgboost as xgb

# Dataset (Excluding 2024)
data = {
    'Year': [2016, 2017, 2018, 2019, 2021, 2022, 2023],
    'Sales': [108646, 117966, 126746, 150774, 167311, 195772, 228907],
    'PBT': [31675, 34513, 34092, 41563, 44978, 51687, 56907], 
    'PAT': [24291, 26357, 25880, 31562, 43760, 38449, 42303]   
}

df = pd.DataFrame(data)

# Feature Engineering
# Create rolling mean and standard deviation to capture trends
df['PBT_RollingMean'] = df['PBT'].rolling(3, min_periods=1).mean()
df['PAT_RollingMean'] = df['PAT'].rolling(3, min_periods=1).mean()
df['PBT_Std'] = df['PBT'].rolling(3, min_periods=1).std().fillna(0)
df['PAT_Std'] = df['PAT'].rolling(3, min_periods=1).std().fillna(0)

# Prepare data for training
X = df[['Year', 'PBT_RollingMean', 'PAT_RollingMean', 'PBT_Std', 'PAT_Std']]
y = df['Sales']

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Finding best polynomial degree
degree_range = range(2, 6)
best_score = float('inf')
best_degree = 2

for d in degree_range:
    model = make_pipeline(PolynomialFeatures(d), Ridge(alpha=1e-3))
    scores = cross_val_score(model, X_scaled, y, cv=3, scoring='neg_mean_absolute_error')
    score = -scores.mean()
    if score < best_score:
        best_score = score
        best_degree = d

# Train final polynomial model
poly_model = make_pipeline(PolynomialFeatures(best_degree), Ridge(alpha=1e-3))
poly_model.fit(X_scaled, y)

# Train XGBoost model
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, max_depth=3, learning_rate=0.1)
xgb_model.fit(X_scaled, y)

# Predict 2024 Sales
pbt_avg = df['PBT'].mean()
pat_avg = df['PAT'].mean()
pbt_std = df['PBT'].std()
pat_std = df['PAT'].std()

test_data_2024 = np.array([[2024, pbt_avg, pat_avg, pbt_std, pat_std]])
test_data_2024_scaled = scaler.transform(test_data_2024)

poly_pred = poly_model.predict(test_data_2024_scaled)
xgb_pred = xgb_model.predict(test_data_2024_scaled)

final_pred = (poly_pred[0] + xgb_pred[0]) / 2  # Averaging both predictions

print(f"Predicted Sales for 2024: {final_pred:.2f}")
print(f"Actual Sales for 2024: 245315.00")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Year'], y=df['Sales'], color='blue', label='Actual Sales')
plt.scatter(2024, final_pred, color='red', marker='x', s=100, label='Predicted 2024 Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Prediction for 2024 using Polynomial Regression & XGBoost')
plt.legend()
plt.grid()
plt.show()

