import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the transaction data
transactions = pd.read_csv('transaction_data.csv')

# Preprocess the data
# Assume that 'amount' and 'balance' are normalized already
features = ['amount', 'balance']
X = transactions[features]
y = transactions['is_fraud']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# Make predictions on new transactions
new_transactions = pd.DataFrame({
    'amount': [1000.0, 500.0],
    'balance': [5000.0, 1000.0]
})
new_predictions = model.predict(new_transactions)
print(f"New predictions: {new_predictions}")