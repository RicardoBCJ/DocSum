# app/utils/file_processing.py

import os
from PyPDF2 import PdfReader
import docx2txt
import re

def preprocess_text(text: str) -> str:
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Additional preprocessing steps can be added here
    return text



async def extract_text(file_path: str) -> str:
    file_extension = file_path.rsplit('.', 1)[1].lower()
    text = ""

    if file_extension == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension == 'docx':
        text = extract_text_from_docx(file_path)
    elif file_extension == 'txt':
        text = extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file type.")
    
    text = preprocess_text(text)
    return text


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def extract_text_from_docx(file_path: str) -> str:
    text = docx2txt.process(file_path)
    return text

def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
