"""
News Shield - Model Training & Benchmarking Pipeline
Author: News Shield Project Team (GNIOT / AKTU)
Supervisor: Mr. Rohit Vaid

Evaluates candidate classifiers matching Project Synopsis Objectives:
1. Support Vector Machine (Linear SVM with probability calibration)
2. Logistic Regression (L2-regularized linear baseline)
3. Multinomial Naive Bayes (probabilistic NLP baseline)
4. Passive Aggressive Classifier (online streaming classifier)
5. Random Forest Classifier (ensemble decision trees)
6. Soft Voting Ensemble (combines top models for highest generalization)
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier

from src.preprocessor import clean_text
from src.evaluate import evaluate_model_performance, print_evaluation_summary
from data.dataset_downloader import create_dataset, DATASET_PATH

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
ALL_MODELS_PATH = os.path.join(MODEL_DIR, "all_models.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
METRICS_PATH = os.path.join(MODEL_DIR, "model_metrics.json")


def load_and_preprocess_data():
    """Loads dataset and applies NLP preprocessing."""
    if not os.path.exists(DATASET_PATH):
        print("[INFO] Dataset not found, generating comprehensive dataset...")
        df = create_dataset()
    else:
        df = pd.read_csv(DATASET_PATH)

    print(f"[INFO] Loaded {len(df)} news articles from {DATASET_PATH}")

    # Combine Title and Text for rich contextual representation
    df['combined_content'] = df['title'].fillna('') + ' ' + df['text'].fillna('')

    print("[INFO] Cleaning and stemming text corpus using Porter Stemmer...")
    df['clean_content'] = df['combined_content'].apply(clean_text)

    # Filter out empty entries
    df = df[df['clean_content'].str.strip() != ''].reset_index(drop=True)
    return df


def train_models():
    """Trains, compares multiple models, and exports top performers."""
    os.makedirs(MODEL_DIR, exist_ok=True)
    df = load_and_preprocess_data()

    X = df['clean_content']
    y = df['label']

    # 80-20 Train-Test split with stratification
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    print("\n[INFO] Vectorizing text with TF-IDF (Unigrams + Bigrams, max_features=8000)...")
    tfidf = TfidfVectorizer(
        max_features=8000,
        ngram_range=(1, 2),
        sublinear_tf=True,
        min_df=2,
        max_df=0.98,
        strip_accents='unicode'
    )

    X_train = tfidf.fit_transform(X_train_raw)
    X_test = tfidf.transform(X_test_raw)

    print(f" Vocabulary size: {len(tfidf.vocabulary_)} features.")

    # 1. Base Classifiers
    svm_base = LinearSVC(C=1.0, random_state=42, max_iter=2000)
    svm_calibrated = CalibratedClassifierCV(svm_base, cv=5)
    
    lr = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    nb = MultinomialNB(alpha=0.2)
    pac = PassiveAggressiveClassifier(max_iter=1000, C=0.5, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, max_depth=25, random_state=42)

    # 2. Ensemble Voting Classifier
    voting_ensemble = VotingClassifier(
        estimators=[
            ('svm', svm_calibrated),
            ('lr', lr),
            ('nb', nb)
        ],
        voting='soft'
    )

    candidate_models = {
        "Ensemble Classifier (Soft Voting)": voting_ensemble,
        "Support Vector Machine (Linear SVM)": svm_calibrated,
        "Logistic Regression": lr,
        "Passive Aggressive Classifier": pac,
        "Multinomial Naive Bayes": nb,
        "Random Forest Classifier": rf
    }

    all_metrics = []
    best_model_name = None
    best_f1 = -1.0
    best_score = -1.0
    best_fitted_model = None
    fitted_models = {}

    print("\n" + "=" * 65)
    print("      TRAINING & BENCHMARKING MULTIPLE ML CLASSIFIERS        ")
    print("=" * 65)

    cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    for name, clf in candidate_models.items():
        print(f"\n[Training] {name}...")
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        # Predict probability for ROC-AUC
        y_prob = None
        if hasattr(clf, "predict_proba"):
            y_prob = clf.predict_proba(X_test)[:, 1]
        elif hasattr(clf, "decision_function"):
            df_val = clf.decision_function(X_test)
            y_prob = 1 / (1 + np.exp(-df_val))

        # 5-Fold Stratified Cross Validation on Training set
        cv_scores = cross_val_score(clf, X_train, y_train, cv=cv_strategy, scoring='accuracy')
        cv_mean = round(float(np.mean(cv_scores)) * 100, 2)
        cv_std = round(float(np.std(cv_scores)) * 100, 2)

        metrics = evaluate_model_performance(y_test, y_pred, y_prob=y_prob, model_name=name)
        metrics["5-Fold CV Accuracy"] = cv_mean
        metrics["5-Fold CV Std"] = cv_std
        all_metrics.append(metrics)
        fitted_models[name] = clf

        print_evaluation_summary(metrics)
        print(f"  5-Fold CV Accuracy: {cv_mean}% (+/- {cv_std}%)\n")

        # Rank by Cross-Validation Mean Accuracy + Test F1-Score
        # Prefer models with native predict_proba for smooth probability estimates
        has_proba_bonus = 0.5 if hasattr(clf, "predict_proba") else 0.0
        score = (metrics["F1-Score"] * 0.5) + (cv_mean * 0.5) + has_proba_bonus

        if score > best_score:
            best_score = score
            best_f1 = metrics["F1-Score"]
            best_model_name = name
            best_fitted_model = clf

    print("=" * 65)
    print(f" WINNER: {best_model_name} (F1-Score: {best_f1}%)")
    print("=" * 65)

    # Save Top Model, All Models, Vectorizer, and Metrics JSON
    print(f"[INFO] Saving best model ({best_model_name}) to {MODEL_PATH}...")
    joblib.dump(best_fitted_model, MODEL_PATH)

    print(f"[INFO] Saving all trained candidate models to {ALL_MODELS_PATH}...")
    joblib.dump(fitted_models, ALL_MODELS_PATH)

    print(f"[INFO] Saving TF-IDF vectorizer to {VECTORIZER_PATH}...")
    joblib.dump(tfidf, VECTORIZER_PATH)

    serialized_metrics = {
        "best_model": best_model_name,
        "models_evaluated": all_metrics
    }
    with open(METRICS_PATH, "w") as f:
        json.dump(serialized_metrics, f, indent=4)

    print(f"[INFO] Metrics saved to {METRICS_PATH}")
    print("[SUCCESS] Model training and evaluation completed successfully!")
    return best_fitted_model, tfidf, all_metrics


if __name__ == "__main__":
    train_models()
