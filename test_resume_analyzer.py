import json

from backend.services.resume_parser import extract_text_from_pdf
from backend.services.resume_analyzer import analyze_resume

resume_text = extract_text_from_pdf("test_files/sample_resume.pdf")

result = analyze_resume(resume_text)

print(json.dumps(result, indent=4))