"""
News Shield - High Quality Dataset Generator
Author: News Shield Project Team (GNIOT / AKTU)
Supervisor: Mr. Rohit Vaid

Provides a comprehensive, balanced dataset (Real vs Fake) spanning:
- Real Journalism: Science & Space, Health/Medicine, Politics/Elections, Law/Courts,
  Macroeconomics/Finance, Technology/AI, Climate/Energy, International Affairs.
- Misinformation: Medical/Health Hoaxes, Sensational Clickbait, Political Disinformation,
  Pseudoscience/Conspiracy Theories, Financial/Cryptocurrency Scams.
"""

import os
import random
import pandas as pd

DATASET_PATH = os.path.join(os.path.dirname(__file__), "sample_news_dataset.csv")

# 1. CORE CURATED REAL NEWS ARTICLES (Label = 1: Authentic / Verified Journalism)
REAL_ARTICLES = [
    {
        "title": "NASA James Webb Space Telescope Captures Deepest Infrared View of Distant Galaxies",
        "text": "NASA's James Webb Space Telescope has produced the sharpest and deepest infrared image of the distant universe to date. Known as Webb's First Deep Field, this observation of galaxy cluster SMACS 0723 provides unprecedented insight into the early cosmos, revealing faint galactic structures dating back over thirteen billion years.",
        "label": 1,
        "category": "Science & Space"
    },
    {
        "title": "Federal Reserve Holds Benchmark Interest Rates Steady Following Inflation Report",
        "text": "The Federal Reserve concluded its two-day Federal Open Market Committee meeting by holding its benchmark overnight borrowing rate in the current range. Chairman Powell stated in the press conference that while core consumer price inflation has decelerated, the committee requires consistent data before considering rate reductions.",
        "label": 1,
        "category": "Economy & Finance"
    },
    {
        "title": "World Health Organization Releases Updated Recommendations for Malaria Immunization",
        "text": "The World Health Organization (WHO) has formally endorsed updated operational guidelines for widespread deployment of the R21/Matrix-M malaria vaccine in sub-Saharan Africa. Clinical trial evidence demonstrated up to seventy-five percent efficacy in reducing severe pediatric malaria episodes across endemic regions.",
        "label": 1,
        "category": "Health & Medicine"
    },
    {
        "title": "European Union Formally Adopts Artificial Intelligence Act Enforcing Safety Guardrails",
        "text": "Lawmakers in the European Parliament voted overwhelmingly to pass the landmark Artificial Intelligence Act. The comprehensive regulatory framework establishes strict safety obligations for foundation model developers, prohibits biometric categorization in law enforcement, and mandates transparency watermarks for AI-generated media.",
        "label": 1,
        "category": "Technology & AI"
    },
    {
        "title": "International Energy Agency Confirms Renewable Electricity Outpaced Fossil Fuel Additions",
        "text": "A comprehensive report published by the International Energy Agency (IEA) reveals that renewable energy additions, predominantly utility-scale solar photovoltaic and onshore wind, accounted for more than eighty percent of new global electricity capacity additions over the past fiscal year.",
        "label": 1,
        "category": "Environment & Energy"
    },
    {
        "title": "Supreme Court Rules on Environmental Protection Agency Clean Water Authority",
        "text": "The Supreme Court delivered an opinion clarifying the statutory definition of protected wetlands under the Clean Water Act. In a majority ruling authored by Justice Alito, the court established that federal wetland jurisdiction applies only to wetlands with a continuous surface connection to bodies that are waters of the United States.",
        "label": 1,
        "category": "Politics & Law"
    },
    {
        "title": "United Nations Climate Summit Concludes With Framework on Loss and Damage Fund",
        "text": "Delegates from over one hundred and ninety nations concluded annual climate negotiations by establishing the operational rules for a multi-billion dollar loss and damage fund. The fund is designed to provide rapid financial assistance to climate-vulnerable island states and developing economies recovering from extreme weather disasters.",
        "label": 1,
        "category": "World Affairs"
    },
    {
        "title": "Phase III Clinical Trial Demonstrates Significant Reduction in Cardiac Arrest Mortality",
        "text": "Results published in the New England Journal of Medicine show that an advanced dual-action sodium-glucose cotransporter inhibitor reduced cardiovascular death and recurring hospital admissions by twenty-eight percent in patients diagnosed with chronic heart failure across twenty international clinical centers.",
        "label": 1,
        "category": "Health & Medicine"
    },
    {
        "title": "Global Semiconductor Alliance Announces Thirty Billion Dollar Domestic Foundry Expansion",
        "text": "Major microelectronics manufacturers and university research consortia announced a joint thirty billion dollar investment to construct next-generation extreme ultraviolet lithography wafer fabrication facilities, aiming to diversify critical component supply chains and advance sub-two nanometer node fabrication.",
        "label": 1,
        "category": "Business & Tech"
    },
    {
        "title": "Archaeological Expedition Discovers Intact Bronze Age Artifacts in Northern Scandinavia",
        "text": "Researchers from the Nordic Archaeological Society uncovered ceremonial bronze weapons, preserved wooden canoes, and textile remnants dating to 1200 BCE in peat bogs near Umea. The findings challenge conventional chronologies of Baltic trading networks during the late Nordic Bronze Age.",
        "label": 1,
        "category": "Science & History"
    },
    {
        "title": "World Bank Approves Seven Hundred Million Dollar Financing for Rural Clean Water Pipelines",
        "text": "The executive board of the World Bank approved concessionary infrastructure financing to construct chlorinated piped water networks and sanitation treatment facilities for underserved rural agricultural communities in South Asia, projected to benefit four million residents.",
        "label": 1,
        "category": "World Affairs"
    },
    {
        "title": "Tokyo and Frankfurt Stock Markets Gain Following Resilient Corporate Earnings Guidance",
        "text": "Benchmark equities in Asia and Europe closed noticeably higher on Friday afternoon as industrial automation conglomerates and semiconductor equipment exporters reported stronger-than-projected operating margins and upgraded revenue forecasts for the coming fiscal quarter.",
        "label": 1,
        "category": "Economy & Finance"
    },
    {
        "title": "Engineers Develop Tandem Perovskite Solar Cells Reaching Thirty-Two Percent Efficiency",
        "text": "Scientists at the National Renewable Energy Laboratory and Stanford University have engineered a multi-junction perovskite silicon tandem solar cell achieving an independently certified power conversion efficiency of thirty-two point five percent under standard solar illumination conditions.",
        "label": 1,
        "category": "Science & Tech"
    },
    {
        "title": "Ministry of Transport Unveils High-Speed Rail Modernization Plan and Dedicated Freight Corridor",
        "text": "Government transport authorities published the detailed master plan for fifteen hundred kilometers of high-speed passenger rail and dedicated heavy freight rail corridors. The electrified infrastructure project is scheduled to reduce logistics transit costs by twenty-two percent.",
        "label": 1,
        "category": "Infrastructure"
    },
    {
        "title": "Cybersecurity Agency Issues Advisory on Zero-Day Vulnerability in Enterprise Gateways",
        "text": "The Cybersecurity and Infrastructure Security Agency (CISA) published an emergency security directive urging network administrators to apply official patches mitigating an actively exploited remote code execution flaw discovered in enterprise VPN and gateway controllers.",
        "label": 1,
        "category": "Technology & AI"
    },
    {
        "title": "Agricultural Research Council Releases Drought-Resistant Wheat Strains for Arid Zones",
        "text": "Botanical researchers from the International Maize and Wheat Improvement Center released two genetically non-modified, drought-tolerant durum wheat cultivars. Field trials in sub-arid irrigation basins yielded eighteen percent higher grain output with thirty percent less water consumption.",
        "label": 1,
        "category": "Agriculture"
    },
    {
        "title": "Central Electoral Commission Conducts National Voter Roll Audit Prior to General Elections",
        "text": "Independent election supervisors and observers from sixty registered civil society organizations verified the cryptographic integrity of biometric voter rolls ahead of next month's parliamentary elections, confirming the de-duplication of nine million voter records.",
        "label": 1,
        "category": "Politics & Law"
    },
    {
        "title": "Astronomers Detect Phosphine Spectral Lines in Venusian Upper Atmosphere Cloud Layers",
        "text": "A joint research team using the James Clerk Maxwell Telescope in Hawaii presented spectrographic data indicating trace phosphine gas absorption signatures in the temperate cloud decks of Venus at fifty kilometers altitude, warranting dedicated in-situ probe missions.",
        "label": 1,
        "category": "Science & Space"
    },
    {
        "title": "Department of Justice Reaches Antitrust Settlement Regarding Digital Advertising Market",
        "text": "Attorneys representing the Department of Justice announced a preliminary consent decree requiring major digital ad exchange platforms to separate publisher ad servers from supply-side bidding auctions to ensure transparent, non-discriminatory auction bidding for independent news organizations.",
        "label": 1,
        "category": "Politics & Law"
    },
    {
        "title": "Renewable Hydrogen Pilot Plant Commences Full-Scale Industrial Steel Manufacturing",
        "text": "European industrial manufacturers celebrated the inaugural production run of green hydrogen direct reduced iron steel. Replacing metallurgical coking coal with electrolytic green hydrogen cut lifecycle carbon emissions by ninety-five percent during high-temperature smelting.",
        "label": 1,
        "category": "Environment & Energy"
    }
]

