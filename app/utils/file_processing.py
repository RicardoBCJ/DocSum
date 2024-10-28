# app/utils/file_processing.py

import os
from PyPDF2 import PdfReader
import docx2txt
import re
from pdf2image import convert_from_path
import numpy as np
import easyocr

def preprocess_text(text: str) -> str:
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Additional preprocessing steps can be added here
    return text



async def extract_text(file_path: str) -> str:
    file_extension = file_path.rsplit('.', 1)[1].lower()
    text = ""

    if file_extension == 'pdf':
        text = await extract_text_from_pdf(file_path)
    elif file_extension == 'docx':
        text = extract_text_from_docx(file_path)
    elif file_extension == 'txt':
        text = extract_text_from_txt(file_path)
    elif file_extension in ['png', 'jpg', 'jpeg']:
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file type.")

    text = preprocess_text(text)
    return text


def extract_text_from_image(image_np: np.ndarray) -> str:
    print(f"Image dtype: {image_np.dtype}, shape: {image_np.shape}")
    if image_np.dtype != np.uint8:
        image_np = image_np.astype(np.uint8)

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_np, detail=0)
    text = ' '.join(result)
    return text



def extract_text_from_pdf(file_path: str) -> str:

    images = convert_from_path(file_path, poppler_path=r'C:\poppler\poppler-24.08.0\Library\bin')
    text = ""
    for image in images:
        # Convert PIL Image to NumPy array
        image_np = np.array(image)
        text += extract_text_from_image(image_np)
    return text


def extract_text_from_docx(file_path: str) -> str:
    text = docx2txt.process(file_path)
    return text

def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
