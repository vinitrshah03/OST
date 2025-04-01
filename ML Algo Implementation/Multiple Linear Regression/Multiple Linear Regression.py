'''
This script predicts the sales of TCS for the year 2024 using multiple linear regression analysis.

Author: Vinit Shah
Date: 25/03/2024
'''

# Sales - 2024 - 245315
# PBT - 2024 - 61997
# PAT - 2024 - 46099

# ------------- Multiple Linear Regression ---------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

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
X = df[['Year', 'PBT', 'PAT']]  # Independent variables
y = df['Sales']  # Dependent variable

# Train the model
model = LinearRegression()
model.fit(X, y)

# avg_PBT = sum(data['PBT']) / len(data['PBT'])
# avg_PAT = sum(data['PAT']) / len(data['PAT'])

# Predict sales for 2024
test_data_2024 = np.array([[2024, 56907, 42303]])  # Using 2023 PBT & PAT
predicted_sales_2024 = model.predict(test_data_2024)

print(f"Predicted Sales for 2024: {predicted_sales_2024[0]:.2f}")
print(f"Actual Sales for 2024: 245315.00")

# Visualizing the trend
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Year'], y=df['Sales'], color='blue', label='Actual Sales')
plt.plot(df['Year'], model.predict(X), color='red', label='Regression Line')
plt.scatter(2024, predicted_sales_2024, color='green', label='Predicted 2024 Sales', marker='x', s=100)
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('TCS Sales Prediction for 2024')
plt.legend()
plt.grid()
plt.show()

# Model evaluation
y_pred = model.predict(X)
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
print(f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}")
