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

# --------------------Career Data ---
career_domains = {
    "Technology": [
        "Data Scientist", "Software Developer", "AI Engineer",
        "Cybersecurity Analyst", "Cloud Engineer", "DevOps Engineer",
        "Machine Learning Engineer", "Web Developer"
    ],
    "Design": [
        "UI/UX Designer", "Animator", "Graphic Designer",
        "Product Designer", "Motion Designer"
    ],
    "Business": [
        "Business Analyst", "Entrepreneur", "Marketing Manager",
        "HR Manager", "Financial Analyst", "Product Manager",
        "Operations Manager"
    ],
    "Healthcare": [
        "Doctor", "Nurse", "Research Scientist",
        "Pharmacist", "Medical Technologist", "Physiotherapist"
    ],
    "Education": [
        "Teacher", "Academic Researcher", "Education Consultant",
        "Instructional Designer"
    ],
    "Law & Policy": [
        "Lawyer", "Policy Analyst", "Compliance Officer"
    ]
}

# -------------------- CAREER FULL DATA --------------------
career_data = {
    "Data Scientist": {
        "description": "Data Scientists analyze complex datasets to uncover insights, build predictive models, and help organizations make data-driven decisions.",
        "skills": ["Python", "SQL", "Machine Learning", "Statistics", "Data Visualization", "Pandas", "Scikit-learn"],
        "salary": "$85,000 – $145,000/year",
        "pros": ["High demand globally", "Excellent salaries", "Intellectually stimulating", "Works across all industries"],
        "cons": ["Requires strong math background", "Data cleaning is tedious", "Long hours during project crunch"],
        "roadmap": [
            "Learn Python & SQL fundamentals",
            "Study statistics and probability",
            "Practice with real datasets on Kaggle",
            "Learn ML algorithms (regression, classification, clustering)",
            "Build 3–5 portfolio projects",
            "Get certified (Google Data Analytics / IBM DS)",
            "Apply for internships or junior roles"
        ]
    },
    "Software Developer": {
        "description": "Software Developers design, build, and maintain applications and systems that power modern technology.",
        "skills": ["Programming (Python/Java/C++)", "Data Structures", "Algorithms", "Git", "Problem Solving", "APIs"],
        "salary": "$75,000 – $135,000/year",
        "pros": ["High job availability", "Remote-friendly", "Creative problem-solving", "Clear career progression"],
        "cons": ["Fast-changing technology", "Debugging can be frustrating", "Requires continuous learning"],
        "roadmap": [
            "Choose a language (Python, JavaScript, or Java)",
            "Learn data structures and algorithms",
            "Build small projects (calculator, to-do app)",
            "Understand version control with Git",
            "Contribute to open-source projects",
            "Practice on LeetCode / HackerRank",
            "Apply for internships, build your GitHub"
        ]
    },
    "AI Engineer": {
        "description": "AI Engineers design and implement artificial intelligence systems including neural networks, NLP models, and computer vision solutions.",
        "skills": ["Deep Learning", "TensorFlow / PyTorch", "Python", "Math & Linear Algebra", "Cloud Platforms", "MLOps"],
        "salary": "$100,000 – $175,000/year",
        "pros": ["Cutting-edge field", "Top salaries", "Huge global demand", "Impacts multiple industries"],
        "cons": ["Steep learning curve", "Requires strong math", "Rapidly changing landscape"],
        "roadmap": [
            "Master Python and linear algebra",
            "Study neural networks and deep learning",
            "Learn TensorFlow or PyTorch",
            "Build NLP or computer vision projects",
            "Study MLOps and model deployment",
            "Publish models on HuggingFace or GitHub",
            "Target AI-focused companies or research labs"
        ]
    },
    "Cybersecurity Analyst": {
        "description": "Cybersecurity Analysts protect systems and networks from digital attacks, vulnerabilities, and unauthorized access.",
        "skills": ["Networking", "Ethical Hacking", "SIEM Tools", "Risk Assessment", "Linux", "Cryptography"],
        "salary": "$70,000 – $130,000/year",
        "pros": ["Critical and growing field", "Job security", "Diverse specializations", "Protects real-world impact"],
        "cons": ["High-pressure incidents", "Constantly evolving threats", "Requires vigilance 24/7"],
        "roadmap": [
            "Learn networking fundamentals (TCP/IP, DNS)",
            "Study Linux and command line",
            "Get CompTIA Security+ certification",
            "Practice ethical hacking on TryHackMe / Hack The Box",
            "Learn SIEM tools like Splunk",
            "Specialize (penetration testing, forensics, etc.)",
            "Apply for SOC Analyst or junior roles"
        ]
    },
    "Cloud Engineer": {
        "description": "Cloud Engineers design and manage cloud infrastructure on platforms like AWS, Azure, and Google Cloud to ensure scalability and reliability.",
        "skills": ["AWS / Azure / GCP", "Linux", "Networking", "Terraform", "Docker", "Kubernetes"],
        "salary": "$90,000 – $155,000/year",
        "pros": ["Massive industry demand", "Remote work friendly", "Great salaries", "Vendor certifications valued"],
        "cons": ["Complex architecture decisions", "Costs can spiral", "Vendor lock-in risks"],
        "roadmap": [
            "Learn Linux and basic networking",
            "Pick a cloud provider (AWS recommended for beginners)",
            "Get AWS Cloud Practitioner certification",
            "Study infrastructure as code (Terraform)",
            "Learn containerization (Docker, Kubernetes)",
            "Build a cloud-hosted portfolio project",
            "Pursue Solutions Architect certification"
        ]
    },
    "DevOps Engineer": {
        "description": "DevOps Engineers bridge software development and IT operations, automating pipelines and ensuring smooth software delivery.",
        "skills": ["CI/CD Pipelines", "Docker", "Kubernetes", "Shell Scripting", "Git", "Monitoring Tools"],
        "salary": "$85,000 – $145,000/year",
        "pros": ["In high demand", "Automation-focused", "Cross-functional role", "Strong salaries"],
        "cons": ["On-call responsibilities", "Complex tooling ecosystem", "Requires broad technical knowledge"],
        "roadmap": [
            "Learn Linux and shell scripting",
            "Understand Git and version control workflows",
            "Set up CI/CD with Jenkins or GitHub Actions",
            "Learn Docker and containerization",
            "Study Kubernetes for orchestration",
            "Implement monitoring with Prometheus/Grafana",
            "Build an end-to-end DevOps pipeline project"
        ]
    },
    "Machine Learning Engineer": {
        "description": "ML Engineers build scalable machine learning systems, translating research models into production-ready applications.",
        "skills": ["Python", "ML Algorithms", "Feature Engineering", "Model Deployment", "Cloud ML Services", "APIs"],
        "salary": "$95,000 – $165,000/year",
        "pros": ["Highly paid", "Innovative work", "Combines software + AI", "Strong global demand"],
        "cons": ["Requires deep expertise", "Model performance tuning is complex", "Research-to-production gaps"],
        "roadmap": [
            "Master Python and key libraries (NumPy, Pandas)",
            "Study supervised and unsupervised ML algorithms",
            "Learn model evaluation and feature engineering",
            "Practice on Kaggle competitions",
            "Study model serving (Flask, FastAPI, TensorFlow Serving)",
            "Deploy a model to a cloud platform",
            "Build an end-to-end ML project for your portfolio"
        ]
    },
    "Web Developer": {
        "description": "Web Developers build and maintain websites and web applications, working on front-end, back-end, or both (full stack).",
        "skills": ["HTML/CSS", "JavaScript", "React or Vue", "Node.js", "Databases", "REST APIs"],
        "salary": "$60,000 – $120,000/year",
        "pros": ["Huge job market", "Freelance opportunities", "Visible creative output", "Fast to get started"],
        "cons": ["Browser compatibility challenges", "Rapidly changing frameworks", "Competition is high"],
        "roadmap": [
            "Learn HTML, CSS, and JavaScript fundamentals",
            "Build a personal portfolio website",
            "Learn a front-end framework (React is best for jobs)",
            "Study back-end with Node.js or Python (Django/Flask)",
            "Learn databases (SQL and MongoDB)",
            "Build 3 full-stack projects",
            "Apply for junior web developer roles"
        ]
    },
    "UI/UX Designer": {
        "description": "UI/UX Designers create user-friendly digital experiences by combining visual design with user research and interaction design.",
        "skills": ["Figma", "Wireframing", "User Research", "Prototyping", "Design Systems", "Adobe XD"],
        "salary": "$65,000 – $120,000/year",
        "pros": ["Creative and impactful work", "Growing demand", "Collaborative role", "Portfolio-driven career"],
        "cons": ["Subjective feedback", "Balancing aesthetics with usability", "Constant iteration required"],
        "roadmap": [
            "Learn design principles (color, typography, layout)",
            "Master Figma for wireframing and prototyping",
            "Study user research and usability testing",
            "Redesign existing apps for your portfolio",
            "Learn about design systems",
            "Build 4–5 case study projects",
            "Apply for junior UX roles or freelance"
        ]
    },
    "Animator": {
        "description": "Animators create motion-based visual content for films, games, advertising, and digital media using 2D or 3D tools.",
        "skills": ["Adobe Animate", "Blender", "After Effects", "Storytelling", "Rigging", "Keyframing"],
        "salary": "$50,000 – $100,000/year",
        "pros": ["Highly creative work", "Film & gaming industries", "Growing demand for 3D content", "Freelance potential"],
        "cons": ["Competitive field", "Project-based income can vary", "Long rendering times"],
        "roadmap": [
            "Learn animation principles (12 principles of animation)",
            "Start with 2D animation using Adobe Animate",
            "Move to 3D with Blender",
            "Create short animation projects",
            "Study character rigging and motion",
            "Build a showreel portfolio",
            "Apply to studios or freelance platforms"
        ]
    },
    "Graphic Designer": {
        "description": "Graphic Designers create visual content for brands, marketing, media, and digital platforms using design software.",
        "skills": ["Adobe Photoshop", "Illustrator", "InDesign", "Typography", "Color Theory", "Branding"],
        "salary": "$45,000 – $90,000/year",
        "pros": ["Creative freedom", "Wide range of industries", "Freelance-friendly", "Visible output"],
        "cons": ["Client revisions can be exhausting", "Competitive market", "Pricing your work is hard"],
        "roadmap": [
            "Learn design fundamentals (color, type, layout)",
            "Master Adobe Illustrator and Photoshop",
            "Create logo and branding projects",
            "Develop a diverse design portfolio",
            "Learn InDesign for print design",
            "Build a Behance or Dribbble portfolio",
            "Freelance or apply to creative agencies"
        ]
    },
    "Product Designer": {
        "description": "Product Designers own the end-to-end design of digital products, from research and strategy to UI and usability.",
        "skills": ["Figma", "Design Thinking", "UX Research", "Prototyping", "Product Strategy", "Stakeholder Communication"],
        "salary": "$80,000 – $140,000/year",
        "pros": ["Strategic and creative", "High impact role", "Works with cross-functional teams", "Great salaries"],
        "cons": ["Requires both design and business thinking", "High expectations", "Involves lots of meetings"],
        "roadmap": [
            "Learn UX/UI fundamentals",
            "Study design thinking and product strategy",
            "Master Figma and advanced prototyping",
            "Conduct user research and usability studies",
            "Build end-to-end product case studies",
            "Learn about product metrics and A/B testing",
            "Apply to product design or UX roles at tech companies"
        ]
    },
    "Motion Designer": {
        "description": "Motion Designers create animated graphics and visual effects for digital media, advertisements, and brand storytelling.",
        "skills": ["After Effects", "Cinema 4D", "Premiere Pro", "Typography in Motion", "Storyboarding", "Sound Design"],
        "salary": "$55,000 – $105,000/year",
        "pros": ["Highly creative", "Growing demand in digital media", "Freelance market is strong", "Fun and dynamic work"],
        "cons": ["Render times are long", "Software is expensive", "Tight deadlines in agencies"],
        "roadmap": [
            "Learn animation principles",
            "Master Adobe After Effects",
            "Study motion typography and logo animation",
            "Learn Cinema 4D for 3D motion",
            "Build a motion reel with diverse projects",
            "Study brand motion guidelines",
            "Freelance or apply to agencies and studios"
        ]
    },
    "Business Analyst": {
        "description": "Business Analysts bridge the gap between business needs and technology solutions by analyzing processes and data.",
        "skills": ["Data Analysis", "SQL", "Excel", "Requirements Gathering", "Process Mapping", "Communication"],
        "salary": "$65,000 – $115,000/year",
        "pros": ["Versatile across industries", "Good salaries", "Improves real business outcomes", "Less technical than engineering"],
        "cons": ["Heavy documentation work", "Managing stakeholder expectations", "Can be slow-paced in large orgs"],
        "roadmap": [
            "Learn business process fundamentals",
            "Master Excel and SQL for data analysis",
            "Study requirements gathering and documentation",
            "Learn tools like JIRA, Confluence, or Visio",
            "Get CBAP or PMI-PBA certification",
            "Work on case studies simulating real business problems",
            "Apply for BA or junior analyst roles"
        ]
    },
    "Entrepreneur": {
        "description": "Entrepreneurs identify market opportunities and build businesses from the ground up, taking calculated risks for growth.",
        "skills": ["Business Planning", "Finance", "Marketing", "Leadership", "Problem Solving", "Networking"],
        "salary": "Highly variable ($0 – $1M+)",
        "pros": ["Unlimited earning potential", "Creative freedom", "Build your own vision", "Personal fulfillment"],
        "cons": ["High risk and uncertainty", "Long working hours", "Financial pressure especially early on", "No guaranteed income"],
        "roadmap": [
            "Read widely on business, finance, and your industry",
            "Identify a problem worth solving",
            "Validate your idea with potential customers",
            "Build a simple MVP (Minimum Viable Product)",
            "Learn basic finance and marketing",
            "Seek mentorship and a support network",
            "Launch, iterate, and learn from feedback"
        ]
    },
    "Marketing Manager": {
        "description": "Marketing Managers plan and execute campaigns to promote products or services and grow brand awareness.",
        "skills": ["Digital Marketing", "SEO/SEM", "Social Media", "Analytics", "Copywriting", "Campaign Management"],
        "salary": "$60,000 – $110,000/year",
        "pros": ["Creative and analytical blend", "Wide industry applicability", "Visible results", "Strong growth path"],
        "cons": ["Pressure to show ROI", "Fast-paced environment", "Algorithm changes affect strategy constantly"],
        "roadmap": [
            "Learn digital marketing fundamentals",
            "Master Google Analytics and Meta Ads",
            "Study SEO, content marketing, and email marketing",
            "Get Google or Meta certified",
            "Build a personal brand or run mock campaigns",
            "Create a marketing portfolio with results",
            "Apply for coordinator or specialist roles first"
        ]
    },
    "HR Manager": {
        "description": "HR Managers oversee hiring, employee relations, performance management, and organizational culture.",
        "skills": ["Recruitment", "Labor Law", "Conflict Resolution", "HRIS Software", "Communication", "Empathy"],
        "salary": "$55,000 – $100,000/year",
        "pros": ["People-focused role", "Stable employment", "Broad organizational influence", "Growing field"],
        "cons": ["Difficult conversations are frequent", "Emotionally demanding", "Policy limitations can be frustrating"],
        "roadmap": [
            "Study human resource management fundamentals",
            "Learn labor laws and employment regulations",
            "Get SHRM-CP or PHR certification",
            "Gain experience in recruitment or payroll",
            "Master HRIS tools (Workday, BambooHR)",
            "Develop strong communication and mediation skills",
            "Apply for HR coordinator or generalist roles"
        ]
    },
    "Financial Analyst": {
        "description": "Financial Analysts evaluate financial data, build models, and advise businesses or individuals on investment decisions.",
        "skills": ["Excel", "Financial Modeling", "Accounting", "Valuation", "Bloomberg Terminal", "PowerPoint"],
        "salary": "$65,000 – $120,000/year",
        "pros": ["High earning potential", "Valued in every industry", "Clear career path to senior roles", "Analytical and strategic"],
        "cons": ["Long hours especially in banking", "High-pressure reporting periods", "Requires strong attention to detail"],
        "roadmap": [
            "Learn accounting and financial statements",
            "Master Excel for financial modeling",
            "Study valuation methods (DCF, comparables)",
            "Get CFA Level 1 or relevant certification",
            "Build financial models for real companies",
            "Internships in banking, consulting, or corporate finance",
            "Apply for analyst roles at firms or in-house finance teams"
        ]
    },
    "Product Manager": {
        "description": "Product Managers own the strategy and roadmap of products, working with engineering, design, and business teams to deliver value.",
        "skills": ["Product Strategy", "Agile / Scrum", "Data Analysis", "Roadmapping", "Stakeholder Management", "Communication"],
        "salary": "$90,000 – $160,000/year",
        "pros": ["High impact and visibility", "No single technical track required", "Great salaries", "Leadership opportunities"],
        "cons": ["Lots of meetings and alignment work", "Accountability without direct authority", "Requires influence skills"],
        "roadmap": [
            "Learn product thinking and strategy fundamentals",
            "Study Agile and Scrum methodology",
            "Learn data analysis basics (SQL, analytics tools)",
            "Read PM frameworks (RICE, OKRs, Jobs-to-be-done)",
            "Build a product case study",
            "Get experience in adjacent roles (BA, UX, engineering)",
            "Apply for Associate PM programs at tech companies"
        ]
    },
    "Operations Manager": {
        "description": "Operations Managers ensure an organization's processes run efficiently, overseeing logistics, teams, and resource planning.",
        "skills": ["Process Improvement", "Supply Chain Basics", "Leadership", "Data Analysis", "Project Management", "Communication"],
        "salary": "$60,000 – $110,000/year",
        "pros": ["Broad industry applicability", "Leadership role", "Tangible impact on efficiency", "Stable demand"],
        "cons": ["Can be stressful managing multiple priorities", "Requires strong multi-tasking", "Often involves difficult team decisions"],
        "roadmap": [
            "Study operations and supply chain fundamentals",
            "Learn project management principles",
            "Get PMP or Six Sigma certification",
            "Use tools like Excel, ERP systems, or Tableau",
            "Develop leadership and team management skills",
            "Work in coordination or analyst roles first",
            "Build expertise in a specific industry vertical"
        ]
    },
    "Doctor": {
        "description": "Doctors diagnose and treat illnesses, injuries, and medical conditions to restore and maintain patient health.",
        "skills": ["Medical Knowledge", "Diagnosis", "Clinical Decision-Making", "Patient Communication", "Empathy", "Specialization"],
        "salary": "$150,000 – $350,000+/year",
        "pros": ["Highly respected profession", "Excellent salaries", "Life-changing impact", "Job security globally"],
        "cons": ["Very long and expensive education", "Extremely high-pressure decisions", "Long working hours", "Emotional toll"],
        "roadmap": [
            "Excel in science subjects (Biology, Chemistry, Physics)",
            "Complete a medical degree (MBBS / MD)",
            "Clear licensing exams (USMLE, PLAB, etc.)",
            "Complete internship / residency program",
            "Choose a specialization (cardiology, surgery, etc.)",
            "Obtain board certification in your specialty",
            "Begin practice or fellowship"
        ]
    },
    "Nurse": {
        "description": "Nurses provide patient care, administer treatments, and support doctors in delivering quality healthcare.",
        "skills": ["Patient Care", "Clinical Skills", "Medical Knowledge", "Communication", "Critical Thinking", "Empathy"],
        "salary": "$55,000 – $95,000/year",
        "pros": ["Essential and respected profession", "Diverse specializations", "Strong job security", "Emotionally rewarding"],
        "cons": ["Physically demanding shifts", "Emotionally taxing cases", "Staffing shortages in many regions"],
        "roadmap": [
            "Complete a Bachelor of Science in Nursing (BSN)",
            "Pass the NCLEX-RN licensing exam",
            "Gain clinical experience in a hospital",
            "Choose a specialization (ICU, pediatrics, oncology, etc.)",
            "Pursue advanced certifications (CCRN, CEN)",
            "Consider becoming a Nurse Practitioner (NP) for advancement",
            "Join professional nursing associations"
        ]
    },
    "Research Scientist": {
        "description": "Research Scientists conduct experiments and studies to expand knowledge in fields like medicine, biology, chemistry, and materials science.",
        "skills": ["Research Methodology", "Data Analysis", "Scientific Writing", "Lab Techniques", "Critical Thinking", "Statistics"],
        "salary": "$70,000 – $130,000/year",
        "pros": ["Intellectually rewarding", "Advances human knowledge", "Academic freedom", "Diverse funding opportunities"],
        "cons": ["Long time to results", "Competitive funding environment", "Publish or perish pressure", "Often requires a PhD"],
        "roadmap": [
            "Earn a Bachelor's degree in a science field",
            "Work in a research lab as an assistant",
            "Complete a Master's or PhD in your specialty",
            "Publish research papers in peer-reviewed journals",
            "Apply for postdoctoral positions",
            "Secure research grants and funding",
            "Build collaborations and a research network"
        ]
    },
    "Pharmacist": {
        "description": "Pharmacists dispense medications, counsel patients, and work with healthcare teams to ensure safe and effective drug therapy.",
        "skills": ["Pharmacology", "Patient Counseling", "Drug Interaction Knowledge", "Attention to Detail", "Chemistry", "Communication"],
        "salary": "$90,000 – $130,000/year",
        "pros": ["High earning potential", "Important patient safety role", "Stable profession", "Multiple work settings"],
        "cons": ["Long education path", "Repetitive tasks in retail settings", "High liability"],
        "roadmap": [
            "Complete pre-pharmacy coursework (biology, chemistry)",
            "Earn a Doctor of Pharmacy (Pharm.D.) degree",
            "Pass NAPLEX and MPJE licensing exams",
            "Complete pharmacy residency if pursuing clinical roles",
            "Choose a setting (hospital, retail, clinical, research)",
            "Pursue board certification in specialty areas",
            "Stay updated with pharmacology advancements"
        ]
    },
    "Medical Technologist": {
        "description": "Medical Technologists perform diagnostic lab tests on blood, tissue, and other specimens to support clinical diagnoses.",
        "skills": ["Lab Techniques", "Analytical Skills", "Equipment Operation", "Attention to Detail", "Microbiology", "Hematology"],
        "salary": "$55,000 – $90,000/year",
        "pros": ["Critical role in diagnosis", "Stable demand", "Variety of specializations", "Work-life balance in many settings"],
        "cons": ["Behind-the-scenes role", "Exposure to biohazards", "Shift work common"],
        "roadmap": [
            "Earn a degree in Medical Laboratory Science",
            "Complete clinical rotations",
            "Pass ASCP certification exam",
            "Specialize (hematology, microbiology, chemistry)",
            "Gain experience in hospital or reference labs",
            "Pursue supervisory or specialist certifications",
            "Stay updated with lab technology advancements"
        ]
    },
    "Physiotherapist": {
        "description": "Physiotherapists help patients recover from injuries and manage physical conditions through movement, exercise, and therapy.",
        "skills": ["Anatomy & Physiology", "Manual Therapy", "Exercise Prescription", "Patient Assessment", "Empathy", "Communication"],
        "salary": "$60,000 – $100,000/year",
        "pros": ["Highly rewarding patient care", "Growing demand", "Diverse settings (sports, hospitals, clinics)", "Work-life balance possible"],
        "cons": ["Physically demanding", "Requires patience with slow progress", "Documentation-heavy"],
        "roadmap": [
            "Complete a Bachelor's in Physiotherapy or Kinesiology",
            "Earn a Master's or DPT (Doctor of Physical Therapy)",
            "Pass national licensing exam",
            "Complete supervised clinical hours",
            "Choose a specialty (sports, neuro, pediatric, ortho)",
            "Join professional PT associations",
            "Pursue advanced certifications in your specialty"
        ]
    },
    "Teacher": {
        "description": "Teachers educate and inspire students across various subjects and age groups in schools and academic institutions.",
        "skills": ["Subject Knowledge", "Communication", "Classroom Management", "Lesson Planning", "Patience", "Creativity"],
        "salary": "$40,000 – $80,000/year",
        "pros": ["Deeply meaningful work", "Stable employment", "Summers off (in many systems)", "Shaping future generations"],
        "cons": ["Often underpaid for the effort", "Large class sizes", "Administrative burden", "Emotionally demanding"],
        "roadmap": [
            "Earn a Bachelor's degree in Education or your subject",
            "Complete a teaching practicum or student teaching",
            "Obtain your state/national teaching license",
            "Start as a substitute or assistant teacher",
            "Develop your personal teaching philosophy",
            "Pursue a Master's for higher pay and advancement",
            "Engage in ongoing professional development"
        ]
    },
    "Academic Researcher": {
        "description": "Academic Researchers generate new knowledge through systematic study and publish findings in academic journals.",
        "skills": ["Research Design", "Statistical Analysis", "Academic Writing", "Critical Thinking", "Literature Review", "Grant Writing"],
        "salary": "$55,000 – $110,000/year",
        "pros": ["Intellectual freedom", "Contribute to human knowledge", "Flexible working environment", "International collaboration"],
        "cons": ["Highly competitive positions", "Publish or perish pressure", "Grant dependency", "Years of training required"],
        "roadmap": [
            "Excel academically in your undergraduate studies",
            "Assist professors in research projects early",
            "Complete a Master's degree in your field",
            "Pursue a PhD with a strong research focus",
            "Publish in peer-reviewed journals",
            "Apply for postdoctoral positions",
            "Secure faculty or senior researcher positions"
        ]
    },
    "Education Consultant": {
        "description": "Education Consultants advise students, schools, and organizations on educational planning, curriculum, and learning strategies.",
        "skills": ["Advising", "Curriculum Knowledge", "Communication", "Data Analysis", "Policy Understanding", "Empathy"],
        "salary": "$55,000 – $95,000/year",
        "pros": ["Flexible work options", "Rewarding student impact", "Wide range of clients", "Growing EdTech sector"],
        "cons": ["Self-employment income variability", "Requires building a client base", "Can be repetitive for standardized advice"],
        "roadmap": [
            "Get a degree in Education or a relevant field",
            "Gain experience teaching or in school administration",
            "Build expertise in college counseling or curriculum design",
            "Get certified (IECA membership, etc.)",
            "Build a network of schools and families",
            "Develop a consulting practice or join a firm",
            "Stay updated on admissions trends and policy changes"
        ]
    },
    "Instructional Designer": {
        "description": "Instructional Designers create structured learning experiences for corporate training, online education, and academic programs.",
        "skills": ["Curriculum Design", "E-Learning Tools (Articulate)", "LMS Platforms", "Adult Learning Theory", "Writing", "Visual Design"],
        "salary": "$60,000 – $100,000/year",
        "pros": ["Growing demand with remote learning", "Blend of creativity and structure", "Corporate and academic paths", "Remote-friendly"],
        "cons": ["Feedback cycles can be lengthy", "Requires stakeholder alignment", "Solo work can be isolating"],
        "roadmap": [
            "Study education or instructional design fundamentals",
            "Learn adult learning theory (Bloom's Taxonomy, ADDIE)",
            "Master e-learning tools like Articulate Storyline or Rise",
            "Work on LMS platforms (Canvas, Moodle, Cornerstone)",
            "Build a portfolio of sample courses",
            "Get certified (ATD CPTD or similar)",
            "Apply to EdTech companies or corporate L&D departments"
        ]
    },
    "Lawyer": {
        "description": "Lawyers represent clients in legal matters, draft legal documents, and provide expert advice on law and regulation.",
        "skills": ["Legal Research", "Argumentation", "Writing", "Negotiation", "Critical Thinking", "Ethics"],
        "salary": "$80,000 – $200,000+/year",
        "pros": ["High earning potential", "Diverse specializations", "Intellectually stimulating", "High social impact potential"],
        "cons": ["Very long education path", "High-stress environment", "Long working hours", "Emotionally heavy cases"],
        "roadmap": [
            "Excel in undergraduate studies (any major)",
            "Score well on LSAT",
            "Complete a Juris Doctor (JD) degree",
            "Pass the Bar Exam in your jurisdiction",
            "Join a law firm as an associate",
            "Choose a specialization (corporate, criminal, family, IP, etc.)",
            "Build courtroom and client experience over time"
        ]
    },
    "Policy Analyst": {
        "description": "Policy Analysts research, evaluate, and develop public policies for governments, NGOs, and think tanks.",
        "skills": ["Policy Research", "Data Analysis", "Report Writing", "Economics", "Critical Thinking", "Communication"],
        "salary": "$55,000 – $105,000/year",
        "pros": ["High public impact", "Intellectually demanding", "Diverse policy areas", "Government stability"],
        "cons": ["Slow pace of policy change", "Political constraints", "Often requires graduate-level education"],
        "roadmap": [
            "Study political science, economics, or public policy",
            "Master data analysis and policy research methods",
            "Complete a Master's in Public Policy (MPP) or related field",
            "Intern at government agencies or think tanks",
            "Publish policy briefs and research reports",
            "Build a network in your policy area",
            "Apply for analyst roles in government or nonprofits"
        ]
    },
    "Compliance Officer": {
        "description": "Compliance Officers ensure organizations follow legal regulations, internal policies, and industry standards.",
        "skills": ["Regulatory Knowledge", "Auditing", "Risk Assessment", "Documentation", "Communication", "Ethics"],
        "salary": "$65,000 – $115,000/year",
        "pros": ["Stable and growing demand", "Works across all industries", "Important risk management role", "Clear career progression"],
        "cons": ["Can be bureaucratic", "High attention to detail required", "Responsibility for company-wide adherence"],
        "roadmap": [
            "Study law, business, or finance",
            "Understand regulatory frameworks in your industry",
            "Get certified (CCEP, CRCM, or similar)",
            "Work in audit, legal, or risk roles first",
            "Build expertise in specific regulations (GDPR, SOX, etc.)",
            "Develop strong documentation and reporting skills",
            "Move into Compliance Officer roles in financial or healthcare sectors"
        ]
    }
}


