from pathlib import Path
import streamlit as st
from PIL import Image
import random

# Set Path Configuration

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print(current_dir)

css_file = current_dir / "styles.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile-picture.png"

# Details

Page_Title = "Virtual Resume | Anuj Seshan"
Page_Icon = ":wave:"
Name = "Anuj Seshan"
Description = """
- A calm and composed, hard-working and committed individual who enjoys and cherishes working in teams which helps in developing social and communication skills and I get to learn about and experience diversified cultures and traditions.
- I define myself as an individual who is enthusiastic about Data and is always eager to learn new skills and technologies.
"""
Email = "anuj.downunder@gmail.com"
Blogger = "https://www.blogger.com/profile/16952388212820659471"
Social_Media = {
    "Email": "📧 anuj.downunder@gmail.com",
    "Address" : " 28/2 Riverpark Drive, Liverpool Sydney NSW 2170",
    "Blogger" : "https://www.blogger.com/profile/16952388212820659471",
    "Phone Number" : "+61 493-419-330"
}

Projects = {
"📈 Power BI" : "https://drive.google.com/drive/folders/19DC-Zlq0MX2CBdlDS4PV3H-azewNK1ZZ?usp=sharing",
"🔢 Microsoft Excel":"https://drive.google.com/drive/folders/1i5d1MZWNJ2TCtgLTpE1NDMhRGk1VXU7V?usp=sharing",
"🐍 Python":"https://drive.google.com/drive/folders/1IQBywTD2RjcvUXXwSNEahwj9CC_y2Qeu?usp=sharing",
"®️ RStudio":"https://drive.google.com/drive/folders/1VRiaIA8M3z4o-0CG7sVqJ6TO5Yct_R3T?usp=sharing"
}

st.set_page_config(page_title=Page_Title,layout="wide",page_icon=Page_Icon)

# Allow HTML Modifications, Resume Access and Profile Picture

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

#snowflakes_html = '<div class="snowflake-container">'
#for _ in range(5):
    #left = random.randint(0, 95)
    #fall_duration = random.uniform(4, 8)
    #wave_duration = random.uniform(2, 5)
    #snowflakes_html += (
        #f'<span class="snowflake-icon" '
        #f'style="--snowflake-left: {left}%; --fall-duration: {fall_duration}s; --wave-duration: {wave_duration}s;">🔢</span>')
    
    #left2 = random.randint(0, 95)
    #fall_duration2 = random.uniform(4, 8)
    #wave_duration2 = random.uniform(2, 5)
    #snowflakes_html += (
        #f'<span class="snowflake-icon" '
        #f'style="--snowflake-left: {left2}%; --fall-duration: {fall_duration2}s; --wave-duration: {wave_duration2}s;">📊</span>')

#snowflakes_html += '</div>'
#st.markdown(snowflakes_html, unsafe_allow_html=True)

#   st.title("Profile")
column1, column2 = st.columns(2, gap="small")
with column1:
    st.write("#")
    st.image(profile_pic, width = 300)
