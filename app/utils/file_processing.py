# app/utils/file_processing.py

import os
import re
import numpy as np
from PIL import Image
from PyPDF2 import PdfReader
import docx2txt
from pdf2image import convert_from_path
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
        text = extract_text_from_pdf(file_path)
    elif file_extension == 'docx':
        text = extract_text_from_docx(file_path)
    elif file_extension == 'txt':
        text = extract_text_from_txt(file_path)
    elif file_extension in ['png', 'jpg', 'jpeg']:
        text = extract_text_from_image_file(file_path)
    else:
        raise ValueError("Unsupported file type.")

    text = preprocess_text(text)
    return text

def extract_text_from_image(image_np: np.ndarray) -> str:
    if image_np is None:
        raise ValueError("Image data is None")
    if not isinstance(image_np, np.ndarray):
        raise TypeError(f"Expected image_np to be a NumPy array, got {type(image_np)}")
    if image_np.size == 0:
        raise ValueError("Empty image data")
    # Ensure image data type is uint8
    if image_np.dtype != np.uint8:
        image_np = image_np.astype(np.uint8)
    # Ensure image is in RGB format
    import cv2
    if len(image_np.shape) == 2:
        # Grayscale image
        image_rgb = cv2.cvtColor(image_np, cv2.COLOR_GRAY2RGB)
    elif image_np.shape[2] == 4:
        # RGBA image
        image_rgb = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
    else:
        image_rgb = image_np  # Assume already RGB

    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_rgb, detail=0)
    text = ' '.join(result)
    return text

def extract_text_from_image_file(file_path: str) -> str:
    # Open image file
    try:
        image = Image.open(file_path)
    except Exception as e:
        raise ValueError(f"Unable to open image file: {e}")
    # Convert image to RGB
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_np = np.array(image)
    text = extract_text_from_image(image_np)
    return text

def extract_text_from_pdf(file_path: str) -> str:
    poppler_path = r'C:\poppler\poppler-24.08.0\Library\bin'  # Update to your poppler path
    try:
        images = convert_from_path(file_path, poppler_path=poppler_path)
    except Exception as e:
        raise ValueError(f"Error converting PDF to images: {e}")
    text = ""
    for image in images:
        # Convert image to RGB
        if image.mode != 'RGB':
            image = image.convert('RGB')
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
