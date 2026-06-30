import streamlit as st


def render_ats_card(ats: dict):
    score = ats.get("score", 0)
    rating = ats.get("rating", "")
    emoji = ats.get("emoji", "📊")
    breakdown = ats.get("breakdown", {})

    if score >= 90:
        color = "#22c55e"
    elif score >= 75:
        color = "#84cc16"
    elif score >= 50:
        color = "#f59e0b"
    else:
        color = "#ef4444"

    stats_html = "".join([

    _mini_stat(
        "Skill Match",
        breakdown.get("skills", 0),
        40,
        "#2563eb"
    ),

    _mini_stat(
        "Critical",
        breakdown.get("critical_skills", 0),
        20,
        "#dc2626"
    ),

    _mini_stat(
        "Education",
        breakdown.get("education", 0),
        10,
        "#16a34a"
    ),

    _mini_stat(
        "Experience",
        breakdown.get("experience", 0),
        10,
        "#f59e0b"
    ),

    _mini_stat(
        "Projects",
        breakdown.get("projects", 0),
        10,
        "#8b5cf6"
    ),

    _mini_stat(
        "Certificates",
        breakdown.get("certifications", 0),
        5,
        "#0891b2"
    ),

    _mini_stat(
        "Resume",
        breakdown.get("resume_quality", 0),
        5,
        "#64748b"
    )

    ])

    html = (
        '<div class="sb-card" style="border-left:4px solid ' + color + ';">'
        '<div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:20px;">'
        '<div>'
        '<div style="font-size:13px;color:var(--text-dim);letter-spacing:1px;text-transform:uppercase;font-weight:700;margin-bottom:6px;">'
        'ATS Compatibility Score</div>'
        '<div style="font-size:58px;font-weight:900;color:' + color + ';line-height:1;">'
        f'{score:.0f}<span style="font-size:26px;color:var(--text-dim);font-weight:600;"> / 100</span></div>'
        f'<div style="font-size:18px;color:var(--text);margin-top:8px;font-weight:600;">{emoji} {rating}</div>'
        '</div>'
        f'<div style="display:flex;gap:12px;flex-wrap:wrap;">{stats_html}</div>'
        '</div>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def _mini_stat(label: str, value: float, max_val: int, color: str) -> str:
    pct = int((value / max_val) * 100) if max_val else 0
    return (
        '<div style="background:var(--bg-soft);border:1px solid var(--card-border);'
        'border-radius:12px;padding:12px 16px;min-width:96px;text-align:center;">'
        f'<div style="font-size:20px;font-weight:800;color:{color};">{value:.0f}'
        f'<span style="font-size:11px;color:var(--text-dim);font-weight:500;"> /{max_val}</span></div>'
        f'<div style="font-size:11.5px;color:var(--text-dim);margin-top:2px;font-weight:600;">{label}</div>'
        f'<div style="background:var(--card-border);border-radius:4px;height:4px;margin-top:8px;">'
        f'<div style="background:{color};width:{pct}%;height:4px;border-radius:4px;"></div></div>'
        '</div>'
    )