import streamlit as st


def render_footer():

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns([3, 2, 3])

    with col1:
        st.caption("🚀 SkillBridge AI")

    with col2:
        st.caption("Version 1.0.0")

    with col3:
        st.caption("Developed by Rishav Kumar Shrivastava")

    st.markdown(
        """
<div style="
text-align:center;
padding:18px;
margin-top:10px;
font-size:14px;
color:var(--text-dim);
">

Built with ❤️ for SkillBridge AI - Developed by Rishav Kumar Shrivastava | Aspiring Data Scientist

<br><br>

© 2026 SkillBridge AI

</div>
""",
        unsafe_allow_html=True,
    )