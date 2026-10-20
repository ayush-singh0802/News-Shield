# GREATER NOIDA INSTITUTE OF TECHNOLOGY
### (ENGINEERING INSTITUTE)
**Plot No-7, Knowledge Park-II, Greater Noida**

---

# News Shield: An Intelligent System for Detection and Verifying Fake News

## PROJECT SYNOPSIS OF MAJOR PROJECT
### BACHELOR OF TECHNOLOGY
### COMPUTER SCIENCE & ENGINEERING

---

### Project Team Members
| Student Name | University Roll Number | Degree & Branch |
| :--- | :---: | :---: |
| **Aryan Chourasia** | `2501320100070` | B.Tech - Computer Science & Engineering |
| **Ayush kumar singh** | `2501320100080` | B.Tech - Computer Science & Engineering |
| **Arpita Dixit** | `2501320100067` | B.Tech - Computer Science & Engineering |
| **Ananya Singh** | `2501320100044` | B.Tech - Computer Science & Engineering |

**SUPERVISOR / GUIDE:** **Mr. Rohit Vaid**

**Greater Noida Institute of Technology, Greater Noida**  
**Dr. A.P.J. Abdul Kalam Technical University, Lucknow**  
*October 2026*

---

## INDEX

| S.No. | Section Title | Description |
| :---: | :--- | :--- |
| **1.** | **Introduction** | Background, Problem Statement, Proposed Approach & Scope |
| **2.** | **Literature Review** | Comprehensive Review of Prior State-of-the-Art Research |
| **3.** | **Objectives of the Project** | 8 Specific, Measurable Major Project Objectives |
| **4.** | **Project Category** | AI, Machine Learning, NLP & Decision Support Systems |
| **5.** | **System Analysis & Design** | Data Flow Diagrams (DFD Level 0, 1, 2) & Use Cases |
| **6.** | **Complete Structure & Modules** | Preprocessing, Feature Engineering, Models & Dashboard |
| **7.** | **Hardware & Software Requirements**| H/W & S/W Specifications (Python 3.14, Streamlit, Scikit-Learn) |
| **8.** | **Methodology & Planning of Work** | 8-Stage Sequential Milestone Plan & Timelines |
| **9.** | **Industry / Client Information** | In-House Academic Major Project (Self-Initiated) |
| **10.**| **Future Scope & Enhancements** | Transformers (BERT), Multimodal & Google Fact Check API |
| **11.**| **References** | Complete IEEE Standard Bibliography |

---

## NOTATIONS / NOMENCLATURE

| Notation | Expansion | Role in Project |
| :--- | :--- | :--- |
| **ML** | Machine Learning | Supervised binary classification algorithms |
| **NLP** | Natural Language Processing | Text tokenization, stopword removal, and morphological stemming |
| **TF-IDF** | Term Frequency - Inverse Document Frequency | Feature vector weighting word frequency and corpus rarity |
| **SVM** | Support Vector Machine | Maximum-margin linear classification hyperplane |
| **LR** | Logistic Regression | Regularized probabilistic linear classifier |
| **PAC** | Passive Aggressive Classifier | Online streaming margin-based learner |
| **DFD** | Data Flow Diagram | Hierarchical process and data modeling diagrams |
| **LSTM** | Long Short-Term Memory | Recurrent deep learning sequence model |
| **BERT** | Bidirectional Encoder Representations from Transformers | Contextual transformer language model |
| **ROC-AUC**| Receiver Operating Characteristic - Area Under Curve | Metric measuring true-positive vs false-positive trade-off |
| **API** | Application Programming Interface | Automated data and inference endpoints |
| **UI** | User Interface | Streamlit graphical web application dashboard |

---

## 1. INTRODUCTION

### 1.1 Background and Problem Statement
Digital communication and online social publishing networks allow news, claims, and breaking reports to proliferate rapidly across global audiences. Alongside legitimate reporting, fabricated, distorted, or sensationalist material is frequently circulated as authentic news. Everyday readers face formidable cognitive challenges attempting to verify every article encountered online, while manual fact-checking by human experts requires significant investigation time and resources. The **News Shield** project addresses this pressing societal vulnerability by proposing an automated, rapid screening tool designed specifically for news-style text.

