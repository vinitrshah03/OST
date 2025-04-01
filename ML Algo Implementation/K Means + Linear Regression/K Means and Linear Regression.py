'''
This script predicts the sales for the year 2024 using K-Means clustering and regression analysis.

Author: Vinit Shah
Date: 01/04/2024
'''

# Sales - 2024 - 245315
# PBT - 2024 - 61997
# PAT - 2024 - 46099
# --------------- K means + Regression ---------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Dataset (Excluding 2024)
data = {
    'Year': [2016, 2017, 2018, 2019, 2021, 2022, 2023],
    'Sales': [108646, 117966, 126746, 150774, 167311, 195772, 228907],
    'PBT': [31675, 34513, 34092, 41563, 44978, 51687, 56907], 
    'PAT': [24291, 26357, 25880, 31562, 43760, 38449, 42303]   
}

df = pd.DataFrame(data)

# Prepare data for clustering
X_cluster = df[['PBT', 'PAT']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

# Finding the optimal number of clusters using Elbow Method
wcss = []
for i in range(1, 6):  # Trying clusters from 1 to 5
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Optimal clusters (choosing 2 for simplicity)
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X_scaled)
df['Cluster'] = kmeans.labels_

# Train Regression Model within each Cluster
models = {}
for cluster in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == cluster]
    X_train = cluster_data[['Year', 'PBT', 'PAT']]
    y_train = cluster_data['Sales']
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    models[cluster] = model

# Determine the Cluster for 2024 Data
pbt_2024, pat_2024 = 61997, 46099  # Actual 2024 PBT & PAT
test_scaled = scaler.transform([[pbt_2024, pat_2024]])
predicted_cluster = kmeans.predict(test_scaled)[0]

# Predict 2024 Sales using the Regression Model for that Cluster
test_data_2024 = np.array([[2024, pbt_2024, pat_2024]])
predicted_sales_2024 = models[predicted_cluster].predict(test_data_2024)[0]

print(f"Predicted Sales for 2024: {predicted_sales_2024:.2f}")
print(f"Actual Sales for 2024: 245315.00")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Year'], y=df['Sales'], hue=df['Cluster'], palette='coolwarm', s=100)
plt.scatter(2024, predicted_sales_2024, color='black', marker='x', s=200, label='Predicted 2024 Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('K-Means Clustering + Regression Sales Prediction for 2024')
plt.legend()
plt.grid()
plt.show()
