from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import base64
from io import BytesIO
from app.pdf_extractor import extract_text, extract_tables, extract_images
from app.nlp import summarize, extract_keywords
from app.image_classifier import classify_image

app = FastAPI()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Backend running!"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    filename = f"/tmp/{file.filename}"
    with open(filename, "wb") as f:
        f.write(contents)

    # Extract text, tables, and images
    raw_text = extract_text(filename)
    tables = extract_tables(filename)
    images = extract_images(filename)

    # NLP: Summarization and keyword extraction
    summary = summarize(raw_text)
    keywords = extract_keywords(raw_text)

    # Convert images to base64 for frontend, placeholder type 'figure'
    figures = []
    for img_obj in images:
        buffered = BytesIO()
        img_obj["image"].save(buffered, format="PNG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()
        img_type = classify_image(img_obj["image"])
        figures.append({
            "dataUrl": f"data:image/png;base64,{img_b64}",
            "type": img_type
        })

    return JSONResponse({
        "summary": summary,
        "tables": tables,
        "figures": figures,
        "raw_text": raw_text,
        "keywords": keywords
    }) 