from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class ScanResult:
    extracted_text: str
    summary: str
    word_count: int
    confidence_hint: str


def preprocess_image(image):
    """Convert to OpenCV format and improve OCR readability."""
    import cv2
    import numpy as np

    rgb = np.array(image.convert("RGB"))
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=18)
    thresholded = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        15,
    )

    return cv2.resize(thresholded, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)


def extract_text(image) -> str:
    import pytesseract

    processed = preprocess_image(image)
    custom_config = "--oem 3 --psm 6"
    text = pytesseract.image_to_string(processed, config=custom_config)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def local_summary(text: str, max_sentences: int = 4) -> str:
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return "No text detected to summarize."

    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    if len(sentences) <= max_sentences:
        return cleaned

    keywords = [w.lower() for w in re.findall(r"[A-Za-z]{4,}", cleaned)]
    if not keywords:
        return " ".join(sentences[:max_sentences])

    freq: dict[str, int] = {}
    for word in keywords:
        freq[word] = freq.get(word, 0) + 1

    scored: list[tuple[int, str]] = []
    for sentence in sentences:
        words = re.findall(r"[A-Za-z]{4,}", sentence.lower())
        score = sum(freq.get(w, 0) for w in words)
        scored.append((score, sentence))

    top = sorted(scored, key=lambda x: x[0], reverse=True)[:max_sentences]
    top_sentences = {s for _, s in top}

    ordered = [s for s in sentences if s in top_sentences]
    return " ".join(ordered)


def ai_summary(text: str) -> Optional[str]:
    if len(text.split()) < 40:
        return None

    try:
        from transformers import pipeline

        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        clipped = text[:3000]
        result = summarizer(clipped, max_length=120, min_length=30, do_sample=False)
        return result[0]["summary_text"].strip()
    except Exception:
        return None


def scan_document(image) -> ScanResult:
    text = extract_text(image)
    summary = ai_summary(text) or local_summary(text)
    word_count = len(text.split())

    if word_count > 150:
        confidence_hint = "High confidence: lots of text detected."
    elif word_count > 40:
        confidence_hint = "Medium confidence: moderate text detected."
    elif word_count > 0:
        confidence_hint = "Low confidence: limited text detected. Try a clearer scan."
    else:
        confidence_hint = "No text detected. Use a higher-quality image."

    return ScanResult(
        extracted_text=text,
        summary=summary,
        word_count=word_count,
        confidence_hint=confidence_hint,
    )