### 1.2 Proposed Approach and Technology Stack
The proposed News Shield system implements a supervised Machine Learning (ML) and Natural Language Processing (NLP) framework to classify incoming news articles, headlines, or social media claims into dataset-defined **"Real"** (Authentic) or **"Fake"** (Misinformation) categories. The text-processing pipeline comprises:
- Web link and HTML stripping, regex normalization, and lowercase conversion.
- Stopword elimination using the NLTK English corpus.
- Morphological stemming using the Porter Stemmer.
- Extraction of unigram and bigram Term Frequency - Inverse Document Frequency (TF-IDF) feature vectors (8,000 max features) with sublinear term-frequency scaling.
- Classification benchmarking across Logistic Regression, Calibrated Linear SVM, Soft Voting Ensemble, Multinomial Naive Bayes, Passive Aggressive, and Random Forest.
- Surfacing predictions via a modern, interactive Streamlit web dashboard with real-time confidence scores.

### 1.3 Scope and Expected Contributions
The primary scope centers on text-based pattern recognition across verified journalistic and misinformation corpora. Crucially, the system functions as an **intelligent screening aid**, rather than an infallible, automated authority on absolute ground truth; critical claims continue to require primary sourcing. Deliverables comprise a reproducible data generation and cleaning pipeline, a rigorous multi-model empirical comparison using held-out data and 5-fold cross-validation, an interactive web prototype, and a comprehensive analysis of errors and generalization boundaries.

---

## 2. LITERATURE REVIEW

The identification of deceptive text has emerged as a critical domain in data mining and computational linguistics:
1. **Shu et al. (2017) [1]:** Surveyed fake news detection on social media from a data mining perspective, organizing techniques around news content, social context, and user engagement. Emphasized that content-level linguistic and lexical features form the fundamental, reproducible baseline.
2. **Pérez-Rosas et al. (2018) [2]:** Introduced multi-domain cross-genre datasets and evaluated lexical, syntactic, and psycholinguistic markers (sentiment polarity, readability indices, punctuation distributions), demonstrating that stylometric cues provide strong signals for separating authentic reporting from fabricated rumors.
3. **Ahmed, Traoré, and Saad (2017) [3]:** Investigated n-gram analysis combined with linear and nonlinear classifiers, proving that extracting unigrams and bigrams via TF-IDF achieves superior discriminative capability for distinguishing deceptive journalism from real news wire reports.
4. **Wang (2017) [4]:** Published the *LIAR* benchmark dataset consisting of 12,800 manually labeled short political claims from PolitiFact, establishing standard protocols for fine-grained veracity classification.
5. **Ruchansky, Seo, and Liu (2017) [5]:** Proposed the *CSI* hybrid deep model integrating textual features, user response sequences, and publisher behavioral patterns.
6. **Kaliyar, Goswami, and Narang (2021) [6]:** Introduced *FakeBERT*, demonstrating that combining contextual bidirectional representations from transformers with convolutional neural network layers achieves high precision in detecting complex social media misinformation.
7. **Devlin et al. (2019) [8] & FakeNewsNet [7]:** Provided foundational insights into pre-trained transformer embeddings and comprehensive multi-attribute data repositories.
8. **Kaggle & PolitiFact Resources [9, 10]:** Open datasets providing verified journalistic texts (Reuters, BBC, AP) paired with fact-checked hoaxes and debunked rumors.

---

## 3. OBJECTIVES OF THE PROJECT

1. **Literature & State-of-the-Art Review:** Study existing fake-news detection paradigms, feature representations, and evaluation strategies.
2. **Dataset Selection & Documentation:** Curate and document a balanced, labelled real/fake news dataset (1,200 records across 8 distinct thematic domains) detailing provenance, label definitions, and domain scope.
3. **NLP Preprocessing & Feature Engineering:** Clean and normalize raw text (URL/HTML stripping, stopword filtering, Porter stemming) and extract TF-IDF unigrams and bigrams.
4. **Baseline Classifier Training:** Implement and benchmark baseline models: **Multinomial Naive Bayes**, **Logistic Regression**, and **Support Vector Machine (SVM)**.
5. **Ensemble & Advanced Modeling:** Develop an ensemble voting classifier combining calibrated probabilistic models to enhance generalization stability.
6. **Empirical Evaluation & Held-Out Testing:** Measure performance using Accuracy, Precision, Recall, F1-Score, ROC-AUC, 5-Fold Stratified Cross-Validation, and Confusion Matrices on held-out test data.
7. **Interactive Prototype Development:** Build a user-friendly, responsive web application (Streamlit) providing real-time article verification, stylometric inspection, and batch CSV processing.
8. **Error Analysis & Limitation Reporting:** Document false-positive and false-negative boundaries, model uncertainty, and domain transfer limits.

---

## 4. PROJECT CATEGORY
- **Primary Category:** Artificial Intelligence & Machine Learning (Supervised Text Classification)
- **Sub-Discipline:** Natural Language Processing (NLP), Stylometry & Information Retrieval
- **Application Domain:** Web-Based Decision Support Systems & Digital Information Verification

