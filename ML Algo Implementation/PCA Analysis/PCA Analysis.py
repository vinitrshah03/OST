'''
This script attempts to predict the sales for the year 2024 using PCA and Linear Regression.

Author: Vinit Shah
Date: 18/03/2024
'''

# Sales - 2024 - 245315
# PBT - 2024 - 61997
# PAT - 2024 - 46099

# ----------- PCA & Linear Regression ------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Dataset (Excluding 2024)
data = {
    'Year': [2016, 2017, 2018, 2019, 2021, 2022, 2023],
    'Sales': [108646, 117966, 126746, 150774, 167311, 195772, 228907],
    'PBT': [31675, 34513, 34092, 41563, 44978, 51687, 56907], 
    'PAT': [24291, 26357, 25880, 31562, 43760, 38449, 42303]   
}

df = pd.DataFrame(data)

# Prepare data for training
X = df[['Year', 'PBT', 'PAT']]
y = df['Sales']

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Applying PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
X_pca = pca.fit_transform(X_scaled)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_pca, y)

# Predict sales for 2024
X_2024 = np.array([[2024, 61997, 46099]])  # Using actual 2024 PBT & PAT
X_2024_scaled = scaler.transform(X_2024)
X_2024_pca = pca.transform(X_2024_scaled)
predicted_sales_2024 = model.predict(X_2024_pca)

print(f"Predicted Sales for 2024: {predicted_sales_2024[0]:.2f}")
print(f"Actual Sales for 2024: 245315.00")

# Model evaluation
y_pred = model.predict(X_pca)
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Year'], y=df['Sales'], color='blue', label='Actual Sales')
plt.scatter(2024, predicted_sales_2024, color='red', marker='x', s=100, label='Predicted 2024 Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Prediction for 2024 using PCA & Linear Regression')
plt.legend()
plt.grid()
plt.show()
