from transformers import pipeline
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def analyze_text(text):
    # Summarization
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    summary = summarizer(text[:1024], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    # Keyword extraction (simple)
    vectorizer = CountVectorizer(stop_words='english', max_features=10)
    X = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    return {'summary': summary, 'keywords': list(keywords)} 