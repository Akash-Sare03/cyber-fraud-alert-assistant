import nltk
nltk.download('punkt')

import re
from nltk.tokenize import word_tokenize

# Hindi + Marathi stopwords (add more later as needed)
stopwords_hi_mr = set([
    "का", "कि", "के", "यह", "और", "पर", "से", "है", "था", "थे", "नाही", "आहे", "असे", "मध्ये", "आपला"
])

def clean_text_mixed_with_stopwords(text):
    text = text.lower()
    text = re.sub(r'[^ऀ-ॿa-zA-Z\s]', '', text)  # Keep Devanagari + English
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word not in stopwords_hi_mr]
    return ' '.join(filtered)

