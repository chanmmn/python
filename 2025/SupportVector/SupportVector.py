import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Sample data
data = {
    'Age': [25, 45, 35, 50, 23, 40, 29, 33, 48, 31, 27, 36, 42, 38, 26],
    'Income': [50000, 80000, 60000, 120000, 40000, 75000, 52000, 58000, 110000, 62000, 48000, 67000, 85000, 77000, 45000],
    'LoanAmount': [20000, 30000, 25000, 40000, 15000, 28000, 22000, 24000, 35000, 26000, 18000, 27000, 32000, 29000, 20000],
    'CreditScore': [700, 650, 720, 680, 710, 690, 705, 715, 660, 725, 695, 710, 675, 685, 705],
    'WillPayLoan': [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]  # 1: Will pay, 0: Will not pay
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['Age', 'Income', 'LoanAmount', 'CreditScore']]
y = df['WillPayLoan']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Support Vector Machine (SVM) model
model_svm = SVC(random_state=42)
model_svm.fit(X_train, y_train)
y_pred_svm = model_svm.predict(X_test)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"SVM Accuracy: {accuracy_svm:.2f}")

# Make predictions
y_pred = model_svm.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Predict for new data
new_data = pd.DataFrame({
    'Age': [30],
    'Income': [70000],
    'LoanAmount': [22000],
    'CreditScore': [690]
})

prediction_svm = model_svm.predict(new_data)

print(f"SVM Prediction (1: Will pay, 0: Will not pay): {prediction_svm[0]}")
