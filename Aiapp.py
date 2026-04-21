import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Career Intelligence System", layout="centered")

# -------------------- STYLING --------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
h1, h2, h3 {
    color: #ffffff;
}
.stButton>button {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Career Intelligence System")
st.caption("“Clarity comes from action, not overthinking.”")

# -------------------- CAREER DATA --------------------
career_domains = {
    "Technology": [
        "Data Scientist", "Software Developer", "AI Engineer",
        "Cybersecurity Analyst", "Cloud Engineer"
    ],
    "Design": [
        "UI/UX Designer", "Animator", "Graphic Designer"
    ],
    "Business": [
        "Business Analyst", "Entrepreneur", "Marketing Manager", "HR Manager"
    ],
    "Healthcare": [
        "Doctor", "Nurse", "Research Scientist"
    ]
}

career_explanations = {
    "Data Scientist": """A Data Scientist works with data to uncover patterns and insights.

They collect, clean, and analyze structured and unstructured data.

This role involves machine learning, statistics, and programming.

They build predictive models to forecast future trends.

Tools like Python, SQL, and visualization libraries are essential.

They work across industries like finance, healthcare, and tech.

Strong analytical thinking is required.

Communication skills help explain findings to stakeholders.

It is one of the fastest-growing careers globally.

Continuous learning is necessary due to evolving technologies.

Ideal for those who enjoy problem-solving and logic.
""",

    "Doctor": """A Doctor diagnoses and treats illnesses to improve health.

They work in hospitals, clinics, and healthcare institutions.

This profession requires years of education and training.

Doctors must make critical decisions under pressure.

They specialize in various medical fields.

Compassion and communication are essential.

They play a key role in saving lives.

Medical knowledge constantly evolves.

Highly respected but demanding profession.

Long working hours are common.

Ideal for those passionate about helping others.
"""
}

# -------------------- PDF FUNCTION --------------------
def generate_pdf(text):
    file_path = "career_report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []
    for line in text.split("\n"):
        content.append(Paragraph(line, styles["Normal"]))

    doc.build(content)
    return file_path

# -------------------- SECTION 1: PERSONAL QUIZ --------------------
st.header("🧩 Personal Intelligence Quiz")

interest = st.radio("What excites you?", ["Solving problems", "Designing", "Leading"])
strength = st.radio("Your strength?", ["Logic", "Creativity", "Communication"])
work_style = st.radio("Work style?", ["Independent", "Teamwork", "Leadership"])

if st.button("🔘 Analyze"):
    st.success("Analysis Complete!")

    if interest == "Solving problems":
        st.write("👉 You are inclined towards Technology roles.")
    elif interest == "Designing":
        st.write("👉 You are inclined towards Creative/Design roles.")
    else:
        st.write("👉 You are inclined towards Business/Leadership roles.")

# -------------------- SECTION 2: ABOUT YOURSELF --------------------
st.header("📝 Tell Us About Yourself")

about = st.text_area("Write about your interests, goals, or personality...")

if st.button("🧠 Analyze Yourself"):
    if about:
        st.success("Insight Generated!")
        st.write(f"""
Based on your input:

👉 You show strong self-awareness and clarity of thought.  
👉 Your personality indicates potential for growth in dynamic careers.  
👉 You seem adaptable and capable of learning new skills.  
👉 Focus on consistency and practical execution to reach goals.  

“Success is built on small consistent actions.”
""")
    else:
        st.warning("Please write something first.")

# -------------------- SECTION 3: EXPLORE CAREERS --------------------
st.header("🌍 Explore Careers")

selected_domain = st.selectbox("Choose domain", list(career_domains.keys()))

if st.button("🔍 Show Careers"):
    careers = career_domains[selected_domain]

    st.subheader(f"Careers in {selected_domain}")
    for career in careers:
        st.write(f"• {career}")

# -------------------- SECTION 4: EXPLAIN CAREER --------------------
st.header("📘 Explain Career")

selected_career = st.selectbox(
    "Choose a career",
    [c for careers in career_domains.values() for c in careers]
)

if st.button("📖 Explain"):
    if selected_career in career_explanations:
        st.write(career_explanations[selected_career])
    else:
        st.write(f"""
{selected_career} is a professional career path with strong growth potential.

It requires dedication, skill development, and practical experience.

You will need to build core knowledge in this domain.

Hands-on projects will improve your understanding.

Consistency and learning attitude are key.

This career offers opportunities across industries.

You should focus on building relevant skills.

Networking and internships can boost your growth.

Staying updated with trends is important.

With effort, you can build a successful future in this field.
""")

# -------------------- SECTION 5: ROADMAP + PDF --------------------
st.header("🗺️ Career Roadmap")

if st.button("📥 Generate Report"):
    report_text = f"""
Career: {selected_career}

Skills Required:
- Core domain knowledge
- Problem-solving
- Communication
- Practical experience

Roadmap:
1. Learn fundamentals
2. Build small projects
3. Practice real-world problems
4. Gain internship experience
5. Build portfolio
6. Apply for jobs

“Discipline beats motivation.”
"""

    pdf_file = generate_pdf(report_text)

    with open(pdf_file, "rb") as f:
        st.download_button(
            label="Download PDF",
            data=f,
            file_name="career_report.pdf",
            mime="application/pdf"
        )