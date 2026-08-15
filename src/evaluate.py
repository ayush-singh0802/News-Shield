"""
Model Evaluation and Metric Calculation Helpers
Author: 2nd Year CSE Student (Mini Project)
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def evaluate_model_performance(y_true, y_pred, model_name="Model"):
    """
    Computes all standard classification metrics.

    Returns:
        dict: Standard metrics dictionary + confusion matrix array.
    """
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='binary', zero_division=0)
    rec = recall_score(y_true, y_pred, average='binary', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='binary', zero_division=0)
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)

    metrics = {
        "Model": model_name,
        "Accuracy": round(acc * 100, 2),
        "Precision": round(prec * 100, 2),
        "Recall": round(rec * 100, 2),
        "F1-Score": round(f1 * 100, 2),
        "Confusion Matrix": cm.tolist(),
        "Raw Report": report
    }
    return metrics


def print_evaluation_summary(metrics_dict: dict):
    """Prints a clean CLI summary table for terminal logging."""
    print("=" * 60)
    print(f" Performance Summary for: {metrics_dict['Model']} ")
    print("=" * 60)
    print(f"Accuracy  : {metrics_dict['Accuracy']}%")
    print(f"Precision : {metrics_dict['Precision']}%")
    print(f"Recall    : {metrics_dict['Recall']}%")
    print(f"F1-Score  : {metrics_dict['F1-Score']}%")
    print("\nConfusion Matrix [TN, FP], [FN, TP]:")
    cm = np.array(metrics_dict["Confusion Matrix"])
    print(f"   [True Fake (TN): {cm[0][0]:<4} | False Real (FP): {cm[0][1]:<4}]")
    print(f"   [False Fake (FN): {cm[1][0]:<4} | True Real (TP): {cm[1][1]:<4}]")
    print("=" * 60)
