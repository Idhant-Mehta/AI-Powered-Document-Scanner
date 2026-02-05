from __future__ import annotations

import streamlit as st
from PIL import Image

from scanner import scan_document


st.set_page_config(page_title="AI-Powered Document Scanner", page_icon="📄", layout="wide")

st.title("📄 AI-Powered Document Scanner")
st.write(
    "Upload a document image to run OCR, extract text, and generate an AI-powered summary."
)

with st.sidebar:
    st.header("How it works")
    st.markdown(
        """
1. Upload a document photo or scan
2. Image is enhanced for OCR
3. Text is extracted with Tesseract
4. Summary is generated with AI (or local fallback)
        """
    )

uploaded_file = st.file_uploader(
    "Upload image",
    type=["png", "jpg", "jpeg", "webp", "tif", "tiff", "bmp"],
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with st.spinner("Scanning and analyzing document..."):
        result = scan_document(image)

    with col2:
        st.subheader("Scan Insights")
        st.metric("Words detected", result.word_count)
        st.info(result.confidence_hint)

    st.subheader("Summary")
    st.write(result.summary)

    st.subheader("Extracted Text")
    st.text_area("OCR Output", result.extracted_text, height=320)
else:
    st.info("Upload a document image to get started.")
