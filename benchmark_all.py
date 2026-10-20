"""
Benchmark all trained candidate models on the unseen real-world test cases.
"""
import joblib
import numpy as np
from src.preprocessor import clean_text

all_models = joblib.load('models/all_models.pkl')
vec = joblib.load('models/vectorizer.pkl')

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

print("=" * 70)
print(f"{'Model Name':<38} | {'Correct':<8} | {'Unseen Acc':<10}")
print("=" * 70)

for name, model in all_models.items():
    correct = 0
    for title, text, label in test_cases:
        cleaned = clean_text(title + " " + text)
        vec_sample = vec.transform([cleaned])
        pred = model.predict(vec_sample)[0]
        if pred == label:
            correct += 1
    acc = (correct / len(test_cases)) * 100
    print(f"{name:<38} | {correct:>2}/{len(test_cases)}   | {acc:>6.2f}%")

print("=" * 70)
