import streamlit as st

_PRIORITY_COLORS = {
    "High":   "🔴",
    "Medium": "🟡",
    "Low":    "🟢",
}

_IMPACT_LABELS = {
    "High":   "🚀 High Resume Impact",
    "Medium": "📈 Medium Resume Impact",
    "Low":    "💡 Nice to Have",
}


def render_recommendation_card(recommendations: list):
    st.markdown('<div class="sb-section-title">💡 AI Recommendations</div>', unsafe_allow_html=True)

    if not recommendations:
        st.success("🎉 Excellent! Your resume covers all required skills.")
        return

    st.info(f"**{len(recommendations)} skill gap(s) identified.** Prioritized by impact on your ATS score.")

    for rec in recommendations:
        priority = rec.get("priority", "Medium")
        priority_emoji = _PRIORITY_COLORS.get(priority, "⚪")
        impact = _IMPACT_LABELS.get(rec.get("resume_impact", "Medium"), "")

        with st.expander(
            f"{priority_emoji} **{rec.get('title', rec.get('skill', 'Skill'))}**  — {priority} Priority   {impact}",
            expanded=(priority == "High"),
        ):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**❓ Why it matters:**  \n{rec.get('reason', '')}")
                st.markdown(f"**✅ What to do:**  \n{rec.get('suggestion', '')}")

            with col2:
                st.metric("Difficulty", rec.get("difficulty", "Intermediate"))
                st.metric("Time to Learn", rec.get("learning_time", "4-8 weeks"))

            resources = rec.get("resources", [])
            if resources:
                st.markdown("**📚 Suggested Resources:**")
                cols = st.columns(min(len(resources), 3))
                for i, res in enumerate(resources[:3]):
                    cols[i].markdown(f"• {res}")