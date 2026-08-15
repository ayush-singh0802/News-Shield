"""
Model Training & Evaluation Pipeline for Fake News Detection
Author: 2nd Year CSE Student (Mini Project)

Algorithms Evaluated:
1. Passive Aggressive Classifier (Best for stream text classification)
2. Logistic Regression (Classic Linear Baseline)
3. Multinomial Naive Bayes (Probabilistic NLP Model)
4. Random Forest (Ensemble Tree Model)
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier, LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

from src.preprocessor import clean_text
from src.evaluate import evaluate_model_performance, print_evaluation_summary
from data.dataset_downloader import create_dataset, DATASET_PATH

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
METRICS_PATH = os.path.join(MODEL_DIR, "model_metrics.json")


def load_and_preprocess_data():
    """Loads dataset and applies NLP preprocessing."""
    if not os.path.exists(DATASET_PATH):
        print("[INFO] Dataset not found, generating sample dataset...")
        df = create_dataset()
    else:
        df = pd.read_csv(DATASET_PATH)

    print(f"[INFO] Loaded {len(df)} news articles.")

    # Combine Title and Text for rich contextual representation
    df['combined_content'] = df['title'].fillna('') + ' ' + df['text'].fillna('')

    print("[INFO] Cleaning and stemming text corpus...")
    df['clean_content'] = df['combined_content'].apply(clean_text)

    # Filter out empty entries
    df = df[df['clean_content'].str.strip() != ''].reset_index(drop=True)
    return df


def train_models():
    """Trains, compares multiple models, and exports the top performer."""
    os.makedirs(MODEL_DIR, exist_ok=True)
    df = load_and_preprocess_data()

    X = df['clean_content']
    y = df['label']

    # 80-20 Train-Test split with stratification
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print("\n[INFO] Vectorizing text with TF-IDF (Unigrams + Bigrams, max_features=5000)...")
    tfidf = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        sublinear_tf=True
    )

    X_train = tfidf.fit_transform(X_train_raw)
    X_test = tfidf.transform(X_test_raw)

    print(f" Vocabulary size: {len(tfidf.vocabulary_)} features.")

    # Candidate Classifiers
    models = {
        "Passive Aggressive Classifier": PassiveAggressiveClassifier(
            max_iter=1000,
            C=0.5,
            random_state=42
        ),
        "Logistic Regression": LogisticRegression(
            C=1.0,
            max_iter=1000,
            random_state=42
        ),
        "Multinomial Naive Bayes": MultinomialNB(alpha=0.5),
        "Random Forest Classifier": RandomForestClassifier(
            n_estimators=100,
            max_depth=20,
            random_state=42
        )
    }

    all_metrics = []
    best_model_name = None
    best_f1 = -1.0
    best_fitted_model = None

    print("\n" + "=" * 60)
    print("           TRAINING & BENCHMARKING MODELS                  ")
    print("=" * 60)

    for name, clf in models.items():
        print(f"\n[Training] {name}...")
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        # 5-Fold Cross Validation on Training set
        cv_scores = cross_val_score(clf, X_train, y_train, cv=5, scoring='accuracy')
        cv_mean = round(float(np.mean(cv_scores)) * 100, 2)

        metrics = evaluate_model_performance(y_test, y_pred, model_name=name)
        metrics["5-Fold CV Accuracy"] = cv_mean
        all_metrics.append(metrics)

        print_evaluation_summary(metrics)
        print(f"5-Fold CV Mean Accuracy: {cv_mean}%\n")

        if metrics["F1-Score"] > best_f1:
            best_f1 = metrics["F1-Score"]
            best_model_name = name
            best_fitted_model = clf

    print("=" * 60)
    print(f" WINNER: {best_model_name} (F1-Score: {best_f1}%)")
    print("=" * 60)

    # Save Top Model, Vectorizer, and Metrics JSON
    print(f"[INFO] Saving best model to {MODEL_PATH}...")
    joblib.dump(best_fitted_model, MODEL_PATH)

    print(f"[INFO] Saving TF-IDF vectorizer to {VECTORIZER_PATH}...")
    joblib.dump(tfidf, VECTORIZER_PATH)

    # Convert metrics for JSON serialization
    serialized_metrics = {
        "best_model": best_model_name,
        "models_evaluated": all_metrics
    }
    with open(METRICS_PATH, "w") as f:
        json.dump(serialized_metrics, f, indent=4)

    print(f"[INFO] Metrics saved to {METRICS_PATH}")
    print("[SUCCESS] Training pipeline complete!")
    return best_fitted_model, tfidf, all_metrics


if __name__ == "__main__":
    train_models()
