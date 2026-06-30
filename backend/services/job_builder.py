from models.job_profile import JobProfile
from services.job_parser import clean_job_description
from services.skill_extractor import extract_skills
import re


def build_job_profile(job_description: str):

    profile = JobProfile()

    cleaned_text = clean_job_description(job_description)

    profile.raw_job_description = cleaned_text

    lines = cleaned_text.splitlines()

    # -----------------------------
    # Job Title
    # -----------------------------
    if lines:
        profile.job_title = lines[0].strip()

    # -----------------------------
    # Skills
    # -----------------------------
    profile.required_skills = extract_skills(cleaned_text)

    # -----------------------------
    # Preferred Skills
    # -----------------------------
    preferred = []

    preferred_keywords = [
        "good to have",
        "preferred",
        "bonus",
        "nice to have",
        "plus",
        "advantage"
    ]

    lower_text = cleaned_text.lower()

    for key in preferred_keywords:

        if key in lower_text:

            idx = lower_text.find(key)

            block = cleaned_text[idx:idx + 350]

            preferred.extend(extract_skills(block))

    profile.preferred_skills = sorted(list(set(preferred)))

    # -----------------------------
    # Education
    # -----------------------------
    education_patterns = [

        r"b\.?tech",

        r"bachelor",

        r"master",

        r"m\.?tech",

        r"b\.?e",

        r"computer science",

        r"information technology",

        r"engineering"
    ]

    education_found = []

    for pattern in education_patterns:

        if re.search(pattern, lower_text):

            education_found.append(pattern)

    profile.required_education = ", ".join(education_found)

    # -----------------------------
    # Experience
    # -----------------------------
    exp_match = re.search(

        r"(\d+)\+?\s*(?:years?|yrs?)",

        lower_text

    )

    if exp_match:

        profile.required_experience = exp_match.group(1) + " years"

    else:

        profile.required_experience = "Not Specified"

    return profile