# -------------------- QUIZ LOGIC --------------------
# Map each answer to career domain weights: Technology, Design, Business, Healthcare, Education, Law
quiz_weights = {
    # Interest
    "Solving problems with data & code": {"Technology": 3, "Business": 1},
    "Creating visual & artistic things": {"Design": 3, "Education": 1},
    "Leading teams & building businesses": {"Business": 3, "Law & Policy": 1},
    "Helping & healing people": {"Healthcare": 3, "Education": 2},
    "Researching & discovering knowledge": {"Healthcare": 1, "Education": 3, "Law & Policy": 1},

    # Strength
    "Logical & analytical thinking": {"Technology": 3, "Business": 1, "Law & Policy": 1},
    "Creativity & visual imagination": {"Design": 3, "Education": 1},
    "Empathy & communication": {"Healthcare": 3, "Education": 2, "Business": 1},
    "Leadership & decision-making": {"Business": 3, "Law & Policy": 2},
    "Research & writing": {"Education": 3, "Law & Policy": 3, "Healthcare": 1},

    # Work style
    "Independent / deep focus work": {"Technology": 2, "Design": 2, "Education": 1},
    "Collaborative & team-driven": {"Business": 2, "Healthcare": 2, "Education": 2},
    "Leadership & managing others": {"Business": 3, "Law & Policy": 2},
    "Hands-on & physical work": {"Healthcare": 3},
    "Mix of field & desk work": {"Business": 1, "Law & Policy": 1, "Education": 2},

    # Education level
    "High school / diploma": {"Design": 2, "Business": 1},
    "Bachelor's degree": {"Technology": 2, "Business": 2, "Design": 2, "Education": 2},
    "Master's / MBA": {"Business": 3, "Technology": 1, "Education": 2, "Law & Policy": 2},
    "Doctoral / Medical / Law degree": {"Healthcare": 3, "Education": 3, "Law & Policy": 3},

    # Salary priority
    "Passion over pay": {"Education": 2, "Healthcare": 1, "Design": 2},
    "Good work-life balance": {"Education": 2, "Business": 1, "Technology": 1},
    "Top earning potential": {"Technology": 3, "Business": 3, "Law & Policy": 3, "Healthcare": 2},
    "Stable & predictable income": {"Healthcare": 2, "Education": 2, "Law & Policy": 2},

    # Environment
    "Office / corporate setting": {"Business": 2, "Law & Policy": 2, "Technology": 1},
    "Remote / flexible location": {"Technology": 3, "Design": 3, "Education": 1},
    "Outdoors / fieldwork": {"Healthcare": 1},
    "Hospital / clinic": {"Healthcare": 3},
    "Creative studio": {"Design": 3}
}

