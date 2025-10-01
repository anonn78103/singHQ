import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1) Load
df = pd.read_csv("drug200.csv")

# 2) Encode categorical columns and keep encoders for inverse transform
encoders = {}
for col in ["Sex", "BP", "Cholesterol", "Drug"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# 3) Features and target
X = df.drop("Drug", axis=1)
y = df["Drug"]

# 4) Train-test split (hold out 20% for evaluation)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)

# 5) Train (limit depth to reduce overfitting)
clf = DecisionTreeClassifier(criterion="entropy")
clf.fit(X_train, y_train)

# 6) Evaluate on unseen test set
y_pred = clf.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=encoders["Drug"].classes_))

new_samples = [
    [30, 0, 0, 0, 18.5],   # Female, BP=HIGH, Chol=HIGH
    [45, 1, 1, 1, 10.2]    # Male, BP=LOW, Chol=NORMAL
]

pred_nums = clf.predict(new_samples)
pred_names = encoders["Drug"].inverse_transform(pred_nums)

for sample, name in zip(new_samples, pred_names):
    print(f"Input (encoded): {sample} --> Predicted Drug: {name}")