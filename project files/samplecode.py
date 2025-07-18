#generated sample dataset
import pandas as pd
import numpy as np

np.random.seed(42)

events = ['view', 'cart', 'purchase']
probabilities = [0.7, 0.2, 0.1]

user_ids = np.random.randint(1000, 5000, size=20000)
event_types = np.random.choice(events, size=20000, p=probabilities)
timestamps = pd.date_range(start='2023-01-01', periods=20000, freq='T')

df = pd.DataFrame({
    'user_id': user_ids,
    'event_type': event_types,
    'timestamp': timestamps
})

df.to_csv('mock_ecommerce_sample.csv', index=False)

print("Mock e-commerce funnel dataset created as 'mock_ecommerce_sample.csv'")
