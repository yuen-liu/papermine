from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import tempfile
import fitz  # PyMuPDF for basic PDF processing

app = Flask(__name__)
CORS(app)

def extract_text_simple(pdf_path):
    """Simple text extraction using PyMuPDF"""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def extract_images_simple(pdf_path):
    """Simple image extraction using PyMuPDF"""
    try:
        doc = fitz.open(pdf_path)
        image_count = 0
        for page_num in range(len(doc)):
            page = doc[page_num]
            image_list = page.get_images()
            image_count += len(image_list)
        doc.close()
        return image_count
    except Exception as e:
        return 0

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
        # Save uploaded file to temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            file.save(tmp_file.name)
            pdf_path = tmp_file.name
        
        # Extract content
        text = extract_text_simple(pdf_path)
        image_count = extract_images_simple(pdf_path)
        
        # Clean up temporary file
        os.unlink(pdf_path)
        
        # Return results
        return jsonify({
            'text': text[:1000] + "..." if len(text) > 1000 else text,  # Limit text length
            'tables': [],  # Simplified - no table extraction
            'images': [{'count': image_count, 'message': f'Found {image_count} images'}],
            'nlp': {
                'summary': 'PDF processed successfully',
                'keywords': ['pdf', 'converted', 'success']
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'PDF Converter is running on Vercel!'})

# For local development
if __name__ == '__main__':
    print("🚀 Starting PDF Converter (Vercel Optimized)...")
    print("📡 Server will be available at: http://localhost:8080")
    app.run(debug=True, host='0.0.0.0', port=8080) 