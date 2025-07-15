
# Streamlit Portfolio App for Kwaw Ebenezer
import streamlit as st
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Kwaw Ebenezer Portfolio", page_icon="📄", layout="wide")

# Enforce sea blue background (Streamlit-specific containers)
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #caf0f8 !important;
    }
    a {
        color: #0077b6;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #0077b6;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    h2, h3 {
        color: #0077b6;
    }
    </style>
""", unsafe_allow_html=True)

# Helper to load image from images/ folder
def load_image(filename, caption=None, width=None):
    path = os.path.join("images", filename)
    try:
        img = Image.open(path)
        st.image(img, caption=caption, use_container_width=(width is None))
    except FileNotFoundError:
        st.warning(f"Image '{filename}' not found in 'images/' folder.")

# ---------- HEADER SECTION ----------
st.title("Kwaw Ebenezer")
st.subheader("Public Health Specialist | Data & ML Practitioner | AI Enthusiast")

st.markdown("""
📍 **Accra, Ghana**  
📧 ebenezer.kwaw@ghs.gov.gh | ekwaw4545@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kwaw-ebenezer-a40117159) | [GitHub](https://github.com/kwaw-ebn/kwaw-ebn)  
📱 +233244837234  
📄 [Download CV](https://github.com/kwaw-ebn/Portfolio/blob/main/cv.pdf)
""")

# ---------- PROFILE IMAGE ----------
load_image("profile1.png", width=180)

# ---------- ABOUT ME ----------
st.header("👋 About Me")
st.write("""
I am a dedicated Public Health Specialist with over 7 years of experience designing and implementing community health and nutrition programs. 
My mission is to improve lives using evidence-based strategies enhanced with technology.

I’m currently transitioning into a Data & AI Practitioner role, applying machine learning, data analytics, and interactive web apps to solve real-world problems in public and preventive health. 
I’m passionate about using AI and digital health to improve lives in low-resource settings and open to collaborating on impactful data-driven projects.
""")

# ---------- SKILLS ----------
st.header("🛠 Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Technical")
    st.markdown("""
- Python, Jupyter Notebook
- Pandas, Numpy, Scikit-learn
- Streamlit, Power BI, SQL
- Excel, Kobo Toolbox
- Model Deployment
    """)

with col2:
    st.subheader("Public Health / Analytics")
    st.markdown("""
- M&E Systems, SBCC
- Survey Design
- Data Cleaning & Analysis
- Predictive Modelling
- Health Systems Strengthening
    """)

with col3:
    st.subheader("Soft Skills")
    st.markdown("""
- Leadership & Teamwork
- Communication & Reporting
- Project Management
- Problem Solving
- Community Mobilization
    """)

# ---------- PROJECTS ----------
st.header("🚀 Projects")

st.subheader("ITN Usage Prediction Web App")
load_image("project.png", caption="ITN Prediction Tool")
st.markdown("""
Developed and deployed a machine learning model to predict ITN usage. Supports malaria prevention planning.

🔗 [GitHub](https://github.com/kwaw-ebn/ITN-Usage-Prediction)  
🔗 [Live App](https://itn-usage-prediction-nywkrcihz3teyjvze27um8.streamlit.app/)
""")

st.subheader("Loan Defaulter Risk Prediction App")
load_image("project2.png", caption="Loan Risk Classifier UI")
st.markdown("""
A supervised ML model to classify loan risk, deployed with an interactive web interface.

🔗 [GitHub](https://github.com/kwaw-ebn/Machine-Learning-Model-to-predict-Loan-Defaulters)  
🔗 [Live App](https://machine-learning-model-to-predict-loan-defaulters-mazkvkvr4t2q.streamlit.app/)
""")

st.subheader("Movie Recommendation System")
load_image("project1.png", caption="Movie Recommender UI")
st.markdown("""
Content-based movie recommender using cosine similarity and Streamlit.

🔗 [GitHub](https://github.com/kwaw-ebn/Movie_Recommendation)  
🔗 [Live App](https://movierecommendation-khmzfv7djvecuar2hcmc6j.streamlit.app/)
""")

# ---------- EXPERIENCE ----------
st.header("💼 Work Experience")
st.markdown("""
**Public Health Specialist / AI Practitioner** – Self-employed (2025–Present)  
- Build data-driven tools for public health  
- Train in cloud & cybersecurity  

**District Nutrition Officer** – GHS, Agona East (2021–Present)  
- Led immunization programs & emergency preparedness  
- Developed tools for health monitoring  

**Program Coordinator – IPTp** – RootsLink Africa (2023–Present)  
- Coordinated malaria prevention across Agona East  
- Built M&E tools and campaign materials  

**Nutritionist** – Samartex Hospital (2018–2021)  
**Nutritionist** – Shama Health Center (2016–2017)  
""")

# ---------- RESEARCH ----------
st.header("🔬 Research Contributor")
st.markdown("""
**Title:** Assessing the Prevalence of Hypertension and Obesity Among Diabetics in Tamale Metropolis (2017)  
🔗 [Read Paper](https://www.researchgate.net/profile/Yussif-Adams/publication/315943323_Assessing_the_Prevalence_of_Hypertension_and_Obesity_among_Diabetics_in_the_Tamale_Metropolis_Ghana/links/5f40c768a6fdcccc43e55e10/Assessing-the-Prevalence-of-Hypertension-and-Obesity-among-Diabetics-in-the-Tamale-Metropolis-Ghana.pdf)
""")

# ---------- PROGRAMS MANAGED ----------
st.header("📌 Programs Managed")
st.markdown("""
- Girls’ Iron-Folic Tablet Supplementation (GIFTS)  
- Wellness Clinic Coordinator, Agona East  
- IYCF Training Program (with Kokoplus Ghana)  
""")

# ---------- EDUCATION ----------
st.header("🎓 Education & Certifications")
st.markdown("""
- BSc. Public Health (Nutrition), UDS (2012–2016)  
- Data Science, Thrive Africa & KTU (2025)  
- AI & ML, Thrive Africa & KTU (2025)  
- Cybersecurity, Thrive Africa & KTU (2025)  
- Data Lab Certificate, WorldQuant University (ongoing)  
- Cloud Engineer Certificate (ongoing)  
- M&E and Global Health Courses – University of Washington (2023)  
""")

# ---------- CONTACT ----------
st.header("📬 Contact")
st.markdown("""
📧 ebenezer.kwaw@ghs.gov.gh / ekwaw4545@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kwaw-ebenezer-a40117159)  
📱 +233244837234
""")
