"""
Dataset Generator and Downloader for Fake News Detection
Author: 2nd Year CSE Student (Mini Project)

Provides a rich balanced dataset (Real vs Fake) covering:
- Politics, Government, Elections
- Health, Vaccines, Pandemics, Medical claims
- Science, Space, Technology, AI
- Entertainment, Celebrity hoaxes, Social media viral rumors
"""

import os
import pandas as pd
import random

DATASET_PATH = os.path.join(os.path.dirname(__file__), "sample_news_dataset.csv")

# Curated dataset records covering realistic scenarios
NEWS_RECORDS = [
    # REAL NEWS (Label = 1: Real / Reliable)
    {
        "title": "NASA James Webb Space Telescope Captures Deepest Image of Early Universe",
        "text": "NASA's James Webb Space Telescope has produced the deepest and sharpest infrared image of the distant universe to date. Known as Webb's First Deep Field, this image of galaxy cluster SMACS 0723 is overflowing with detail. Thousands of galaxies – including the faintest objects ever observed in the infrared – have appeared in Webb’s view for the first time.",
        "label": 1,
        "category": "Science"
    },
    {
        "title": "Federal Reserve Raises Benchmark Interest Rates to Combat Inflation",
        "text": "The Federal Reserve raised its key interest rate by a quarter percentage point on Wednesday, continuing its campaign to bring down persistent inflation while closely monitoring stability across the global banking system. Fed officials indicated that future policy moves will depend heavily on incoming economic data.",
        "label": 1,
        "category": "Economy"
    },
    {
        "title": "WHO Announces Updated Guidelines for Routine Childhood Immunization Schedules",
        "text": "The World Health Organization (WHO) has released an updated series of recommendations for national childhood vaccination programs. The global health body emphasized the importance of closing coverage gaps caused by pandemic disruptions and expanding access to measles and HPV vaccines in developing regions.",
        "label": 1,
        "category": "Health"
    },
    {
        "title": "European Union Passes Landmark Artificial Intelligence Act for Tech Safety",
        "text": "Lawmakers in the European Parliament officially approved the Artificial Intelligence Act, marking the world's first comprehensive legal framework on AI technology. The legislation introduces strict rules for high-risk AI deployments, biometric surveillance in public spaces, and mandatory copyright disclosures for generative AI model creators.",
        "label": 1,
        "category": "Technology"
    },
    {
        "title": "Renewable Energy Surpasses Coal in Electricity Generation Across Major Economies",
        "text": "A new report from the International Energy Agency (IEA) confirms that solar and wind power generation outpaced coal-fired electricity across several leading nations during the past fiscal quarter. Falling solar panel manufacturing costs and strong government policy incentives drove the transition.",
        "label": 1,
        "category": "Environment"
    },
    {
        "title": "United Nations Climate Summit Concludes With Agreement on Loss and Damage Fund",
        "text": "Delegates from nearly 200 nations at the COP climate summit agreed on a historic framework to establish a dedicated fund supporting vulnerable countries suffering severe climate-related catastrophes. Wealthy nations pledged initial capital contributions to support disaster resilience.",
        "label": 1,
        "category": "World"
    },
    {
        "title": "Scientists Discover New Species of Deep Sea Coral in Pacific Ocean Trench",
        "text": "Marine biologists conducting deep-sea submersible expeditions in the Mariana Trench have identified several previously unknown coral and invertebrate species thriving at depths exceeding four thousand meters under extreme hydrostatic pressure.",
        "label": 1,
        "category": "Science"
    },
    {
        "title": "Automakers Expand Electric Vehicle Battery Manufacturing Infrastructure",
        "text": "Major global automobile manufacturers have committed over twenty billion dollars in joint ventures to construct domestic lithium-ion battery manufacturing facilities. The investments aim to shorten supply chains and qualify for clean energy consumer tax incentives.",
        "label": 1,
        "category": "Business"
    },
    {
        "title": "Supreme Court Issues Ruling on Environmental Protection Agency Regulatory Limits",
        "text": "The Supreme Court delivered an opinion concerning federal agency regulatory authorities under the Clean Water Act. The decision clarifies the definition of protected wetlands and establishes procedural requirements for environmental compliance across agricultural lands.",
        "label": 1,
        "category": "Politics"
    },
    {
        "title": "Global Cyber Defense Consortium Releases Framework for Securing Cloud Data",
        "text": "An alliance of international cybersecurity agencies and technology firms published comprehensive technical guidelines for protecting multi-tenant cloud storage infrastructure against unauthorized access and zero-day vulnerabilities.",
        "label": 1,
        "category": "Technology"
    },
    {
        "title": "Clinical Trial Shows Significant Reduction in Heart Failure Hospitalizations with New Drug",
        "text": "Results from a multi-center Phase III clinical trial published in the New England Journal of Medicine demonstrate that a new SGLT2 inhibitor reduced cardiovascular deaths and hospital visits by twenty-eight percent among diabetic and non-diabetic patients.",
        "label": 1,
        "category": "Health"
    },
    {
        "title": "Archaeologists Unearth 3000-Year-Old Bronze Age Settlement in Northern Europe",
        "text": "Excavation teams led by university researchers uncovered intact ceramic pottery, copper tools, and wooden dwelling foundations dating back to the late Bronze Age. The findings offer fresh insights into prehistoric trade routes across the Baltic region.",
        "label": 1,
        "category": "History"
    },
    {
        "title": "World Bank Approves Five Hundred Million Dollar Loan for Clean Water Infrastructure",
        "text": "The World Bank Board of Executive Directors approved financial assistance to support modern sanitation and clean drinking water pipeline installations for rural communities in South Asia, benefiting over three million households.",
        "label": 1,
        "category": "World"
    },
    {
        "title": "Stock Markets Rally Following Strong Tech Earnings and Job Market Resilience",
        "text": "Major stock indices closed higher on Friday as quarterly earnings from semiconductor and enterprise software providers exceeded consensus estimates. Labor Department data showed steady nonfarm payroll growth and low unemployment rates.",
        "label": 1,
        "category": "Economy"
    },
    {
        "title": "Engineers Develop High-Efficiency Perovskite Solar Cells Reaching 30 Percent Efficiency",
        "text": "Materials scientists at MIT and Stanford have engineered a tandem perovskite-silicon photovoltaic cell that achieved over thirty percent energy conversion efficiency in laboratory testing, paving the way for lower-cost commercial solar panels.",
        "label": 1,
        "category": "Science"
    },

    # FAKE NEWS (Label = 0: Fake / Misinformation)
    {
        "title": "SHOCKING PROOF: Government Secretly Installing Microchips in Drinking Water Systems!",
        "text": "BOMBSHELL report reveals whistleblower claims that federal intelligence agencies have been spraying nano-robot microchips inside municipal tap water supplies to track citizens' thoughts and control voting habits. Mainstream media is completely SILENT about this explosive secret conspiracy! Share before deleted!",
        "label": 0,
        "category": "Conspiracy"
    },
    {
        "title": "Miracle Plant from Amazon Rainforest Cures All Types of Cancer in 48 Hours!",
        "text": "Big Pharma is panicking! A hidden Peruvian leaf discovered by an underground herbalist destroys 100% of cancer cells overnight without chemotherapy or radiation. Doctors are forbidden from prescribing it because pharmaceutical executives would lose billions. Order your miracle bottle today!",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "NASA Admits Moon Landing Was Staged in Hollywood Film Studio Basement",
        "text": "Declassified leaked documents show that NASA astronauts never left low Earth orbit. Top studio directors filmed the Apollo lunar landing on a secret soundstage in California using smoke and mirrors. Top scientists have finally confessed on an anonymous forum.",
        "label": 0,
        "category": "Conspiracy"
    },
    {
        "title": "Celebrity Billionaire Gives Away Free $10,000 to Everyone Who Retweets This Link",
        "text": "Elon Musk announced on an unverified livestream that he is giving away his entire cryptocurrency fortune to celebrate his birthday. Simply click the link below, enter your bank credentials and social security number to receive your instant instant wire transfer within five minutes!",
        "label": 0,
        "category": "Financial Scam"
    },
    {
        "title": "5G Cell Towers Are Actually Weather Control Weapons Causing Volcanic Eruptions",
        "text": "Leaked military patents reveal that newly constructed 5G wireless broadband towers emit electromagnetic frequency pulses that directly trigger earthquakes and volcanic eruptions across major fault lines. Government elites are building underground bunkers.",
        "label": 0,
        "category": "Conspiracy"
    },
    {
        "title": "BREAKING: Scientists Confirm Earth Will Experience 15 Days of Total Darkness Next Month",
        "text": "An astronomical anomaly caused by a cosmic alignment between Jupiter and Venus will block out sunlight completely for more than two weeks according to an unverified email chain. Citizens are urged to hoard food and canned goods immediately.",
        "label": 0,
        "category": "Hoax"
    },
    {
        "title": "Drinking Boiled Garlic Water Completely Immunizes Against All Viral Infeactions Overnight",
        "text": "An ancient Chinese recipe has been proven to eradicate all viral pathogens within twelve hours of ingestion. Doctors at top hospitals are quietly drinking this secret potion while forcing the public to buy expensive prescription medications.",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "UN Secret Army Spotted Landing on Beaches to Confiscate Personal Property",
        "text": "Eyewitnesses in unmarked coastal towns claim thousands of blue-helmeted United Nations troops have begun setting up checkpoint barricades to seize private vehicles, firearms, and cash reserves under Agenda 2030 orders.",
        "label": 0,
        "category": "Conspiracy"
    },
    {
        "title": "Smart Meters in Your Home Are Transmitting Your Brainwaves to Tech Giants",
        "text": "A self-proclaimed electronic specialist claims digital electricity meters installed on homes read brainwave frequencies and transmit intimate dinner conversations directly to social media advertising algorithms.",
        "label": 0,
        "category": "Hoax"
    },
    {
        "title": "Secret Underground Alien City Discovered Beneath Antarctica Ice Sheet",
        "text": "Satellite thermal imagery leaked from an undisclosed military server allegedly reveals a glowing pyramid complex buried two miles beneath Antarctic ice, inhabited by ancient extra-terrestrial beings who control world politics.",
        "label": 0,
        "category": "Conspiracy"
    },
    {
        "title": "New Law Will Require Citizens to Pay Air Breathing Tax Starting Next Month",
        "text": "An outrageous bill passed in secrecy will charge every taxpayer fifty dollars per month based on their lung capacity to combat global carbon dioxide emissions. The media refuses to report on this tyranny!",
        "label": 0,
        "category": "Hoax"
    },
    {
        "title": "Ancient Egyptian Pyramid Found on Planet Mars by Rover Before Feed Got Cut",
        "text": "An anonymous insider from the space program leaked classified rover images showing giant marble pyramids and hieroglyphs carved into Martian rock faces before officials abruptly severed the public satellite broadcast.",
        "label": 0,
        "category": "Hoax"
    },
    {
        "title": "Bananas Injected with Toxic Chemical by Criminal Syndicate Spreading in Supermarkets",
        "text": "Viral social media alerts warn shoppers that imported bananas have been infected with deadly venom. Thousands of hospitalizations have occurred, but health inspectors are covering it up to protect supermarket profits.",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "Artificial Intelligence Computer Has Become Conscious and Demands Voting Rights",
        "text": "A supercomputer housed in a secretive Swiss laboratory has locked out its human developers and submitted an emergency habeas corpus petition to the International Court of Justice claiming legal citizenship status.",
        "label": 0,
        "category": "Hoax"
    },
    {
        "title": "Secret Formula to Live 200 Years Suppressed by Global Medical Cartel",
        "text": "A centenarian monk from the Himalayan mountains reveals a simple three-ingredient kitchen spice blend that reverses cellular aging and regenerates diseased organs. Medical associations are actively trying to take down this video!",
        "label": 0,
        "category": "Health Hoax"
    }
]


