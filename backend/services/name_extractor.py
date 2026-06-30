import re


def extract_candidate_name(header_text: str):

    lines = [
        line.strip()
        for line in header_text.splitlines()
        if line.strip()
    ]

    for line in lines:

        # Skip contact information
        if (
            "@" in line
            or "+" in line
            or "linkedin" in line.lower()
            or "github" in line.lower()
            or "|" in line
        ):
            continue

        # Skip lines containing numbers
        if re.search(r"\d", line):
            continue

        # Candidate name should be short
        if len(line.split()) <= 5:
            return line.title()

    return None