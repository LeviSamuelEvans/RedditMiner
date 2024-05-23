import spacy

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    return nlp(text)