def calculate_career_matches(answers):
    domain_scores = {"Technology": 0, "Design": 0, "Business": 0, "Healthcare": 0, "Education": 0, "Law & Policy": 0}
    for answer in answers:
        if answer in quiz_weights:
            for domain, weight in quiz_weights[answer].items():
                domain_scores[domain] += weight
    total = sum(domain_scores.values()) or 1
    percentages = {k: round((v / total) * 100) for k, v in domain_scores.items()}
    sorted_domains = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
    return sorted_domains

# -------------------- SECTION 1: PERSONAL QUIZ --------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("🧩 Personal Career Quiz")
st.caption("Answer honestly — there are no wrong answers.")

interest = st.radio("1️⃣ What excites you most?", [
    "Solving problems with data & code",
    "Creating visual & artistic things",
    "Leading teams & building businesses",
    "Helping & healing people",
    "Researching & discovering knowledge"
])

strength = st.radio("2️⃣ What is your greatest strength?", [
    "Logical & analytical thinking",
    "Creativity & visual imagination",
    "Empathy & communication",
    "Leadership & decision-making",
    "Research & writing"
])

work_style = st.radio("3️⃣ How do you prefer to work?", [
    "Independent / deep focus work",
    "Collaborative & team-driven",
    "Leadership & managing others",
    "Hands-on & physical work",
    "Mix of field & desk work"
])

