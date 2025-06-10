def test_imports():
    from pdf_extraction.text_extractor import extract_text
    from pdf_extraction.table_extractor import extract_tables
    from pdf_extraction.image_extractor import extract_images
    from nlp.nlp_processing import analyze_text
    from image_analysis.image_classifier import classify_images
    assert callable(extract_text)
    assert callable(extract_tables)
    assert callable(extract_images)
    assert callable(analyze_text)
    assert callable(classify_images) 