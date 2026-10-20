"""
Generate News Shield Project Synopsis in Microsoft Word (.docx) format
conforming strictly to the guidelines in 'synopsis format.docx'.

Author: News Shield Project Team
College: Greater Noida Institute of Technology (GNIOT) / AKTU
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "News_Shield_Project_Synopsis.docx")


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner padding for table cell."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_background(cell, hex_color):
    """Set background color of a table cell."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)


def create_synopsis():
    doc = docx.Document()

    # 1. Page Setup: A4, Margins: Left 2.5cm, Top 2.5cm, Right 1.25cm, Bottom 1.25cm
    section = doc.sections[0]
    section.page_width = Inches(8.27)   # A4 Width (21.0 cm)
    section.page_height = Inches(11.69) # A4 Height (29.7 cm)
    section.left_margin = Inches(0.984)  # 2.5 cm
    section.top_margin = Inches(0.984)   # 2.5 cm
    section.right_margin = Inches(0.492) # 1.25 cm
    section.bottom_margin = Inches(0.492)# 1.25 cm

    # Base Normal Style: Times New Roman, 12pt, 1.5 line spacing
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.space_after = Pt(4)

    # -------------------------------------------------------------
    # COVER / TITLE PAGE
    # -------------------------------------------------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.line_spacing = 1.15
    p_inst.paragraph_format.space_after = Pt(2)
    r = p_inst.add_run("GREATER NOIDA INSTITUTE OF TECHNOLOGY\n(ENGINEERING INSTITUTE)")
    r.bold = True
    r.font.size = Pt(14)
    r.font.name = 'Times New Roman'
    
    p_addr = doc.add_paragraph()
    p_addr.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_addr.paragraph_format.space_after = Pt(28)
    r = p_addr.add_run("Plot No-7, Knowledge Park-II, Greater Noida")
    r.font.size = Pt(11)
    r.font.name = 'Times New Roman'

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.line_spacing = 1.2
    p_title.paragraph_format.space_after = Pt(20)
    r = p_title.add_run("News Shield: An Intelligent System for Detection and Verifying Fake News")
    r.bold = True
    r.font.size = Pt(22)
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(16, 44, 87)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.line_spacing = 1.15
    p_sub.paragraph_format.space_after = Pt(16)
    r = p_sub.add_run("PROJECT SYNOPSIS\nOF MAJOR PROJECT")
    r.bold = True
    r.font.size = Pt(13)
    r.font.name = 'Times New Roman'

    p_deg = doc.add_paragraph()
    p_deg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_deg.paragraph_format.line_spacing = 1.15
    p_deg.paragraph_format.space_after = Pt(24)
    r1 = p_deg.add_run("BACHELOR OF TECHNOLOGY\n")
    r1.bold = True
    r1.font.size = Pt(14)
    r2 = p_deg.add_run("COMPUTER SCIENCE & ENGINEERING")
    r2.bold = True
    r2.font.size = Pt(15)

    # Students Table
    t_stud = doc.add_table(rows=1, cols=2)
    t_stud.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_stud.rows[0].cells
    hdr[0].text = "Name of Student"
    hdr[1].text = "University Roll Number"
    set_cell_background(hdr[0], "0F2C59")
    set_cell_background(hdr[1], "0F2C59")
    for c in hdr:
        for p in c.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.bold = True
                run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(c, top=80, bottom=80)

    students = [
        ("Aryan Chourasia", "2501320100070"),
        ("Ayush kumar singh", "2501320100080"),
        ("Arpita Dixit", "2501320100067"),
        ("Ananya Singh", "2501320100044")
    ]
    for name, roll in students:
        row = t_stud.add_row().cells
        row[0].text = name
        row[1].text = roll
        row[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        row[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for c in row:
            for p in c.paragraphs:
                for run in p.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(11)
            set_cell_margins(c, top=60, bottom=60)

    p_guide = doc.add_paragraph()
    p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_guide.paragraph_format.space_before = Pt(24)
    p_guide.paragraph_format.space_after = Pt(24)
    r = p_guide.add_run("SUPERVISOR / GUIDE: Mr. Rohit Vaid")
    r.bold = True
    r.font.size = Pt(13)
    r.font.name = 'Times New Roman'

    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_univ.paragraph_format.line_spacing = 1.15
    p_univ.paragraph_format.space_after = Pt(0)
    r1 = p_univ.add_run("Greater Noida Institute of Technology, Greater Noida\n")
    r1.bold = True
    r1.font.size = Pt(13)
    r2 = p_univ.add_run("Dr. A.P.J. Abdul Kalam Technical University, Lucknow\n")
    r2.bold = True
    r2.font.size = Pt(15)
    r3 = p_univ.add_run("October 2026")
    r3.font.size = Pt(12)

    doc.add_page_break()

    # -------------------------------------------------------------
    # INDEX & NOTATIONS / NOMENCLATURE
    # -------------------------------------------------------------
    p_idx = doc.add_paragraph()
    p_idx.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_idx.add_run("INDEX")
    r.bold = True
    r.font.size = Pt(14)

    index_items = [
        ("1. Introduction", "3"),
        ("2. Literature Review", "4"),
        ("3. Objectives of the Project", "5"),
        ("4. Project Category", "6"),
        ("5. System Analysis & Architecture Design (DFDs, Use Cases)", "6"),
        ("6. Complete Structure & Module Descriptions", "8"),
        ("7. Hardware & Software Requirements", "10"),
        ("8. Methodology & Planning of Work", "11"),
        ("9. Industry / Client Information", "12"),
        ("10. Future Scope & Enhancements", "12"),
        ("11. References", "13")
    ]

    t_idx = doc.add_table(rows=1, cols=2)
    t_idx.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_idx.autofit = False
    t_idx.columns[0].width = Inches(5.8)
    t_idx.columns[1].width = Inches(1.2)
    h_idx = t_idx.rows[0].cells
    h_idx[0].text = "Section Title"
    h_idx[1].text = "Page No."
    set_cell_background(h_idx[0], "E2E8F0")
    set_cell_background(h_idx[1], "E2E8F0")
    for c in h_idx:
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.name = 'Times New Roman'
        set_cell_margins(c, top=60, bottom=60)

    for title, pg in index_items:
        row = t_idx.add_row().cells
        row[0].text = title
        row[1].text = pg
        row[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        row[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for c in row:
            p = c.paragraphs[0]
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(11)
            set_cell_margins(c, top=50, bottom=50)

    p_not = doc.add_paragraph()
    p_not.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_not.paragraph_format.space_before = Pt(18)
    r = p_not.add_run("NOTATIONS / NOMENCLATURE")
    r.bold = True
    r.font.size = Pt(14)

    notations = [
        ("ML", "Machine Learning"),
        ("NLP", "Natural Language Processing"),
        ("TF-IDF", "Term Frequency - Inverse Document Frequency"),
        ("SVM", "Support Vector Machine"),
        ("LR", "Logistic Regression"),
        ("PAC", "Passive Aggressive Classifier"),
        ("DFD", "Data Flow Diagram"),
        ("LSTM", "Long Short-Term Memory"),
        ("BERT", "Bidirectional Encoder Representations from Transformers"),
        ("ROC-AUC", "Receiver Operating Characteristic - Area Under Curve"),
        ("API", "Application Programming Interface"),
        ("UI", "User Interface (Streamlit Framework)")
    ]

    t_not = doc.add_table(rows=1, cols=2)
    t_not.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_not.columns[0].width = Inches(2.2)
    t_not.columns[1].width = Inches(4.8)
    h_not = t_not.rows[0].cells
    h_not[0].text = "Abbreviation"
    h_not[1].text = "Full Technical Description"
    set_cell_background(h_not[0], "E2E8F0")
    set_cell_background(h_not[1], "E2E8F0")
    for c in h_not:
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(11)
        p.runs[0].font.name = 'Times New Roman'
        set_cell_margins(c, top=60, bottom=60)

    for abbr, desc in notations:
        row = t_not.add_row().cells
        row[0].text = abbr
        row[1].text = desc
        row[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
        for c in row:
            p = c.paragraphs[0]
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(11)
            set_cell_margins(c, top=40, bottom=40)

    doc.add_page_break()

    # Helper function for Section Headings
    def add_section_heading(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(14)
        run.font.name = 'Times New Roman'
        run.font.color.rgb = RGBColor(15, 44, 89)
        return p

    def add_sub_heading(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title)
        run.bold = True
        run.font.size = Pt(12)
        run.font.name = 'Times New Roman'
        return p

    def add_body(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        return p

    # -------------------------------------------------------------
    # 1. INTRODUCTION
    # -------------------------------------------------------------
    add_section_heading("1. INTRODUCTION")

    add_sub_heading("1.1 Background and Problem Statement")
    add_body(
        "Digital communication and modern social networking platforms enable news, breaking reports, and public claims to proliferate rapidly across the globe. Alongside legitimate and rigorous investigative journalism, fabricated, distorted, or sensationalist material is routinely manufactured and disseminated as genuine reporting. Everyday readers face formidable cognitive challenges when attempting to manually authenticate every article encountered online, while exhaustive manual fact-checking by human experts requires substantial investigation time and resources. The News Shield project addresses this pressing societal vulnerability by proposing an automated, rapid screening tool designed specifically for news-style text."
    )

    add_sub_heading("1.2 Proposed Approach and Technology Stack")
    add_body(
        "The proposed News Shield system implements a supervised Machine Learning (ML) and Natural Language Processing (NLP) framework to classify incoming news articles, headlines, and social media posts into dataset-defined 'Real' (Authentic) or 'Fake' (Misinformation) categories. The end-to-end processing pipeline comprises automated web cleansing, tokenization, stopword elimination, and morphological stemming via the Porter Stemmer. For numeric representation, the system extracts high-dimensional unigram and bigram Term Frequency - Inverse Document Frequency (TF-IDF) feature vectors with sublinear scaling. The classification backend benchmarks baseline models including Logistic Regression, Multinomial Naive Bayes, Support Vector Machines (SVM), and an ensemble Soft Voting classifier. Predictions are surfaced through a modern, responsive web application (Streamlit) featuring real-time probabilistic confidence estimates."
    )

    add_sub_heading("1.3 Scope, Operating Philosophy, and Expected Contributions")
    add_body(
        "The primary operational scope centers on text-based pattern recognition across verified corpora. Crucially, the system functions as an intelligent screening aid rather than an infallible, automated authority on absolute ground truth; critical claims and high-stakes reports continue to necessitate primary sourcing. Expected project deliverables comprise a reproducible data generation and cleaning pipeline, a rigorous multi-model empirical comparison using held-out test data and 5-fold cross-validation, an interactive web prototype, and a comprehensive analysis of errors and generalization boundaries across diverse domains."
    )

    # -------------------------------------------------------------
    # 2. LITERATURE REVIEW
    # -------------------------------------------------------------
    add_section_heading("2. LITERATURE REVIEW")
    add_body(
        "The identification of deceptive text has emerged as a vibrant domain in data mining and computational linguistics. A thorough review of prior state-of-the-art literature was conducted to contextualize the proposed News Shield architecture:"
    )

    lit_points = [
        ("Shu et al. (2017) [1]:", "Surveyed fake news detection on social media from a data mining perspective, organizing techniques around news content, social context, and user engagement. Their analysis demonstrated that while social graph propagation offers valuable signals, content-level linguistic and lexical features form the fundamental, reproducible baseline for automated detection systems."),
        ("Pérez-Rosas et al. (2018) [2]:", "Introduced multi-domain cross-genre datasets and evaluated lexical, syntactic, and psycholinguistic markers (sentiment polarity, readability indices, and punctuation distributions), demonstrating that stylometric cues provide strong signals for separating authentic reporting from fabricated rumors."),
        ("Ahmed, Traoré, and Saad (2017) [3]:", "Investigated n-gram analysis combined with linear and nonlinear classifiers. Their experimental results proved that extracting unigrams and bigrams via TF-IDF achieves superior discriminative capability for distinguishing deceptive journalism from real news wire reports."),
        ("Wang (2017) [4]:", "Published the LIAR benchmark dataset consisting of 12,800 manually labeled short political claims from PolitiFact, establishing standard protocols for fine-grained veracity classification."),
        ("Ruchansky, Seo, and Liu (2017) [5]:", "Proposed the CSI hybrid deep model integrating textual features, user response sequences, and publisher behavioral patterns, highlighting the complementary nature of content and context."),
        ("Kaliyar, Goswami, and Narang (2021) [6]:", "Introduced FakeBERT, demonstrating that combining contextual bidirectional representations from transformers with convolutional neural network layers achieves high precision in detecting complex social media misinformation."),
        ("Devlin et al. (2019) [8] & FakeNewsNet [7]:", "Provided foundational insights into pre-trained transformer embeddings and comprehensive multi-attribute data repositories incorporating spatial-temporal attributes."),
        ("Kaggle & PolitiFact Resources [9, 10]:", "Documented the standard public benchmarks of authentic news wire feeds (Reuters, AP) alongside verified political hoaxes, forming the structural foundation for balanced corpus generation.")
    ]

    for title, desc in lit_points:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(3)
        r_bold = p.add_run(f"• {title} ")
        r_bold.bold = True
        r_bold.font.name = 'Times New Roman'
        r_bold.font.size = Pt(11.5)
        r_desc = p.add_run(desc)
        r_desc.font.name = 'Times New Roman'
        r_desc.font.size = Pt(11.5)

    # -------------------------------------------------------------
    # 3. OBJECTIVES OF THE PROJECT
    # -------------------------------------------------------------
    add_section_heading("3. OBJECTIVES OF THE PROJECT")
    add_body("The specific, measurable objectives established for the News Shield Major Project are:")

    objectives = [
        "1. Study existing fake-news detection paradigms, feature extraction techniques, and benchmark datasets relevant to the computational scope.",
        "2. Curate and document a balanced, labelled real/fake news dataset (1,200 records across 8 distinct thematic domains) detailing provenance, label definitions, and domain scope.",
        "3. Implement an NLP text-processing pipeline incorporating regex filtering, stopword elimination, and Porter morphological stemming; extract TF-IDF unigram and bigram feature representations.",
        "4. Train, tune, and evaluate baseline classifiers: Logistic Regression, Multinomial Naive Bayes, and Support Vector Machines (SVM).",
        "5. Develop and evaluate an advanced Soft Voting Ensemble model that pools posterior probabilities across complementary linear and probabilistic architectures.",
        "6. Benchmark all candidate classifiers using Accuracy, Precision, Recall, F1-Score, ROC-AUC, 5-Fold Stratified Cross-Validation, and Confusion Matrix analysis on held-out test data.",
        "7. Build an interactive, user-friendly web interface (Streamlit) featuring single-click preset verification, live probability meters, stylometric marker breakdowns, and bulk CSV processing.",
        "8. Perform comprehensive error analysis on false positives and false negatives to delineate model generalization limits across unseen topics, writing styles, and sensationalism levels."
    ]

    for obj in objectives:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(obj)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11.5)

    # -------------------------------------------------------------
    # 4. PROJECT CATEGORY
    # -------------------------------------------------------------
    add_section_heading("4. PROJECT CATEGORY")
    add_body(
        "• Primary Category: Artificial Intelligence & Machine Learning (Supervised Text Classification)\n"
        "• Sub-Discipline: Natural Language Processing (NLP), Stylometry & Information Retrieval\n"
        "• Application Domain: Web-Based Decision Support Systems & Digital Information Verification"
    )

    # -------------------------------------------------------------
    # 5. SYSTEM ANALYSIS & ARCHITECTURE DESIGN
    # -------------------------------------------------------------
    add_section_heading("5. SYSTEM ANALYSIS & ARCHITECTURE DESIGN")

    add_sub_heading("5.1 Data Flow Diagrams (DFDs)")
    add_body(
        "Data Flow Diagrams model the movement, storage, and transformation of data within News Shield across hierarchical levels of abstraction:"
    )

    dfd_desc = [
        ("Level 0 DFD (Context Level):", 
         "The external user submits raw news headlines and paragraph texts to the News Shield System boundary. The system passes data through the vectorized inference engine and returns a validated classification result ('Authentic' or 'Misinformation') accompanied by a calibrated confidence percentage and stylometric marker report."),
        ("Level 1 DFD (Subsystem Decomposition):",
         "Decomposes processing into four sequential processes: [P1.0 Data Ingestion & Sanitization] cleans URLs and symbols; [P2.0 NLP Feature Transformation] applies Porter Stemming and TF-IDF matrix projection using the fitted vocabulary; [P3.0 Multi-Model Inference Engine] invokes the active classifier (Logistic Regression, SVM, Ensemble) to compute decision probabilities; [P4.0 Visualization & Reporting Subsystem] renders the UI badges, confidence meters, and CSV batch tables."),
        ("Level 2 DFD (Feature Engineering & Inference Engine):",
         "Illustrates the detailed flow within the classification subsystem: transformed vectors are matched against calibrated model weights, Platt-scaled sigmoid probabilities are derived, and decision logic evaluates whether P(Real) exceeds the configured decision threshold (default: 0.50).")
    ]
    for d_title, d_text in dfd_desc:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"• {d_title} ")
        r1.bold = True
        r1.font.name = 'Times New Roman'
        r2 = p.add_run(d_text)
        r2.font.name = 'Times New Roman'

    add_sub_heading("5.2 Use Case Analysis")
    add_body(
        "• Primary Actor: End-User (Reader, Student, Journalist, or Content Moderator)\n"
        "• System Boundary: News Shield Web Interface & Inference API\n"
        "• Core Use Cases:\n"
        "   1. UC-1 [Verify Single Article]: User inputs headline/body; system computes authenticity and returns classification badge.\n"
        "   2. UC-2 [Inspect Stylometric Markers]: User inspects ALL-CAPS ratios, sensational keyword counts, and credibility tokens.\n"
        "   3. UC-3 [Select Active Classifier]: User dynamically switches between Logistic Regression, Linear SVM, Soft Voting Ensemble, etc.\n"
        "   4. UC-4 [Batch CSV Processing]: User uploads a multi-article CSV file; system processes rows in bulk and provides annotated CSV download.\n"
        "   5. UC-5 [Review Benchmark & Viva Notes]: User reviews empirical 5-fold CV charts, confusion matrices, and academic theory."
    )

    add_sub_heading("5.3 System Architecture Workflow")
    add_body(
        "The architecture is organized into four modular layers:\n"
        "1. Presentation Layer: Built with Streamlit, providing interactive web dashboards, Plotly charts, and responsive CSS styling.\n"
        "2. Service / Preprocessing Layer: Python modules executing text cleaning, NLTK stopword pruning, and linguistic feature extraction.\n"
        "3. Machine Learning Core Layer: Scikit-Learn TF-IDF vectorizer (8,000 features) coupled with serialized model estimators (.pkl).\n"
        "4. Data & Serialization Layer: File-based persistence storing training datasets (sample_news_dataset.csv), serialized models (model.pkl, all_models.pkl), and evaluation metrics (model_metrics.json)."
    )

    # -------------------------------------------------------------
    # 6. COMPLETE STRUCTURE & MODULE DESCRIPTIONS
    # -------------------------------------------------------------
    add_section_heading("6. COMPLETE STRUCTURE & MODULE DESCRIPTIONS")

    modules = [
        ("Module 1: Text Preprocessing & Cleaning (src/preprocessor.py)",
         "Responsible for text normalization and sanitization. Strips web hyperlinks, HTML markup tags, and non-alphanumeric punctuation. Converts characters to lowercase, tokenizes sentences, filters stopwords using the NLTK English corpus, and reduces terms to their root morphological stem via the Porter Stemmer. Also computes stylometric markers including word counts, uppercase character ratios, exclamation mark frequencies, and sensational keyword hits."),
        ("Module 2: Feature Engineering & Vectorization (models/vectorizer.pkl)",
         "Extracts TF-IDF feature representations across unigrams and bigrams (ngram_range=(1, 2)) capped at the top 8,000 most informative features. Sublinear term-frequency scaling is enabled (1 + log(tf)) to reduce distortion from hyper-frequent terms, with document frequency boundaries (min_df=2, max_df=0.98) to filter isolated typographical errors."),
        ("Module 3: Multi-Model Training & Benchmarking (train.py, src/evaluate.py)",
         "Implements 6 candidate machine learning classifiers: (i) L2-Regularized Logistic Regression, (ii) Calibrated Linear Support Vector Machine (LinearSVC with 5-fold Platt scaling), (iii) Soft Voting Ensemble combining LR, SVM, and Naive Bayes, (iv) Multinomial Naive Bayes, (v) Passive Aggressive Classifier, and (vi) Random Forest. Conducts 5-Fold Stratified Cross-Validation on training data and computes Precision, Recall, F1-Score, and ROC-AUC on held-out test data."),
        ("Module 4: Interactive Web Application & Batch Analyzer (app.py)",
         "Provides an end-to-end graphical web interface with 4 dedicated functional tabs: Real-Time News Verifier, Multi-Model Benchmark & Analytics Dashboard, Batch CSV Classifier, and Project Synopsis & Viva Notes. Features interactive model selection and adjustable decision threshold sliders.")
    ]

    for m_name, m_desc in modules:
        add_sub_heading(m_name)
        add_body(m_desc)

    add_sub_heading("6.1 Data Structures Employed")
    add_body(
        "• SciPy Compressed Sparse Row (CSR) Matrix: Encodes high-dimensional sparse TF-IDF text features (1,200 × 8,000) with minimal memory footprint.\n"
        "• Pandas DataFrame: Manages structured tabular article records, category tags, batch CSV inputs, and evaluation metrics.\n"
        "• NumPy ndarrays: Stores calibrated probability distributions, confusion matrix arrays, and decision function values.\n"
        "• Python Dictionaries & JSON: Serializes candidate model collections (all_models.pkl) and benchmark evaluation summaries (model_metrics.json)."
    )

    add_sub_heading("6.2 Testing Strategies & Validation Process")
    add_body(
        "• 5-Fold Stratified Cross-Validation: Evaluates model generalization stability across 5 disjoint subsets preserving exact class balance.\n"
        "• 20% Held-Out Test Set: Measures final model generalization on 240 unseen articles, generating confusion matrices and classification reports.\n"
        "• 16-Article Real-World Generalization Benchmark: Rigorous testing against authentic, challenging real-world news stories (NASA, WHO, Federal Reserve, Supreme Court, 5G hoaxes, cancer cure scams) to ensure zero overfitting."
    )

    # -------------------------------------------------------------
    # 7. HARDWARE & SOFTWARE REQUIREMENTS
    # -------------------------------------------------------------
    add_section_heading("7. HARDWARE & SOFTWARE REQUIREMENTS")

    add_sub_heading("7.1 Software Requirements")
    add_body(
        "• Operating System: Windows 10/11, macOS, or Linux (Ubuntu 20.04+)\n"
        "• Programming Language: Python 3.9 or higher (Tested on Python 3.14)\n"
        "• Machine Learning Framework: Scikit-Learn 1.9+, SciPy 1.18+\n"
        "• Natural Language Toolkit: NLTK 3.10+ (PorterStemmer, English stopwords corpus)\n"
        "• Web Application Framework: Streamlit 1.61+\n"
        "• Data Handling & Visualization: Pandas 3.0+, NumPy 2.5+, Plotly 6.9+, Matplotlib 3.11+\n"
        "• Model Serialization: Joblib 1.5+"
    )

    add_sub_heading("7.2 Hardware Specifications")
    add_body(
        "• Processor: Intel Core i3 / AMD Ryzen 3 or higher (Intel Core i5 recommended)\n"
        "• Primary Memory (RAM): Minimum 4 GB (8 GB recommended for batch vectorization)\n"
        "• Secondary Storage: 500 MB free hard disk space for code, virtual environment, and serialized models\n"
        "• Network: Standard internet connection for initial dependency installation"
    )

    # -------------------------------------------------------------
    # 8. METHODOLOGY & PLANNING OF WORK
    # -------------------------------------------------------------
    add_section_heading("8. METHODOLOGY & PLANNING OF WORK")
    add_body(
        "The project execution follows a structured milestone schedule aligned with academic major project rubrics:"
    )

    phases = [
        ("Phase 1: Problem Definition & Literature Survey (Weeks 1-2)", "Review state-of-the-art NLP fake news literature; define project scope, baseline models, and evaluation criteria."),
        ("Phase 2: Dataset Selection & Synthesis (Weeks 3-4)", "Compile balanced 1,200-sample corpus across 8 journalistic and misinformation domains; perform EDA and class balance checks."),
        ("Phase 3: NLP Preprocessing & Feature Engineering (Weeks 5-6)", "Implement regex sanitization, stopword pruning, and Porter stemming; optimize 8,000-feature TF-IDF vectorizer."),
        ("Phase 4: Model Training & Hyperparameter Tuning (Weeks 7-8)", "Train Logistic Regression, Linear SVM, Multinomial Naive Bayes, Passive Aggressive, and Soft Voting Ensemble; conduct 5-Fold Stratified Cross-Validation."),
        ("Phase 5: Prototype Development (Weeks 9-10)", "Construct interactive Streamlit web application with model selector, probability meters, stylometric visualizers, and batch CSV processor."),
        ("Phase 6: Empirical Testing & Error Analysis (Weeks 11-12)", "Evaluate models on 16-article unseen real-world benchmark suite; analyze false-positive boundaries; finalize project synopsis and documentation.")
    ]

    for p_title, p_desc in phases:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"• {p_title}: ")
        r1.bold = True
        r1.font.name = 'Times New Roman'
        r2 = p.add_run(p_desc)
        r2.font.name = 'Times New Roman'

    # -------------------------------------------------------------
    # 9. INDUSTRY / CLIENT INFORMATION
    # -------------------------------------------------------------
    add_section_heading("9. INDUSTRY / CLIENT INFORMATION")
    add_body(
        "• Project Type: In-House Academic Major Project (B.Tech Computer Science & Engineering)\n"
        "• Sponsoring Industry / Client: None (Self-initiated open research prototype)\n"
        "• Institutional Affiliation: Greater Noida Institute of Technology (GNIOT), Knowledge Park-II, Greater Noida"
    )

    # -------------------------------------------------------------
    # 10. FUTURE SCOPE & FURTHER ENHANCEMENT
    # -------------------------------------------------------------
    add_section_heading("10. FUTURE SCOPE & FURTHER ENHANCEMENT")
    add_body(
        "1. Deep Transformer Representations: Fine-tune pre-trained contextual language models (BERT, RoBERTa, DistilBERT) to capture long-range contextual nuance and subtle semantic irony.\n"
        "2. Multimodal Verification: Expand detection to analyze accompanying multimedia (photographs, synthetic deepfake imagery, and video clips) alongside article text.\n"
        "3. Live Fact-Checking API Integration: Connect to external automated claim-checking services (Google Fact Check Tools API, ClaimReview) to retrieve authoritative source verdicts in real time.\n"
        "4. Multilingual Misinformation Detection: Extend tokenization and embedding architectures to support Indian regional languages (Hindi, Bengali, Tamil) to combat localized digital disinformation."
    )

    # -------------------------------------------------------------
    # 11. REFERENCES (IEEE FORMAT)
    # -------------------------------------------------------------
    add_section_heading("11. REFERENCES")

    references = [
        "[1] K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu, 'Fake News Detection on Social Media: A Data Mining Perspective,' ACM SIGKDD Explorations Newsletter, vol. 19, no. 1, pp. 22-36, 2017. doi: 10.1145/3137597.3137600.",
        "[2] V. Pérez-Rosas, B. Kleinberg, A. Lefevre, and R. Mihalcea, 'Automatic Detection of Fake News,' in Proc. 27th International Conference on Computational Linguistics (COLING), Santa Fe, NM, USA, 2018, pp. 3391-3401.",
        "[3] H. Ahmed, I. Traoré, and S. Saad, 'Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques,' in Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments, Springer, Cham, 2017, pp. 127-138. doi: 10.1007/978-3-319-69155-8_9.",
        "[4] W. Y. Wang, ''Liar, Liar Pants on Fire': A New Benchmark Dataset for Fake News Detection,' in Proc. 55th Annual Meeting of the Association for Computational Linguistics (ACL), Vancouver, Canada, 2017, pp. 422-426. doi: 10.18653/v1/P17-2067.",
        "[5] N. Ruchansky, S. Seo, and Y. Liu, 'CSI: A Hybrid Deep Model for Fake News Detection,' in Proc. ACM Conference on Information and Knowledge Management (CIKM), Singapore, 2017, pp. 797-806. doi: 10.1145/3132847.3132877.",
        "[6] R. K. Kaliyar, A. Goswami, and P. Narang, 'FakeBERT: Fake News Detection in Social Media with a BERT-Based Deep Learning Approach,' Multimedia Tools and Applications, vol. 80, no. 8, pp. 11765-11788, 2021. doi: 10.1007/s11042-020-10183-2.",
        "[7] K. Shu, D. Mahudeswaran, S. Wang, D. Lee, and H. Liu, 'FakeNewsNet: A Data Repository with News Content, Social Context, and Spatiotemporal Information for Studying Fake News on Social Media,' Big Data, vol. 8, no. 3, pp. 171-188, 2020. doi: 10.1089/big.2020.0062.",
        "[8] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, 'BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding,' in Proc. NAACL-HLT, vol. 1, Minneapolis, MN, USA, 2019, pp. 4171-4186. doi: 10.18653/v1/N19-1423.",
        "[9] C. Bisaillon, 'Fake and Real News Dataset,' Kaggle, 2020. [Online]. Available: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset. Accessed: Oct. 16, 2026.",
        "[10] 'PolitiFact: Fact-Checking Journalism,' [Online]. Available: https://www.politifact.com. Accessed: Oct. 16, 2026."
    ]

    for ref in references:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(ref)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    # Save to destination
    doc.save(OUTPUT_FILE)
    print(f"[SUCCESS] Synopsis document created at: {OUTPUT_FILE}")
    return OUTPUT_FILE


if __name__ == "__main__":
    create_synopsis()
