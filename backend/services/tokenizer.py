import re


def tokenize_text(text: str):

    text = text.lower()

    text = text.replace("/", " ")

    text = text.replace(",", " ")

    text = text.replace("|", " ")

    text = text.replace(":", " ")

    text = text.replace("(", " ")

    text = text.replace(")", " ")

    text = re.sub(r"\s+", " ", text)

    return text