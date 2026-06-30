import json
from pathlib import Path

_db_path = Path(__file__).resolve().parent.parent / "data" / "recommendation_database.json"

try:
    with open(_db_path, "r", encoding="utf-8") as _f:
        RECOMMENDATION_DATABASE = json.load(_f)
except FileNotFoundError:
    RECOMMENDATION_DATABASE = {}

_PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def _build_recommendation(skill: str) -> dict:
    data = RECOMMENDATION_DATABASE.get(skill.lower(), {})
    return {
        "skill": skill.title(),
        "priority": data.get("priority", "Medium"),
        "title": data.get("title", skill.title()),
        "reason": data.get("reason", f"'{skill.title()}' was listed in the job description but not found in your resume."),
        "suggestion": data.get("suggestion", f"Add projects or coursework demonstrating {skill.title()} to your resume."),
        "difficulty": data.get("difficulty", "Intermediate"),
        "learning_time": data.get("learning_time", "4-8 weeks"),
        "resources": data.get("resources", ["Coursera", "YouTube", "Official Docs"]),
        "resume_impact": data.get("resume_impact", "Medium"),
    }


def generate_recommendations(matching_result: dict) -> list:
    missing_skills = matching_result.get("missing_skills", [])
    recommendations = [_build_recommendation(skill) for skill in missing_skills]
    recommendations.sort(key=lambda r: _PRIORITY_ORDER.get(r["priority"], 99))
    return recommendations