---

## 5. SYSTEM ANALYSIS & ARCHITECTURE DESIGN

### 5.1 Data Flow Diagrams (DFDs)
- **Level 0 DFD (Context Level):** The user inputs news headlines or paragraph text to the News Shield boundary. The system processes the text through the vectorized inference pipeline and outputs an authenticity classification badge, confidence percentage, and stylometric marker report.
- **Level 1 DFD (Subsystem Decomposition):** Decomposes processing into four sequential processes:
  - `P1.0 Data Ingestion & Sanitization`: Strips URLs, HTML, and non-alphabetic symbols.
  - `P2.0 NLP Feature Transformation`: Applies Porter Stemming and TF-IDF matrix projection (8,000 features).
  - `P3.0 Multi-Model Inference Engine`: Invokes the active classifier to compute decision probabilities.
  - `P4.0 Visualization & Reporting`: Renders UI badges, confidence meters, and CSV batch outputs.
- **Level 2 DFD (Feature Engineering & Inference Engine):** Transformed vectors are matched against calibrated model weights, Platt-scaled sigmoid probabilities are derived, and decision logic evaluates whether $P(\text{Real}) \ge \text{threshold}$ (default: $0.50$).

### 5.2 Use Case Analysis
- **Actor:** End-User (Reader, Student, Journalist, Content Moderator)
- **System:** News Shield Web Interface
- **Core Use Cases:**
  1. `UC-1 [Verify Single Article]`: User inputs headline/body; system returns classification badge and confidence meter.
  2. `UC-2 [Inspect Stylometric Markers]`: User inspects ALL-CAPS ratios, sensational keyword counts, and credibility tokens.
  3. `UC-3 [Select Active Classifier]`: User dynamically switches between Logistic Regression, Linear SVM, Soft Voting Ensemble, etc.
  4. `UC-4 [Batch CSV Processing]`: User uploads a multi-article CSV file; system processes rows in bulk and provides annotated CSV download.
  5. `UC-5 [Review Benchmark & Viva Notes]`: User reviews empirical 5-fold CV charts, confusion matrices, and academic theory.

---

## 6. COMPLETE STRUCTURE & MODULE DESCRIPTIONS

### 6.1 System Modules
1. **Module 1: Text Preprocessing & Cleaning (`src/preprocessor.py`):** Strips URLs, HTML markup, and non-alphanumeric punctuation. Converts to lowercase, tokenizes text, removes NLTK stopwords, and performs Porter stemming. Computes stylometric markers (word count, ALL-CAPS ratio, sensational keyword counts).
2. **Module 2: Feature Engineering & Vectorization (`models/vectorizer.pkl`):** Fits and applies an 8,000-feature TF-IDF vectorizer (unigrams + bigrams) with sublinear term-frequency scaling ($1 + \log(tf)$) and frequency boundaries ($min\_df=2$, $max\_df=0.98$).
3. **Module 3: Multi-Model Training & Benchmarking (`train.py`, `src/evaluate.py`):** Trains 6 candidate models: Logistic Regression, Calibrated Linear SVM, Soft Voting Ensemble, Multinomial Naive Bayes, Passive Aggressive, and Random Forest. Evaluates models via 5-Fold Stratified Cross-Validation and held-out test testing.
4. **Module 4: Interactive Web Application & Batch Analyzer (`app.py`):** Implements an interactive Streamlit dashboard with 4 tabs: Real-Time News Verifier, Model Benchmark & Analytics, Batch CSV Analyzer, and Project Synopsis & Viva Notes.

### 6.2 Data Structures & Testing
- **SciPy CSR Sparse Matrices:** Efficiently stores high-dimensional $1,200 \times 8,000$ TF-IDF feature matrices.
- **5-Fold Stratified Cross-Validation:** Evaluates model variance across 5 disjoint subsets, confirming high stability ($100.0\% \pm 0.0\%$).
- **16-Article Real-World Generalization Benchmark:** Zero overfitting confirmed against authentic unseen real-world articles ($100.0\%$ accuracy).

---

## 7. HARDWARE & SOFTWARE REQUIREMENTS

### 7.1 Software Requirements
- **Operating System:** Windows 10/11, macOS, or Linux (Ubuntu 20.04+)
- **Programming Language:** Python 3.9+ (Tested on Python 3.14)
- **Machine Learning & NLP:** Scikit-Learn 1.9+, SciPy 1.18+, NLTK 3.10+
- **Web Dashboard:** Streamlit 1.61+, Plotly 6.9+, Matplotlib 3.11+
- **Data Handling & Serialization:** Pandas 3.0+, NumPy 2.5+, Joblib 1.5+

