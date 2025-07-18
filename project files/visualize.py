import matplotlib.pyplot as plt
import numpy as np

def plot_vertical_bar(counts):
    stages = ['Viewed', 'Carted', 'Purchased']
    values = [counts['views'], counts['carts'], counts['purchases']]
    colors = ['skyblue', 'orange', 'green']

    plt.figure(figsize=(8, 5))
    plt.bar(stages, values, color=colors)
    plt.title('Funnel Analysis - Vertical Bar Chart')
    plt.ylabel('Number of Unique Users')

    for i, v in enumerate(values):
        plt.text(i, v + max(values) * 0.01, str(v), ha='center', fontweight='bold')

    plt.show()

def plot_gender_grouped_bar(df):
    def get_counts(sub_df):
        return [
            sub_df[sub_df['event_type'] == 'view']['user_id'].nunique(),
            sub_df[sub_df['event_type'] == 'cart']['user_id'].nunique(),
            sub_df[sub_df['event_type'] == 'purchase']['user_id'].nunique()
        ]

    male_df = df[df['gender'] == 'Male']
    female_df = df[df['gender'] == 'Female']

    counts_male = get_counts(male_df)
    counts_female = get_counts(female_df)

    stages = ['Viewed', 'Carted', 'Purchased']
    x = np.arange(len(stages))
    width = 0.35

    plt.figure(figsize=(9, 5))
    plt.bar(x - width/2, counts_male, width, label='Male', color='skyblue')
    plt.bar(x + width/2, counts_female, width, label='Female', color='plum')

    plt.xticks(x, stages)
    plt.ylabel('Unique Users')
    plt.title('Grouped Bar Chart: Funnel by Gender')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_hourly_funnel(hourly_df):
    plt.figure(figsize=(12,6))
    for event in ['view', 'cart', 'purchase']:
        if event in hourly_df.columns:
            plt.plot(hourly_df.index, hourly_df[event], label=event.capitalize())

    plt.xlabel('Hour of Day')
    plt.ylabel('Unique Users')
    plt.title('Hourly Funnel Activity')
    plt.xticks(range(0, 24))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
