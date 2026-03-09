# ==============================
# SAMPLE 2: Classification Pipeline
# Predict Customer Churn
# ==============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# -------------------------------
# 1. Generate Sample Dataset
# -------------------------------

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "tenure_months": np.random.randint(1, 60, n),
    "monthly_spend": np.random.normal(70, 20, n),
    "support_calls": np.random.randint(0, 10, n),
    "contract_type": np.random.randint(0, 3, n)
})

# Target
data["churn"] = (
    (data["support_calls"] > 6) |
    (data["monthly_spend"] > 100) |
    (data["tenure_months"] < 6)
).astype(int)

data.to_csv("churn_raw.csv", index=False)

# -------------------------------
# 2. Load CSV
# -------------------------------

df = pd.read_csv("churn_raw.csv")

X = df.drop("churn", axis=1)
y = df["churn"]

# -------------------------------
# 3. Feature Engineering
# -------------------------------

numeric_features = X.columns

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features)
    ]
)

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", RandomForestClassifier(random_state=42))
])

# -------------------------------
# 4. Hyperparameter Tuning
# -------------------------------

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 10, 20]
}

grid = GridSearchCV(pipeline, param_grid, cv=3, scoring="accuracy")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

# -------------------------------
# 5. Evaluation
# -------------------------------

y_pred = best_model.predict(X_test)

acc = accuracy_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print(f"Best Params: {grid.best_params_}")
print(f"Accuracy: {acc:.4f}")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -------------------------------
# 6. AI Reporting
# -------------------------------

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
# plt.show()
plt.savefig("churn_confusion_matrix.png", dpi=150, bbox_inches='tight')
plt.close()
print("Plot saved as 'churn_confusion_matrix.png'")

print("\n===== AI INSIGHTS =====")
if acc > 0.90:
    print("Excellent churn detection performance.")
elif acc > 0.80:
    print("Good performance, may improve with feature engineering.")
else:
    print("Model needs improvement, consider advanced feature engineering.")