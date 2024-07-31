import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Load data
df = pd.read_csv('product_reviews.csv')

# Basic text cleaning
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()
    return text

df['Review'] = df['Review'].apply(preprocess_text)

# Remove stopwords and perform stemming
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def remove_stopwords_stem(text):
    words = text.split()
    words = [ps.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

df['Review'] = df['Review'].apply(remove_stopwords_stem)
