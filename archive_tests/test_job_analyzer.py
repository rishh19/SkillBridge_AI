import json

from backend.services.job_analyzer import analyze_job

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

result = analyze_job(job_description)

print(json.dumps(result, indent=4))