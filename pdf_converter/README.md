# PDF Converter with NLP and Image Analysis

This tool extracts text, tables, and figures from research paper PDFs, applies NLP for text analysis, and uses image recognition to classify extracted images (e.g., graphs, tables, other figures). It is designed for easy integration into a web application.

## Features
- Extracts text, tables, and images from PDFs
- Applies NLP (summarization, keyword extraction, etc.)
- Classifies images (figures, graphs, tables)
- REST API for web integration

## Project Structure

```
pdf_converter/
│
├── main.py                  # Entry point for the tool
├── requirements.txt         # Python dependencies
│
├── pdf_extraction/
│   ├── __init__.py
│   ├── text_extractor.py    # Extracts text from PDFs
│   ├── table_extractor.py   # Extracts tables from PDFs
│   └── image_extractor.py   # Extracts images (figures/graphs) from PDFs
│
├── nlp/
│   ├── __init__.py
│   └── nlp_processing.py    # NLP tasks (summarization, keyword extraction, etc.)
│
├── image_analysis/
│   ├── __init__.py
│   └── image_classifier.py  # Classifies images (e.g., graph, table, other)
│
├── utils/
│   ├── __init__.py
│   └── helpers.py           # Utility functions (file handling, logging, etc.)
│
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py     # Unit tests for the pipeline
│
└── README.md                # Project documentation
```

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the web API:
   ```bash
   python main.py
   ```
3. Use the `/upload` endpoint to upload a PDF and receive extracted content.

## API
- `POST /upload` - Upload a PDF file and receive extracted text, tables, images, and analysis results.

---

## License
MIT 