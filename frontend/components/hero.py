import streamlit as st


def render_hero():
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-eyebrow">⚡ AI-Powered Career Intelligence</div>
        <div class="hero-title">SkillBridge <span class="accent">AI</span></div>
        <p class="hero-subtitle">
            Get an instant, data-driven breakdown of how your resume stacks up
            against any job description — ATS scoring, skill-gap detection,
            and a personalized roadmap to close the gap.
        </p>
        <div class="feature-row">
            <div class="feature-pill"><span class="icon">📄</span> Resume Parsing</div>
            <div class="feature-pill"><span class="icon">🎯</span> ATS Scoring</div>
            <div class="feature-pill"><span class="icon">🧠</span> Skill Matching</div>
            <div class="feature-pill"><span class="icon">📈</span> Smart Recommendations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)