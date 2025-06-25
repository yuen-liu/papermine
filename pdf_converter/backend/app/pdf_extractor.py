# pdf_extractor.py
# Handles extraction of text, tables, and images from PDF files

import fitz  # PyMuPDF
import pdfplumber
from PIL import Image
import io

# Extract all text from the PDF
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    doc.close()
    return text

# Extract tables from the PDF using pdfplumber
def extract_tables(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                tables.append(table)
    return tables

# Extract images from the PDF using PyMuPDF, return as list of dicts with PIL Image and metadata
def extract_images(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            pil_img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
            images.append({
                "image": pil_img,
                "page": page_num + 1,
                "index": img_index,
                "ext": image_ext
            })
    doc.close()
    return images 