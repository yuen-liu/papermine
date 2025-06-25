from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from pdf_extraction.text_extractor import extract_text
from pdf_extraction.table_extractor import extract_tables
from pdf_extraction.image_extractor import extract_images
from image_analysis.image_classifier import classify_images
from utils.helpers import save_uploaded_file

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return send_file('test_upload.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    try:
        # Save uploaded file
        pdf_path = save_uploaded_file(file)
        
        # Extract content
        text = extract_text(pdf_path)
        tables = extract_tables(pdf_path)
        image_paths = extract_images(pdf_path)
        image_classes = classify_images(image_paths)
        
        # Return results
        return jsonify({
            'text': text,
            'tables': tables,
            'images': [
                {'path': path, 'class': image_classes.get(path, 'unknown')}
                for path in image_paths
            ],
            'nlp': {
                'summary': 'NLP processing disabled for testing',
                'keywords': []
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'PDF Converter is running!'})

# For local development
if __name__ == '__main__':
    print("🚀 Starting PDF Converter (Simple Mode)...")
    print("📡 Server will be available at: http://localhost:8080")
    print("📤 Upload endpoint: POST http://localhost:8080/upload")
    print("💚 Health check: GET http://localhost:8080/health")
    print("🌐 Web interface: http://localhost:8080/")
    app.run(debug=True, host='0.0.0.0', port=8080) 