from flask import Flask, request, jsonify
import os
from pdf_extraction.text_extractor import extract_text
from pdf_extraction.table_extractor import extract_tables
from pdf_extraction.image_extractor import extract_images
from nlp.nlp_processing import analyze_text
from image_analysis.image_classifier import classify_images
from utils.helpers import save_uploaded_file

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    pdf_path = save_uploaded_file(file)
    text = extract_text(pdf_path)
    tables = extract_tables(pdf_path)
    image_paths = extract_images(pdf_path)
    nlp_results = analyze_text(text)
    image_classes = classify_images(image_paths)
    return jsonify({
        'text': text,
        'tables': tables,
        'nlp': nlp_results,
        'images': [
            {'path': path, 'class': image_classes.get(path, 'unknown')}
            for path in image_paths
        ]
    })

if __name__ == '__main__':
    app.run(debug=True) 