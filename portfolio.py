
import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Ebenezer Kwaw Portfolio",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load profile images from 'images/' folder
profile_images = []
for img_name in ["Picture.jpg", "profile1.png", "profiile.png"]:
    try:
        profile_images.append(Image.open(f"images/{img_name}"))
    except:
        pass

# Load project images from 'images/' folder
project_images = []
for img_name in ["project.png", "project1.png", "project2.png"]:
    try:
        project_images.append(Image.open(f"images/{img_name}"))
    except:
        pass

# Header section
st.markdown("""
    <style>
        .main, .block-container {
            background-color: #cceeff;
            color: #1c1c1c;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 {
            color: #004466;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Ebenezer Kwaw")
st.subheader("Public Health Specialist | Data & ML Practitioner | AI Enthusiast | Future Cybersecurity Analyst | Cloud Engineer in Training | Nutrition Advocate")

# Show profile pictures
if profile_images:
    st.markdown("### 📸 Profile Pictures")
    cols = st.columns(len(profile_images))
    for i, img in enumerate(profile_images):
        with cols[i]:
            st.image(img, width=200)
else:
    st.warning("No profile images found in the 'images/' folder.")

# About Me
st.markdown("""
### About Me
I am a dedicated Public Health Specialist with over 7 years of experience designing and implementing community health and nutrition programs. My mission has always been to improve lives using evidence-based strategies — and now, I’m enhancing that mission with technology.

Currently, I’m transitioning into a Data & AI Practitioner role, applying machine learning, data analytics, and interactive web apps to solve real-world problems — especially in public and preventive health.

Through hands-on projects like:
- 🛏️ ITN Usage Prediction App (malaria prevention analytics)
- 💳 Loan Defaulters Risk Model
- 🎬 Movie Recommendation System

I’ve built full-stack solutions using Python, Streamlit, and scikit-learn — and deployed them live for stakeholder use. I’ve also completed formal training in Data Science, Machine Learning, and Cybersecurity, and I’m currently advancing in Cloud Engineering to better manage scalable, secure, and data-driven systems.

I’m passionate about using AI and digital health solutions to improve lives — especially in low-resource settings — and I’m eager to collaborate on impactful projects in data, healthcare, tech-for-good, or global development.
""")

# Skills
st.markdown("""
### 🧠 Skills
- Machine Learning (intermediate)
- Public Health Program Management
- Data Analysis (Python, Excel, Power BI, SQL)
- Public Speaking
- Cloud Computing
- Scikit-Learn
- Research
- Leadership
- Communication
- Counselling
- Project Management
""")

# Education
st.markdown("""
### 🎓 Education
- BSc. Public Health (Community Nutrition), University for Development Studies (2012–2016)
- Data Science Certificate, Thrive Africa & Koforidua Technical University (2025)
- Machine Learning & AI Certificate, Thrive Africa & Koforidua Technical University (2025)
- Cybersecurity Certificate, Thrive Africa & Koforidua Technical University (2025)
- Data Lab Certificate, World Quant University (Ongoing)
- Advance Cloud Engineer Certificate, (Ongoing)
- Project Management in Global Health, University of Washington (2023)
- Monitoring & Evaluation in Global Health, University of Washington (2023)
""")

# Experience
st.markdown("""
### 💼 Experience
**Public Health Specialist | Data & AI Practitioner | Cloud & Cybersecurity Trainee**  
Self-employed, January 2025 – Present (Remote)
- Applied data science and AI techniques to public health problems
- Developed and deployed predictive models using Streamlit
- Built interactive dashboards and ML-powered tools
- Integrated cloud engineering and cybersecurity concepts into health solutions

**District Nutrition Officer / Public Health Officer**  
Ghana Health Service – Agona East District (2021 – Present)
- Led public health programs, M&E, COVID-19 vaccination
- Supervised National Immunization Days
- Managed emergency response strategies and communication

**Nutritionist**  
Samartex Hospital, Samreboi (2018 – 2021)
- Designed and managed nutrition programs for vulnerable populations

**Nutritionist**  
Shama Health Center (2016 – 2017)
- Provided dietary counseling and conducted community outreach
""")

# Contact
st.markdown("""
### 📫 Contact
📧 Email: ebenezer.kwaw@ghs.gov.gh / ekwaw4545@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kwaw-ebenezer-a40117159)  
💻 [GitHub](https://github.com/kwaw-ebn/kwaw-ebn)
""")

# Download CV
try:
    with open("cv.pdf", "rb") as file:
        st.download_button(label="📄 Download My CV", data=file, file_name="Ebenezer_Kwaw_CV.pdf", mime="application/pdf")
except FileNotFoundError:
    st.warning("Upload 'cv.pdf' to enable the download button.")

# Projects
st.markdown("""
### 🚀 Projects
""")

project_details = [
    ("ITN Usage Prediction Web App", "https://github.com/kwaw-ebn/ITN-Usage-Prediction", "https://itn-usage-prediction-nywkrcihz3teyjvze27um8.streamlit.app/"),
    ("Loan Defaulter Risk Prediction App", "https://github.com/kwaw-ebn/Machine-Learning-Model-to-predict-Loan-Defaulters", "https://machine-learning-model-to-predict-loan-defaulters-mazkvkvr4t2q.streamlit.app/"),
    ("Movie Recommendation System", "https://github.com/kwaw-ebn/Movie_Recommendation", "https://movierecommendation-khmzfv7djvecuar2hcmc6j.streamlit.app/")
]

for img, (title, github, demo) in zip(project_images, project_details):
    st.image(img)
    st.markdown(f"**🔹 {title}**")
    st.markdown(f"[GitHub]({github}) | [Demo]({demo})")
    st.markdown("---")
