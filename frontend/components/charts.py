import streamlit as st
import plotly.graph_objects as go


def _palette():
    is_dark = st.session_state.get("theme", "dark") == "dark"
    if is_dark:
        return {
            "template": "plotly_dark",
            "paper": "rgba(0,0,0,0)",
            "plot": "rgba(0,0,0,0)",
            "font": "#e5e7eb",
            "grid_bg": "#141b2d",
            "muted": "#94a3b8",
        }
    return {
        "template": "plotly_white",
        "paper": "rgba(0,0,0,0)",
        "plot": "rgba(0,0,0,0)",
        "font": "#0f172a",
        "grid_bg": "#eef1f7",
        "muted": "#64748b",
    }


COLORS = {
    "skills":     "#6366f1",
    "education":  "#22c55e",
    "experience": "#f59e0b",
    "quality":    "#06b6d4",
    "matched":    "#22c55e",
    "missing":    "#ef4444",
}


def _hex_to_rgba(hex_color: str, alpha: float) -> str:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def _layout(p):
    return dict(
        template=p["template"],
        paper_bgcolor=p["paper"],
        plot_bgcolor=p["plot"],
        font=dict(color=p["font"], family="Inter, sans-serif"),
        margin=dict(t=50, b=30, l=20, r=20),
    )


def _gauge_chart(score: float) -> go.Figure:
    p = _palette()

    if score >= 90:
        color = "#22c55e"
    elif score >= 75:
        color = "#84cc16"
    elif score >= 50:
        color = "#f59e0b"
    else:
        color = "#ef4444"

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        delta={"reference": 75, "valueformat": ".1f"},
        gauge={
            "axis": {"range": [0, 100], "tickwidth": 1, "tickcolor": p["muted"]},
            "bar": {"color": color, "thickness": 0.3},
            "bgcolor": p["grid_bg"],
            "borderwidth": 0,
            "steps": [
                {"range": [0, 50],   "color": p["grid_bg"]},
                {"range": [50, 75],  "color": p["grid_bg"]},
                {"range": [75, 90],  "color": p["grid_bg"]},
                {"range": [90, 100], "color": p["grid_bg"]},
            ],
            "threshold": {
                "line": {"color": p["font"], "width": 3},
                "thickness": 0.75,
                "value": 75,
            },
        },
        title={"text": "ATS Score", "font": {"size": 16, "color": p["font"]}},
    ))
    fig.update_layout(height=300, **_layout(p))
    return fig


def _breakdown_bar(breakdown: dict) -> go.Figure:

    p = _palette()

    labels = [
        "Skills",
        "Critical Skills",
        "Education",
        "Experience",
        "Projects",
        "Certifications",
        "Resume Quality"
    ]

    max_scores = {
        "skills": 40,
        "critical_skills": 20,
        "education": 10,
        "experience": 10,
        "projects": 10,
        "certifications": 5,
        "resume_quality": 5,
    }

    values = [
        round((breakdown.get("skills", 0) / max_scores["skills"]) * 100, 1),
        round((breakdown.get("critical_skills", 0) / max_scores["critical_skills"]) * 100, 1),
        round((breakdown.get("education", 0) / max_scores["education"]) * 100, 1),
        round((breakdown.get("experience", 0) / max_scores["experience"]) * 100, 1),
        round((breakdown.get("projects", 0) / max_scores["projects"]) * 100, 1),
        round((breakdown.get("certifications", 0) / max_scores["certifications"]) * 100, 1),
        round((breakdown.get("resume_quality", 0) / max_scores["resume_quality"]) * 100, 1),
    ]

    colors = [
        COLORS["skills"],
        "#8b5cf6",
        COLORS["education"],
        COLORS["experience"],
        "#3b82f6",
        "#10b981",
        COLORS["quality"],
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            marker_color=colors,
            text=[f"{v}%" for v in values],
            textposition="outside",
        )
    )

    fig.update_layout(
        title="ATS Score Breakdown (%)",
        height=420,
        yaxis=dict(range=[0, 100], title="Percentage"),
        showlegend=False,
        **_layout(p),
    )

    return fig


def _skill_donut(matching: dict) -> go.Figure:
    p = _palette()
    matched = len(matching["matched_skills"])
    missing = len(matching["missing_skills"])
    total = matched + missing or 1

    fig = go.Figure(go.Pie(
        labels=["Matched", "Missing"],
        values=[matched, missing],
        hole=0.65,
        marker=dict(colors=[COLORS["matched"], COLORS["missing"]],
                    line=dict(color=p["grid_bg"], width=2)),
        textinfo="label+percent",
        textfont=dict(size=13, color="#ffffff"),
    ))
    fig.add_annotation(
        text=f"<b>{matched}/{total}</b>",
        x=0.5, y=0.5,
        font=dict(size=22, color=p["font"]),
        showarrow=False,
    )
    fig.update_layout(
        title="Skill Match",
        height=380,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, x=0.25),
        **_layout(p),
    )
    return fig


def render_charts(ats_score: dict, matching: dict):
    st.markdown('<div class="sb-section-title">📊 ATS Analytics</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.plotly_chart(_gauge_chart(ats_score["score"]), width="stretch")
    with col2:
        st.plotly_chart(_skill_donut(matching), width="stretch")

    st.plotly_chart(_breakdown_bar(ats_score["breakdown"]), width="stretch")