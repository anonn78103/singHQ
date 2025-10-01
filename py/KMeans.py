import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1) Load dataset
df = pd.read_csv("insta.csv")

# 2) Select features for clustering
X = df[["Instagram visit score", "Spending_rank(0 to 100)"]]

# 3) Train K-Means (let's try 3 clusters first)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

# 4) Plot clusters
plt.figure(figsize=(8,6))
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=df["Cluster"], cmap="viridis", s=50)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            c="red", marker="X", s=200, label="Centroids")
plt.xlabel("Instagram Visit Score")
plt.ylabel("Spending Rank")
plt.title("K-Means Clustering on insta.csv")
plt.legend()
plt.show()
