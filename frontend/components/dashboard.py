import streamlit as st

from components.ats_card import render_ats_card
from components.profile_card import render_profile_card
from components.skills_card import render_skills_card
from components.recommendation_card import render_recommendation_card
from components.charts import render_charts


def render_dashboard(result):

    if result is None:
        return

    ats = result["ats_score"]
    profile = result["candidate_profile"]
    matching = result["matching"]
    recommendations = result["recommendations"]

    st.write("✅ Dashboard started")

    try:
        render_ats_card(ats)
        st.write("✅ ATS Card OK")
    except Exception as e:
        st.error(f"ATS Card Error: {e}")
        return

    try:
        render_profile_card(profile)
        st.write("✅ Profile Card OK")
    except Exception as e:
        st.error(f"Profile Card Error: {e}")
        return

    try:
        render_skills_card(matching)
        st.write("✅ Skills Card OK")
    except Exception as e:
        st.error(f"Skills Card Error: {e}")
        return

    try:
        render_charts(ats, matching)
        st.write("✅ Charts OK")
    except Exception as e:
        st.error(f"Charts Error: {e}")
        return

    try:
        render_recommendation_card(recommendations)
        st.write("✅ Recommendation Card OK")
    except Exception as e:
        st.error(f"Recommendation Card Error: {e}")
        return