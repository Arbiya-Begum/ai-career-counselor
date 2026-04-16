
# final version - 07

import streamlit as st
import os
from openai import OpenAI
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# 🔑 API KEY (from Streamlit secrets)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=30
)

# ⚡ CACHE FUNCTION (fixes loading issue)
@st.cache_data(show_spinner=False)
def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# 🌐 PAGE CONFIG
st.set_page_config(page_title="AI Career Counselor Pro", page_icon="🧠", layout="centered")

# 🎨 PREMIUM UI
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #ffffff;
}
.block-container {
    padding-top: 2rem;
}
.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #00c6ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# 🧠 HEADER
st.title("🧠 AI Career Counselor Pro")
st.caption("🚀 Discover. Analyze. Grow.")
st.markdown("---")

# 🧠 QUIZ
st.markdown("## 🧠 Personality Quiz")

col1, col2 = st.columns(2)

with col1:
    q1 = st.radio("What do you enjoy most?", 
                  ["Solving problems", "Creating designs", "Leading people"])

    q2 = st.radio("Your strongest skill?", 
                  ["Logic", "Creativity", "Communication"])

with col2:
    q3 = st.radio("Preferred work style?", 
                  ["Independent", "Teamwork", "Leadership"])

st.markdown("---")

# 💬 USER INPUT
st.markdown("## 💬 Tell us more about yourself")
user_input = st.text_area("Write about your interests, goals, personality...")

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

        # GRAPH
        st.markdown("## 📊 Your Strength Profile")
        categories = list(scores.keys())
        values = list(scores.values())

        fig, ax = plt.subplots()
        ax.bar(categories, values)
        ax.set_ylabel("Score")
        ax.set_title("Your Strength Analysis")
        st.pyplot(fig)

        # AI RESPONSE
        prompt = f"""
        You are an expert career counselor.

        User scores:
        {scores}

        User description:
        {user_input}

        Give:

        Top 3 Career Options (Detailed)
        - Why suitable
        - Skills required
        - Where to learn

        Additional 5 career options

        Also give roadmap and motivation.
        """

        result = get_ai_response(prompt)

        st.markdown("## 🎯 Career Recommendations")
        st.markdown(result)

        # PDF
        def create_pdf(text):
            doc = SimpleDocTemplate("career_report.pdf")
            styles = getSampleStyleSheet()
            story = [Paragraph(text, styles["Normal"])]
            doc.build(story)

        create_pdf(result)

        with open("career_report.pdf", "rb") as file:
            st.download_button(
                label="📥 Download Report",
                data=file,
                file_name="career_report.pdf",
                mime="application/pdf"
            )

# 🌍 EXPLORE
st.markdown("---")
st.markdown("## 🌍 Explore Career Paths")

category = st.selectbox(
    "Choose a category",
    ["Technology", "Creative", "Business", "Science", "Healthcare", "Law", "Education"]
)

if st.button("🔎 Show Careers"):
    explore_prompt = f"List 20 careers in {category} with 1-line description"
    careers_list = get_ai_response(explore_prompt)

    st.markdown("### 📌 Career Options")
    st.markdown(careers_list)

# 🔍 EXPLAIN
st.markdown("---")
st.markdown("## 🔍 Know Any Career")

career_name = st.text_input("Enter a career name")

if st.button("📖 Explain Career"):
    explain_prompt = f"""
    Explain the career '{career_name}' with:
    - Definition
    - Skills required
    - Where to learn
    """
    explanation = get_ai_response(explain_prompt)

    st.markdown("### 📘 Career Details")
    st.markdown(explanation)

# 📌 FOOTER
st.markdown("---")
st.caption("🏆 Hackathon Project | AI Career Counselor Pro")