from backend.models.candidate_profile import CandidateProfile
from backend.services.section_parser import split_resume_sections
from backend.services.skill_extractor import extract_skills
from backend.services.education_extractor import extract_education
from backend.services.project_extractor import extract_projects
from backend.services.experience_extractor import extract_experience
from backend.services.name_extractor import extract_candidate_name
from backend.services.certification_extractor import extract_certifications


def build_candidate_profile(resume_text: str) -> CandidateProfile:

    profile = CandidateProfile()

    # Store complete resume text
    profile.raw_resume_text = resume_text

    # Split resume into sections
    sections = split_resume_sections(resume_text)

    # Extract Header
    header = sections.get("HEADER", "")
    profile.candidate_name = extract_candidate_name(header)

    # Extract Skills
    skills_text = "\n".join([
    sections.get("SKILLS", ""),
    sections.get("PROJECTS", ""),
    sections.get("EXPERIENCE", ""),
    sections.get("PROFESSIONAL SUMMARY", "")
    ])

    profile.skills = extract_skills(skills_text)

    # Extract Education
    education_section = sections.get("EDUCATION", "")
    profile.education = extract_education(education_section)

    # Extract Experience
    experience_section = sections.get("EXPERIENCE", "")
    profile.experience = extract_experience(experience_section)

    # Extract Project
    project_section = sections.get("PROJECTS", "")
    profile.projects = extract_projects(project_section)

    # Extract Certificate
    achievement_section = sections.get("ACHIEVEMENTS", "")
    profile.certifications = extract_certifications(achievement_section)

    return profile