education = st.radio("4️⃣ What is your highest planned education level?", [
    "High school / diploma",
    "Bachelor's degree",
    "Master's / MBA",
    "Doctoral / Medical / Law degree"
])

salary_pref = st.radio("5️⃣ What matters most to you in a career?", [
    "Passion over pay",
    "Good work-life balance",
    "Top earning potential",
    "Stable & predictable income"
])

environment = st.radio("6️⃣ What work environment suits you best?", [
    "Office / corporate setting",
    "Remote / flexible location",
    "Outdoors / fieldwork",
    "Hospital / clinic",
    "Creative studio"
])
if st.button("🔍 Analyse My Career Fit"):
    answers = [interest, strength, work_style, education, salary_pref, environment]
    sorted_domains = calculate_career_matches(answers)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.subheader("📊 Your Career Domain Match")

    for domain, pct in sorted_domains:
        bar_color = "#0f3460"
        st.markdown(f"**{domain}** — {pct}%")
        st.markdown(f"""
        <div class="match-bar-bg">
            <div class="match-bar-fill" style="width:{pct}%;"></div>
        </div>
        """, unsafe_allow_html=True)

    top_domain = sorted_domains[0][0]
    st.success(f"✅ Your strongest match is **{top_domain}**!")
    st.markdown(f"**Suggested careers to explore:** {', '.join(career_domains[top_domain])}")

    if sorted_domains[1][1] >= 15:
        second_domain = sorted_domains[1][0]
        st.info(f"💡 You also show strong potential in **{second_domain}**: {', '.join(career_domains[second_domain][:3])}...")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# -------------------- SECTION 2: ABOUT YOURSELF --------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("📝 Tell Us About Yourself")

