import streamlit as st
import os
from PIL import Image

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Shanza - Portfolio",
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="👩💻"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    .nav {
        display: flex;
        gap: 2rem;
        padding: 1rem 0;
        margin-bottom: 2rem;
        justify-content: center;
        border-bottom: 1px solid #eee;
    }
    .nav a {
        text-decoration: none;
        font-weight: 600;
        font-size: 1.2rem;
        color: #333;
    }
    .nav a:hover {
        color: #4a6bff;
    }
    h1 {
        font-size: 3rem !important;
    }
    h2 {
        font-size: 2.3rem !important;
        border-bottom: 3px solid #4a6bff;
        padding-bottom: 0.5rem;
        margin-top: 3rem !important;
    }
    h3 {
        font-size: 1.5rem !important;
    }
    p {
        font-size: 1.2rem !important;
    }
    .stProgress > div > div > div {
        background-color: #4a6bff;
        height: 10px;
        border-radius: 5px;
    }
    .project-image {
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ===== NAVIGATION =====
st.markdown("""
<div class="nav">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ===== IMAGE LOAD FUNCTION =====
def load_image(image_name):
    try:
        image_path = os.path.join(os.path.dirname(__file__), image_name)
        return Image.open(image_path)
    except:
        return None

# ===== HOME SECTION (TRUE HALF-HALF) =====
st.markdown('<a id="home"></a>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    profile_img = load_image("profile.jpg")
    if profile_img:
        st.image(profile_img, use_column_width=True)

with col2:
    st.markdown("### 👋 Hi, I'm")
    st.markdown("# **Shanza**")
    st.markdown("### AI Engineer & Computer Vision Specialist")
    st.write("📞 (+92) 3195025857")
    st.write("📧 shanzashakeel270@gmail.com")
    st.markdown("[🌐 LinkedIn](https://linkedin.com/in/shanza-shakeel-9a76932a42)")

# ===== ABOUT SECTION =====
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
st.header("About Me")
st.write("""
Computer Engineering graduate with specialization in AI/ML from Institute of Space Technology. 
Gold medalist with 3.89/4.0 CGPA. Passionate about developing cutting-edge computer vision 
solutions and embedded systems for real-world applications.
""")

# ===== SKILLS SECTION =====
st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
st.header("My Skills")
skills = {
    "AI/ML": 95,
    "Python": 90,
    "Computer Vision": 85,
    "Embedded Systems": 80,
    "Data Structures": 85
}
for skill, level in skills.items():
    st.write(f"{skill}: {level}%")
    st.progress(level)

# ===== PROJECTS SECTION =====
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("My Projects")

# Project 1 - Jet Detection
st.subheader("Jet Detection System")
jet_img = load_image("jet_detection.jpg")
if jet_img:
    st.image(jet_img, caption="Jet Detection System", use_column_width=True, output_format="JPEG")
st.markdown("""
- Real-time jet detection using YOLOv6 and OpenCV  
- Achieved 92% accuracy  
- Technologies: Python, Deep Learning, Computer Vision  
""")

# Project 2 - RFID Parking
st.subheader("RFID Parking System")
rfid_img = load_image("rfid_parking.jpg")
if rfid_img:
    st.image(rfid_img, caption="RFID Parking System", use_column_width=True, output_format="JPEG")
st.markdown("""
- Automated parking management system using Arduino and RFID  
- Reduced entry time by 70%  
- Technologies: Embedded Systems, C++, Hardware Prototyping  
""")

# ===== CONTACT SECTION =====
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("Contact Me")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you for your message! I'll get back to you soon.")
