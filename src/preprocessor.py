"""
Text Preprocessing Pipeline for News Shield (Fake News Detection)
Author: News Shield Project Team (GNIOT / AKTU)
Supervisor: Mr. Rohit Vaid

Key Steps:
1. Cleaning HTML tags, URLs, special characters, and numbers.
2. Converting all text to lowercase.
3. Stopword removal (NLTK English stopwords with fallback).
4. Stemming using Porter Stemmer.
5. Stylometric and linguistic marker extraction (ALL-CAPS ratio, sensational keywords, punctuation density).
"""

import re
import string

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    try:
        STOP_WORDS = set(stopwords.words('english'))
    except Exception:
        nltk.download('stopwords', quiet=True)
        STOP_WORDS = set(stopwords.words('english'))
    ps = PorterStemmer()
except Exception:
    # Graceful fallback stopwords
    STOP_WORDS = {
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
        'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself',
        'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
        'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',
        'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
        'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
        'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
        'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
        'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
        'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
        'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
        'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
        'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
        'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren'
    }

    class SimpleStemmer:
        def stem(self, word):
            if word.endswith('ing') and len(word) > 5:
                return word[:-3]
            elif word.endswith('ed') and len(word) > 4:
                return word[:-2]
            elif word.endswith('s') and len(word) > 3:
                return word[:-1]
            return word
    ps = SimpleStemmer()

# Common Sensational / Clickbait Indicators
SENSATIONAL_PATTERNS = {
    'shocking', 'bombshell', 'exposed', 'leaked', 'conspiracy', 'whistleblower',
    'secret', 'miracle', 'hoax', 'banned', 'suppressed', 'furious', 'bribed',
    'scam', 'unbelievable', 'urgent', 'disaster', 'alien', 'coverup'
}

# Common Objective Journalistic Credibility Markers
CREDIBILITY_PATTERNS = {
    'published', 'study', 'researchers', 'scientists', 'investigation', 'reuters',
    'spokesperson', 'confirmed', 'official', 'department', 'court', 'report',
    'statistics', 'clinical', 'peer', 'regulatory', 'committee', 'conference'
}


def clean_text(text: str, apply_stemming: bool = True) -> str:
    """
    Cleans and standardizes raw news text.

    Args:
        text (str): Raw article title or body.
        apply_stemming (bool): Whether to apply Porter Stemming.

    Returns:
        str: Processed and stemmed text string ready for vectorization.
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    # 1. Strip URLs & web links
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # 2. Strip HTML tags
    text = re.sub(r'<.*?>', ' ', text)

    # 3. Strip non-alphanumeric characters (keep only letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # 4. Convert to lowercase
    text = text.lower()

    # 5. Tokenize by whitespace
    words = text.split()

    # 6. Remove stopwords and optionally apply stemming
    if apply_stemming:
        processed_words = [ps.stem(word) for word in words if word not in STOP_WORDS and len(word) > 2]
    else:
        processed_words = [word for word in words if word not in STOP_WORDS and len(word) > 2]

    # 7. Join back to clean string
    return " ".join(processed_words)


def extract_linguistic_features(title: str, text: str) -> dict:
    """
    Extracts statistical & stylistic markers often found in sensational fake news
    (e.g., excessive exclamation marks, ALL CAPS words, sensational terminology).
    """
    full_content = f"{title or ''} {text or ''}".strip()
    words = full_content.split()
    word_count = len(words)

    # Exclamation & question counts
    exclamation_count = full_content.count('!')
    question_count = full_content.count('?')

    # Uppercase ratio (excluding spaces)
    non_space_chars = [c for c in full_content if not c.isspace()]
    upper_chars = [c for c in non_space_chars if c.isupper()]
    caps_ratio = (len(upper_chars) / len(non_space_chars) * 100) if non_space_chars else 0.0

    # Average word length
    avg_word_len = round(sum(len(w) for w in words) / max(word_count, 1), 1)

    # Sensational vs Credibility keyword matches
    lower_tokens = set(re.findall(r'[a-zA-Z]+', full_content.lower()))
    sensational_hits = len(lower_tokens.intersection(SENSATIONAL_PATTERNS))
    credibility_hits = len(lower_tokens.intersection(CREDIBILITY_PATTERNS))

    return {
        "word_count": word_count,
        "char_count": len(full_content),
        "exclamation_count": exclamation_count,
        "question_count": question_count,
        "caps_ratio_percent": round(caps_ratio, 2),
        "avg_word_length": avg_word_len,
        "sensational_indicators": sensational_hits,
        "credibility_indicators": credibility_hits
    }
