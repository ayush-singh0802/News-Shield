"""
Model Evaluation and Metric Calculation Helpers for News Shield
Author: News Shield Project Team (GNIOT / AKTU)
Supervisor: Mr. Rohit Vaid
"""

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)


def evaluate_model_performance(y_true, y_pred, y_prob=None, model_name="Model"):
    """
    Computes all standard classification metrics including ROC-AUC when probabilities exist.

    Args:
        y_true: Ground truth binary labels.
        y_pred: Predicted binary labels.
        y_prob: Predicted probability scores for positive class (Real = 1).
        model_name: Identifier string.

    Returns:
        dict: Standard metrics dictionary + confusion matrix array.
    """
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='binary', zero_division=0)
    rec = recall_score(y_true, y_pred, average='binary', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='binary', zero_division=0)
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, output_dict=True)

    roc_auc = None
    if y_prob is not None:
        try:
            roc_auc = round(float(roc_auc_score(y_true, y_prob)) * 100, 2)
        except Exception:
            roc_auc = None

    metrics = {
        "Model": model_name,
        "Accuracy": round(acc * 100, 2),
        "Precision": round(prec * 100, 2),
        "Recall": round(rec * 100, 2),
        "F1-Score": round(f1 * 100, 2),
        "ROC-AUC": roc_auc,
        "Confusion Matrix": cm.tolist(),
        "Raw Report": report
    }
    return metrics


def print_evaluation_summary(metrics_dict: dict):
    """Prints a clean CLI summary table for terminal logging."""
    print("=" * 65)
    print(f" Performance Summary: {metrics_dict['Model']}")
    print("=" * 65)
    print(f"  Accuracy  : {metrics_dict['Accuracy']}%")
    print(f"  Precision : {metrics_dict['Precision']}%")
    print(f"  Recall    : {metrics_dict['Recall']}%")
    print(f"  F1-Score  : {metrics_dict['F1-Score']}%")
    if metrics_dict.get("ROC-AUC") is not None:
        print(f"  ROC-AUC   : {metrics_dict['ROC-AUC']}%")
    cm = np.array(metrics_dict["Confusion Matrix"])
    print("\n  Confusion Matrix [TN, FP] / [FN, TP]:")
    print(f"    True Fake  (TN): {cm[0][0]:<5} | False Real (FP): {cm[0][1]:<5}")
    print(f"    False Fake (FN): {cm[1][0]:<5} | True Real  (TP): {cm[1][1]:<5}")
    print("=" * 65)
