import streamlit as st
from utils.api import analyze_resume


def render_upload_section():

    st.markdown("## 📄 Resume Analysis")

    left, right = st.columns([1.2, 1])

    with left:

        resume = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"],
            help="Upload your latest resume in PDF format."
        )

        if resume is not None:

            file_size = len(resume.getvalue()) / (1024 * 1024)

            if file_size > 10:
                st.error("Resume size must be less than 10 MB.")
                return None

            st.success(
                f"✅ {resume.name} ({file_size:.2f} MB)"
            )

    with right:

        st.info(
            """
### 💡 Tips

✔ Upload ATS-friendly PDF

✔ Keep projects updated

✔ Mention technical skills

✔ Add certifications

✔ Use action verbs

✔ Keep resume under 2 pages
"""
        )

    st.markdown("### 💼 Job Description")

    job_description = st.text_area(
        "",
        height=260,
        placeholder="Paste complete Job Description here..."
    )

    analyze = st.button(
        "🚀 Analyze Resume",
        width="stretch"
    )

    if not analyze:
        return None

    if resume is None:
        st.warning("Please upload a resume.")
        return None

    if not job_description.strip():
        st.warning("Please enter the job description.")
        return None

    with st.spinner("🤖 AI is analyzing your resume..."):

        result = analyze_resume(
            resume,
            job_description
        )

    return result