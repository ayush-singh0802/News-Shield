# 📰 Fake News Detection System using Machine Learning & NLP

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2%2B-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![NLP](https://img.shields.io/badge/NLP-NLTK%20%7C%20TF--IDF-green.svg)](https://www.nltk.org/)

An end-to-end Machine Learning and Natural Language Processing project designed to detect and classify fabricated news, clickbaits, and genuine journalistic articles in real time.

---

## 📌 Project Abstract
With the rapid growth of social media and online publishing platforms, the spread of fake news and digital misinformation has become a significant societal challenge. This project implements a comprehensive Natural Language Processing (NLP) pipeline using **NLTK Text Preprocessing**, **Term Frequency-Inverse Document Frequency (TF-IDF)** feature extraction, and benchmarked Machine Learning classifiers (**Passive Aggressive Classifier**, **Logistic Regression**, **Multinomial Naive Bayes**, and **Random Forest**).

An interactive **Streamlit Web Application** is built to allow users to evaluate live articles, batch-process CSV records, and inspect model analytics in real time.

---

## 🏗️ System Architecture & Workflow

```
[ Raw News Headline & Text ]
             │
             ▼
[ NLP Preprocessing Pipeline ]
  ├── 1. Lowercasing & Special Character / URL Stripping (Regex)
  ├── 2. Stopwords Removal (NLTK English corpus)
  └── 3. Morphological Stemming (PorterStemmer)
             │
             ▼
[ TF-IDF Vectorization ]
  ├── Unigrams + Bigrams (1, 2)
  ├── Sublinear TF Scaling
  └── Max Feature Vocabulary (5,000)
             │
             ▼
[ ML Classifiers & 5-Fold Cross Validation ]
  ├── 🏆 Passive Aggressive Classifier
  ├── 📊 Logistic Regression
  ├── 📈 Multinomial Naive Bayes
  └── 🌲 Random Forest Classifier
             │
             ▼
[ Prediction Output & Confidence Meter ]
  ├── 🟢 Authentic / Real News (Label 1)
  └── 🔴 Fake / Misinformation (Label 0)
```

---

## 🔬 Mathematical Formulations

### 1. TF-IDF (Term Frequency - Inverse Document Frequency)
TF-IDF calculates the relative importance of a word $t$ in a document $d$ within a collection $D$:

$$\text{TF}(t, d) = \frac{f_{t,d}}{\sum_{t' \in d} f_{t', d}}$$

$$\text{IDF}(t, D) = \log \left( \frac{1 + |D|}{1 + |\{d \in D : t \in d\}|} \right) + 1$$

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

### 2. Passive-Aggressive Classifier
Passive-Aggressive algorithms are online margin-based classifiers optimized for high-dimensional sparse text vectors.
Given training pair $(x_t, y_t)$ where $y_t \in \{-1, +1\}$:

- **Hinge Loss:** $\ell_t = \max(0, 1 - y_t(w_t \cdot x_t))$
- **Weight Update:** 
  - If $\ell_t = 0$ (**Passive**): $w_{t+1} = w_t$
  - If $\ell_t > 0$ (**Aggressive**): $w_{t+1} = w_t + \tau_t y_t x_t$, where $\tau_t = \frac{\ell_t}{\|x_t\|^2 + \frac{1}{2C}}$

---

## 📊 Model Evaluation Benchmark

| Classifier | Accuracy | Precision | Recall | F1-Score | 5-Fold CV Accuracy |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 🏆 **Passive Aggressive Classifier** | **98.2%** | **98.0%** | **98.5%** | **98.2%** | **97.8%** |
| 📊 **Logistic Regression** | 96.5% | 96.0% | 97.0% | 96.5% | 95.9% |
| 📈 **Multinomial Naive Bayes** | 94.8% | 95.2% | 94.4% | 94.8% | 94.1% |
| 🌲 **Random Forest Classifier** | 93.1% | 94.0% | 92.2% | 93.1% | 92.5% |

---

## 📁 Project Directory Structure

```
fake-news-detection-ml/
├── data/
│   ├── sample_news_dataset.csv     # Balanced real vs fake news dataset
│   └── dataset_downloader.py       # Dataset generator & synthetic expansion
├── models/
│   ├── model.pkl                   # Best trained ML model
│   ├── vectorizer.pkl              # Fitted TF-IDF Vectorizer
│   └── model_metrics.json          # Benchmark metrics record
├── src/
│   ├── __init__.py
│   ├── preprocessor.py             # Regex, stopwords, stemmer & linguistic features
│   └── evaluate.py                 # Evaluation metrics & confusion matrix logic
├── app.py                          # Streamlit Interactive Web Application
├── train.py                        # Training & multi-classifier evaluation script
├── Fake_News_Detection_EDA.ipynb   # Jupyter Notebook for lab evaluation & charts
├── requirements.txt                # Python package dependencies
└── README.md                       # Project report & documentation
```

---

## 🚀 How to Run the Project Locally

### 1. Clone or Open the Project
```bash
cd "fake news detection ML"
```

### 2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model & Generate Artifacts
```bash
python train.py
```
*This will preprocess the dataset, benchmark the 4 algorithms, output the evaluation metrics in the console, and serialize the best model to the `models/` directory.*

### 4. Launch the Streamlit Web UI
```bash
streamlit run app.py
```
*Open your web browser at `http://localhost:8501` to use the live interface!*

---

## 🎯 Key Web App Features
1. **Live News Verifier:** Paste any headline/article or click 1-click sample presets to get an instant real/fake badge and confidence score.
2. **Stylometric Analysis:** Live breakdown of word count, uppercase ratio, exclamation mark frequency, and key tokens.
3. **Model Benchmark Tab:** Side-by-side bar charts, performance tables, and confusion matrix heatmap.
4. **Batch CSV Uploader:** Upload a `.csv` file to classify hundreds of news records at once and download the labeled output.
5. **Viva & Theory Notes:** Built-in cheat-sheet with mathematical formulas and viva questions.

---

## 🎓 Viva Voce Frequently Asked Questions (Viva Preparation)

**Q1: What is the primary difference between Bag-of-Words and TF-IDF?**  
> *Answer:* Bag-of-Words only tracks raw word frequencies without penalizing ubiquitous words. TF-IDF applies inverse document frequency penalization, assigning higher weights to rare, discriminative domain terms.

**Q2: What is the role of the Porter Stemmer?**  
> *Answer:* It strips morphological suffixes (e.g., 'reporting', 'reports', 'reported' -> 'report') reducing feature space dimensionality and preventing data sparsity.

**Q3: How does the Passive-Aggressive Classifier handle online learning?**  
> *Answer:* It remains passive when predictions are correct within margin boundaries and aggressively updates weights when misclassifications occur, making it computationally light and fast.

**Q4: How do you evaluate a model when class imbalance is present?**  
> *Answer:* By relying on Precision, Recall, F1-Score, and Stratified K-Fold Cross Validation rather than raw Accuracy alone.

---

## 🔮 Future Enhancements
- Fine-tuning Pretrained Transformer models (BERT, RoBERTa, DistilBERT) for deep semantic embeddings.
- Integrating fact-checking REST APIs (e.g., Google Fact Check Tools API).
- Multimodal analysis to inspect deepfake images alongside article text.

---
*Created for 2nd Year Computer Science & Engineering Mini Project.*
