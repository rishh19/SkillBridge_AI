import re


def extract_certifications(certification_text: str):

    certifications = []

    lines = [
        line.strip()
        for line in certification_text.splitlines()
        if line.strip()
    ]

    current = None

    for line in lines:

        # Ignore category headings
        if not line.startswith("•"):
            continue

        line = line.replace("•", "").strip()

        year_match = re.search(r"\((.*?)\)", line)

        year = ""

        if year_match:
            year = year_match.group(1)

        # Remove year from line
        clean_line = re.sub(r"\(.*?\)", "", line).strip()

        parts = clean_line.split("–")

        if len(parts) >= 2:

            title = parts[0].strip()

            issuer = parts[1].strip()

        else:

            title = clean_line

            issuer = ""

        certifications.append({

            "title": title,

            "issuer": issuer,

            "year": year

        })

    return certifications