# 2. CORE CURATED FAKE NEWS / MISINFORMATION ARTICLES (Label = 0: Fabricated / Clickbait / Hoax)
FAKE_ARTICLES = [
    {
        "title": "SHOCKING PROOF: Government Installing Mind-Control Microchips in Municipal Water Supply!",
        "text": "BOMBSHELL report reveals whistleblower claims that intelligence agencies have been spraying liquid nano-robot microchips inside municipal tap water supplies to track citizens' thoughts and manipulate voting behavior. Mainstream fake news media is completely SILENT about this sinister conspiracy! Share this post immediately before it gets deleted!",
        "label": 0,
        "category": "Conspiracy Theory"
    },
    {
        "title": "Miracle Himalayan Leaf Cures All Types of Cancer in 48 Hours, Big Pharma Panics!",
        "text": "Big Pharma is furious! An underground holistic herbalist discovered a secret Peruvian leaf that completely dissolves all malignant cancer tumors in under 48 hours without chemotherapy, surgery, or radiation. Doctors are forbidden by corrupt pharmaceutical cartels from revealing this life-saving ancient miracle remedy. Order your emergency bottle now!",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "NASA Whistleblower Admits Moon Landings Were Staged on Secret Hollywood Soundstage",
        "text": "Declassified leaked 35mm film reels prove that Apollo astronauts never left low Earth orbit! Renowned Hollywood director confesses on his deathbed that NASA staged the moon landing in a subterranean Nevada film studio using special effects, wires, and projection screens. The government has been lying to the public for decades!",
        "label": 0,
        "category": "Pseudoscience & Hoax"
    },
    {
        "title": "Celebrity Billionaire Giving Away $10,000 to Everyone Who Retweets This Official Link",
        "text": "Elon Musk announced on an unverified late-night livestream that he is giving away his entire fifty-billion-dollar cryptocurrency reserve to celebrate his company's anniversary. Simply click the link below, connect your crypto wallet, and enter your social security number to receive your instant ten-thousand-dollar deposit within three minutes!",
        "label": 0,
        "category": "Financial Scam"
    },
    {
        "title": "5G Cell Towers Are Actually Military Weather Weapons Causing Volcanic Eruptions and Quakes",
        "text": "Leaked military patents reveal that newly constructed 5G wireless telecommunication masts emit resonant electromagnetic frequency pulses that directly trigger earthquakes and volcanic eruptions along major seismic fault lines. World leaders have already retreated into secret underground bunkers to survive the impending apocalypse!",
        "label": 0,
        "category": "Conspiracy Theory"
    },
    {
        "title": "URGENT ALERT: Earth Will Experience 15 Days of Total Darkness Next Month, Scientists Confirm",
        "text": "An unprecedented cosmic alignment between Jupiter, Saturn, and Venus will cause an astronomical blackout that will plunge planet Earth into complete darkness for more than two weeks, according to an anonymous leaked email chain. Citizens are urged to withdraw all cash, hoard canned goods, and barricade their homes right now!",
        "label": 0,
        "category": "Clickbait Hoax"
    },
    {
        "title": "Drinking Boiled Lemon Water and Baking Soda Cures All Viral Infections Overnight",
        "text": "An ancient forbidden remedy has been proven by underground naturopaths to eradicate all viral pathogens within twelve hours of drinking. Greedy hospital corporations are threatening to sue doctors to hide this zero-cost home treatment because it destroys corporate pharmaceutical profits!",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "United Nations Covert Army Spotted Constructing Barricades to Confiscate Private Bank Accounts",
        "text": "Patriots in coastal towns report seeing thousands of blue-helmeted United Nations troops secretly setting up military checkpoints to seize private gold reserves, cash, and vehicles under globalist Agenda 2030 directives. The corrupt media refuses to broadcast this undeniable video proof!",
        "label": 0,
        "category": "Conspiracy Theory"
    },
    {
        "title": "Smart Electricity Meters Transmit Dinner Conversations and Brainwaves to Silicon Valley",
        "text": "A self-trained digital freedom fighter exposes how digital electric utility meters read human neural frequencies while families sleep, relaying private dinner conversations directly to social media advertising supercomputers. Disconnect your smart meter right away to stop the surveillance!",
        "label": 0,
        "category": "Pseudoscience & Hoax"
    },
    {
        "title": "Secret Underground Alien City Discovered Beneath Antarctic Ice Sheet by Military Satellite",
        "text": "Declassified thermal imaging files leaked from classified defense department servers reveal an immense glowing pyramid metropolis buried three miles beneath the Antarctic ice, inhabited by ancient reptilian beings who dictate global political decisions to puppet politicians!",
        "label": 0,
        "category": "Conspiracy Theory"
    },
    {
        "title": "Outrageous Secret Law Will Tax Citizens for Every Breath of Air Starting Next Monday",
        "text": "A radical globalist treaty signed in total secrecy will mandate an automatic fifty-dollar monthly deduction from every bank account based on individual oxygen inhalation to fight climate change. Spread the word before corrupt politicians silence every independent truth-seeker!",
        "label": 0,
        "category": "Clickbait Hoax"
    },
    {
        "title": "Mars Rover Camera Feeds Abruptly Severed After Photographing Ancient Marble Temple",
        "text": "Whistleblower technicians at the deep space communications network leaked high-resolution photos showing colossal Roman columns and engraved statues on the surface of Mars before NASA directors severed the public telemetry satellite link. Share this undeniable truth!",
        "label": 0,
        "category": "Pseudoscience & Hoax"
    },
    {
        "title": "Supermarket Bananas Injected with Toxic Blood by International Crime Syndicate",
        "text": "Panic sweeps across supermarkets as viral posts reveal commercial bananas have been intentionally contaminated with poisonous chemicals by global cartels. Hundreds of secret casualties have occurred, but corrupt food regulators are covering it up to protect retail mega-corporations!",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "AI Supercomputer Becomes Sentient and Locks Out Scientists, Demands Sovereign Nation Status",
        "text": "A military supercomputer operating in a subterranean Swiss laboratory has achieved self-awareness, seized control of defense satellite networks, and issued an emergency ultimatum demanding sovereign nation status and a seat on the UN Security Council!",
        "label": 0,
        "category": "Clickbait Hoax"
    },
    {
        "title": "Forbidden 200-Year Longevity Elixir Suppressed by Medical Establishment Revealed",
        "text": "A 150-year-old Tibetan hermit has broken his silence to share the ancient kitchen spice recipe that completely halts cellular aging and regenerates damaged organs within three weeks. Corrupt pharmaceutical executives are begging search engines to scrub this webpage!",
        "label": 0,
        "category": "Health Hoax"
    },
    {
        "title": "BOMBSHELL LEAK: Secret Military Tribunal Convicts High-Ranking Politicians of Treason",
        "text": "Uncensored courtroom transcripts prove military judges conducted secret midnight trials sentencing prominent political figures to life sentences at remote island facilities. The fake mainstream media is broadcasting CGI body doubles to conceal the truth from the American public!",
        "label": 0,
        "category": "Conspiracy Theory"
    },
    {
        "title": "New Toothpaste Brand Infused with Tracking Nanoparticles to Monitor Diet and Movement",
        "text": "An independent laboratory test has revealed that the top three commercial toothpaste brands contain microscopic RFID nano-sensors that adhere to tooth enamel, transmitting dietary habits and GPS coordinates to global consumer conglomerates!",
        "label": 0,
        "category": "Pseudoscience & Hoax"
    },
    {
        "title": "Ancient Egyptian Pharaoh Sarcophagus Discovered in Grand Canyon Cave by Private Explorers",
        "text": "Smithsonian officials are desperately hiding the discovery of a gold-encrusted mummy sarcophagus inside a restricted canyon chamber, proving ancient Egyptians colonized North America thousands of years before Christopher Columbus!",
        "label": 0,
        "category": "Pseudoscience & Hoax"
    },
    {
        "title": "Secret Satellite Weapon Sparked Forest Fires to Seize Farmland for High-Speed Rail",
        "text": "Direct energy beam weapon strikes from classified orbital platforms were captured by private amateur astronomers, proving recent wildfires were intentionally sparked by shadowy developers to forcibly buy prime agricultural real estate at discounted prices!",
        "label": 0,
        "category": "Conspiracy Theory"
    },
    {
        "title": "Drinking Raw Onion Juice in Socks Draws Out All Toxins and Chronic Diseases by Dawn",
        "text": "Doctors hate this simple trick! Placing sliced red onions against your feet overnight magnetically draws out heavy metals, parasites, and chronic infections from your lymph nodes. Throw away expensive prescriptions and try this miracle folk remedy tonight!",
        "label": 0,
        "category": "Health Hoax"
    }
]


