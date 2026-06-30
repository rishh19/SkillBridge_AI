import streamlit as st


def render_skills_card(matching: dict):
    matched = matching.get("matched_skills", [])
    missing = matching.get("missing_skills", [])
    pct = matching.get("match_percentage", 0)

    st.markdown('<div class="sb-section-title">🧠 Skill Analysis</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Match %", f"{pct:.1f}%")
    c2.metric("Matched Skills", len(matched))
    c3.metric("Missing Skills", len(missing))

    st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div style="font-weight:700;font-size:14px;margin-bottom:10px;color:var(--text);">✅ Matched Skills</div>', unsafe_allow_html=True)
        if matched:
            pills = "".join(
                f'<span style="background:var(--success-soft);color:var(--success);'
                f'border:1px solid var(--success);border-radius:20px;padding:5px 13px;'
                f'font-size:12.5px;font-weight:600;margin:3px;display:inline-block;">'
                f'{s.title()}</span>'
                for s in matched
            )
            st.markdown(f'<div>{pills}</div>', unsafe_allow_html=True)
        else:
            st.warning("No skill matches found.")

    with col2:
        st.markdown('<div style="font-weight:700;font-size:14px;margin-bottom:10px;color:var(--text);">❌ Missing Skills</div>', unsafe_allow_html=True)
        if missing:
            pills = "".join(
                f'<span style="background:var(--danger-soft);color:var(--danger);'
                f'border:1px solid var(--danger);border-radius:20px;padding:5px 13px;'
                f'font-size:12.5px;font-weight:600;margin:3px;display:inline-block;">'
                f'{s.title()}</span>'
                for s in missing
            )
            st.markdown(f'<div>{pills}</div>', unsafe_allow_html=True)
        else:
            st.success("🎉 No missing skills! Perfect match.")

    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)