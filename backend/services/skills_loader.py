import re

from services.tokenizer import tokenize_text
from services.skills_loader import load_skill_database


SKILL_DATABASE = load_skill_database()


def extract_skills(text: str):

    text = tokenize_text(text)

    found_skills = set()

    for category in SKILL_DATABASE.values():

        for skill in category:

            skill = skill.lower()

            if skill == "c":

                pattern = r"\bc\b"

            elif skill == "c++":

                pattern = r"\bc\+\+"

            else:

                pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):

                found_skills.add(skill)

    return sorted(found_skills)