import nltk
nltk.data.path.append("./nltk_data")  # Force NLTK to use local data

from nltk.tokenize import word_tokenize
import re

# Hindi + Marathi stopwords
stopwords_hi_mr = set([
    "है", "के", "का", "की", "को", "में", "से", "पर", "और", "यह", "था",
    "था", "हो", "रहा", "हूँ", "आप", "हम", "वे", "जो", "भी", "नहीं",  "आहे", 
    "च्या", "मध्ये", "वर","आणि", "तो", "ती", "हे", "की", "होते",
    "नाही", "तुमचे", "आपण", "माझे", "तसेच"
])

def clean_text_mixed_with_stopwords(text):
    text = text.lower()
    text = re.sub(r'[^ऀ-ॿa-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word not in stopwords_hi_mr]
    return ' '.join(filtered)
