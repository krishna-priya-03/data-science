
import pandas as pd
from sklearn.cluster import KMeans

# Create dataset
data = {
    'X': [1, 2, 3, 8, 9, 10],
    'Y': [1, 2, 3, 8, 9, 10]
}

df = pd.DataFrame(data)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=10, n_init=10)
kmeans.fit(df)

df['Cluster'] = kmeans.labels_

print("Clustered Data:")
print(df)

# Print each cluster separately
for i in range(3):
    print(f"\nCluster {i + 1}:")
    print(df[df['Cluster'] == i])
