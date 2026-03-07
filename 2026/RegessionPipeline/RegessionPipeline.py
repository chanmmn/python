# ==============================
# SAMPLE 1: Regression Pipeline
# Predict House Prices
# ==============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# -------------------------------
# 1. Generate Sample Dataset
# -------------------------------

np.random.seed(42)

n = 500

data = pd.DataFrame({
    "square_feet": np.random.normal(1500, 500, n),
    "bedrooms": np.random.randint(1, 6, n),
    "age": np.random.randint(0, 30, n),
    "distance_to_city": np.random.normal(10, 5, n),
})

# Target variable
data["price"] = (
    data["square_feet"] * 200 +
    data["bedrooms"] * 10000 -
    data["age"] * 1500 -
    data["distance_to_city"] * 3000 +
    np.random.normal(0, 20000, n)
)

# Save as raw CSV
data.to_csv("housing_raw.csv", index=False)

# -------------------------------
# 2. Load Raw CSV
# -------------------------------

df = pd.read_csv("housing_raw.csv")

X = df.drop("price", axis=1)
y = df["price"]

# -------------------------------
# 3. Feature Engineering
# -------------------------------

numeric_features = X.columns

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features)
    ]
)

# -------------------------------
# 4. Model + Pipeline
# -------------------------------

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", RandomForestRegressor(random_state=42))
])

# -------------------------------
# 5. Hyperparameter Tuning
# -------------------------------

param_grid = {
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 10, 20]
}

grid = GridSearchCV(pipeline, param_grid, cv=3, scoring="r2")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

# -------------------------------
# 6. Evaluation
# -------------------------------

y_pred = best_model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print(f"Best Params: {grid.best_params_}")
print(f"MAE: {mae:,.2f}")
print(f"RMSE: {rmse:,.2f}")
print(f"R² Score: {r2:.4f}")

# -------------------------------
# 7. AI-Generated Report
# -------------------------------

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.savefig("price_prediction_plot.png", dpi=150, bbox_inches='tight')
plt.close()
print("Plot saved as 'price_prediction_plot.png'")

print("\n===== AI INSIGHTS =====")
if r2 > 0.85:
    print("Model performance is strong. Features capture most price variance.")
elif r2 > 0.70:
    print("Model performs reasonably well but may benefit from feature expansion.")
else:
    print("Model performance is weak. Consider adding more relevant features.")