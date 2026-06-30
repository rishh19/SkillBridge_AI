import re
import json
from pathlib import Path

from services.tokenizer import tokenize_text


# ==========================================================
# Load Skills Database
# ==========================================================

_data_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "skills_database.json"
)

with open(_data_path, "r", encoding="utf-8") as f:
    SKILL_DATABASE = json.load(f)


# ==========================================================
# Skill Aliases
# ==========================================================

SKILL_ALIASES = {

    "ml": "machine learning",
    "ai": "artificial intelligence",
    "gen ai": "generative ai",
    "genai": "generative ai",

    "dl": "deep learning",

    "nlp": "natural language processing",

    "cv": "computer vision",

    "llm": "large language models",
    "llms": "large language models",

    "rag": "rag",

    "js": "javascript",

    "ts": "typescript",

    "tf": "tensorflow",

    "torch": "pytorch",

    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",

    "xgb": "xgboost",

    "lgbm": "lightgbm",

    "k8s": "kubernetes",

    "pg": "postgresql",

    "postgres": "postgresql",

    "mongo": "mongodb",

    "node": "node.js",

    "next": "next.js",

    "reactjs": "react",

    "tailwind": "tailwind css",

    "pbi": "power bi",
    "powerbi": "power bi",

    "aws ec2": "aws",
    "aws s3": "aws",

    "huggingface": "hugging face",

    "rest api": "rest api",
    "rest apis": "rest api",
}


# ==========================================================
# Build Master Skill List
# ==========================================================

ALL_SKILLS = set()

for category in SKILL_DATABASE.values():

    for skill in category:

        ALL_SKILLS.add(skill.lower())


# ==========================================================
# Normalize Text
# ==========================================================

def normalize_text(text: str):

    text = text.lower()

    for alias, actual in SKILL_ALIASES.items():

        text = re.sub(

            r"\b" + re.escape(alias) + r"\b",

            actual,

            text,

            flags=re.IGNORECASE

        )

    text = text.replace("/", " ")

    text = text.replace("-", "-")

    return text


# ==========================================================
# Skill Extraction
# ==========================================================

def extract_skills(text: str):

    text = tokenize_text(text)

    text = normalize_text(text)

    found = set()

    for skill in ALL_SKILLS:

        if skill == "c":

            pattern = r"\bc\b"

        elif skill == "c++":

            pattern = r"\bc\+\+"

        elif skill == "r":

            pattern = r"(?<!\w)r(?!\w)"

        else:

            pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(

            pattern,

            text,

            flags=re.IGNORECASE

        ):

            found.add(skill)

    return sorted(found)