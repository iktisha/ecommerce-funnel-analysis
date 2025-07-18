import pandas as pd
import numpy as np
from analysis import calculate_funnel_counts, print_funnel_counts, calculate_conversion_rates, print_conversion_rates
from visualize import plot_vertical_bar, plot_gender_grouped_bar

from analysis import hourly_funnel_counts
from visualize import plot_hourly_funnel

from churnmodel import build_churn_dataset
from modeltrain import train_and_evaluate


df = pd.read_csv('../.venv/mock_ecommerce_sample.csv')


np.random.seed(42)
df['gender'] = np.random.choice(['Male', 'Female'], size=len(df))

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour


counts = calculate_funnel_counts(df)
print_funnel_counts(counts)

rates = calculate_conversion_rates(counts)
print_conversion_rates(rates)

plot_vertical_bar(counts)
plot_gender_grouped_bar(df)

hourly_df = hourly_funnel_counts(df)
print(hourly_df.head())
plot_hourly_funnel(hourly_df)


churn_df = build_churn_dataset(df)
train_and_evaluate(churn_df)
