import re


SECTION_PATTERNS = {

    "PROFESSIONAL SUMMARY": [
        "professional summary",
        "summary",
        "profile",
        "career objective",
        "objective",
        "about me"
    ],

    "EDUCATION": [
        "education",
        "academic background",
        "academic qualification",
        "qualification"
    ],

    "SKILLS": [
        "skills",
        "technical skills",
        "core skills",
        "key skills",
        "technical expertise",
        "technologies",
        "tools"
    ],

    "EXPERIENCE": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "internship",
        "internships"
    ],

    "PROJECTS": [
        "projects",
        "academic projects",
        "personal projects",
        "project experience",
        "major projects",
        "minor projects"
    ],

    "CERTIFICATIONS": [
        "certifications",
        "certificates",
        "licenses",
        "training"
    ],

    "ACHIEVEMENTS": [
        "achievements",
        "awards",
        "honors",
        "accomplishments"
    ]

}


def find_section(header):

    header = header.lower().strip()

    header = re.sub(r"[:\-]+$", "", header)

    for section, aliases in SECTION_PATTERNS.items():

        for alias in aliases:

            if header == alias:

                return section

    return None


def split_resume_sections(resume_text: str):

    sections = {}

    current_section = "HEADER"

    sections[current_section] = []

    for line in resume_text.splitlines():

        line = line.strip()

        if not line:

            continue

        detected = find_section(line)

        if detected:

            current_section = detected

            if current_section not in sections:

                sections[current_section] = []

            continue

        sections[current_section].append(line)

    for section in sections:

        sections[section] = "\n".join(sections[section])

    return sections