about = st.text_area("Write about your interests, goals, or personality...", height=120)

if st.button("🧠 Generate Insight"):
    if about:
        text_lower = about.lower()

        # Keyword-based logic
        tech_keywords = ["code", "program", "tech", "data", "software", "ai", "machine", "computer", "algorithm", "developer", "engineer"]
        design_keywords = ["design", "art", "creative", "visual", "draw", "animate", "color", "graphic", "ui", "ux"]
        business_keywords = ["business", "manage", "lead", "market", "finance", "strategy", "entrepreneur", "sales", "growth"]
        health_keywords = ["health", "medicine", "doctor", "nurse", "care", "patient", "hospital", "biology", "science"]
        edu_keywords = ["teach", "learn", "educate", "research", "study", "academic", "school", "knowledge"]
        law_keywords = ["law", "legal", "policy", "compliance", "justice", "rights", "regulation"]

        scores = {
            "Technology": sum(1 for k in tech_keywords if k in text_lower),
            "Design": sum(1 for k in design_keywords if k in text_lower),
            "Business": sum(1 for k in business_keywords if k in text_lower),
            "Healthcare": sum(1 for k in health_keywords if k in text_lower),
            "Education": sum(1 for k in edu_keywords if k in text_lower),
            "Law & Policy": sum(1 for k in law_keywords if k in text_lower),
        }

        top = max(scores, key=scores.get)
        top_score = scores[top]

        analytical = any(w in text_lower for w in ["analyze", "logic", "data", "research", "solve", "problem"])
        creative = any(w in text_lower for w in ["creative", "art", "design", "imagine", "innovate", "build"])
        people = any(w in text_lower for w in ["people", "team", "help", "care", "communicate", "lead", "collaborate"])

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🔍 Insight Based on Your Description")

        if top_score > 0:
            st.write(f"👉 Your writing suggests a strong leaning toward **{top}** careers.")
            st.write(f"💼 Explore: {', '.join(career_domains[top][:4])}")
        else:
            st.write("👉 Your writing reflects broad curiosity — you'd thrive in versatile roles.")

        traits = []
        if analytical:
            traits.append("🧠 **Analytical thinker** — you enjoy logic, research, and problem-solving.")
        if creative:
            traits.append("🎨 **Creative mind** — you value innovation and original thinking.")
        if people:
            traits.append("🤝 **People-oriented** — collaboration and communication are your strengths.")

        if traits:
            st.markdown("**Personality signals detected:**")
            for t in traits:
                st.markdown(t)

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please write something about yourself first.")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# -------------------- SECTION 3: EXPLORE CAREERS --------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("🌍 Explore Careers")

