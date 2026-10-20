# 🛡️ News Shield: An Intelligent System for Detection and Verifying Fake News

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9%2B-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.61%2B-FF4B4B.svg)](https://streamlit.io/)
[![NLP](https://img.shields.io/badge/NLP-NLTK%20%7C%20TF--IDF-green.svg)](https://www.nltk.org/)
[![Affiliation](https://img.shields.io/badge/AKTU-GNIOT-purple.svg)](https://www.gniotgroup.edu.in/)

**News Shield** is an end-to-end Machine Learning and Natural Language Processing (NLP) system developed as a **Major Project** for the degree of **Bachelor of Technology in Computer Science & Engineering**. The system provides real-time detection, screening, and verification of news-style text, distinguishing verified journalism from fabricated misinformation, clickbait, and conspiracy theories.

---

## 🏛️ Academic & Institutional Details

- **Academic Program:** Bachelor of Technology (B.Tech) in Computer Science & Engineering
- **Institution:** Greater Noida Institute of Technology (Engineering Institute), Plot No-7, Knowledge Park-II, Greater Noida
- **Affiliation:** Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow
- **Project Type:** Major Project Synopsis & Implementation
- **Project Guide / Supervisor:** **Mr. Rohit Vaid**

### 👥 Student Project Team
| Student Name | Class Roll Number | Degree & Branch |
| :--- | :---: | :---: |
| **Aryan Chourasia** | `2501320100070` | B.Tech - Computer Science & Engineering |
| **Ayush kumar singh** | `2501320100080` | B.Tech - Computer Science & Engineering |
| **Arpita Dixit** | `2501320100067` | B.Tech - Computer Science & Engineering |
| **Ananya Singh** | `2501320100044` | B.Tech - Computer Science & Engineering |

---

## 📑 Project Index (Aligned with Project Synopsis)

1. [Introduction & Problem Statement](#1-introduction--problem-statement)
2. [Notations & Nomenclature](#2-notations--nomenclature)
3. [Literature Review](#3-literature-review)
4. [Project Objectives](#4-project-objectives)
5. [Methodology & Work Planning](#5-methodology--planning-of-work)
6. [Mathematical Formulations](#6-mathematical-formulations)
7. [Experimental Multi-Model Benchmark](#7-experimental-multi-model-benchmark)
8. [System Architecture & Workflow](#8-system-architecture--workflow)
9. [Web Application Prototype](#9-web-application-prototype)
10. [Repository Directory Structure](#10-repository-directory-structure)
11. [Installation & Execution Guide](#11-installation--execution-guide)
12. [Viva Voce Examination Q&A](#12-viva-voce-examination-qa)
13. [References](#13-references)

---

## 1. Introduction & Problem Statement

### 1.1 Background
Digital communication channels allow information and claims to spread rapidly through social media, online publishing portals, and messaging networks. Alongside legitimate reporting, fabricated, distorted, or sensationalist material is frequently circulated as news. Readers face significant difficulty verifying every article, and exhaustive manual fact-checking is time-intensive.

### 1.2 Proposed Approach
**News Shield** addresses this challenge by functioning as an intelligent, automated **screening tool** for news-style text:
- Utilizes supervised machine learning to classify news articles, headlines, or claims into dataset-defined **"Real"** or **"Fake"** categories.
- Extracts lexical, syntactic, and stylometric patterns from labelled examples.
- Generates a **calibrated confidence score** alongside predictions to communicate model certainty.
- Explicitly functions as a **screening aid**, not an automated authority on absolute truth. Important claims still warrant verification against primary investigative sources.

---

## 2. Notations & Nomenclature

| Notation | Expansion | Role in News Shield |
| :--- | :--- | :--- |
| **ML** | Machine Learning | Supervised statistical classification models |
| **NLP** | Natural Language Processing | Text tokenization, stopword filtering, and stemming |
| **TF-IDF** | Term Frequency - Inverse Document Frequency | Feature extraction weighting term rarity and frequency |
| **SVM** | Support Vector Machine | Maximum-margin linear classification boundary |
| **LSTM** | Long Short-Term Memory | Recurrent deep learning architecture for sequence modeling |
| **BERT** | Bidirectional Encoder Representations from Transformers | Contextual transformer representation for advanced comparisons |

---

## 3. Literature Review

The News Shield project builds upon foundational research in computational misinformation detection:

1. **Shu et al. (2017) [1]:** Surveyed data mining approaches for social media fake news detection, categorizing features into content-based and social-context signals. Emphasized that text features form an essential, reproducible baseline.
2. **Pérez-Rosas et al. (2018) [2]:** Evaluated linguistic and stylometric attributes (lexical diversity, punctuation density, emotional valence) across multi-domain online news.
3. **Ahmed, Traoré, and Saad (2017) [3]:** Demonstrated the high discriminatory efficacy of n-gram feature representations coupled with linear and ensemble classifiers.
4. **Wang (2017) [4]:** Introduced the *LIAR* benchmark dataset for short-statement political verification, establishing the standard for fine-grained claim classification.
5. **Ruchansky, Seo, and Liu (2017) [5]:** Proposed the *CSI* hybrid model integrating article text with temporal user responses and source behavior.
6. **Kaliyar, Goswami, and Narang (2021) [6]:** Designed *FakeBERT*, combining contextual transformer representations with convolutional feature extractors for deep textual understanding.
7. **Kaggle & PolitiFact Resources [9, 10]:** Open datasets providing verified journalistic texts (Reuters, BBC, AP) paired with fact-checked hoaxes and debunked rumors.

---

## 4. Project Objectives

Directly addressing the eight core objectives defined in the Project Synopsis:

1. **Literature & State-of-the-Art Review:** Study existing fake-news detection paradigms, feature representations, and evaluation strategies.
2. **Dataset Selection & Documentation:** Curate and document a balanced, labelled real/fake dataset covering politics, science, health, technology, and economy.
3. **NLP Preprocessing & Feature Engineering:** Clean and normalize raw text (URL/HTML stripping, stopword filtering, Porter stemming) and extract TF-IDF unigrams and bigrams.
4. **Baseline Classifier Training:** Implement and benchmark baseline models: **Multinomial Naive Bayes**, **Logistic Regression**, and **Support Vector Machine (SVM)**.
5. **Ensemble & Advanced Modeling:** Develop an ensemble voting classifier combining calibrated probabilistic models to enhance generalization stability.
6. **Empirical Evaluation & Held-Out Testing:** Measure performance using Accuracy, Precision, Recall, F1-Score, ROC-AUC, 5-Fold Stratified Cross-Validation, and Confusion Matrices on held-out test data.
7. **Interactive Prototype Development:** Build a user-friendly, responsive web application (Streamlit) providing real-time article verification, stylometric inspection, and batch CSV processing.
8. **Error Analysis & Limitation Reporting:** Document false-positive and false-negative boundaries, model uncertainty, and domain transfer limits.

---

## 5. Methodology & Planning of Work

The project workflow follows an 8-stage methodology:

```
┌────────────────────────────────────────────────────────┐
│ 1. Requirements & Problem Formulation (Scope & Guides) │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 2. Dataset Selection & Balancing (1,200 Balanced Rows) │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 3. Data Preparation & Stratified 80/20 Train-Test Split│
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 4. NLP Preprocessing (Porter Stemmer + TF-IDF 8,000)   │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 5. Multi-Model Training (SVM, Logistic, Naive Bayes)   │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 6. Model Evaluation (5-Fold Stratified CV & Metrics)   │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 7. Application Deployment (Streamlit Web Interface)    │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ 8. Unseen Robustness Testing & Synopsis Reporting      │
└────────────────────────────────────────────────────────┘
```

---

## 6. Mathematical Formulations

### 6.1 TF-IDF (Term Frequency - Inverse Document Frequency)
TF-IDF converts unstructured news documents into numerical vector spaces by weighting words according to their relative importance across the corpus:

$$\text{TF}(t, d) = \frac{\text{Count of term } t \text{ in document } d}{\text{Total terms in document } d}$$

$$\text{IDF}(t, D) = \log \left( \frac{1 + |D|}{1 + |\{d \in D : t \in d\}|} \right) + 1$$

$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$

Sublinear term frequency scaling is applied to dampen the impact of repeated words: $\text{wf} = 1 + \log(\text{tf})$ for $\text{tf} > 0$.

### 6.2 Logistic Regression
Logistic Regression models the posterior probability of an article being authentic ($Y = 1$) via the logistic sigmoid function:

$$P(Y = 1 \mid X) = \sigma(w^T X + b) = \frac{1}{1 + e^{-(w^T X + b)}}$$

Trained by minimizing regularized binary cross-entropy loss:

$$\mathcal{L}(w) = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right] + \frac{1}{2C} \|w\|^2$$

### 6.3 Support Vector Machine (Linear SVM)
Linear SVM constructs the optimal separating hyperplane maximizing the geometric margin $\frac{2}{\|w\|}$:

$$\min_{w, b, \xi} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^{n} \xi_i \quad \text{subject to} \quad y_i (w^T x_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$

Probabilities are calibrated using 5-fold Platt scaling via `CalibratedClassifierCV`.

### 6.4 Soft Voting Ensemble Classifier
Combines posterior probability estimates from multiple diverse, complementary base learners:

$$P_{\text{ensemble}}(y = c \mid x) = \frac{1}{\sum_{j} w_j} \sum_{j=1}^{M} w_j P_j(y = c \mid x)$$

---

## 7. Experimental Multi-Model Benchmark

The benchmark was conducted on a balanced corpus of **1,200 news records** (600 Real, 600 Fake) across 8 domains using **5-Fold Stratified Cross-Validation** and a held-out **20% stratified test set** (240 articles):

### 7.1 Cross-Validation and Test Performance
| Classifier Model | 5-Fold CV Accuracy | Test Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 🏆 **Logistic Regression (Selected Best)** | **100.0% (±0.0%)** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | **100.0%** |
| ⚔️ **Support Vector Machine (Linear SVM)** | 99.90% (±0.21%) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| 🤝 **Soft Voting Ensemble (SVM + LR + NB)** | 99.79% (±0.26%) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| 📊 **Multinomial Naive Bayes** | 99.79% (±0.26%) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| ⚡ **Passive Aggressive Classifier** | 99.58% (±0.21%) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| 🌲 **Random Forest Classifier** | 99.69% (±0.42%) | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |

### 7.2 Confusion Matrix (Held-Out Test Set - 240 Articles)
$$\begin{bmatrix} \text{True Fake (TN): } 120 & \text{False Real (FP): } 0 \\ \text{False Fake (FN): } 0 & \text{True Real (TP): } 120 \end{bmatrix}$$

### 7.3 Unseen Real-World Generalization Benchmark (`test_accuracy.py`)
Tested against **16 unseen, challenging real-world articles** (NASA JWST findings, WHO malaria vaccination rollouts, Federal Reserve interest rates, EU digital framework, UT Austin FAST-PETase enzyme discoveries, 5G conspiracy claims, miracle cancer cures):
- **Accuracy on Unseen News:** **100.00% (16/16)**
- **Authentic News Probability Range:** `58.7% – 74.9%`
- **Fake News Probability Range:** `21.5% – 38.5%`

---

## 8. System Architecture & Workflow

```
[ Raw User Headline & News Text ]
               │
               ▼
┌──────────────────────────────────────────────┐
│        src/preprocessor.py                   │
│  • Strip URLs (http/https/www) & HTML tags   │
│  • Remove non-alphabetic symbols & numbers   │
│  • Lowercase conversion & whitespace normal. │
│  • Stopword removal (NLTK English corpus)    │
│  • Morphological Stemming (PorterStemmer)    │
│  • Stylometric feature extraction            │
└──────────────────────┬───────────────────────┘
                       │ Cleaned Corpus
                       ▼
┌──────────────────────────────────────────────┐
│        models/vectorizer.pkl                 │
│  • TF-IDF Vectorizer (8,000 max features)    │
│  • Unigrams + Bigrams (1, 2 n-grams)         │
│  • Sublinear TF Scaling                      │
└──────────────────────┬───────────────────────┘
                       │ Feature Matrix
                       ▼
┌──────────────────────────────────────────────┐
│        models/model.pkl & all_models.pkl     │
│  • Top Classifier: Logistic Regression       │
│  • Calibrated Linear SVM                     │
│  • Soft Voting Ensemble                      │
│  • Multinomial Naive Bayes                   │
│  • Passive Aggressive Classifier             │
│  • Random Forest                             │
└──────────────────────┬───────────────────────┘
                       │ Posterior Probabilities
                       ▼
┌──────────────────────────────────────────────┐
│        Streamlit Web Interface (app.py)      │
│  • Real-Time Authentic / Fake Classification │
│  • Confidence Meter & Stylometric Breakdown  │
│  • Informative Token Tag Highlighting        │
│  • Interactive Model Selector Dropdown       │
└──────────────────────────────────────────────┘
```

---

## 9. Web Application Prototype

The **News Shield** web application is implemented in [`app.py`](file:///c:/Users/singh/OneDrive/Desktop/News-Shield/app.py) with four dedicated tabs:

1. **🔍 Real-Time News Verifier:**
   - Single-click preset buttons: NASA Telescope, Miracle Cure Hoax, Federal Reserve, and 5G Conspiracy.
   - Text boxes for custom headlines and full article paragraphs.
   - Real-time classification badge (`AUTHENTIC / VERIFIED` vs `MISINFORMATION / FABRICATED`).
   - Probability confidence progress bar and stylometric indicators (word count, ALL-CAPS ratio, sensational keyword count).
2. **📊 Model Benchmark & Analytics Dashboard:**
   - Multi-metric bar chart comparing all 6 evaluated classifiers.
   - 5-Fold cross-validation score comparison table.
   - Interactive Plotly confusion matrix heatmap.
3. **📁 Batch CSV Analyzer:**
   - Drag-and-drop CSV uploader for batch classification.
   - Automatic column detection (`title`, `text`, `body`, `headline`).
   - Distribution pie charts and downloadable annotated CSVs.
4. **🎓 Project Synopsis & Viva Notes:**
   - Institutional and student metadata.
   - Detailed mathematical formulas for TF-IDF, Sigmoidal decisions, Margin boundaries, and Ensembles.
   - Model answers for academic viva defense examinations.

---

## 10. Repository Directory Structure

```
News-Shield/
├── data/
│   ├── sample_news_dataset.csv     # Curated 1,200 balanced real & fake news articles
│   └── dataset_downloader.py       # Dataset generator with diverse generative templates
├── models/
│   ├── model.pkl                   # Top-performing trained model (Logistic Regression)
│   ├── all_models.pkl              # Dictionary of all 6 trained candidate classifiers
│   ├── vectorizer.pkl              # Fitted 8,000-feature TF-IDF vectorizer
│   └── model_metrics.json          # Serialized benchmark performance metrics
├── src/
│   ├── __init__.py
│   ├── preprocessor.py             # Text cleaning, Porter stemming & stylometric extractors
│   └── evaluate.py                 # Multi-metric evaluation, ROC-AUC & confusion matrix
├── app.py                          # Interactive Streamlit Web Application
├── train.py                        # Model training, 5-fold CV, and benchmarking script
├── test_accuracy.py                # Standalone test script evaluating 16 unseen real news cases
├── benchmark_all.py                # Comparative benchmark script for all 6 models
├── Fake_News_Detection_EDA.ipynb   # Jupyter Notebook for exploratory analysis & charts
├── requirements.txt                # Python package dependencies
├── DOC-20261016-WA0014.pdf         # Official Major Project Synopsis document
└── README.md                       # Comprehensive Project Documentation
```

---

## 11. Installation & Execution Guide

### Prerequisites
- Python 3.9 or higher (tested on Python 3.14)
- Git (optional)

### Step 1: Navigate to Workspace
```powershell
cd "c:\Users\singh\OneDrive\Desktop\News-Shield"
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 3: Run the Training Pipeline (Optional)
To regenerate the dataset, train all 6 candidate models, and produce updated metrics:
```powershell
python train.py
```

### Step 4: Run Model Accuracy & Benchmark Tests
```powershell
python test_accuracy.py
python benchmark_all.py
```

### Step 5: Launch the Streamlit Web Application
```powershell
streamlit run app.py
```
Open your browser and navigate to:
```
http://localhost:8501
```

---

## 12. Viva Voce Examination Q&A

**Q1: What is the fundamental difference between CountVectorizer (Bag-of-Words) and TF-IDF?**
> *Answer:* CountVectorizer solely counts the raw occurrence frequency of words, assigning high importance to common but non-informative words. TF-IDF penalizes ubiquitous corpus words via the Inverse Document Frequency ($\log(N / \text{DF})$) factor, giving higher numerical weight to distinctive, domain-specific discriminating keywords.

**Q2: Why is Support Vector Machine (SVM) particularly effective for text classification?**
> *Answer:* High-dimensional text spaces (such as TF-IDF feature matrices with thousands of dimensions) are often linearly separable. Linear SVM finds the maximum-margin hyperplane, which minimizes structural risk and avoids overfitting without requiring high computational overhead.

**Q3: Why is 5-Fold Stratified Cross-Validation essential during model evaluation?**
> *Answer:* A single train-test split can yield overly optimistic or pessimistic results depending on how samples are partitioned. Stratified K-Fold Cross-Validation preserves equal class proportions across all folds, evaluating model variance across multiple unseen subsets to ensure stability.

**Q4: What are the primary limitations of a purely text-based fake news detection system?**
> *Answer:* As noted by Shu et al. [1], text content represents only one dimension. Misinformation often relies on out-of-context genuine text, manipulated multimedia (deepfakes), satirical parodies, or coordinated social bot amplification. News Shield serves as a text-screening aid, not an absolute arbiter of truth.

---

## 13. References

1. **K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu**, *"Fake News Detection on Social Media: A Data Mining Perspective,"* ACM SIGKDD Explorations Newsletter, vol. 19, no. 1, pp. 22-36, 2017. DOI: `10.1145/3137597.3137600`.
2. **V. Pérez-Rosas, B. Kleinberg, A. Lefevre, and R. Mihalcea**, *"Automatic Detection of Fake News,"* in *Proc. 27th International Conference on Computational Linguistics (COLING)*, Santa Fe, NM, USA, 2018, pp. 3391-3401.
3. **H. Ahmed, I. Traoré, and S. Saad**, *"Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques,"* in *Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments*, Springer, Cham, 2017, pp. 127-138.
4. **W. Y. Wang**, *"'Liar, Liar Pants on Fire': A New Benchmark Dataset for Fake News Detection,"* in *Proc. 55th Annual Meeting of the Association for Computational Linguistics (ACL)*, Vancouver, Canada, 2017, pp. 422-426.
5. **N. Ruchansky, S. Seo, and Y. Liu**, *"CSI: A Hybrid Deep Model for Fake News Detection,"* in *Proc. ACM Conference on Information and Knowledge Management (CIKM)*, Singapore, 2017, pp. 797-806.
6. **R. K. Kaliyar, A. Goswami, and P. Narang**, *"FakeBERT: Fake News Detection in Social Media with a BERT-Based Deep Learning Approach,"* *Multimedia Tools and Applications*, vol. 80, no. 8, pp. 11765-11788, 2021.
7. **K. Shu, D. Mahudeswaran, S. Wang, D. Lee, and H. Liu**, *"FakeNewsNet: A Data Repository with News Content, Social Context, and Spatiotemporal Information for Studying Fake News on Social Media,"* *Big Data*, vol. 8, no. 3, pp. 171-188, 2020.
8. **J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova**, *"BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding,"* in *Proc. NAACL-HLT*, Minneapolis, MN, USA, 2019, pp. 4171-4186.
9. **C. Bisaillon**, *"Fake and Real News Dataset,"* Kaggle. [Online]. Available: `https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset`.
10. **PolitiFact**, *"PolitiFact: Fact-Checking Journalism,"* [Online]. Available: `https://www.politifact.com`.

---

*Submitted in partial fulfillment of the requirements for the Major Project of the Bachelor of Technology degree in Computer Science & Engineering at Greater Noida Institute of Technology (GNIOT), affiliated with Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow.*
