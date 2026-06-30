import streamlit as st

from assets.style import load_css
from utils.theme import apply_theme, render_theme_toggle
from utils.api import analyze_resume

from components.hero import render_hero
from components.dashboard import render_dashboard
from components.footer import render_footer

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------
# Theme + CSS (theme must apply before anything renders)
# ----------------------------------------------------

apply_theme()
load_css()

# ----------------------------------------------------
# Top bar: theme toggle (no sidebar dependency)
# ----------------------------------------------------

render_theme_toggle()

# ----------------------------------------------------
# Hero
# ----------------------------------------------------

render_hero()

# ----------------------------------------------------
# Upload + Job Description
# ----------------------------------------------------

st.markdown('<div class="sb-section-title">📄 Resume Analysis</div>', unsafe_allow_html=True)

left, right = st.columns([1.3, 1])

with left:
    resume = st.file_uploader(
        "Upload your resume",
        type=["pdf"],
        help="PDF only, max 10MB",
    )

    if resume is not None:
        file_size_mb = len(resume.getvalue()) / (1024 * 1024)
        if file_size_mb > 10:
            st.error("File too large. Please upload a PDF under 10MB.")
            resume = None
        else:
            st.success(f"✅ {resume.name}  ·  {file_size_mb:.2f} MB")

with right:
    st.markdown(
        """
        <div class="sb-card" style="height:100%;">
        <div style="font-weight:800;font-size:15px;margin-bottom:10px;">💡 Resume Tips</div>
        <div style="color:var(--text-dim);font-size:13.5px;line-height:2;">
        ✅ ATS-friendly formatting<br>
        ✅ Clean, single-column PDF<br>
        ✅ Updated, relevant skills<br>
        ✅ Quantified project impact<br>
        ✅ Relevant certifications
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

job_description = st.text_area(
    "💼 Paste the Job Description",
    height=220,
    placeholder="Paste the complete job description here...",
)

analyze = st.button("🚀 Analyze Resume", width="stretch")

result = None

if analyze:
    if resume is None:
        st.warning("Please upload a resume.")
    elif not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        with st.spinner("🤖 Analyzing your resume..."):
            result = analyze_resume(resume, job_description)

# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

if result is not None:
    st.success("✅ Analysis complete")
    render_dashboard(result)

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

render_footer()