selected_domain = st.selectbox("Choose a domain", list(career_domains.keys()))

if st.button("🔍 Show Careers in This Domain"):
    st.subheader(f"Careers in {selected_domain}")
    for career in career_domains[selected_domain]:
        data = career_data.get(career)
        if data:
            with st.expander(f"📌 {career}"):
                st.write(data["description"])
                st.markdown(f'<span class="salary-badge">💰 {data["salary"]}</span>', unsafe_allow_html=True)
                st.markdown("**Key Skills:** " + " ".join([f'<span class="metric-pill">{s}</span>' for s in data["skills"]]), unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)


# -------------------- SECTION 4: CAREER DEEP DIVE --------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("📘 Career Deep Dive")

all_careers = [c for careers in career_domains.values() for c in careers]
selected_career = st.selectbox("Choose a career to explore in detail", all_careers)

if st.button("📖 Show Full Details"):
    data = career_data.get(selected_career)
    if data:
        st.subheader(f"🎯 {selected_career}")
        st.write(data["description"])
        st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**💰 Salary Range**")
            st.markdown(f'<span class="salary-badge">{data["salary"]}</span>', unsafe_allow_html=True)

            st.markdown("**🛠 Key Skills**")
            skills_html = " ".join([f'<span class="metric-pill">{s}</span>' for s in data["skills"]])
            st.markdown(skills_html, unsafe_allow_html=True)

        with col2:
            st.markdown("**✅ Pros**")
            for pro in data["pros"]:
                st.markdown(f'<div class="pro-item">✔ {pro}</div>', unsafe_allow_html=True)

            st.markdown("**❌ Cons**")
            for con in data["cons"]:
                st.markdown(f'<div class="con-item">✘ {con}</div>', unsafe_allow_html=True)

        st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)
        st.markdown("**🗺 Career Roadmap**")
        for i, step in enumerate(data["roadmap"], 1):
            st.markdown(f'<div class="roadmap-step">Step {i}: {step}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<hr class="styled-divider">', unsafe_allow_html=True)

