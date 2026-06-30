def calculate_ats_score(candidate_profile, job_profile, matching_result):

    # =====================================================
    # Weight Configuration
    # =====================================================

    WEIGHTS = {
        "skill_match": 40,
        "critical_skills": 20,
        "education": 10,
        "experience": 10,
        "projects": 10,
        "certifications": 5,
        "resume_quality": 5
    }

    # =====================================================
    # Skill Match (40)
    # =====================================================

    skill_score = round(
        (matching_result["match_percentage"] / 100)
        * WEIGHTS["skill_match"],
        2
    )

    # =====================================================
    # Critical Skill Match (20)
    # =====================================================

    critical_score = round(
        (
            matching_result["critical_match_percentage"]
            / 100
        )
        * WEIGHTS["critical_skills"],
        2
    )

    # =====================================================
    # Education (10)
    # =====================================================

    education = candidate_profile.get("education", [])

    if not education:

        education_score = 0

    else:

        degree = education[0].get(
            "degree",
            ""
        ).lower()

        if any(
            x in degree
            for x in [
                "computer",
                "information",
                "artificial intelligence",
                "data science",
                "software",
                "electronics"
            ]
        ):

            education_score = 10

        else:

            education_score = 7

    # =====================================================
    # Experience (10)
    # =====================================================

    experience = candidate_profile.get(
        "experience",
        []
    )

    exp_count = len(experience)

    if exp_count == 0:

        experience_score = 0

    elif exp_count == 1:

        experience_score = 7

    else:

        experience_score = 10

    # =====================================================
    # Projects (10)
    # =====================================================

    projects = candidate_profile.get(
        "projects",
        []
    )

    if len(projects) >= 4:

        project_score = 10

    elif len(projects) == 3:

        project_score = 8

    elif len(projects) == 2:

        project_score = 6

    elif len(projects) == 1:

        project_score = 3

    else:

        project_score = 0

    # =====================================================
    # Certifications (5)
    # =====================================================

    certifications = candidate_profile.get(
        "certifications",
        []
    )

    cert_score = min(
        len(certifications),
        5
    )

    # =====================================================
    # Resume Quality (5)
    # =====================================================

    quality_score = 0

    if candidate_profile.get("name"):
        quality_score += 1

    if education:
        quality_score += 1

    if experience:
        quality_score += 1

    if projects:
        quality_score += 1

    if candidate_profile.get("skills"):
        quality_score += 1

    # =====================================================
    # Final Score
    # =====================================================

    total = round(

        skill_score
        + critical_score
        + education_score
        + experience_score
        + project_score
        + cert_score
        + quality_score,

        2

    )

    total = min(total, 100)

    # =====================================================
    # Rating
    # =====================================================

    if total >= 90:

        rating = "Excellent Match"

        emoji = "🏆"

    elif total >= 75:

        rating = "Good Match"

        emoji = "✅"

    elif total >= 60:

        rating = "Average Match"

        emoji = "⚠️"

    else:

        rating = "Needs Improvement"

        emoji = "❌"

    # =====================================================
    # Return
    # =====================================================

    return {

        "score": total,

        "rating": rating,

        "emoji": emoji,

        "breakdown": {

            "skills": skill_score,

            "critical_skills": critical_score,

            "education": education_score,

            "experience": experience_score,

            "projects": project_score,

            "certifications": cert_score,

            "resume_quality": quality_score

        }

    }