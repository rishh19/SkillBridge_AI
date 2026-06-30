SKILL_ALIASES = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "js": "javascript",
    "ts": "typescript",
    "tf": "tensorflow",
    "torch": "pytorch",
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "xgb": "xgboost",
    "lgbm": "lightgbm",
    "k8s": "kubernetes",
    "pg": "postgresql",
    "postgres": "postgresql",
    "mongo": "mongodb",
    "node": "node.js",
    "next": "next.js",
    "pbi": "power bi",
    "powerbi": "power bi",
    "reactjs": "react",
}


CRITICAL_SKILLS = {
    "python",
    "sql",
    "machine learning",
    "data science",
    "scikit-learn",
    "tensorflow",
    "pytorch",
}


def normalize_skill(skill: str):

    skill = skill.lower().strip()

    return SKILL_ALIASES.get(skill, skill)


def normalize_skills(skills):

    return sorted(
        {
            normalize_skill(skill)
            for skill in skills
            if skill.strip()
        }
    )


def match_skills(candidate_skills, job_skills):

    candidate = set(normalize_skills(candidate_skills))

    job = set(normalize_skills(job_skills))

    matched = sorted(candidate & job)

    missing = sorted(job - candidate)

    if len(job) == 0:

        match_percentage = 0

    else:

        match_percentage = round(
            (len(matched) / len(job)) * 100,
            2
        )

    critical_required = sorted(
        CRITICAL_SKILLS & job
    )

    critical_matched = sorted(
        CRITICAL_SKILLS & set(matched)
    )

    critical_missing = sorted(
        set(critical_required) - set(critical_matched)
    )

    if len(critical_required):

        critical_percentage = round(

            len(critical_matched)
            /
            len(critical_required)
            *
            100,

            2

        )

    else:

        critical_percentage = 100

    return {

        "matched_skills": matched,

        "missing_skills": missing,

        "match_percentage": match_percentage,

        "critical_skills_required": critical_required,

        "critical_skills_matched": critical_matched,

        "critical_skills_missing": critical_missing,

        "critical_match_percentage": critical_percentage,

        "total_job_skills": len(job),

        "total_candidate_skills": len(candidate),

        "matched_count": len(matched),

        "missing_count": len(missing)

    }