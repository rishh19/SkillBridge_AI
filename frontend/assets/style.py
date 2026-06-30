import streamlit as st


def load_css():
    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    html, body, [class*="css"]{
        font-family:'Inter',sans-serif;
    }

    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    header[data-testid="stHeader"]{
        background:transparent;
        height:0;
    }

    .block-container{
        padding-top:1.6rem;
        padding-left:3rem;
        padding-right:3rem;
        padding-bottom:3rem;
        max-width:1400px;
    }

    h1,h2,h3,h4,h5,h6{
        color:var(--text) !important;
    }

    /* ---------------- HERO ---------------- */

    .hero-wrap{
        position:relative;
        padding:44px 48px;
        border-radius:24px;
        background:var(--card);
        border:1px solid var(--card-border);
        box-shadow:var(--shadow);
        margin-bottom:28px;
        overflow:hidden;
    }

    .hero-wrap::before{
        content:"";
        position:absolute;
        top:-60%;
        right:-10%;
        width:420px;
        height:420px;
        background:radial-gradient(circle,var(--primary-soft) 0%,transparent 70%);
    }

    .hero-eyebrow{
        display:inline-flex;
        align-items:center;
        gap:8px;
        padding:6px 14px;
        border-radius:100px;
        background:var(--primary-soft);
        color:var(--primary);
        font-size:12px;
        font-weight:700;
        text-transform:uppercase;
        letter-spacing:1.3px;
    }

    .hero-title{
        font-size:2.8rem;
        font-weight:900;
        line-height:1.1;
        color:var(--text);
        margin-top:18px;
    }

    .hero-title .accent{
        background:linear-gradient(90deg,var(--primary),#8b5cf6);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .hero-subtitle{
        color:var(--text-dim);
        font-size:16px;
        line-height:1.7;
        margin-top:10px;
    }

    /* ---------------- FEATURE PILLS ---------------- */

    .feature-row{
        display:flex;
        gap:12px;
        flex-wrap:wrap;
        margin-top:25px;
    }

    .feature-pill{
        background:var(--bg-soft);
        border:1px solid var(--card-border);
        border-radius:12px;
        padding:12px 18px;
        color:var(--text);
        font-weight:600;
    }

    /* ---------------- CARDS ---------------- */

    .sb-card{
        background:var(--card);
        border:1px solid var(--card-border);
        border-radius:18px;
        padding:24px;
        box-shadow:var(--shadow);
        color:var(--text);
    }

    .sb-card p{
        color:var(--text-dim);
    }

    .sb-section-title{
        font-size:1.65rem;
        font-weight:800;
        color:var(--text);
        margin:12px 0 18px;
    }

    /* ---------------- GLOBAL TEXT ---------------- */

    p,
    li,
    span,
    strong,
    label{
        color:var(--text);
    }

    small{
        color:var(--text-dim);
    }

    [data-testid="stMarkdownContainer"] p{
        color:var(--text);
    }

    [data-testid="stMarkdownContainer"] li{
        color:var(--text);
    }

    /* ---------------- FILE UPLOADER ---------------- */

    [data-testid="stFileUploaderDropzone"]{
        border-radius:16px !important;
        border:1.5px dashed var(--card-border) !important;
        background:var(--bg-soft);
    }

    [data-testid="stFileUploaderDropzone"] *{
        color:var(--text) !important;
    }

    /* ---------------- TEXTAREA ---------------- */

    textarea{
        border-radius:14px !important;
        color:var(--text) !important;
        background:var(--card) !important;
    }

    textarea::placeholder{
        color:var(--text-dim) !important;
    }

    /* ---------------- BUTTON ---------------- */

    .stButton>button{
        width:100%;
        height:52px;
        border:none;
        border-radius:12px;
        background:linear-gradient(90deg,var(--primary),#818cf8);
        color:white !important;
        font-weight:700;
        transition:.2s;
    }

    .stButton>button:hover{
        transform:translateY(-2px);
    }

    .stButton>button p{
        color:white !important;
    }

    /* ---------------- METRICS ---------------- */

    [data-testid="stMetric"]{
        border:1px solid var(--card-border);
        border-radius:14px;
        background:var(--card);
    }

    [data-testid="stMetricLabel"]{
        color:var(--text-dim) !important;
    }

    [data-testid="stMetricValue"]{
        color:var(--text) !important;
        font-weight:800;
    }

    /* ---------------- EXPANDERS ---------------- */

    [data-testid="stExpander"]{
        border-radius:14px;
        border:1px solid var(--card-border);
    }

    [data-testid="stExpander"] summary{
        color:var(--text) !important;
        font-weight:700;
    }

    [data-testid="stExpander"] p{
        color:var(--text) !important;
    }

    /* ---------------- ALERTS ---------------- */

    [data-testid="stAlert"]{
        border-radius:14px;
    }

    [data-testid="stAlert"] *{
        color:var(--text) !important;
    }

    /* ---------------- SCROLLBAR ---------------- */

    ::-webkit-scrollbar{
        width:8px;
    }

    ::-webkit-scrollbar-thumb{
        background:var(--card-border);
        border-radius:8px;
    }

    </style>
    """, unsafe_allow_html=True)