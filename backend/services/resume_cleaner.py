import re


def clean_resume_text(text: str) -> str:
    """
    Cleans raw text extracted from PDF.
    """

    # ---------------------------------------
    # Fix words broken by line wrapping
    # Example:
    # Health-
    # care
    # ->
    # Healthcare
    # ---------------------------------------

    text = re.sub(r"-\n", "", text)

    # ---------------------------------------
    # Merge wrapped sentences
    # Example:
    # machine learning
    # models
    # ->
    # machine learning models
    # ---------------------------------------

    text = re.sub(r"\n(?=[a-z])", " ", text)

    # ---------------------------------------
    # Remove page numbers
    # ---------------------------------------

    text = re.sub(r"\n\d+\n", "\n", text)

    # ---------------------------------------
    # Remove extra blank lines
    # ---------------------------------------

    text = re.sub(r"\n{2,}", "\n", text)

    # ---------------------------------------
    # Remove unnecessary spaces
    # ---------------------------------------

    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()