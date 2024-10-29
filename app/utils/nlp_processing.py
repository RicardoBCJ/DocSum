# app/utils/nlp_processing.py

import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser', 'lemmatizer'])

def extract_entities(text: str) -> list:
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    return entities

def generate_summary(text: str, sentences_count: int = 3) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summarizer.stop_words = get_stop_words("english")
    summary_sentences = summarizer(parser.document, sentences_count)
    summary = ' '.join(str(sentence) for sentence in summary_sentences)
    return summary
