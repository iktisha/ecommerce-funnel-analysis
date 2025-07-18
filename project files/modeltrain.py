import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_and_evaluate(df):
    X = df[['views', 'carts', 'time_gap_mins', 'first_hour']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Logistic Regression
    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(X_train, y_train)
    y_pred_log = log_reg.predict(X_test)

    print("Logistic Regression Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred_log))
    print(classification_report(y_test, y_pred_log))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))

    # Random Forest
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    print("\nRandom Forest Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred_rf))
    print(classification_report(y_test, y_pred_rf))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))

    # Feature importance from Random Forest
    importances = rf.feature_importances_
    features = X.columns
    print("\nFeature Importances (Random Forest):")
    for feat, imp in zip(features, importances):
        print(f"{feat}: {imp:.4f}")
    plot_feature_importance(features, importances)


def plot_feature_importance(features, importances):
            indices = np.argsort(importances)
            plt.figure(figsize=(8, 5))
            plt.title('Feature Importances')
            plt.barh(range(len(indices)), importances[indices], color='skyblue', align='center')
            plt.yticks(range(len(indices)), [features[i] for i in indices])
            plt.xlabel('Importance')
            plt.tight_layout()
            plt.show()
