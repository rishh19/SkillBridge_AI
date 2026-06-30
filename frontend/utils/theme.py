import streamlit as st

_THEMES = {
    "dark": {
        "--bg": "#0b1220",
        "--bg-soft": "#0f1729",
        "--card": "#141b2d",
        "--card-border": "#232b41",
        "--text": "#e5e7eb",
        "--text-dim": "#94a3b8",
        "--primary": "#6366f1",
        "--primary-soft": "rgba(99,102,241,0.15)",
        "--success": "#22c55e",
        "--success-soft": "rgba(34,197,94,0.14)",
        "--danger": "#ef4444",
        "--danger-soft": "rgba(239,68,68,0.14)",
        "--warning": "#f59e0b",
        "--warning-soft": "rgba(245,158,11,0.14)",
        "--shadow": "0 8px 30px rgba(0,0,0,0.35)",
    },

    "light": {
        "--bg": "#f5f7fb",
        "--bg-soft": "#eef1f7",
        "--card": "#ffffff",
        "--card-border": "#dde3ee",
        "--text": "#0f172a",
        "--text-dim": "#52607a",
        "--primary": "#4f46e5",
        "--primary-soft": "rgba(79,70,229,0.10)",
        "--success": "#15803d",
        "--success-soft": "rgba(21,128,61,0.10)",
        "--danger": "#b91c1c",
        "--danger-soft": "rgba(185,28,28,0.10)",
        "--warning": "#b45309",
        "--warning-soft": "rgba(180,83,9,0.10)",
        "--shadow": "0 8px 30px rgba(15,23,42,0.10)",
    },
}


def initialize_theme():

    if "theme" not in st.session_state:
        st.session_state.theme = "dark"


def apply_theme():

    initialize_theme()

    vars_dict = _THEMES[st.session_state.theme]

    css = ""

    for key, value in vars_dict.items():
        css += f"{key}:{value};"

    st.markdown(
        f"""
<style>

:root{{
{css}
}}

.stApp{{
background:var(--bg);
}}

</style>
""",
        unsafe_allow_html=True,
    )


def render_theme_toggle():

    initialize_theme()

    option = st.segmented_control(
        "Appearance",
        ["🌙 Dark", "☀️ Light"],
        default="🌙 Dark" if st.session_state.theme == "dark" else "☀️ Light",
    )

    if option == "🌙 Dark":
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"