import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# ---------------------------
# 1. Create dummy dataset
# ---------------------------
X = pd.DataFrame({
    "age": [25, 32, 47, 51, 62, 23, 44, 36, 52, 48],
    "income": [50000, 60000, 80000, 72000, 91000, 40000, 67000, 56000, 85000, 79000],
    "gender": ["M", "F", "F", "M", "M", "F", "F", "M", "M", "F"],
    "region": ["east", "west", "south", "north", "west", "east", "south", "north", "east", "west"]
})

# Target labels (binary classification)
y = np.array([0, 1, 1, 0, 0, 1, 1, 0, 1, 0])

# ---------------------------
# 2. Define preprocessing
# ---------------------------
numeric_columns = X.select_dtypes(include=np.number).columns.tolist()
categorical_columns = X.select_dtypes(exclude=np.number).columns.tolist()

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_columns),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
])

# ---------------------------
# 3. Define pipeline & models
# ---------------------------
pipeline = Pipeline([
    ("preproc", preprocessor),
    ("clf", LogisticRegression(max_iter=1000))
])

# param_grid = [
#     {"clf": [LogisticRegression(max_iter=1000)], "clf__C": [0.01, 0.1, 1, 10]},
#     {"clf": [RandomForestClassifier()], "clf__n_estimators": [100, 300], "clf__max_depth": [None, 10, 30]},
#     {"clf": [SVC(probability=True)], "clf__C": [0.1, 1, 10], "clf__kernel": ["rbf", "linear"]}
# ]

# # ---------------------------
# # 4. Nested CV
# # ---------------------------
cv_inner = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)  # smaller folds for small dataset
#grid = GridSearchCV(pipeline, param_grid, cv=cv_inner, scoring="f1_macro", n_jobs=-1)

cv_outer = StratifiedKFold(n_splits=3, shuffle=True, random_state=1)
# scores = cross_val_score(grid, X, y, cv=cv_outer, scoring="f1_macro")

# print("Nested CV f1_macro: mean=%.3f std=%.3f" % (scores.mean(), scores.std()))

# Individual F1 scores for each classifier using cross_val_score
models = {
    "LogisticRegression": Pipeline([
        ("preproc", preprocessor),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    # ,
    # "RandomForestClassifier": Pipeline([
    #     ("preproc", preprocessor),
    #     ("clf", RandomForestClassifier())
    # ]),
    # "SVC": Pipeline([
    #     ("preproc", preprocessor),
    #     ("clf", SVC(probability=True))
    # ])
}

for name, model in models.items():
    score = cross_val_score(model, X, y, cv=cv_outer, scoring="f1_macro")
    print(f"{name} f1_macro: mean={score.mean():.3f} std={score.std():.3f}")