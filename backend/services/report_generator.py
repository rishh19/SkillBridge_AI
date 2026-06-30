def generate_report(
    ats_score,
    matching_result,
    recommendations
):

    if ats_score >= 90:
        rating = "Excellent Match"

    elif ats_score >= 75:
        rating = "Good Match"

    elif ats_score >= 50:
        rating = "Average Match"

    else:
        rating = "Needs Improvement"

    return {

        "summary": {

            "ats_score": ats_score,

            "rating": rating,

            "matched_skills": len(
                matching_result["matched_skills"]
            ),

            "missing_skills": len(
                matching_result["missing_skills"]
            )
        },

        "matched_skills":
            matching_result["matched_skills"],

        "missing_skills":
            matching_result["missing_skills"],

        "recommendations":
            recommendations
    }