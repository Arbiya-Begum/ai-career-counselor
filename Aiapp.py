# final version - NO AI (Stable Hackathon Version)

import streamlit as st
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# 🌐 PAGE
st.set_page_config(page_title="AI Career Counselor Pro", page_icon="🧠")

st.title("🧠 AI Career Counselor Pro")
st.caption("🚀 Smart Career Guidance (No API Mode)")
st.markdown("---")

# 🧠 QUIZ
col1, col2 = st.columns(2)

with col1:
    q1 = st.radio("What do you enjoy most?", 
                  ["Solving problems", "Creating designs", "Leading people"])
    q2 = st.radio("Your strongest skill?", 
                  ["Logic", "Creativity", "Communication"])

with col2:
    q3 = st.radio("Preferred work style?", 
                  ["Independent", "Teamwork", "Leadership"])

# 💬 INPUT
user_input = st.text_area("Tell us about yourself")

# 📊 SCORING
def calculate_scores(q1, q2, q3):
    scores = {"Tech": 0, "Creative": 0, "Business": 0}

    if q1 == "Solving problems":
        scores["Tech"] += 2
    elif q1 == "Creating designs":
        scores["Creative"] += 2
    else:
        scores["Business"] += 2

    if q2 == "Logic":
        scores["Tech"] += 2
    elif q2 == "Creativity":
        scores["Creative"] += 2
    else:
        scores["Business"] += 2

    if q3 == "Independent":
        scores["Tech"] += 1
    elif q3 == "Teamwork":
        scores["Creative"] += 1
    else:
        scores["Business"] += 1

    return scores

# 🧠 CAREER LOGIC
def get_career_recommendation(scores, user_input):
    if scores["Tech"] >= scores["Creative"] and scores["Tech"] >= scores["Business"]:
        return """
## 💻 Top Careers
- Data Scientist  
- Software Developer  
- AI Engineer  

### 📌 Why?
You are strong in logic and problem-solving.

### 🛠 Skills Needed
- Python → programming language  
- Data Analysis → working with data  
- Machine Learning → teaching machines  

### 🚀 Roadmap
1. Learn Python  
2. Learn SQL  
3. Build projects  
4. Learn Machine Learning  

### ⭐ More Options
- Cybersecurity Analyst  
- Cloud Engineer  
"""

    elif scores["Creative"] >= scores["Business"]:
        return """
## 🎨 Top Careers
- UI/UX Designer  
- Graphic Designer  
- Animator  

### 📌 Why?
You are creative and design-focused.

### 🛠 Skills Needed
- Design Thinking  
- Tools like Figma  
- Creativity  

### 🚀 Roadmap
1. Learn design basics  
2. Practice tools  
3. Build portfolio  

### ⭐ More Options
- Video Editor  
- Content Creator  
"""

    else:
        return """
## 📊 Top Careers
- Business Analyst  
- Marketing Manager  
- Entrepreneur  

### 📌 Why?
You have leadership and communication skills.

### 🛠 Skills Needed
- Communication  
- Strategy  
- Management  

### 🚀 Roadmap
1. Learn business basics  
2. Study case studies  
3. Gain internships  

### ⭐ More Options
- HR Manager  
- Sales Executive  
"""

# 🚀 ANALYZE
if st.button("🚀 Analyze My Career"):

    if not user_input:
        st.warning("Please write something about yourself")
    else:
        scores = calculate_scores(q1, q2, q3)

        # 📊 GRAPH
        fig, ax = plt.subplots()
        ax.bar(scores.keys(), scores.values())
        ax.set_title("Your Strength Analysis")
        st.pyplot(fig)

        result = get_career_recommendation(scores, user_input)

        st.markdown(result)

        # 📥 PDF
        def create_pdf(text):
            doc = SimpleDocTemplate("career_report.pdf")
            styles = getSampleStyleSheet()
            story = [Paragraph(text, styles["Normal"])]
            doc.build(story)

        create_pdf(result)

        with open("career_report.pdf", "rb") as file:
            st.download_button("📥 Download Report", file, "career_report.pdf")

# 🌍 EXPLORE
st.markdown("---")
category = st.selectbox(
    "Explore Careers",
    ["Technology", "Creative", "Business", "Science", "Healthcare"]
)

if st.button("🔎 Show Careers"):
    if category == "Technology":
        st.markdown("""
- Data Scientist  
- Web Developer  
- AI Engineer  
- Cybersecurity Analyst  
- Cloud Engineer  
""")

    elif category == "Creative":
        st.markdown("""
- Graphic Designer  
- Animator  
- UI/UX Designer  
- Video Editor  
- Content Creator  
""")

    elif category == "Business":
        st.markdown("""
- Business Analyst  
- Marketing Manager  
- Entrepreneur  
- HR Manager  
- Sales Executive  
""")

    elif category == "Science":
        st.markdown("""
- Research Scientist  
- Lab Technician  
- Physicist  
- Chemist  
""")

    else:
        st.markdown("""
- Doctor  
- Nurse  
- Pharmacist  
- Medical Lab Technician  
""")

# 🔍 EXPLAIN
st.markdown("---")
career_name = st.text_input("Enter career name")

if st.button("📖 Explain Career"):
    if career_name.lower() == "data scientist":
        st.markdown("""
### 📘 Data Scientist
Analyzes data to extract insights.

### 🛠 Skills:
- Python  
- Statistics  
- Machine Learning  

### 🚀 Roadmap:
1. Learn Python  
2. Learn Data Analysis  
3. Build projects  
""")
    else:
        st.markdown("⚠️ Detailed info coming soon...")

# FOOTER
st.markdown("---")
st.caption("🏆 AI Career Counselor Pro (Hackathon Version - No API)")