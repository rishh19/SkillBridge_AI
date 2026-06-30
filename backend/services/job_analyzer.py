from services.job_builder import build_job_profile


def analyze_job(job_description: str):

    profile = build_job_profile(job_description)

    return profile.model_dump()