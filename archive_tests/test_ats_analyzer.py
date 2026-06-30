import json

from backend.services.resume_parser import extract_text_from_pdf
from backend.services.ats_analyzer import analyze_candidate_for_job

resume_text = extract_text_from_pdf(
    "test_files/sample_resume.pdf"
)

job_description = """
Data Scientist

Requirements

Python
SQL
Machine Learning
TensorFlow
Docker
AWS

Experience

2+ years

Education

Bachelor's Degree

Responsibilities

Build ML models
Deploy APIs
"""

result = analyze_candidate_for_job(
    resume_text,
    job_description
)

print(json.dumps(result, indent=4))