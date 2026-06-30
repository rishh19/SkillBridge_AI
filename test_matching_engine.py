import json

from backend.services.matching_engine import match_skills

candidate_skills = [
    "python",
    "sql",
    "git",
    "pandas",
    "numpy",
    "machine learning"
]

job_skills = [
    "python",
    "sql",
    "docker",
    "aws",
    "tensorflow",
    "machine learning"
]

result = match_skills(
    candidate_skills,
    job_skills
)

print(json.dumps(result, indent=4))