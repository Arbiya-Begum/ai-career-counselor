# Career Intelligence System (Clean Premium Version)

import streamlit as st
import matplotlib.pyplot as plt
import time

# 🌐 CONFIG
st.set_page_config(page_title="Career Intelligence System", page_icon="🧠")

# 🎨 FIXED UI (NO FADED TEXT)
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: white;
}
h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}
.stButton>button {
    background: linear-gradient(90deg, #2563eb, #1e40af);
    color: white;
    border-radius: 10px;
    height: 3em;
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

# 🧠 SMART RESULT
def smart_text(scores, user_input):
    dominant = max(scores, key=scores.get)

    intro = f"""
### 🎯 Your Dominant Strength: **{dominant}**

From your inputs, especially:  
“{user_input[:100]}...”
you show a strong inclination towards {dominant.lower()} thinking.
"""

    if dominant == "Tech":
        body = """
### 💻 Recommended Careers:
- Data Scientist  
- Software Developer  
- AI Engineer  
- Cybersecurity Analyst  
- Cloud Engineer  
- Machine Learning Engineer  

### 🚀 Roadmap:
Python → Projects → Data/ML → Real-world practice
"""

    elif dominant == "Creative":
        body = """
### 🎨 Recommended Careers:
- UI/UX Designer  
- Graphic Designer  
- Animator  
- Video Editor  
- Content Creator  

### 🚀 Roadmap:
Tools → Portfolio → Freelance → Personal brand
"""

    else:
        body = """
### 📊 Recommended Careers:
- Business Analyst  
- Entrepreneur  
- Marketing Manager  
- HR Manager  
- Product Manager  

### 🚀 Roadmap:
Business basics → Case studies → Internships → Networking
"""

    return intro + body

# ================= OUTPUT =================
if analyze_quiz:
    scores = calculate_scores()

    st.markdown("## 📊 Your Profile")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.005)
        progress.progress(i + 1)

    fig, ax = plt.subplots()
    ax.bar(scores.keys(), scores.values())
    ax.set_title("Skill Distribution")
    st.pyplot(fig)

if analyze_user:
    if not user_input:
        st.warning("Please enter details")
    else:
        scores = calculate_scores()
        result = smart_text(scores, user_input)
        st.markdown(result)

# ================= EXPLORE =================
st.markdown("---")
st.markdown("## 🌍 Explore Careers")

category = st.selectbox("Choose domain", ["Technology", "Creative", "Business", "Science", "Healthcare"])

if st.button("🔎 Show Careers"):
    st.markdown("""
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
    "Data Scientist": "Analyzes data using Python, ML, and statistics.",
    "Software Developer": "Builds software systems and apps.",
    "AI Engineer": "Creates intelligent systems using AI models.",
    "UI/UX Designer": "Designs user-friendly interfaces.",
    "Graphic Designer": "Creates visual content and branding.",
    "Business Analyst": "Solves business problems using data.",
    "Entrepreneur": "Builds and manages startups.",
    "Doctor": "Diagnoses and treats patients.",
    "Research Scientist": "Conducts experiments and innovations."
}

if st.button("📖 Show Details"):
    st.markdown(f"### {selected}")
    st.markdown(career_info[selected])

# FOOTER
st.markdown("---")
st.caption("“The best way to predict your future is to build it.”")