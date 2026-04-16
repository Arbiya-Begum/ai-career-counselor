
# final version - GEMINI 

import streamlit as st
import os
import google.generativeai as genai
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# 🔑 CONFIGURE GEMINI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    model = genai.GenerativeModel("gemini-1.5-flash-001")
    response = model.generate_content(prompt)

except:
    model = genai.GenerativeModel("gemini-pro")
    

result = response.text

# ⚡ AI FUNCTION
@st.cache_data(show_spinner=False)
def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# 🌐 PAGE
st.set_page_config(page_title="AI Career Counselor Pro", page_icon="🧠")

st.title("🧠 AI Career Counselor Pro")
st.caption("🚀 100% Free AI Powered App")
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

# 🚀 ANALYZE
if st.button("🚀 Analyze My Career"):

    if not user_input:
        st.warning("Please write something about yourself")
    else:
        scores = calculate_scores(q1, q2, q3)

        fig, ax = plt.subplots()
        ax.bar(scores.keys(), scores.values())
        st.pyplot(fig)

        prompt = f"""
        Scores: {scores}
        User: {user_input}

        Suggest:
        - 3 careers (short reason)
        - 5 more careers
        - roadmap
        """

        result = get_ai_response(prompt)

        st.markdown("## 🎯 Career Suggestions")
        st.markdown(result)

        # PDF
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
    prompt = f"List 10 careers in {category} with short description"
    st.markdown(get_ai_response(prompt))

# 🔍 EXPLAIN
st.markdown("---")
career_name = st.text_input("Enter career name")

if st.button("📖 Explain Career"):
    prompt = f"Explain {career_name} with skills and roadmap"
    st.markdown(get_ai_response(prompt))

# FOOTER
st.markdown("---")
st.caption("🏆 AI Career Counselor Pro (Free Version)")