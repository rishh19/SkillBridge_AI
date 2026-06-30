import fitz

from services.resume_cleaner import clean_resume_text


def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return clean_resume_text(text)