# AI-Powered Document Scanner

A simple web app that scans document images, extracts text (OCR), and generates a concise AI-powered summary.

## Features

- OCR extraction with `pytesseract`
- Image preprocessing for stronger OCR results
- AI summary via Hugging Face transformer when available
- Built-in extractive fallback summarizer
- Streamlit UI for quick local usage

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local URL shown by Streamlit (usually `http://localhost:8501`).

## Notes

- You need Tesseract OCR installed on your machine for `pytesseract` to work.
- If the transformer model can't be downloaded/loaded, the app still works using the fallback summarizer.

## Suggested Improvements

- PDF support with page-by-page OCR
- Export extracted text/summary as `.txt` or `.json`
- Multi-language OCR and translation options
