import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.preprocessing import StandardScaler

# --- Load dataset ---
df = pd.read_csv("insta.csv")

# Select features
X = df[["Instagram visit score", "Spending_rank(0 to 100)"]].values

# Optional: scale data so both features count equally
X_scaled = StandardScaler().fit_transform(X)

# --- Step 1: Create linkage matrix (Ward’s method) ---
Z = linkage(X_scaled, method="ward")

# --- Step 2: Plot dendrogram ---
plt.figure(figsize=(10, 4))
dendrogram(Z)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Sample index")
plt.ylabel("Distance")
plt.show()

# --- Step 3: Cut the tree into clusters (choose k) ---
k = 3
df["Cluster"] = fcluster(Z, k, criterion="maxclust")

# --- Step 4: Plot data points colored by cluster ---
plt.figure(figsize=(6, 5))
plt.scatter(df["Instagram visit score"], df["Spending_rank(0 to 100)"],
            c=df["Cluster"], cmap="tab10", s=50)
plt.xlabel("Instagram Visit Score")
plt.ylabel("Spending Rank")
plt.title(f"Hierarchical Clusters (k={k})")
plt.show()

# --- Optional: See cluster counts ---
print(df["Cluster"].value_counts())
