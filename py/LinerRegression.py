import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1) Load dataset
df = pd.read_csv("insta.csv")

# 2) Features & Target
X = df[["Instagram visit score"]]   # independent variable
y = df["Spending_rank(0 to 100)"]   # dependent variable

# 3) Train model
model = LinearRegression()
model.fit(X, y)

# 4) Print model details
print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² score:", model.score(X, y))

# 5) Predictions
df["Predicted"] = model.predict(X)

# 6) Visualization
plt.scatter(X, y, color="blue", label="Actual Spending Rank")
plt.plot(X, df["Predicted"], color="red", label="Regression Line")
plt.xlabel("Instagram Visit Score")
plt.ylabel("Spending Rank")
plt.legend()
plt.show()