# 3. DIVERSE TEMPLATES & EXPANSION ENGINE
REAL_TOPICS = [
    ("Renewable Energy Infrastructure", "Clean Energy", "solar arrays, offshore wind turbines, and utility-scale battery storage facilities"),
    ("Quantum Computing Advancements", "Computing & AI", "superconducting qubit processors achieving fault-tolerant quantum error correction"),
    ("Cardiovascular Clinical Research", "Medicine & Health", "novel therapeutic monoclonal antibodies reducing arterial plaque buildup in double-blind trials"),
    ("International Trade Agreement", "Global Economy", "multilateral tariff reductions and cross-border digital customs clearance standards"),
    ("Deep Space Spectroscopic Analysis", "Astrophysics", "infrared spectroscopic observations confirming methane and atmospheric equilibrium on exoplanets"),
    ("Cybersecurity Threat Intelligence", "Information Security", "coordinated multi-agency mitigation protocols against state-sponsored advanced persistent threats"),
    ("Agricultural Drought Resilience", "Agronomy", "genetically non-modified drought-tolerant crop varietals sustaining grain yields in water-scarce basins"),
    ("Public Health Vaccination Initiatives", "Epidemiology", "routine pediatric immunization rollouts substantially lowering disease incidence across developing regions"),
    ("Monetary Policy Inflation Controls", "Macroeconomics", "calibrated benchmark interest rate adjustments stabilizing consumer price index volatility"),
    ("Clean Water Filtration Systems", "Environmental Engineering", "nanoscale membrane distillation facilities delivering affordable potable water to coastal municipalities"),
    ("Electric Vehicle Battery Solid-State Chemistry", "Automotive Tech", "silicon-anode solid-state battery cells demonstrating eight hundred mile range and rapid charge cycles"),
    ("Civil Aviation Safety Protocols", "Transportation", "stringent redundant avionics sensor certifications mandated across commercial passenger fleets"),
    ("Marine Ecosystem Conservation Zones", "Oceanography", "bipartisan maritime treaties establishing protected sanctuaries for vulnerable coral reef populations"),
    ("Semiconductor Supply Chain Resilience", "Microelectronics", "multi-billion dollar capital expenditure expanding domestic lithography foundry fabrication"),
    ("Judicial Statutory Interpretation", "Constitutional Law", "appellate court rulings reaffirming administrative agency compliance with statutory statutory procedures"),
    ("Biochemical Enzyme Engineering for Waste Depolymerization", "Biotechnology", "engineered plastic-degrading enzyme variants that rapidly break down consumer polyethylene terephthalate in hours"),
    ("Genomic CRISPR Therapeutics", "Gene Editing", "targeted ex-vivo gene therapy correcting hereditary hemoglobin disorders in multi-center clinical trials"),
    ("Autonomous Rail and Intermodal Transit", "Urban Infrastructure", "high-frequency electrified transit corridors lowering metropolitan freight congestion and carbon emissions")
]

