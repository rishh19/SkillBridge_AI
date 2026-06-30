from backend.services.resume_parser import extract_text_from_pdf
from backend.services.skill_extractor import extract_skills

text = extract_text_from_pdf(
    "test_files/sample_resume.pdf"
)

skills = extract_skills(text)

print(skills)