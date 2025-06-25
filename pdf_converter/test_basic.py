#!/usr/bin/env python3
"""
Basic test script to verify PDF extraction functionality
"""

import os
import sys
from pdf_extraction.text_extractor import extract_text
from pdf_extraction.table_extractor import extract_tables
from pdf_extraction.image_extractor import extract_images
from utils.helpers import save_uploaded_file

def test_basic_functionality():
    """Test basic PDF extraction without NLP"""
    print("Testing basic PDF extraction functionality...")
    
    # Create a simple test PDF or check if one exists
    test_pdf_path = "test.pdf"
    
    if not os.path.exists(test_pdf_path):
        print(f"⚠️  No test PDF found at {test_pdf_path}")
        print("Please place a test PDF file named 'test.pdf' in the current directory")
        print("You can download a sample PDF from: https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
        return False
    
    try:
        print("📄 Extracting text...")
        text = extract_text(test_pdf_path)
        print(f"✅ Text extraction successful! Extracted {len(text)} characters")
        
        print("📊 Extracting tables...")
        tables = extract_tables(test_pdf_path)
        print(f"✅ Table extraction successful! Found {len(tables)} tables")
        
        print("🖼️  Extracting images...")
        image_paths = extract_images(test_pdf_path)
        print(f"✅ Image extraction successful! Found {len(image_paths)} images")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        return False

if __name__ == "__main__":
    success = test_basic_functionality()
    if success:
        print("\n🎉 Basic functionality test passed!")
        print("Your PDF converter is ready to use!")
    else:
        print("\n❌ Basic functionality test failed!")
        print("Please check the error messages above.") 