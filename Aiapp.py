 # AI Career Counselor Pro - ADVANCED (No API, Smart Logic)

import streamlit as st
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# 🌐 PAGE CONFIG
st.set_page_config(page_title="AI Career Counselor Pro", page_icon="🧠", layout="centered")

# 🎨 UI STYLE
st.markdown("""
<style>
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
}
</style>
""", unsafe_allow_html=True)

# 🧠 TITLE
st.title("🧠 AI Career Counselor Pro")
st.caption("🚀 Smart Career Intelligence System")
st.markdown("---")

# ================= QUIZ =================
st.markdown("## 🧠 Personal Intelligence Quiz")

col1, col2, col3 = st.columns(3)

with col1:
    q1 = st.radio("What excites you?", ["Solving problems", "Designing", "Leading"])
    q2 = st.radio("Pick a strength", ["Logic", "Creativity", "Communication"])

with col2:
    q3 = st.radio("Work style?", ["Alone", "Team", "Leadership"])
    q4 = st.radio("Favorite subject?", ["Math", "Arts", "Business"])

with col3:
    q5 = st.radio("Decision making?", ["Analytical", "Creative", "Strategic"])
    q6 = st.radio("You prefer?", ["Coding", "Designing", "Managing"])

# 🚀 ANALYZE BUTTON
analyze_btn = st.button("🔘 Analyze My Intelligence")

# ================= USER INPUT =================
st.markdown("---")
st.markdown("## 💬 Tell Us About Yourself")
user_input = st.text_area("Your interests, goals, personality...")

# ================= LOGIC =================
def calculate_scores():
    scores = {"Tech": 0, "Creative": 0, "Business": 0}

    mapping = {
        "Solving problems": "Tech",
        "Designing": "Creative",
        "Leading": "Business",
        "Logic": "Tech",
        "Creativity": "Creative",
        "Communication": "Business",
        "Alone": "Tech",
        "Team": "Creative",
        "Leadership": "Business",
        "Math": "Tech",
        "Arts": "Creative",
        "Business": "Business",
        "Analytical": "Tech",
        "Creative": "Creative",
        "Strategic": "Business",
        "Coding": "Tech",
        "Designing": "Creative",
        "Managing": "Business"
    }

    answers = [q1, q2, q3, q4, q5, q6]

    for ans in answers:
        scores[mapping[ans]] += 1

    return scores

# 🧠 SMART RECOMMENDATION
def generate_result(scores, user_input):
    dominant = max(scores, key=scores.get)

    if dominant == "Tech":
        return """
## 💻 Recommended Path: TECH INTELLIGENCE

You show strong analytical thinking and problem-solving ability.

### 🎯 Careers:
- Data Scientist  
- Software Engineer  
- AI Engineer  

### 🚀 Strategy:
Start with Python → Build Projects → Learn ML → Real-world practice

"""

    elif dominant == "Creative":
        return """
## 🎨 Recommended Path: CREATIVE INTELLIGENCE

You have strong imagination and design thinking.

### 🎯 Careers:
- UI/UX Designer  
- Animator  
- Creative Director  

### 🚀 Strategy:
Learn design tools → Build portfolio → Freelance → Brand yourself

"""

    else:
        return """
## 📊 Recommended Path: BUSINESS INTELLIGENCE

You show leadership and strategic thinking.

### 🎯 Careers:
- Business Analyst  
- Entrepreneur  
- Marketing Manager  

### 🚀 Strategy:
Learn business basics → Case studies → Networking → Internships

"""

# ================= ANALYZE OUTPUT =================
if analyze_btn:
    scores = calculate_scores()

    st.markdown("## 📊 Your Intelligence Profile")

    fig, ax = plt.subplots()
    ax.bar(scores.keys(), scores.values())
    st.pyplot(fig)

    result = generate_result(scores, user_input)
    st.markdown(result)

# ================= EXPLORE =================
st.markdown("---")
st.markdown("## 🌍 Explore Career Domains")

category = st.selectbox("Select Domain", ["Technology", "Creative", "Business"])

if st.button("🔎 Explore"):
    if category == "Technology":
        st.markdown("Data Scientist, AI Engineer, Web Developer, Cybersecurity Analyst")
    elif category == "Creative":
        st.markdown("UI/UX Designer, Animator, Graphic Designer, Video Editor")
    else:
        st.markdown("Business Analyst, Entrepreneur, Marketing Manager")

# ================= EXPLAIN =================
st.markdown("---")
st.markdown("## 🔍 Career Explainer")

career = st.text_input("Enter career (e.g. Data Scientist)")

career_data = {
    "data scientist": "Works with data to find insights. Skills: Python, ML, Stats.",
    "software engineer": "Builds applications. Skills: Programming, Problem solving.",
    "ui ux designer": "Designs user experience. Skills: Figma, Creativity.",
    "business analyst": "Analyzes business problems. Skills: Communication, Strategy."
}

if st.button("📖 Explain"):
    key = career.lower().strip()
    if key in career_data:
        st.markdown(career_data[key])
    else:
        st.markdown("⚠️ Career not found. Try common roles like Data Scientist, Designer, etc.")

# FOOTER
st.markdown("---")
st.caption("🏆 AI Career Counselor Pro | Advanced Logic Version")