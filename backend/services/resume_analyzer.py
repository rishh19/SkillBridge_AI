from backend.services.candidate_builder import build_candidate_profile


def analyze_resume(resume_text: str):

    profile = build_candidate_profile(resume_text)

    return {
        "candidate_profile": profile.model_dump()
    }