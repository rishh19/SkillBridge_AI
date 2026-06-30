from backend.services.resume_parser import extract_text_from_pdf
from backend.services.section_parser import split_resume_sections

resume_text = extract_text_from_pdf("test_files/sample_resume.pdf")

sections = split_resume_sections(resume_text)

for name, content in sections.items():

    print("=" * 60)
    print(name)
    print("=" * 60)

    print(content)
    print()