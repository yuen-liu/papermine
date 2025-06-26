# Papermine
your friendly neighborhood PDF Research Paper Extractor because curating data is hard...

**NOTE: run locally. I am broke so I can't afford to host my backend on Render rip

A modular full-stack web application to extract and analyze research papers in PDF format. Upload a PDF and get:
- **Summary** (NLP-powered)
- **Keywords**
- **Extracted tables** (as HTML + in future CSV - working on the CSV format rn)
- **Extracted figures/images** (with type: plot/table/figure)

---

## Features
- Upload PDF research papers
- Extracts raw text, tables, and images
- Summarizes and extracts keywords from text
- Classifies images as plot, table, or figure
- Clean, minimal React UI
- Modular backend (easy to swap NLP/classifier components)

---

## Tech Stack
- **Backend:** Python, FastAPI, PyMuPDF, pdfplumber, spaCy, HuggingFace Transformers, PIL, OpenCV, pytesseract. Models used: sshleifer/distilbart-cnn-1-2-6 for summarization, en_core_web_sm for keywords.
- **Frontend:** React (Vite), HTML/CSS/JS
- **Deployment:** Backend (Render/Fly.io), Frontend (Vercel)

---

## Local Development

### 1. Backend
```sh
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for API docs.

### 2. Frontend
```sh
cd frontend
npm install
npm run dev
```
- Visit [http://localhost:5173](http://localhost:5173)

---

## Deployment

### Backend (Render Example)
- Set root directory to `backend`
- **Start Command:**
  ```
  uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```
- **Build Command:**
  ```
  pip install -r requirements.txt
  ```
- Expose port `$PORT` (Render sets this automatically)

### Frontend (Vercel Example)
- Set root directory to `frontend`
- **Build Command:**
  ```
  npm install && npm run build
  ```
- **Output Directory:** `dist`
- Update API URL in `frontend/src/components/UploadForm.jsx` to your backend's deployed URL

---

## Notes
- For OCR, you may need to install Tesseract on your server (e.g., `apt-get install tesseract-ocr`)
- HuggingFace models are downloaded on first run; initial startup may take time
- All backend components are modular and can be swapped for more advanced models