with column2:
    st.title(Name)
    st.write(Description)
    st.selectbox("**I am proficient in the roles of a/an**", ["Data Analyst", "Data Scientist", "Business Analyst", "Business Intelligence Expert", "Machine Learning Engineer", "RPA Automation Developer", "Supply Chain Analyst", "Procurement Analyst", "Executive Assistant"])
    st.download_button(
        label="🗒️ Download Resume",
        data = PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📧", Email)
    st.write("🔗 [Blogger](https://www.blogger.com/profile/16952388212820659471)")
    st.write("📞", "+61 493-419-330")
    st.write("📍", "Sydney, Australia")
    st.write("🏠", "28/2 Riverpark Drive, Liverpool Sydney NSW 2170")

# Skills
st.write("#")
st.subheader("**Technical Skills**")
st.write("---")
st.write("""
- 🧑‍💻Programming: **Python**, RStudio, Visual Basic for Applications, HTML and CSS
- 📊 Data Visualisation: **Microsoft Power BI**, Tableau, Domo, Google Analytics and IBM Cognos Analytics
- 🗃️ Databases: **Micorsoft Excel**, Google BigQuery, MySQL, **DuckDB** and **CockroachDB**
- ❄️ RPA Frameworks: **Automation Anywhere**, Power Automate and Robocorp
- 💡Agentic AI Frameworks: **crewai**, langchain, **n8n** and Zapier
"""
)

# Certifications
st.write("#")
st.subheader("**🥇Certifications**")
st.write("---")
st.write("""
- [Harvard Business School](https://drive.google.com/file/d/1U21zBKp-teBtoXyyQ5QT5AVJGLiVNH4A/view?usp=drive_link)
- [Python for Data Science and Machine Learning](https://drive.google.com/file/d/176WfVndzcThQ_HIrSR8B1tSOoUISy1_d/view)
- [Google Data Analytics](https://drive.google.com/file/d/16l4TSLoZHwpLU7aJ2HEKaBC7xzpCh7BR/view)
- [Microsoft Power BI](https://drive.google.com/file/d/1GHVgmtRpoJJzkeLVodxIGWc9BdYWP7J6/view?usp=share_link)
- [Snowflake BI Analytics Bootcamp](https://www.snowflake.com/dca-thankyou/bi-analytics-bootcamp/)  
- [Alteryx](https://drive.google.com/file/d/1q5a3d-Vsk6XoGQ7umwNAruiOAzqob3-5/view?usp=drive_link)
- [KNIME Analytics](https://drive.google.com/drive/folders/11O-8774ed27Ub05ht0EiEJkWmGaXdanT)
- [Tableau](https://drive.google.com/file/d/1t_a2U4xjLjPxs_sV1luAFCM2YKcGiORS/view?usp=share_link)
- [Microsoft Excel Advanced](https://drive.google.com/file/d/1nRyQHJ1Rk2XGNN4mFPs-xOzi8vWLmeYp/view)
- [Microsoft Excel](https://drive.google.com/file/d/1wDEbIAN113mvsCqCuYurXf3D0dd6PTKy/view)
- [Swedish Cultural Exchange Program](https://drive.google.com/file/d/1MB-gSpqYFrx9Cgx7FiPMYiaZnXaffptm/view)                  
"""
)
st.write("#")
st.subheader("**Bosch Accreditations**")
st.write("""
    - [Bosch Accreditations Folder](https://drive.google.com/drive/folders/1Pkcl3VpEeS7bXa5P_JhlmT_jyW01vr1j)
    - [Power BI Issue Resolvance](https://drive.google.com/file/d/16kzIaQQzMb69oZztZAMPlwYu5-523tjQ/view?usp=sharing)
    - [Data Management for Global Plastics](https://drive.google.com/file/d/1V47GtKS9swAqE3RHt8wMsb8kqOYInOxa/view?usp=sharing)
    - [Automation Deployment](https://drive.google.com/file/d/1kmOF08owFP39L2x5vpYIsRyRbkDAxi3B/view?usp=sharing)
    - [Reduction of SLA Days](https://drive.google.com/file/d/1oM5qaSUuwCo0Sljwsjqhtp4b9aTYEPJ6/view?usp=sharing)
    - [Distinguished Individual Achievement](https://drive.google.com/file/d/1I-YMFj-2VVgXGyJ3oUa7QiAPn_3FpSNB/view?usp=sharing)
    """
)

st.write("#")
st.subheader("**Artificial Intelligence Accreditations**")
st.write("""
    - [Artificial Intelligence Accreditations Folder](https://drive.google.com/drive/folders/11O-8774ed27Ub05ht0EiEJkWmGaXdanT?usp=sharing)
    - [crew.ai](https://drive.google.com/file/d/14gks8roXcfj87_dtMbdEpj0EBBEy78qO/view?usp=sharing)
    - [Langchain](https://drive.google.com/file/d/1DTp2gQenTbby-J5mS9QXwA-5G_hBWdU4/view?usp=sharing)
    - [CockroachDB](https://drive.google.com/file/d/1MQa39MqWbr5txsxgtCJF6E0o2gPPhSRE/view?usp=sharing)
    - [ChromaDB](https://drive.google.com/file/d/1iHZH3D2Jazck1TrHkbNtWXZw3B5zJh3w/view?usp=sharing)
    """
)

# Education

st.write("#")
st.subheader("**Education**")
st.write("---")
st.write(
    """
    - Higher Secondary Education in Biological and Medical Sciences from Christ Pre-University College Residential, Bengaluru with a percentage of 77%.
    - Bachelor's Degree in Data Science and Analytics **Honours** from Jain University, School of Sciences Bengaluru with a CGPA of 9.15/10.
    """
    )

# Accomplishments
st.write("#")
st.subheader("**Educational Accomplishments**")
st.write("---")
st.write("""
- Attained 2nd Position in NSO (National Science Olympiad) in Grade 12 in the entire STEM Stream of our Pre-University college.
-  3rd place in a French Ad as part of a collegiate fest organized by Mount Carmel College, Bangalore
- Attained 1st place in a French Quiz organized by St Joseph’s College, Bangalore.
- **During my collegiate tenure, I consistently ranked among the top academic performers of my class while also being a part of intercollegiate cultural festivals.**
- While participating in these collegiate festivals, I won multiple awards as a team and as an individual in the fields of Language, Marketing and Article Publishment.
- I also had the lovely opportunity to serve as the Head of Department, Public Relations wherein my department were touted as **"The Most Streamlined and Well Managed Department"** of Cultural Year of 2025. I had the great pleasure of bonding and working with multiple people during this time due to which our team blossomed and got better.
- I had also published a research paper on Stable Diffusion and Generative Adversarial Networks in collaboration which was appreciated by our University Vice Chancellor and the Head of Department, Data Science.
"""
)

# Work History
st.write("#")
st.subheader("**Work History**")
st.write("---")
st.write("🏢","**Senior Data Expert | Robert Bosch GmbH**")
st.write("07/2023 - 09/2025")
st.write(
    """
    - Analyzing and Handling Supplier Data using Excel, Power BI and Tableau for an increase in purchase forecasts for our manufacturing plants which helped yield significant profitability.
    - Designing and Deployment of Process Automation Solutions using Power Automate and Visual Basic Applications.
    - Creation of Simple Chatbots using Power Automate and Communication Platforms like Outlook and Microsoft Teams.
    - **Creation of Project Management Solutions using Microsoft Lists and Microsoft Teams which increased procurement efficiency and closure of high-urgency Purchase Orders.**
    """)

st.write("#")
st.write("🏢","**Operations Analyst Intern | Vaegter Technovations Private Limited**")
st.write("10/2022 - 07/2023")
st.write(
    """
    - Develop and Create Customer Acquisition models which would increase efficiency.
    - Ensuring punctuality and deliverance of results at the optimal time of need and requirement
    - Analyzing Data inputs in order to create decisive insights which have a positive impact on growth and profitability.
    - **Achieved the highest sales performance of the year 2022 by providing a customer acquisition model based on locations of Bengaluru**.
    """
    )

# Accomplishments
st.write("#")
st.subheader("**Work Accomplishments**")
st.write("---")
st.write("""
- Achieved a saving of ₹24 Crore in GST Returns using purchasing and procurement knowledge acquired and Visual Basic Applications.
- Attained an award for a saving of ₹24 Crore in GST Returns for Bosch from the Senior Vice President of Global Indirect Procurement.         
- Had a vital role in analyzing and managing automotive suppliers data for an €8M ETS (Employee Transportation Services) project for a new Bosch plant, BGSW EC 360 Park.
- Management of €20.2M worth of Purchase Order Data of Petrochemicals and Personal Protectivity Equipment as a Fresher and presentation of a Power BI Dashboard to Senior and Executive Plant Management to identify Potential and Recurring Savings.
- Created a Power BI Dashboard and **Automated Mail Notifier** to track and manage the Employee Engagement for 1300+ Employees across India for Bosch India.
- Attained an award for Employee Data Management from the Executive Vice President, Bosch GS Global.
"""
)
# Projects & Accomplishments
st.write("#")
st.subheader("**Projects**")
st.write("---")
cols = st.columns(len(Projects))
for idx, (name, link) in enumerate(Projects.items()):
    with cols[idx]:
        st.markdown(f"[{name}]({link})", unsafe_allow_html=True)