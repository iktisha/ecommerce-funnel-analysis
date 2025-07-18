import pandas as pd

df = pd.read_csv('../.venv/mock_ecommerce_sample.csv')

missing = df.isnull().sum()
print(missing)
print("Total rows:", len(df))
print("Unique users:", df['user_id'].nunique())
print("\nEvent counts:\n", df['event_type'].value_counts())
print("\nSample data:\n", df.sample(10))

