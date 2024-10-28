# app/utils/nlp_processing.py

import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Load spaCy model globally
nlp = spacy.load('en_core_web_sm', disable=['parser', 'lemmatizer'])

def extract_entities(text: str):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            'text': ent.text,
            'label': ent.label_
        })
    return entities

def generate_summary(text: str, sentence_count: int = 5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count=sentence_count)
    # Combine the summary sentences into a string
    summary_text = ' '.join([str(sentence) for sentence in summary])
    return summary_text