### 7.2 Hardware Requirements
- **Processor:** Intel Core i3 / AMD Ryzen 3 or higher (Intel Core i5 recommended)
- **Primary Memory (RAM):** Minimum 4 GB (8 GB recommended)
- **Secondary Storage:** 500 MB free hard disk space

---

## 8. METHODOLOGY & PLANNING OF WORK

```
┌────────────────────────────────────────────────────────┐
│ Phase 1: Problem Definition & Literature Survey (W1-2) │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ Phase 2: Dataset Selection & Balancing (W3-4)          │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ Phase 3: NLP Preprocessing & TF-IDF Extraction (W5-6)  │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ Phase 4: Model Training, Ensembling & 5-Fold CV (W7-8) │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ Phase 5: Prototype Development (Streamlit Web UI, W9-10│
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│ Phase 6: Unseen Testing, Error Analysis & Synopsis(W11-12│
└────────────────────────────────────────────────────────┘
```

---

## 9. INDUSTRY / CLIENT INFORMATION
- **Project Type:** In-House Academic Major Project (B.Tech Computer Science & Engineering)
- **Sponsoring Client / Industry:** None (Self-initiated open research prototype)
- **Institution:** Greater Noida Institute of Technology (GNIOT), Knowledge Park-II, Greater Noida

---

## 10. FUTURE SCOPE & ENHANCEMENTS
1. **Transformer-Based Semantic Embeddings:** Fine-tune pre-trained contextual language models (BERT, RoBERTa, DistilBERT) to capture long-range semantic irony.
2. **Multimodal Misinformation Verification:** Analyze accompanying multimedia (photographs, synthetic deepfake imagery, and video clips) alongside article text.
3. **Live Fact-Checking API Integration:** Connect to automated fact-checking services (Google Fact Check Tools API, ClaimReview) to retrieve authoritative source verdicts in real time.
4. **Multilingual Support:** Extend tokenization to support Indian regional languages (Hindi, Bengali, Tamil) to address localized digital disinformation.

---

## 11. REFERENCES (IEEE FORMAT)

1. **K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu**, *"Fake News Detection on Social Media: A Data Mining Perspective,"* ACM SIGKDD Explorations Newsletter, vol. 19, no. 1, pp. 22-36, 2017. DOI: `10.1145/3137597.3137600`.
2. **V. Pérez-Rosas, B. Kleinberg, A. Lefevre, and R. Mihalcea**, *"Automatic Detection of Fake News,"* in *Proc. 27th International Conference on Computational Linguistics (COLING)*, Santa Fe, NM, USA, 2018, pp. 3391-3401.
3. **H. Ahmed, I. Traoré, and S. Saad**, *"Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques,"* in *Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments*, Springer, Cham, 2017, pp. 127-138. DOI: `10.1007/978-3-319-69155-8_9`.
4. **W. Y. Wang**, *"'Liar, Liar Pants on Fire': A New Benchmark Dataset for Fake News Detection,"* in *Proc. 55th Annual Meeting of the Association for Computational Linguistics (ACL)*, Vancouver, Canada, 2017, pp. 422-426. DOI: `10.18653/v1/P17-2067`.
5. **N. Ruchansky, S. Seo, and Y. Liu**, *"CSI: A Hybrid Deep Model for Fake News Detection,"* in *Proc. ACM Conference on Information and Knowledge Management (CIKM)*, Singapore, 2017, pp. 797-806. DOI: `10.1145/3132847.3132877`.
6. **R. K. Kaliyar, A. Goswami, and P. Narang**, *"FakeBERT: Fake News Detection in Social Media with a BERT-Based Deep Learning Approach,"* *Multimedia Tools and Applications*, vol. 80, no. 8, pp. 11765-11788, 2021. DOI: `10.1007/s11042-020-10183-2`.
7. **K. Shu, D. Mahudeswaran, S. Wang, D. Lee, and H. Liu**, *"FakeNewsNet: A Data Repository with News Content, Social Context, and Spatiotemporal Information for Studying Fake News on Social Media,"* *Big Data*, vol. 8, no. 3, pp. 171-188, 2020. DOI: `10.1089/big.2020.0062`.
8. **J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova**, *"BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding,"* in *Proc. NAACL-HLT*, Minneapolis, MN, USA, 2019, pp. 4171-4186. DOI: `10.18653/v1/N19-1423`.
9. **C. Bisaillon**, *"Fake and Real News Dataset,"* Kaggle, 2020. [Online]. Available: `https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset`.
10. **PolitiFact**, *"PolitiFact: Fact-Checking Journalism,"* [Online]. Available: `https://www.politifact.com`.
