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

    st.markdown('<div class="sb-section-title">📊 Analysis Dashboard</div>', unsafe_allow_html=True)

    render_ats_card(ats)
    render_profile_card(profile)
    render_skills_card(matching)
    render_charts(ats, matching)
    render_recommendation_card(recommendations)