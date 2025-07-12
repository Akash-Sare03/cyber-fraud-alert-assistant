import nltk
from nltk.tokenize import word_tokenize
import re

# Safe download: Only downloads 'punkt' if missing
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Hindi + Marathi stopwords (expand this list as needed)
stopwords_hi_mr = set([
    "है", "के", "का", "की", "को", "में", "से", "पर", "और", "यह", "था",
    "था", "हो", "रहा", "हूँ", "आप", "हम", "वे", "जो", "भी", "नहीं",  "आहे", 
    "च्या", "मध्ये", "वर","आणि", "तो", "ती", "हे", "की", "होते",
    "नाही", "तुमचे", "आपण", "माझे", "तसेच"
])

def clean_text_mixed_with_stopwords(text):
    text = text.lower()
    text = re.sub(r'[^ऀ-ॿa-zA-Z\s]', '', text)  # Keep Devanagari + English
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word not in stopwords_hi_mr]
    return ' '.join(filtered)
