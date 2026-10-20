"""
Test accuracy and robustness of the current News Shield model.
"""
import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from src.preprocessor import clean_text

model = joblib.load('models/model.pkl')
vec = joblib.load('models/vectorizer.pkl')

print("Loaded Model:", type(model).__name__)
print("Vocabulary Size:", len(vec.vocabulary_))

# 1. Test on the project's existing dataset
df = pd.read_csv('data/sample_news_dataset.csv')
combined = (df['title'].fillna('') + ' ' + df['text'].fillna('')).apply(clean_text)
X = vec.transform(combined)
preds = model.predict(X)
acc = accuracy_score(df['label'], preds)
print(f"\n--- Current Dataset Evaluation ({len(df)} samples) ---")
print(f"Overall Accuracy: {acc * 100:.2f}%")

# 2. Test on a curated suite of realistic, unseen real-world test cases
test_cases = [
    # REAL NEWS CASES
    ("WHO confirms new vaccine distribution partnership in sub-Saharan Africa",
     "The World Health Organization announced on Tuesday a multilateral partnership to deliver over twenty million doses of malaria vaccines to vulnerable children across Central and West Africa.", 1),
    ("James Webb Telescope reveals atmosphere composition of distant exoplanet",
     "Astronomers analyzing spectral transmission data collected by the James Webb Space Telescope have identified carbon dioxide and sulfur compounds in the atmosphere of exoplanet WASP-39 b.", 1),
    ("Central bank leaves benchmark interest rates unchanged amid stable job numbers",
     "The Federal Reserve held the policy interest rate steady at its monetary policy meeting, citing resilient employment data and inflation trending toward the two percent long-term target.", 1),
    ("European Parliament votes to approve digital identity framework",
     "Members of the European Parliament voted in Strasbourg to establish a unified digital identity framework allowing citizens to securely access cross-border public services and financial transactions.", 1),
    ("Scientists develop enzyme capable of breaking down plastic waste in hours",
     "Chemical engineers at the University of Texas have engineered an enzyme variant termed FAST-PETase that depolymerizes post-consumer polyethylene terephthalate in less than 24 hours.", 1),
    ("Tokyo stock exchange closes higher following semiconductor sector gains",
     "Shares on the Tokyo exchange rallied on Friday afternoon led by gains in electronic components and advanced chip manufacturing suppliers following quarterly guidance updates.", 1),
    ("Renewable energy supplies forty percent of electricity during summer peak",
     "Grid operators reported that solar photovoltaic and offshore wind generation supplied a record forty percent of peak electric power demand during the July heatwaves.", 1),
    ("Supreme Court hears oral arguments in federal interstate water compact dispute",
     "The Supreme Court heard ninety minutes of arguments in a long-running dispute between neighboring western states regarding reservoir storage allocations along the Rio Grande.", 1),
     
    # FAKE NEWS CASES
    ("Secret military tribunal sentences top health officials to life imprisonment at covert base",
     "Bombshell reports from underground patriot informants confirm that military tribunals secretly tried and convicted federal health leaders for crimes against humanity. Mainstream media refuses to broadcast the footage!", 0),
    ("Miracle Himalayan salt water cures stage 4 diabetes in seven days without insulin",
     "Doctors are stunned! This forbidden mineral water recipe dissolves high blood sugar instantly. Greedy pharmaceutical companies are bribing search engines to delete this life-saving secret cure before it goes viral!", 0),
    ("5G cell towers emit secret mind-control frequencies tested by international cabal",
     "Anonymous military whistleblowers leaked top-secret schematics proving that all newly installed 5G broadband antennas contain micro-transmitters designed to manipulate human cognitive frequencies and harvest thoughts.", 0),
    ("World Economic Forum orders all citizens to surrender private property by end of month",
     "Leaked audio recordings from a private Davos dinner show globalist elites declaring that private home ownership and bank accounts will be officially outlawed and replaced by social credit tokens next month.", 0),
    ("NASA admits moon landings were staged in Hollywood studio after whistleblower releases footage",
     "A former special effects director for Stanley Kubrick has published uncompressed 35mm film reels proving the Apollo moon landings were filmed on a soundstage in Burbank California. Share before it is removed!", 0),
    ("Drinking boiled lemon water and baking soda destroys all viral infections overnight",
     "A renowned rogue physician reveals the suppressed remedy that eliminates every pathogen from your bloodstream in 12 hours. Hospital administrators tried to revoke his license to keep patients sick!", 0),
    ("Government introduces mandatory microchips inside new driving licenses to track all driving routes",
     "Classified transportation department documents expose an unannounced plan to plant RFID tracking chips inside replacement drivers licenses to monitor vehicle speed and location in real time without warrant.", 0),
    ("Alien spacecraft wreckage recovered from deep trench in Pacific ocean by private billionaires",
     "Leaked submarine sonar logs reveal a metallic flying saucer discovered resting four miles beneath sea level. Elite oligarchs have dispatched deep-sea excavators to retrieve alien anti-gravity technology.", 0)
]

print("\n--- Realistic Unseen Benchmark (16 diverse real-world news articles) ---")
correct = 0
for title, text, label in test_cases:
    cleaned = clean_text(title + " " + text)
    vec_sample = vec.transform([cleaned])
    pred = model.predict(vec_sample)[0]
    
    # Probability or decision
    if hasattr(model, 'predict_proba'):
        prob = model.predict_proba(vec_sample)[0][1]
    elif hasattr(model, 'decision_function'):
        df_val = model.decision_function(vec_sample)[0]
        prob = 1 / (1 + np.exp(-df_val))
    else:
        prob = float(pred)
        
    is_correct = (pred == label)
    if is_correct:
        correct += 1
    mark = "PASS" if is_correct else "FAIL"
    lbl_str = "Real" if label == 1 else "Fake"
    pred_str = "Real" if pred == 1 else "Fake"
    print(f"[{mark}] Actual: {lbl_str:<4} | Pred: {pred_str:<4} (P_Real={prob*100:.1f}%) | {title[:60]}...")

unseen_acc = (correct / len(test_cases)) * 100
print(f"\nUnseen Real-World Benchmark Accuracy: {unseen_acc:.2f}% ({correct}/{len(test_cases)})")