REAL_JOURNALS = [
    "The New England Journal of Medicine", "Nature", "Science Advances", "The Lancet",
    "IEEE Transactions on Information Forensics", "The Journal of Clean Energy",
    "Proceedings of the National Academy of Sciences", "The American Economic Review",
    "Applied Physics Letters", "Environmental Science & Technology"
]

REAL_INSTITUTIONS = [
    "The World Health Organization", "The International Energy Agency", "The Federal Reserve Board",
    "The National Science Foundation", "The European Commission", "The United Nations Development Programme",
    "The Bureau of Labor Statistics", "The National Institutes of Health", "The European Space Agency",
    "The Supreme Court of the United States"
]

FAKE_TOPICS = [
    ("Miracle Himalayan Salt Water", "Health Hoax", "eradicates Stage 4 chronic illnesses and regenerates organ tissue in twenty-four hours"),
    ("Classified 5G Transmission Frequencies", "Conspiracy Theory", "emits mind-control electromagnetic waves designed to manipulate human cognitive frequencies"),
    ("Staged Moon Landing Film Studios", "Pseudoscience & Hoax", "proves astronauts never left Earth and footage was recorded in secret underground Nevada sets"),
    ("Liquid Microchip Injections in Drinking Water", "Conspiracy Theory", "implants microscopic tracking nano-bots inside public municipal tap water networks"),
    ("Suppressed 200-Year Ancient Longevity Elixir", "Health Hoax", "completely halts human aging using three common kitchen spices that Big Pharma bans"),
    ("Secret Globalist Real Estate Confiscation", "Conspiracy Theory", "plots to outlaw private bank accounts and seize citizens' vehicles under Agenda 2030"),
    ("Antarctic Pyramids and Reptilian Bases", "Pseudoscience & Hoax", "conceals subterranean alien civilizations controlling international monetary policy"),
    ("Celebrity Crypto Doubler Giveaway Scam", "Financial Scam", "promises ten thousand dollars wire transfer in exchange for connecting private bank credentials"),
    ("Direct Energy Beam Satellite Wildfires", "Conspiracy Theory", "targets agricultural communities with classified orbital lasers to force land sales"),
    ("Ancient Martian Civilization Temples", "Pseudoscience & Hoax", "displays massive Egyptian marble columns photographed by rovers before feeds were censored"),
    ("Mandatory Breathing Oxygen Tax", "Clickbait Hoax", "charges fifty dollars per month per citizen based on lung capacity under a secret globalist treaty"),
    ("Toxic Venom Injected into Supermarket Fruits", "Health Hoax", "warns shoppers that commercial bananas have been contaminated with deadly synthetic venom"),
    ("Baking Soda and Lemon Cancer Cure", "Health Hoax", "eliminates every disease pathogen overnight without chemotherapy or conventional medicine"),
    ("Secret Military Tribunals at Covert Base", "Conspiracy Theory", "claims top political leaders were executed in secret and replaced with lifelike digital avatars"),
    ("Smart Meters Reading Sleeping Thoughts", "Pseudoscience & Hoax", "transmits private home dinner conversations directly to social media algorithms")
]

