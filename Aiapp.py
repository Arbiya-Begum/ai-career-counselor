import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Career Intelligence System", layout="centered", page_icon="🎯")

# -------------------- STYLING --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #f7f5f2;
    color: #1a1a2e;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #1a1a2e;
}

/* Header banner */
.header-banner {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 18px;
    padding: 40px 36px 32px 36px;
    margin-bottom: 32px;
    box-shadow: 0 8px 32px rgba(26,26,46,0.13);
}
.header-banner h1 {
    color: #f7f5f2 !important;
    font-size: 2.2rem;
    margin-bottom: 6px;
    letter-spacing: -0.5px;
}
.header-banner p {
    color: #a8b2d8;
    font-size: 1rem;
    margin: 0;
    font-style: italic;
}

/* Section cards */
.section-card {
    background: #ffffff;
    border-radius: 14px;
    padding: 28px 28px 20px 28px;
    margin-bottom: 24px;
    box-shadow: 0 2px 16px rgba(26,26,46,0.07);
    border-left: 4px solid #0f3460;
}

/* Metric pill */
.metric-pill {
    display: inline-block;
    background: #eef2ff;
    color: #0f3460;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.82rem;
    font-weight: 500;
    margin: 3px 3px;
    border: 1px solid #c7d2fe;
}

/* Pros/cons */
.pro-item { color: #166534; background: #f0fdf4; border-radius: 8px; padding: 6px 12px; margin: 4px 0; font-size: 0.92rem; }
.con-item { color: #991b1b; background: #fff1f2; border-radius: 8px; padding: 6px 12px; margin: 4px 0; font-size: 0.92rem; }

/* Roadmap steps */
.roadmap-step {
    background: #f7f5f2;
    border-radius: 10px;
    padding: 10px 16px;
    margin: 6px 0;
    border-left: 3px solid #0f3460;
    font-size: 0.93rem;
    color: #1a1a2e;
}

/* Result box */
.result-box {
    background: linear-gradient(135deg, #eef2ff, #f0fdf4);
    border-radius: 12px;
    padding: 20px 24px;
    margin-top: 16px;
    border: 1px solid #c7d2fe;
}

/* Match score bar */
.match-bar-bg {
    background: #e5e7eb;
    border-radius: 20px;
    height: 10px;
    margin: 6px 0 14px 0;
    overflow: hidden;
}
.match-bar-fill {
    height: 10px;
    border-radius: 20px;
    background: linear-gradient(to right, #0f3460, #4facfe);
}

/* Salary badge */
.salary-badge {
    background: #0f3460;
    color: #fff;
    border-radius: 8px;
    padding: 6px 16px;
    font-size: 0.95rem;
    font-weight: 600;
    display: inline-block;
    margin: 8px 0;
}

/* Divider */
.styled-divider {
    border: none;
    border-top: 2px solid #e5e7eb;
    margin: 28px 0;
}

/* Streamlit button override */
.stButton > button {
    background: linear-gradient(135deg, #1a1a2e, #0f3460) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    padding: 10px 24px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(15,52,96,0.18) !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* Radio / selectbox labels */
.stRadio label, .stSelectbox label { font-weight: 500; color: #1a1a2e; }

/* Success / warning overrides */
.stSuccess { border-radius: 10px; }
.stWarning { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown("""
<div class="header-banner">
    <h1>🎯 Career Intelligence System</h1>
    <p>"Clarity comes from action, not overthinking."</p>
</div>
""", unsafe_allow_html=True)

# --------------------