# -------------------- SECTION 5: PDF REPORT --------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.header("📥 Download Career Report")

report_career = st.selectbox("Select career for your report", all_careers, key="report_career")

def generate_pdf(career_name, data):
    file_path = "career_report.pdf"
    doc = SimpleDocTemplate(file_path, rightMargin=inch*0.75, leftMargin=inch*0.75,
                            topMargin=inch*0.75, bottomMargin=inch*0.75)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("Title", parent=styles["Title"], fontSize=22,
                                 textColor=colors.HexColor("#0f3460"), spaceAfter=10)
    heading_style = ParagraphStyle("Heading", parent=styles["Heading2"], fontSize=13,
                                   textColor=colors.HexColor("#1a1a2e"), spaceAfter=6, spaceBefore=12)
    body_style = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10,
                                leading=16, textColor=colors.HexColor("#333333"))
    bullet_style = ParagraphStyle("Bullet", parent=styles["Normal"], fontSize=10,
                                  leading=16, leftIndent=16, textColor=colors.HexColor("#333333"))

    content = []
    content.append(Paragraph(f"Career Report: {career_name}", title_style))
    content.append(Spacer(1, 0.1 * inch))
    content.append(Paragraph("Generated by Career Intelligence System", body_style))
    content.append(Spacer(1, 0.25 * inch))

    content.append(Paragraph("Overview", heading_style))
    content.append(Paragraph(data["description"], body_style))

    content.append(Paragraph("Salary Range", heading_style))
    content.append(Paragraph(data["salary"], body_style))

    content.append(Paragraph("Key Skills", heading_style))
    for skill in data["skills"]:
        content.append(Paragraph(f"• {skill}", bullet_style))

    content.append(Paragraph("Pros", heading_style))
    for pro in data["pros"]:
        content.append(Paragraph(f"✔ {pro}", bullet_style))

    content.append(Paragraph("Cons", heading_style))
    for con in data["cons"]:
        content.append(Paragraph(f"✘ {con}", bullet_style))

    content.append(Paragraph("Career Roadmap", heading_style))
    for i, step in enumerate(data["roadmap"], 1):
        content.append(Paragraph(f"Step {i}: {step}", bullet_style))

    content.append(Spacer(1, 0.3 * inch))
    content.append(Paragraph('"Discipline beats motivation. Consistency builds careers."', body_style))

    doc.build(content)
    return file_path

if st.button("📄 Generate & Download PDF Report"):
    data = career_data.get(report_career)
    if data:
        pdf_file = generate_pdf(report_career, data)
        with open(pdf_file, "rb") as f:
            st.download_button(
                label=f"⬇ Download {report_career} Report (PDF)",
                data=f,
                file_name=f"{report_career.replace(' ', '_')}_career_report.pdf",
                mime="application/pdf"
            )
        st.success("Your report is ready!")

st.markdown('</div>', unsafe_allow_html=True)


# -------------------- FOOTER --------------------
st.markdown("""
<div style="text-align:center; margin-top: 40px; color: #9ca3af; font-size: 0.82rem;">
    Career Intelligence System &nbsp;|&nbsp; Built with Streamlit &nbsp;|&nbsp; Helping you find your path 🎯
</div>
""", unsafe_allow_html=True)
