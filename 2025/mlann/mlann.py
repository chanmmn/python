import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

# Sample dataset (20 samples, 2 features)
X = np.random.rand(20, 2)
y = X[:, 0] * 2 + X[:, 1] * 3 + np.random.randn(20) * 0.1  # Linear relation with noise

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train ANN model
model = MLPRegressor(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Predictions:", y_pred)
print("Actual:", y_test)
print("Score:", model.score(X_test, y_test))