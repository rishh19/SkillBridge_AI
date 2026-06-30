import streamlit as st


def _card(html_inner: str, accent: str = "var(--primary)") -> str:
    return (
        f'<div style="background:var(--card);border:1px solid var(--card-border);'
        f'border-left:4px solid {accent};border-radius:14px;padding:16px 18px;'
        f'margin-bottom:12px;height:100%;">{html_inner}</div>'
    )


def _education_html(edu) -> str:
    if not isinstance(edu, dict):
        return str(edu)
    degree = edu.get("degree") or "Degree N/A"
    institution = edu.get("institution") or "Institution N/A"
    year = edu.get("graduation_year") or "Year N/A"
    cgpa = edu.get("cgpa") or ""
    html = (
        f'<div style="font-weight:700;color:var(--text);font-size:15px;">{degree}</div>'
        f'<div style="font-size:13px;color:var(--text-dim);margin-top:5px;">🏫 {institution}</div>'
        f'<div style="font-size:13px;color:var(--text-dim);margin-top:3px;">📅 {year}'
    )
    if cgpa and cgpa != "N/A":
        html += f' &nbsp;·&nbsp; 📊 CGPA {cgpa}'
    html += '</div>'
    return html


def _experience_html(exp) -> str:
    if not isinstance(exp, dict):
        return str(exp)
    position = exp.get("position", "Unknown Position")
    duration = exp.get("duration", "")
    description = exp.get("description", [])
    if isinstance(description, list):
        description = " ".join(description)
    html = f'<div style="font-weight:700;color:var(--text);font-size:15px;">{position}</div>'
    if duration:
        html += f'<div style="font-size:13px;color:var(--text-dim);margin-top:3px;">🗓 {duration}</div>'
    if description:
        html += f'<div style="font-size:13px;color:var(--text-dim);margin-top:8px;line-height:1.65;">{description}</div>'
    return html


def _project_html(proj) -> str:
    if not isinstance(proj, dict):
        return str(proj)
    name = proj.get("project_name", "Unknown Project")
    desc = proj.get("description", "")
    html = f'<div style="font-weight:700;color:var(--text);font-size:15px;">{name}</div>'
    if desc:
        html += f'<div style="font-size:13px;color:var(--text-dim);margin-top:8px;line-height:1.65;">{desc}</div>'
    return html


def _cert_html(cert) -> str:
    if not isinstance(cert, dict):
        return str(cert)
    title = cert.get("title") or cert.get("certification") or cert.get("name", "Certification")
    issuer = cert.get("issuer", "")
    year = cert.get("year", "")
    html = f'<div style="font-weight:700;color:var(--text);font-size:13.5px;line-height:1.4;">{title}</div>'
    meta = []
    if issuer:
        meta.append(issuer)
    if year:
        meta.append(str(year))
    if meta:
        html += f'<div style="font-size:12px;color:var(--text-dim);margin-top:5px;">{" · ".join(meta)}</div>'
    return html


def _section_label(text: str) -> str:
    return f'<div style="font-weight:700;font-size:14.5px;margin:18px 0 10px 0;color:var(--text);">{text}</div>'


def render_profile_card(profile):
    st.markdown('<div class="sb-section-title">👤 Candidate Profile</div>', unsafe_allow_html=True)

    name = profile.get("candidate_name") or "Unknown Candidate"
    st.markdown(
        f'<div style="font-size:1.35rem;font-weight:800;color:var(--text);margin-bottom:18px;">🧑‍💻 {name}</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(_section_label("🎓 Education"), unsafe_allow_html=True)
        education = profile.get("education", [])
        if education:
            for edu in education:
                st.markdown(_card(_education_html(edu), "var(--primary)"), unsafe_allow_html=True)
        else:
            st.warning("No education information found.")

    with col2:
        st.markdown(_section_label("💼 Experience"), unsafe_allow_html=True)
        experience = profile.get("experience", [])
        if experience:
            for exp in experience:
                st.markdown(_card(_experience_html(exp), "var(--success)"), unsafe_allow_html=True)
        else:
            st.info("No experience entries found.")

    st.markdown(_section_label("🚀 Projects"), unsafe_allow_html=True)
    projects = profile.get("projects", [])
    if projects:
        pcol1, pcol2 = st.columns(2)
        for i, proj in enumerate(projects):
            target_col = pcol1 if i % 2 == 0 else pcol2
            with target_col:
                st.markdown(_card(_project_html(proj), "var(--primary)"), unsafe_allow_html=True)
    else:
        st.info("No projects found.")

    st.markdown(_section_label("📜 Certifications"), unsafe_allow_html=True)
    certs = profile.get("certifications", [])
    if certs:
        ccols = st.columns(3)
        for i, cert in enumerate(certs):
            with ccols[i % 3]:
                st.markdown(_card(_cert_html(cert), "var(--success)"), unsafe_allow_html=True)
    else:
        st.info("No certifications found.")

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)