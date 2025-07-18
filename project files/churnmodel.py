import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def build_churn_dataset(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df_sorted = df.sort_values(by=['user_id', 'timestamp'])

    user_groups = df_sorted.groupby('user_id')

    data = []
    for user_id, group in user_groups:
        events = group['event_type'].tolist()
        views = events.count('view')
        carts = events.count('cart')
        purchased = 'purchase' in events
        label = int(purchased)

        time_gap = (group['timestamp'].max() - group['timestamp'].min()).total_seconds() / 60  # in mins
        hour_first = group['timestamp'].iloc[0].hour

        data.append([user_id, views, carts, time_gap, hour_first, label])

    churn_df = pd.DataFrame(data, columns=['user_id', 'views', 'carts', 'time_gap_mins', 'first_hour', 'label'])
    return churn_df
