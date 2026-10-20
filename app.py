"""
News Shield: An Intelligent System for Detection and Verifying Fake News
Interactive Web Application Built with Streamlit, Scikit-Learn & Plotly

Academic Project: Major Project, Bachelor of Technology (CSE)
Institution: Greater Noida Institute of Technology (GNIOT), Knowledge Park-II, Greater Noida
Affiliated to: Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow
Supervisor / Guide: Mr. Rohit Vaid
Project Team:
- Aryan Chourasia (2501320100070)
- Ayush kumar singh (2501320100080)
- Arpita Dixit (2501320100067)
- Ananya Singh (2501320100044)
"""

import os
import json
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from src.preprocessor import clean_text, extract_linguistic_features

# Streamlit Page Configuration
st.set_page_config(
    page_title="News Shield | Intelligent Fake News Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design & Modern Typography
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e3a8a 100%);
        color: white;
        padding: 30px 36px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 14px 34px rgba(15, 23, 42, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .main-header h1 {
        color: #ffffff !important;
        font-weight: 800;
        font-size: 2.3rem;
        letter-spacing: -0.02em;
        margin-bottom: 8px;
    }
    
    .main-header p {
        color: #cbd5e1 !important;
        font-size: 1.05rem;
        margin-bottom: 0px;
        line-height: 1.5;
    }
    
    .badge-real {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%);
        color: white;
        padding: 22px 28px;
        border-radius: 16px;
        font-size: 1.4rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 8px 24px rgba(16, 185, 129, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .badge-fake {
        background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%);
        color: white;
        padding: 22px 28px;
        border-radius: 16px;
        font-size: 1.4rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 8px 24px rgba(239, 68, 68, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .metric-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }
    
    .tag-token {
        display: inline-block;
        background: #f1f5f9;
        color: #334155;
        padding: 5px 12px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-family: 'JetBrains Mono', monospace;
        margin: 4px;
        font-weight: 500;
        border: 1px solid #e2e8f0;
    }
    
    .tag-real {
        background: #ecfdf5;
        color: #065f46;
        border: 1px solid #a7f3d0;
    }
    
    .tag-fake {
        background: #fef2f2;
        color: #991b1b;
        border: 1px solid #fecaca;
    }
    
    .team-badge {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 8px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
ALL_MODELS_PATH = os.path.join(MODEL_DIR, "all_models.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
METRICS_PATH = os.path.join(MODEL_DIR, "model_metrics.json")


@st.cache_resource
def load_project_artifacts():
    """Loads trained models, vectorizer, and evaluation benchmarks."""
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        with st.spinner("Training baseline & ensemble ML models... Please wait a few seconds."):
            from train import train_models
            train_models()

    default_model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    all_models = {}
    if os.path.exists(ALL_MODELS_PATH):
        all_models = joblib.load(ALL_MODELS_PATH)
    else:
        all_models = {"Default Best Model": default_model}

    metrics_data = None
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, "r") as f:
            metrics_data = json.load(f)

    return default_model, all_models, vectorizer, metrics_data


default_model, all_models, vectorizer, metrics_data = load_project_artifacts()

# ==========================================
# SIDEBAR: Project Meta & Settings
# ==========================================
with st.sidebar:
    st.markdown("## 🛡️ News Shield")
    st.caption("Major Project • B.Tech CSE")
    st.markdown("**Greater Noida Institute of Technology**")
    st.caption("Dr. A.P.J. Abdul Kalam Technical University, Lucknow")
    
    st.divider()
    
    # Model Selector
    st.markdown("### 🤖 Active ML Classifier")
    model_choices = list(all_models.keys())
    best_name = metrics_data.get("best_model", model_choices[0]) if metrics_data else model_choices[0]
    
    default_idx = model_choices.index(best_name) if best_name in model_choices else 0
    selected_model_name = st.selectbox(
        "Choose Model for Classification:",
        options=model_choices,
        index=default_idx,
        help="Select any of the 6 benchmarked classifiers evaluated according to Project Synopsis Objective 4."
    )
    active_model = all_models[selected_model_name]
    
    st.divider()

    # Decision Threshold
    st.markdown("### ⚙️ Decision Threshold")
    prediction_threshold = st.slider(
        "Probability Cutoff for 'Real News':",
        min_value=0.30,
        max_value=0.80,
        value=0.50,
        step=0.01,
        help="Standard neutral probability boundary is 0.50 (50%). Articles with P(Real) ≥ threshold are marked Authentic."
    )
    st.caption(f"Current threshold: **{prediction_threshold:.2%}** (Default: 50.00%)")
    
    st.divider()
    
    # Project Credits
    st.markdown("### 👥 Project Team")
    st.markdown("""
    <div class="team-badge">
        <strong>Aryan Chourasia</strong><br><span style="color:#64748b; font-size:0.8rem;">2501320100070</span>
    </div>
    <div class="team-badge">
        <strong>Ayush kumar singh</strong><br><span style="color:#64748b; font-size:0.8rem;">2501320100080</span>
    </div>
    <div class="team-badge">
        <strong>Arpita Dixit</strong><br><span style="color:#64748b; font-size:0.8rem;">2501320100067</span>
    </div>
    <div class="team-badge">
        <strong>Ananya Singh</strong><br><span style="color:#64748b; font-size:0.8rem;">2501320100044</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption(f"**Guide / Supervisor:** Mr. Rohit Vaid")

# ==========================================
# MAIN HEADER
# ==========================================
st.markdown("""
<div class="main-header">
    <h1>🛡️ News Shield: Intelligent Fake News Detection System</h1>
    <p>A supervised Machine Learning and Natural Language Processing architecture for identifying deceptive news, sensationalist clickbait, and authentic journalism with probabilistic explainability.</p>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Real-Time News Verifier",
    "📊 Model Benchmark & Analytics",
    "📁 Batch CSV Analyzer",
    "🎓 Project Synopsis & Viva Notes"
])

# ==========================================
# TAB 1: Real-Time News Verifier
# ==========================================
with tab1:
    st.subheader("📰 Test Article Authenticity")
    st.markdown("Paste an article headline and text below, or pick a curated sample to test:")

    # Quick Presets
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)

    presets = {
        "nasa": (
            "NASA James Webb Space Telescope Captures Deepest Image of Early Universe",
            "NASA's James Webb Space Telescope has produced the deepest and sharpest infrared image of the distant universe to date. Known as Webb's First Deep Field, this image of galaxy cluster SMACS 0723 is overflowing with detail. Thousands of galaxies – including the faintest objects ever observed – have appeared in infrared."
        ),
        "miracle_herb": (
            "Miracle Plant from Amazon Rainforest Cures All Types of Cancer in 48 Hours!",
            "Big Pharma is in a state of absolute PANIC! A secret leaf discovered by an underground herbalist destroys 100% of cancer tumors overnight without chemotherapy or radiation. Doctors are forbidden by corrupt pharmaceutical executives from revealing this miracle remedy! Order your emergency bottle today!"
        ),
        "central_bank": (
            "Central Bank Holds Benchmark Interest Rates Steady Amid Stable Labor Market Data",
            "The Federal Reserve held the policy interest rate steady at its monetary policy meeting, citing resilient nonfarm employment data and core inflation trending toward the two percent target. Chairman Powell reiterated that policy decisions remain dependent on cumulative macroeconomic indicators."
        ),
        "5g_conspiracy": (
            "BOMBSHELL LEAK: 5G Cell Towers Emit Secret Mind-Control Frequencies Tested by Cabal!",
            "Anonymous military whistleblowers leaked top-secret schematics proving that all newly installed 5G broadband antennas contain micro-transmitters designed to manipulate human cognitive frequencies and harvest citizens' private thoughts. Retweet and share before it is scrubbed!"
        )
    }

    def load_preset(key):
        title, text = presets[key]
        st.session_state["title_input"] = title
        st.session_state["text_input"] = text
        st.session_state["run_prediction"] = True

    col_s1.button("🪐 NASA Telescope (Real)", use_container_width=True, on_click=load_preset, args=("nasa",))
    col_s2.button("💉 Miracle Cure Hoax (Fake)", use_container_width=True, on_click=load_preset, args=("miracle_herb",))
    col_s3.button("📈 Federal Reserve (Real)", use_container_width=True, on_click=load_preset, args=("central_bank",))
    col_s4.button("📡 5G Mind Control (Fake)", use_container_width=True, on_click=load_preset, args=("5g_conspiracy",))

    # Form inputs
    title_input = st.text_input(
        "Headline / Title:",
        key="title_input",
        placeholder="e.g., Supreme Court Issues Ruling on Regulatory Clean Water Limits..."
    )
    text_input = st.text_area(
        "Article Body / Excerpt:",
        key="text_input",
        height=140,
        placeholder="Paste article body paragraph or summary text here..."
    )

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        submit_btn = st.button("🚀 Analyze Authenticity", type="primary", use_container_width=True)
    with col_btn2:
        st.caption(f"Currently analyzing with: **{selected_model_name}** | Threshold: **{prediction_threshold:.0%}**")

    should_predict = submit_btn or st.session_state.pop("run_prediction", False)

    if should_predict:
        if not title_input.strip() and not text_input.strip():
            st.warning("⚠️ Please provide a headline or article text to evaluate.")
        else:
            combined_raw = f"{title_input} {text_input}".strip()
            cleaned_text = clean_text(combined_raw)
            features = extract_linguistic_features(title_input, text_input)

            if not cleaned_text:
                st.warning("⚠️ Content contains only stopwords or symbols. Please enter descriptive news content.")
            else:
                vec_input = vectorizer.transform([cleaned_text])

                # Probability calculation
                if hasattr(active_model, "predict_proba"):
                    proba = active_model.predict_proba(vec_input)[0]
                    prob_real = float(proba[1])
                    prob_fake = float(proba[0])
                elif hasattr(active_model, "decision_function"):
                    df_val = float(active_model.decision_function(vec_input)[0])
                    prob_real = 1.0 / (1.0 + np.exp(-df_val))
                    prob_fake = 1.0 - prob_real
                else:
                    raw_pred = active_model.predict(vec_input)[0]
                    prob_real = 0.90 if raw_pred == 1 else 0.10
                    prob_fake = 1.0 - prob_real

                is_real = (prob_real >= prediction_threshold)
                confidence_score = prob_real if is_real else prob_fake

                st.markdown("---")
                st.subheader("🎯 Classification Outcome")

                col_res1, col_res2 = st.columns([1.3, 1])

                with col_res1:
                    if is_real:
                        st.markdown(f"""
                        <div class="badge-real">
                            ✅ AUTHENTIC / VERIFIED NEWS
                            <div style="font-size: 0.95rem; font-weight: 400; margin-top: 6px; opacity: 0.95;">
                                Vocabulary and phrasing align with standard journalistic reporting standards.
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="badge-fake">
                            🚨 MISINFORMATION / FABRICATED
                            <div style="font-size: 0.95rem; font-weight: 400; margin-top: 6px; opacity: 0.95;">
                                Detected stylometric markers associated with sensationalism or unverified claims.
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown(f"**Model Probability (Real):** `{prob_real * 100:.1f}%` &nbsp;|&nbsp; **Decision Confidence:** `{confidence_score * 100:.1f}%`")
                    st.progress(min(max(float(confidence_score), 0.0), 1.0))
                    
                    st.caption("ℹ️ *Note: News Shield operates as a screening aid based on statistical text features and does not replace primary journalistic fact-checking.*")

                with col_res2:
                    st.markdown("##### 📝 Stylometric & Linguistic Markers")
                    m1, m2 = st.columns(2)
                    m1.metric("Word Count", features["word_count"])
                    m2.metric("ALL-CAPS Ratio", f"{features['caps_ratio_percent']}%")

                    m3, m4 = st.columns(2)
                    m3.metric("Sensational Terms", features["sensational_indicators"], delta="Flagged" if features["sensational_indicators"] > 0 else None, delta_color="inverse")
                    m4.metric("Credibility Terms", features["credibility_indicators"], delta="Positive" if features["credibility_indicators"] > 0 else None)

                    m5, m6 = st.columns(2)
                    m5.metric("Exclamation Marks (!)", features["exclamation_count"])
                    m6.metric("Question Marks (?)", features["question_count"])

                # Feature Explainability & Extracted Tokens
                st.markdown("---")
                st.markdown("##### 🔑 Key Informative Tokens Extracted (After Stopword Removal & Stemming):")
                tokens = cleaned_text.split()
                if tokens:
                    unique_tokens = list(dict.fromkeys(tokens))[:25]
                    tags_html = "".join([f'<span class="tag-token">{tok}</span>' for tok in unique_tokens])
                    st.markdown(tags_html, unsafe_allow_html=True)

# ==========================================
# TAB 2: Model Benchmark & Analytics
# ==========================================
with tab2:
    st.subheader("📊 Multi-Model Performance Benchmark")
    st.markdown("Empirical comparison across 6 Machine Learning algorithms evaluated per Project Synopsis Objective 4 & 5:")

    if metrics_data and "models_evaluated" in metrics_data:
        m_df = pd.DataFrame(metrics_data["models_evaluated"])

        # Summary Metric Cards
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        best_name = metrics_data.get("best_model", "Logistic Regression")
        best_row = m_df[m_df["Model"] == best_name].iloc[0] if not m_df.empty else None

        if best_row is not None:
            col_m1.metric("🏆 Top Classifier", best_name.split()[0])
            col_m2.metric("Test Accuracy", f"{best_row['Accuracy']}%")
            col_m3.metric("F1-Score", f"{best_row['F1-Score']}%")
            col_m4.metric("5-Fold CV Score", f"{best_row.get('5-Fold CV Accuracy', 100.0)}%")

        st.divider()

        # Comparison Chart
        chart_df = m_df.melt(
            id_vars=["Model"],
            value_vars=["Accuracy", "Precision", "Recall", "F1-Score"],
            var_name="Metric",
            value_name="Score (%)"
        )
        fig = px.bar(
            chart_df,
            x="Model",
            y="Score (%)",
            color="Metric",
            barmode="group",
            title="Algorithm Performance Metrics Comparison",
            text_auto=True,
            color_discrete_sequence=["#1e3a8a", "#059669", "#ef4444", "#d97706"]
        )
        fig.update_layout(yaxis_range=[90, 105], height=420)
        st.plotly_chart(fig, use_container_width=True)

        # Performance Table
        st.markdown("##### Detailed Metric Breakdown:")
        display_cols = ["Model", "Accuracy", "Precision", "Recall", "F1-Score", "5-Fold CV Accuracy"]
        if "ROC-AUC" in m_df.columns:
            display_cols.append("ROC-AUC")
        st.dataframe(
            m_df[display_cols],
            use_container_width=True,
            hide_index=True
        )

        # Confusion Matrix Heatmap for Top Model
        st.markdown("##### 🧮 Confusion Matrix (Evaluated on Held-Out Test Set):")
        cm_data = best_row["Confusion Matrix"]
        cm_fig = go.Figure(data=go.Heatmap(
            z=cm_data,
            x=["Predicted Fake (0)", "Predicted Real (1)"],
            y=["Actual Fake (0)", "Actual Real (1)"],
            text=cm_data,
            texttemplate="%{text}",
            textfont={"size": 18, "color": "white"},
            colorscale='Blues',
            showscale=False
        ))
        cm_fig.update_layout(height=350, width=520)
        st.plotly_chart(cm_fig, use_container_width=True)

# ==========================================
# TAB 3: Batch CSV Analyzer
# ==========================================
with tab3:
    st.subheader("📁 Batch CSV News Classification")
    st.markdown("Upload a CSV file containing multiple news articles with a `title` and/or `text` column to perform bulk fake news classification.")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        try:
            batch_df = pd.read_csv(uploaded_file)
            st.write(f"Loaded **{len(batch_df)}** records from CSV.")

            text_col = None
            for col in ['text', 'content', 'body', 'article', 'title', 'headline']:
                if col in [c.lower() for c in batch_df.columns]:
                    text_col = [c for c in batch_df.columns if c.lower() == col][0]
                    break

            if text_col is None:
                st.error("❌ CSV must contain a text column (e.g., 'title', 'text', or 'content').")
            else:
                st.info(f"Using column **`{text_col}`** for classification.")

                if st.button("⚡ Run Batch Classification", type="primary"):
                    with st.spinner("Processing text and running predictions..."):
                        clean_col = batch_df[text_col].fillna('').astype(str).apply(clean_text)
                        vec_batch = vectorizer.transform(clean_col)
                        preds = active_model.predict(vec_batch)

                        batch_df['Predicted_Label'] = ["Real (1)" if p == 1 else "Fake (0)" for p in preds]

                    st.success("✅ Batch classification completed!")

                    counts = batch_df['Predicted_Label'].value_counts()
                    pie_fig = px.pie(
                        values=counts.values,
                        names=counts.index,
                        title="Distribution of Classified News Articles",
                        color=counts.index,
                        color_discrete_map={"Real (1)": "#059669", "Fake (0)": "#dc2626"}
                    )
                    st.plotly_chart(pie_fig, use_container_width=True)

                    st.dataframe(batch_df[[text_col, 'Predicted_Label']].head(50), use_container_width=True)

                    csv_data = batch_df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        "📥 Download Predictions CSV",
                        data=csv_data,
                        file_name="news_shield_predictions.csv",
                        mime="text/csv"
                    )
        except Exception as e:
            st.error(f"Error processing CSV: {str(e)}")

# ==========================================
# TAB 4: Project Synopsis & Viva Notes
# ==========================================
with tab4:
    st.subheader("🎓 Project Synopsis, Academic Methodology & Viva Notes")
    st.caption("Aligned with B.Tech CSE Major Project Specification (GNIOT / AKTU)")

    st.markdown("""
    ### 1. Project Overview & Institutional Details
    - **Project Title:** News Shield: An Intelligent System for Detection and Verifying Fake News
    - **Degree:** Bachelor of Technology in Computer Science & Engineering
    - **College:** Greater Noida Institute of Technology (GNIOT), Knowledge Park-II, Greater Noida
    - **University:** Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow
    - **Supervisor / Guide:** Mr. Rohit Vaid
    - **Student Team:**
      1. Aryan Chourasia (Roll No: 2501320100070)
      2. Ayush kumar singh (Roll No: 2501320100080)
      3. Arpita Dixit (Roll No: 2501320100067)
      4. Ananya Singh (Roll No: 2501320100044)

    ---

    ### 2. Mathematical Foundations & Algorithm Formulation

    #### A. TF-IDF (Term Frequency - Inverse Document Frequency)
    Converts raw text documents into a dense discriminative vector space:
    $$\\text{TF}(t, d) = \\frac{\\text{Frequency of term } t \\text{ in document } d}{\\text{Total terms in document } d}$$
    
    $$\\text{IDF}(t, D) = \\log \\left( \\frac{1 + |D|}{1 + |\\{d \\in D : t \\in d\\}|} \\right) + 1$$
    
    $$\\text{TF-IDF}(t, d, D) = \\text{TF}(t, d) \\times \\text{IDF}(t, D)$$

    #### B. Logistic Regression (Probabilistic Sigmoidal Decision)
    Maps feature representations to calibrated probabilities between 0 and 1:
    $$P(Y = 1 \\mid X) = \\sigma(w^T X + b) = \\frac{1}{1 + e^{-(w^T X + b)}}$$

    #### C. Support Vector Machine (Maximum-Margin Hyperplane)
    Finds the optimal separating hyperplane with maximum geometric margin $\\frac{2}{\\|w\\|}$:
    $$\\min_{w, b, \\xi} \\frac{1}{2} \\|w\\|^2 + C \\sum_{i=1}^{n} \\xi_i \\quad \\text{subject to} \\quad y_i (w^T x_i + b) \\ge 1 - \\xi_i, \\quad \\xi_i \\ge 0$$

    #### D. Soft Voting Ensemble
    Combines posterior probability distributions across complementary model architectures:
    $$P_{\\text{ensemble}}(y=c \\mid x) = \\frac{1}{\\sum_{j} w_j} \\sum_{j=1}^{M} w_j P_j(y=c \\mid x)$$

    ---

    ### 3. Key Viva Examination Questions & Model Answers

    **Q1: What are the main limitations of relying solely on text content for fake news detection?**
    *Answer:* As highlighted in Shu et al. [1], text content is only one dimension. Real-world misinformation often uses truthful text accompanied by misleading imagery (out-of-context media), satire, or coordinated bot networks. News Shield functions as a text-screening aid, not an absolute arbiter of ground truth.

    **Q2: Why is 5-Fold Stratified Cross-Validation preferred over a simple train-test split?**
    *Answer:* A single train-test split can be biased depending on how the data was partitioned. Stratified 5-Fold Cross-Validation ensures that each fold maintains identical class proportions (50% real, 50% fake) and evaluates model variance across multiple unseen subsets, confirming high stability (low standard deviation).

    **Q3: How does the model mitigate overfitting?**
    *Answer:*
    1. Stratified train-test split and 5-fold cross-validation.
    2. Sublinear TF scaling ($1 + \\log(tf)$) and feature vocabulary bound ($8,000$ unigrams and bigrams).
    3. L2 regularization on Logistic Regression ($C=1.0$) and margin penalty tuning on SVM.
    4. Soft voting ensembling which reduces overall prediction variance.

    **Q4: What is the difference between Porter Stemming and WordNet Lemmatization?**
    *Answer:* Stemming applies rule-based heuristic suffix chopping (e.g. 'running' $\\to$ 'run'), which is computationally fast for large corpora. Lemmatization utilizes morphological dictionaries and POS tags to return valid lemmas (e.g. 'better' $\\to$ 'good'), requiring greater computational overhead.
    """)
