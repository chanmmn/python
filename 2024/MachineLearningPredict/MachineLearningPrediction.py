import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the diamond dataset from the CSV file
diamond_data = pd.read_csv("diamondsprice.csv")

# Extract features (carat) and target (price)
X = diamond_data["carat"].values.reshape(-1, 1)
y = diamond_data["price"].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Plot the regression line
plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.plot(X_test, y_pred, color="red", label="Predicted")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Diamond Price Prediction")
plt.legend()
plt.show()

# Example prediction for a new diamond with carat=1.5
new_diamond_carat = 1.5
predicted_price = model.predict([[new_diamond_carat]])
print(f"Predicted price for a {new_diamond_carat:.2f} carat diamond: ${predicted_price[0]:,.2f}")
