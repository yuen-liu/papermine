# nlp.py
# Handles NLP tasks: summarization and keyword extraction

from transformers import pipeline
import spacy

# Load summarization pipeline (small model for speed)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")

# Load spaCy small English model for keyword extraction
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def summarize(text):
    # HuggingFace summarization pipeline (truncate for long texts)
    if not text.strip():
        return ""
    max_chunk = 1000
    chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]
    summaries = []
    for chunk in chunks[:3]:  # Limit to first 3 chunks for speed
        summary = summarizer(chunk, max_length=100, min_length=20, do_sample=False)[0]["summary_text"]
        summaries.append(summary)
    return " ".join(summaries)

def extract_keywords(text):
    # Use spaCy to extract top keywords (noun chunks, unique, sorted by length)
    if not text.strip():
        return []
    doc = nlp(text)
    keywords = set(chunk.text.strip().lower() for chunk in doc.noun_chunks if len(chunk.text.strip()) > 2)
    # Return up to 10 keywords, sorted by length (desc)
    return sorted(keywords, key=len, reverse=True)[:10] 