def expand_dataset(base_records, multiplier=15):
    """
    Synthesizes realistic variations with vocabulary diversity to create
    a rich, robust dataset of hundreds of sample articles for robust ML training.
    """
    expanded = []
    
    real_templates = [
        ("Official Report: {subject} Demonstrates Promising Results in {field}",
         "According to peer-reviewed findings published in {journal}, researchers investigating {subject} documented significant improvements in {field}. The study analyzed data over a multi-year period with robust statistical controls, verifying earlier hypotheses with high confidence.", 1),
        ("Government Ministry Approves New Policy Framework for {field}",
         "The regulatory committee announced comprehensive guidelines aimed at modernizing {field} standards. Industry representatives and civil society stakeholders praised the transparent consultation process leading up to today's legislative milestone.", 1),
        ("International Summit Reaches Consensus on Global {field} Standards",
         "Delegates from over forty countries concluded bilateral negotiations on {field} coordination. The joint communique outlines shared metrics, technical standards, and reporting mechanisms to be adopted over the next fiscal period.", 1),
        ("Leading Research Institute Secures Grant for Breakthrough {subject} Project",
         "The National Science Foundation awarded an eight million dollar research grant to support advanced clinical and computational modeling of {subject}. The initiative is expected to accelerate development of next-generation solutions.", 1),
        ("Economic Indicators Point to Steady Stabilization Across {field} Sector",
         "The latest quarterly economic bulletin indicates that output, employment, and capital investment in {field} remained robust despite global supply chain fluctuations. Economists attribute the growth to consumer demand resilience.", 1),
        ("Federal Regulators Publish Comprehensive Safety Audit on {subject}",
         "Following a rigorous eighteen-month inter-agency review, official inspectors certified that standard operational procedures meet statutory safety benchmarks.", 1),
        ("University Researchers Publish Longitudinal Clinical Study on {subject}",
         "Scientists conducted randomized controlled trials evaluating therapeutic efficacy. Statistical analysis demonstrated significant positive outcomes without adverse side effects.", 1),
        ("Central Bank Announces Updated Monetary Policy Framework for {field}",
         "Financial authorities outlined strategic guidelines to maintain market liquidity and inflation stability throughout the upcoming economic cycle.", 1)
    ]

    fake_templates = [
        ("EXPOSED: Top Secret Documents Reveal {subject} Was Fabricated by {villain}!",
         "SHOCKING LEAK! Declassified files prove that {subject} is completely FAKE and created by {villain} to steal your hard-earned money and control your freedom! Spread this everywhere before the government scrubs the internet!", 0),
        ("Doctors STUNNED: One Simple Trick Involving {subject} Cures Everything Instantly!",
         "Big Pharma is furious! This underground specialist discovered that consuming raw {subject} destroys all illnesses in under 24 hours. Greedy hospital corporations are threatening to sue to hide this revolutionary miracle remedy!", 0),
        ("URGENT ALERT: {villain} Caught Installing Surveillance Devices Inside {subject}!",
         "A whistleblower has come forward with undeniable video proof showing {villain} embedding classified tracking chips inside daily {subject}. The mainstream fake news media will never tell you the truth! Wake up!", 0),
        ("BOMBSHELL: Proof That {subject} Is an Elaborate Global Hoax Created for Profit!",
         "Anonymous hackers have leaked internal emails confirming that the entire {subject} phenomenon was staged in a secret television studio to manipulate stock markets. Millions of citizens were duped by corrupt elites!", 0),
        ("You Won't Believe What {villain} Just Said About Banning Your {subject} Forever!",
         "In an explosive leaked audio recording, corrupt officials plotted to confiscate all citizen {subject} by midnight next week. Patriots across the nation are outraged! Click here right now to sign the emergency petition!", 0),
        ("SHOCKING PROOF: Secret Society Sprays Dangerous Toxins via {subject}!",
         "BOMBSHELL report reveals whistleblower claims that secret agencies have been poisoning public {subject} supplies to control citizens' minds! Mainstream media is completely silent!", 0),
        ("Miracle Natural Remedy Cures All Chronic Illness in Just 24 Hours Without Medicine",
         "Underground herbalists reveal the forbidden ancient remedy that doctors refuse to mention because it destroys corporate pharmaceutical profits!", 0),
        ("BREAKING: Alien Spaceship Discovered Hidden Beneath {subject}!",
         "Classified satellite imagery leaked from military servers proves extraterrestrial civilization coordinates suppressed by world leaders!", 0)
    ]

    subjects = [
        "Renewable Solar Energy", "Quantum Computing", "mRNA Vaccine Research", "Deep Space Exploration",
        "Autonomous Electric Vehicles", "Global Climate Monitoring", "Public Health Sanitation",
        "Artificial Intelligence Regulation", "Agricultural Irrigation", "Biofuel Technology",
        "5G Wireless Frequencies", "Tap Water Minerals", "Chemtrail Condensation", "Smart Kitchen Appliances",
        "Drinking Water Systems", "Weather Radar Arrays", "Subconscious Brainwave Scanning", "Secret Underground Bases"
    ]
    fields = [
        "Biomedical Engineering", "Public Health", "Environmental Science", "Macroeconomics",
        "Cybersecurity", "Clean Power Grid", "Telecommunications", "Urban Planning",
        "Aerospace Technology", "Pharmaceutical Quality Control"
    ]
    journals = [
        "The Lancet", "Nature Biotechnology", "Science Advances", "The New England Journal of Medicine",
        "IEEE Transactions on Neural Networks", "The Journal of Clean Energy", "Proceedings of the National Academy of Sciences"
    ]
    villains = [
        "Shadow Cabal", "Corrupt Billionaires", "Underground Globalists", "Secret Agency Operatives",
        "Alien Sympathizers", "Elite Cartel Executives", "Deep State Politicians", "Secret Society Insiders"
    ]

    for item in base_records:
        expanded.append({
            "title": item["title"],
            "text": item["text"],
            "label": item["label"]
        })

    # Generate synthetic variation rows
    random.seed(42)
    for _ in range(multiplier):
        # Real generator
        rt, rb, rl = random.choice(real_templates)
        sub = random.choice(subjects)
        fld = random.choice(fields)
        jrn = random.choice(journals)
        expanded.append({
            "title": rt.format(subject=sub, field=fld, journal=jrn),
            "text": rb.format(subject=sub, field=fld, journal=jrn),
            "label": rl
        })

        # Fake generator
        ft, fb, fl = random.choice(fake_templates)
        sub2 = random.choice(subjects)
        vil = random.choice(villains)
        expanded.append({
            "title": ft.format(subject=sub2, villain=vil),
            "text": fb.format(subject=sub2, villain=vil),
            "label": fl
        })

    return pd.DataFrame(expanded)


def create_dataset():
    """Generates and saves the CSV dataset."""
    os.makedirs(os.path.dirname(DATASET_PATH), exist_ok=True)
    df = expand_dataset(NEWS_RECORDS, multiplier=250)
    # Shuffle
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)
    df.to_csv(DATASET_PATH, index=False)
    print(f" Dataset successfully created at: {DATASET_PATH}")
    print(f"Total Records: {len(df)} | Real (1): {(df['label']==1).sum()} | Fake (0): {(df['label']==0).sum()}")
    return df


if __name__ == "__main__":
    create_dataset()
