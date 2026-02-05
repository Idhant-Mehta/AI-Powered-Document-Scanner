# AI-Powered Document Scanner

A simple web app that scans document images, extracts text (OCR), and generates a concise AI-powered summary.

## Features

- OCR extraction with `pytesseract`
- Image preprocessing for stronger OCR results
- AI summary via Hugging Face transformer when available
- Built-in extractive fallback summarizer
- Streamlit UI for quick local usage

## Prerequisites

Before running the app, you need to install **Tesseract OCR** on your system:

### macOS

```bash
brew install tesseract
```

### Ubuntu / Debian

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

### Windows

1. Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer and note the installation path
3. Add the Tesseract installation directory to your system PATH

## Quick Start

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Idhant-Mehta/AI-Powered-Document-Scanner.git
   cd AI-Powered-Document-Scanner
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown by Streamlit (usually `http://localhost:8501`).

## How to Use

1. **Upload a Document**: Click the "Upload image" button in the main area of the app and select a document image from your computer.

2. **Supported File Formats**: The app supports the following image formats:
   - PNG (`.png`)
   - JPEG (`.jpg`, `.jpeg`)
   - WebP (`.webp`)
   - TIFF (`.tif`, `.tiff`)
   - BMP (`.bmp`)

3. **View Results**: After uploading, the app will:
   - Display the original image on the left
   - Show scan insights (word count and confidence level) on the right
   - Generate an AI-powered summary of the document
   - Provide the full extracted text in a text area

4. **Tips for Best Results**:
   - Use high-resolution images for better OCR accuracy
   - Ensure the document is well-lit and has good contrast
   - Avoid skewed or rotated images
   - Crop out unnecessary borders or backgrounds

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "TesseractNotFoundError" | Ensure Tesseract OCR is installed and added to your system PATH |
| Poor OCR results | Use a higher quality image with better lighting and contrast |
| AI summary not appearing | The app falls back to a local summarizer if the transformer model cannot be loaded. This is normal behavior and the app will still work. |
| Slow performance | The first run may be slow as it downloads the AI model (~1.2 GB). Subsequent runs will be faster. |

## Notes

- You need Tesseract OCR installed on your machine for `pytesseract` to work.
- If the transformer model can't be downloaded/loaded, the app still works using the fallback summarizer.

## Suggested Improvements

- PDF support with page-by-page OCR
- Export extracted text/summary as `.txt` or `.json`
- Multi-language OCR and translation options
