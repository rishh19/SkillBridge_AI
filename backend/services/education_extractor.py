import re


def extract_education(education_text: str):

    education = []

    lines = [
        line.strip()
        for line in education_text.splitlines()
        if line.strip()
    ]

    degree = None
    institution = None
    graduation_year = None
    cgpa = None

    for line in lines:

        if degree is None and any(
            keyword in line.lower()
            for keyword in [
                "b.tech",
                "btech",
                "b.e",
                "be",
                "bachelor",
                "master",
                "m.tech",
                "mtech",
                "phd"
            ]
        ):
            degree = line

        if institution is None and any(
            keyword in line.lower()
            for keyword in [
                "university",
                "college",
                "institute"
            ]
        ):
            institution = line

        year_match = re.search(r"(20\d{2})", line)

        if year_match:
            graduation_year = year_match.group()

        cgpa_match = re.search(r"(\d+\.\d+)", line)

        if cgpa_match:
            cgpa = cgpa_match.group()

    education.append({

        "degree": degree,

        "institution": institution,

        "graduation_year": graduation_year,

        "cgpa": cgpa

    })

    return education