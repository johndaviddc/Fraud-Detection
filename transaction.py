import pandas as pd
import random

# Generate random transaction data
num_transactions = 1000
min_amount = 10
max_amount = 1000
min_balance = 0
max_balance = 10000

transactions = pd.DataFrame({
    'amount': [random.uniform(min_amount, max_amount) for _ in range(num_transactions)],
    'balance': [random.uniform(min_balance, max_balance) for _ in range(num_transactions)],
    'is_fraud': [random.choice([0, 1]) for _ in range(num_transactions)]
})

# Make some transactions fraudulent
num_fraudulent_transactions = 50
fraud_indices = random.sample(range(num_transactions), num_fraudulent_transactions)
transactions.loc[fraud_indices, 'is_fraud'] = 1

# Save the transaction data to a CSV file
transactions.to_csv('transaction_data.csv', index=False)