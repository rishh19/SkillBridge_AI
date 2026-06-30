from services.resume_analyzer import analyze_resume
from services.job_analyzer import analyze_job
from services.matching_engine import match_skills
from services.recommendation_engine import generate_recommendations
from services.ats_engine import calculate_ats_score

def analyze_candidate_for_job(resume_text, job_description):

    resume_result = analyze_resume(resume_text)

    job_result = analyze_job(job_description)

    candidate_skills = resume_result["candidate_profile"]["skills"]

    job_skills = job_result["required_skills"]

    matching_result = match_skills(
        candidate_skills,
        job_skills
    )

    recommendations = generate_recommendations(
    matching_result
    )

    ats_score = calculate_ats_score(
    resume_result["candidate_profile"],
    job_result,
    matching_result
    )

    return {

    "ats_score": ats_score,

    "candidate_profile": resume_result["candidate_profile"],

    "job_profile": job_result,

    "matching": matching_result,

    "recommendations": recommendations

    }