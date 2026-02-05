from scanner import local_summary


def test_local_summary_handles_empty_text() -> None:
    assert local_summary("") == "No text detected to summarize."


def test_local_summary_reduces_long_text() -> None:
    text = (
        "This project scans receipts quickly. "
        "The OCR pipeline improves image readability before extraction. "
        "Summarization helps users get key points immediately. "
        "The application supports multiple input image formats. "
        "Confidence hints tell users when to rescan documents."
    )

    summary = local_summary(text, max_sentences=2)
    assert summary
    assert len(summary) < len(text)
