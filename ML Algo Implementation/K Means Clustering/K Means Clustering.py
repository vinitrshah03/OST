'''
This script attempts to predict the sales for the year 2024 using K-Means clustering.

Author: Vinit Shah
Date: 25/03/2024
'''

# Sales - 2024 - 245315
# PBT - 2024 - 61997
# PAT - 2024 - 46099

# --------------- K Means ---------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dataset (Excluding 2024)
data = {
    'Year': [2016, 2017, 2018, 2019, 2021, 2022, 2023],
    'Sales': [108646, 117966, 126746, 150774, 167311, 195772, 228907],
    'PBT': [31675, 34513, 34092, 41563, 44978, 51687, 56907], 
    'PAT': [24291, 26357, 25880, 31562, 43760, 38449, 42303]   
}

df = pd.DataFrame(data)

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Year', 'PBT', 'PAT']])

# Finding the optimal number of clusters using the Elbow Method
inertia = []
k_range = range(1, 6)  # Trying cluster sizes from 1 to 5 (since we have only 7 samples)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(6, 4))
plt.plot(k_range, inertia, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Clusters')
plt.show()

# Choose the optimal number of clusters (let's assume 3 based on the elbow method)
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
kmeans.fit(X_scaled)
df['Cluster'] = kmeans.labels_

# Predicting the cluster for 2024
test_data_2024 = np.array([[2024, 61997, 46099]])  # 2024 actual PBT & PAT
test_data_2024_scaled = scaler.transform(test_data_2024)
predicted_cluster = kmeans.predict(test_data_2024_scaled)[0]

# Estimate 2024 Sales by taking the average Sales of the assigned cluster
cluster_avg_sales = df[df['Cluster'] == predicted_cluster]['Sales'].mean()

print(f"Predicted Sales for 2024: {cluster_avg_sales:.2f}")
print(f"Actual Sales for 2024: 245315.00")

# Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Year'], y=df['Sales'], hue=df['Cluster'], palette='viridis', s=100)
plt.scatter(2024, cluster_avg_sales, color='red', marker='x', s=200, label='Predicted 2024 Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Clustering and 2024 Prediction using K-Means')
plt.legend()
plt.grid()
plt.show()