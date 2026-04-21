  # Smart Career Intelligence System (Premium Version)

import streamlit as st
import matplotlib.pyplot as plt
import time
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# 🌐 CONFIG
st.set_page_config(page_title="Career Intelligence System", page_icon="🧠", layout="centered")

# 🎨 PREMIUM UI
st.markdown("""
<style>
body {background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);}
.stApp {background: transparent;}
.block-container {padding: 2rem;}
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# 🧠 HEADER
st.title("🧠 Career Intelligence System")
st.caption("“Clarity comes from action, not overthinking.”")
st.markdown("---")

# ================= QUIZ =================
st.markdown("## 🧠 Personal Intelligence Quiz")

col1, col2, col3 = st.columns(3)

with col1:
    q1 = st.radio("What excites you?", ["Solving problems", "Designing", "Leading"])
    q2 = st.radio("Your strength?", ["Logic", "Creativity", "Communication"])

with col2:
    q3 = st.radio("Work style?", ["Independent", "Teamwork", "Leadership"])
    q4 = st.radio("Favorite subject?", ["Math", "Arts", "Business"])

with col3:
    q5 = st.radio("Thinking type?", ["Analytical", "Creative", "Strategic"])
    q6 = st.radio("You prefer?", ["Coding", "Designing", "Managing"])

analyze_quiz = st.button("🔘 Analyze Intelligence")

# ================= USER INPUT =================
st.markdown("---")
st.markdown("## 💬 Tell Us About Yourself")

user_input = st.text_area("Describe your interests, goals, personality...")

analyze_user = st.button("🎯 Analyze My Profile")

# ================= LOGIC =================
def calculate_scores():
    scores = {"Tech": 0, "Creative": 0, "Business": 0}

    mapping = {
        "Solving problems": "Tech", "Designing": "Creative", "Leading": "Business",
        "Logic": "Tech", "Creativity": "Creative", "Communication": "Business",
        "Independent": "Tech", "Teamwork": "Creative", "Leadership": "Business",
        "Math": "Tech", "Arts": "Creative", "Business": "Business",
        "Analytical": "Tech", "Creative": "Creative", "Strategic": "Business",
        "Coding": "Tech", "Managing": "Business"
    }

    for ans in [q1, q2, q3, q4, q5, q6]:
        scores[mapping[ans]] += 1

    return scores

# 🧠 FAKE-AI GENERATOR
def smart_text(scores, user_input):
    dominant = max(scores, key=scores.get)

    base = f"""
Based on your responses, your dominant strength is **{dominant} Intelligence**.

Your input suggests: "{user_input[:120]}..."

This indicates a natural inclination towards structured thinking and growth-oriented mindset.
"""

    if dominant == "Tech":
        extra = """
You tend to break down problems logically and seek efficient solutions.

### 🎯 Best Career Matches:
- Data Scientist
- Software Developer
- AI Engineer
- Cybersecurity Analyst
- Cloud Engineer
- Machine Learning Engineer

### 🚀 Growth Path:
Learn Python → Work on real datasets → Build ML models → Deploy projects
"""

    elif dominant == "Creative":
        extra = """
You express ideas visually and think beyond conventional boundaries.

### 🎯 Best Career Matches:
- UI/UX Designer
- Graphic Designer
- Animator
- Video Editor
- Content Creator
- Creative Director

### 🚀 Growth Path:
Learn tools → Build portfolio → Freelance → Personal branding
"""

    else:
        extra = """
You naturally lead, strategize, and influence outcomes.

### 🎯 Best Career Matches:
- Business Analyst
- Entrepreneur
- Marketing Manager
- HR Manager
- Sales Strategist
- Product Manager

### 🚀 Growth Path:
Learn business fundamentals → Case studies → Internships → Networking
"""

    return base + extra

# ================= OUTPUT =================
if analyze_quiz:
    scores = calculate_scores()

    st.markdown("## 📊 Intelligence Breakdown")

    # 🔥 Animated feel
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    fig, ax = plt.subplots()
    ax.bar(scores.keys(), scores.values())
    st.pyplot(fig)

    st.success("Analysis Complete ✔")

if analyze_user:
    if not user_input:
        st.warning("Please enter your details")
    else:
        scores = calculate_scores()
        result = smart_text(scores, user_input)

        st.markdown("## 🎯 Personalized Insights")
        st.markdown(result)

        # PDF
        doc = SimpleDocTemplate("career_report.pdf")
        styles = getSampleStyleSheet()
        story = [Paragraph(result, styles["Normal"])]
        doc.build(story)

        with open("career_report.pdf", "rb") as f:
            st.download_button("📥 Download Report", f, "career_report.pdf")

# ================= EXPLORE =================
st.markdown("---")
st.markdown("## 🌍 Explore Career Paths")

category = st.selectbox("Choose domain", ["Technology", "Creative", "Business", "Science", "Healthcare"])

if st.button("🔎 Show Careers"):
    st.markdown("""
### 📌 Career Options
- Data Scientist  
- Software Developer  
- AI Engineer  
- Cybersecurity Analyst  
- Cloud Engineer  
- UI/UX Designer  
- Animator  
- Graphic Designer  
- Business Analyst  
- Entrepreneur  
- Marketing Manager  
- HR Manager  
- Doctor  
- Nurse  
- Research Scientist  
""")

# ================= EXPLAIN =================
st.markdown("---")
st.markdown("## 🔍 Career Explorer")

career_options = [
    "Data Scientist", "Software Developer", "AI Engineer",
    "UI/UX Designer", "Graphic Designer",
    "Business Analyst", "Entrepreneur",
    "Doctor", "Research Scientist"
]

selected = st.selectbox("Select a career", career_options)

career_info = {
    "Data Scientist": "Analyzes data to extract insights using Python, ML, and statistics.",
    "Software Developer": "Builds applications and systems using programming.",
    "AI Engineer": "Designs intelligent systems and machine learning models.",
    "UI/UX Designer": "Creates user-friendly digital experiences.",
    "Graphic Designer": "Designs visual content and branding.",
    "Business Analyst": "Solves business problems using data and strategy.",
    "Entrepreneur": "Builds and manages business ventures.",
    "Doctor": "Diagnoses and treats patients.",
    "Research Scientist": "Conducts experiments and advances knowledge."
}

if st.button("📖 Show Details"):
    st.markdown(f"### {selected}")
    st.markdown(career_info[selected])

# FOOTER
st.markdown("---")
st.caption("“The future depends on what you build today.”")