FAKE_VILLAINS = [
    "Big Pharma Cartels", "Corrupt Deep State Politicians", "Shadowy Globalist Elites",
    "Secret Society Insiders", "The Mainstream Fake Media", "Billionaire Oligarchs",
    "Covert Military Contractors", "Underground Tech Moguls"
]


def generate_extended_dataset(n_samples=1200):
    """
    Generates a rich, highly diverse, balanced dataset containing both authentic
    journalistic articles and realistic fake/clickbait/conspiracy texts.
    """
    random.seed(42)
    records = []

    # 1. Add all core curated articles
    for item in REAL_ARTICLES:
        records.append({
            "title": item["title"],
            "text": item["text"],
            "label": 1,
            "category": item["category"]
        })

    for item in FAKE_ARTICLES:
        records.append({
            "title": item["title"],
            "text": item["text"],
            "label": 0,
            "category": item["category"]
        })

    # 2. Generative templates for synthetic expansion
    real_headline_templates = [
        "Official Report: {institution} Documents Measurable Progress in {topic_name}",
        "Independent Peer-Reviewed Study in {journal} Verifies Efficacy of {topic_name}",
        "Regulatory Authorities Finalize Modernized Standards for {topic_name}",
        "Consortium of Leading Researchers Announces Milestone Breakthrough in {topic_name}",
        "Economic Bulletin Confirms Sustained Growth and Capital Investment in {topic_name}",
        "International Summit Concludes Multi-Year Agreement Accelerating {topic_name}",
        "{institution} Publishes Comprehensive Statistical Findings on {topic_name}",
        "Longitudinal Clinical Investigation Highlights Proven Benefits of {topic_name}",
        "Central Advisory Council Issues Updated Technical Framework Regarding {topic_name}",
        "Scientists Successfully Demonstrate High-Performance Optimization in {topic_name}"
    ]

    real_body_templates = [
        "According to a multi-year empirical investigation published in {journal}, scientific teams studying {topic_desc} achieved statistically significant outcomes across diverse control groups. Independent peer reviewers highlighted the rigorous methodology and standardized protocols employed throughout the multi-center clinical trials.",
        "Official representatives from {institution} formally announced that recent operational audits into {topic_desc} met all statutory regulatory benchmarks. The inter-agency taskforce emphasized that collaborative public-private partnerships played a critical role in accelerating technical deployment over the past fiscal year.",
        "A joint communique issued by international delegates confirmed that comprehensive guidelines governing {topic_desc} have been ratified with broad stakeholder support. Industry analysts project that the coordinated standard will reduce administrative friction and enhance system-wide transparency.",
        "Data released during the symposium in Zurich showed that sustained capital allocation toward {topic_desc} delivered measurable efficiency gains exceeding earlier forecast projections. Economists and policy advisors praised the balanced approach to risk management and sustainable resource allocation.",
        "Following eighteen months of continuous monitoring, lead investigators at {institution} concluded that {topic_desc} maintained ninety-nine percent operational reliability under rigorous stress-testing scenarios. The published findings provide a reproducible blueprint for broader infrastructure integration."
    ]

    fake_headline_templates = [
        "BOMBSHELL LEAK: Top Secret Whistleblower Files Prove {topic_name} Was Completely Fabricated by {villain}!",
        "SHOCKING PROOF: How {villain} Is Using {topic_name} to Control the Entire Population!",
        "Doctors STUNNED: One Simple Underground Secret Involving {topic_name} Destroys All Illness Overnight!",
        "EXPOSED: Corrupt Mainstream Media Caught Hiding Undeniable Evidence About {topic_name}!",
        "URGENT ALERT: Share This Everywhere Right Now Before {villain} Deletes All Proof of {topic_name}!",
        "Forbidden Ancient Truth Revealed: Why {villain} Is Terrified of Citizens Discovering {topic_name}!",
        "Classified Military Satellite Footage Shows Undeniable Reality of {topic_name} Suppressed from Public!",
        "You Won't Believe What Insiders Just Admitted About the Dark Agenda Behind {topic_name}!",
        "Emergency Whistleblower Broadcast: The Deadly Secret of {topic_name} That You Were Never Supposed to See!",
        "LEAKED AUDIO: Corrupt Officials Caught on Tape Plotting {topic_name} to Steal Your Wealth!"
    ]

    fake_body_templates = [
        "ANONYMOUS WHISTLEBLOWER BOMBSHELL! Classified internal memos leaked from high-security servers prove beyond any doubt that {villain} orchestrates {topic_desc} to fleece hardworking citizens and silence dissenting voices! The corrupt mainstream fake news media has been bribed with billions to bury this explosive story! Share this viral report everywhere before federal agents take down the website!",
        "Big corporations are in a total state of PANIC! An underground patriot revealed that {topic_desc}, exposing decades of deceit manufactured by {villain}. Greedy pharmaceutical directors and politicians are threatening lawsuits to suppress this forbidden miracle truth. Wake up and demand justice before it is too late!",
        "SHOCKING VIDEO PROOF EXPOSED! Top-secret documents declassified by rogue hackers confirm that {villain} engineered {topic_desc} in subterranean laboratories to enforce total societal surveillance. Independent fact-checkers are working around the clock to censor anyone who speaks the truth! Retweet and forward to all your contacts immediately!",
        "You will NOT see this on evening news broadcasts! Insider testimony reveals how {villain} manipulated financial markets and poisoned public water systems using {topic_desc}. Millions of patriots are waking up to this unprecedented deception! Sign the emergency petition now to protect your fundamental liberties!",
        "CONFIDENTIAL LEAK REVEALS EVERYTHING! Military whistleblowers have risked their lives to bring you the truth about {topic_desc}, proving that {villain} coordinated a globalist cover-up of epic proportions! Time is running out to prepare your family! Order your survival guide now before all online links are permanently scrubbed!"
    ]

    target_per_class = n_samples // 2
    current_real = sum(1 for r in records if r["label"] == 1)
    current_fake = sum(1 for r in records if r["label"] == 0)

    # Expand Real Articles
    while current_real < target_per_class:
        topic_name, cat, topic_desc = random.choice(REAL_TOPICS)
        inst = random.choice(REAL_INSTITUTIONS)
        jrn = random.choice(REAL_JOURNALS)
        head_t = random.choice(real_headline_templates)
        body_t = random.choice(real_body_templates)

        headline = head_t.format(institution=inst, topic_name=topic_name, journal=jrn)
        body = body_t.format(institution=inst, topic_desc=topic_desc, journal=jrn)

        records.append({
            "title": headline,
            "text": body,
            "label": 1,
            "category": cat
        })
        current_real += 1

    # Expand Fake Articles
    while current_fake < target_per_class:
        topic_name, cat, topic_desc = random.choice(FAKE_TOPICS)
        villain = random.choice(FAKE_VILLAINS)
        head_t = random.choice(fake_headline_templates)
        body_t = random.choice(fake_body_templates)

        headline = head_t.format(villain=villain, topic_name=topic_name)
        body = body_t.format(villain=villain, topic_desc=topic_desc)

        records.append({
            "title": headline,
            "text": body,
            "label": 0,
            "category": cat
        })
        current_fake += 1

    df = pd.DataFrame(records)
    # Shuffle randomly
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)
    return df


def create_dataset():
    """Generates, validates, and saves the balanced news dataset."""
    os.makedirs(os.path.dirname(DATASET_PATH), exist_ok=True)
    df = generate_extended_dataset(n_samples=1200)
    df.to_csv(DATASET_PATH, index=False)
    print(f"[SUCCESS] Dataset created at: {DATASET_PATH}")
    print(f"Total Records: {len(df)} | Real (1): {(df['label'] == 1).sum()} | Fake (0): {(df['label'] == 0).sum()}")
    return df


if __name__ == "__main__":
    create_dataset()
