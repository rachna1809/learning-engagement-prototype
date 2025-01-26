import streamlit as st
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="Learning Engagement Prototype", layout="wide")

# App Title
st.title("Learning Engagement Prototype")
st.markdown("""
This prototype addresses **learner engagement challenges** by targeting inactive users and encouraging re-engagement through personalized triggers and recommendations.
""")

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigate",
    ["Problem and User Segments", "Hypothesis and Solutions", "Success Metrics", "Interactive Prototype"]
)

if menu == "Problem and User Segments":
    # Problem and User Segments
    st.header("Problem and User Segments")
    
    # Problem
    st.subheader("Problem")
    st.write("""
    **High Inactivity Rate**:  
    70% of users on the platform are inactive (not logging in during the last 30 days). This indicates significant challenges in user engagement and retention.
    """)
    
    # User Segments Table
    st.subheader("User Segments Overview")
    st.write("The 70% of inactive users can be divided into four distinct groups:")

    # Summary Table
    st.table([
        ["Segment", "Who", "Why", "Issues"],
        ["🚶 Low Completers", "20% with <20% content completed", 
         "Struggled to find value or faced barriers in engaging", 
         "Poor onboarding, irrelevant content, lack of motivation"],
        ["🏃 Moderate Completers", "30% with 20-49% content completed", 
         "Showed interest but failed to sustain engagement", 
         "Generic emails, content fatigue, no reminders"],
        ["🥇 High Completers", "40% with 50-70% content completed", 
         "Significant engagement but didn’t complete", 
         "No follow-ups, lack of advanced content, limited incentives"],
        ["🎓 Super Completers", "10% with >70% content completed", 
         "Finished content but no reason to return", 
         "Limited new content, no progression paths, lack of challenge"]
    ])

elif menu == "Hypothesis and Solutions":
    # Hypothesis and Solutions
    st.header("Hypothesis and Solutions")
    st.write("""
    **Hypothesis**:  
    If we deliver highly effective and personalized learning experiences for moderate and high completers, users will achieve their learning goals more efficiently by engaging with relevant content, resulting in increased engagement, satisfaction, and completion rates.
    """)
    
    st.subheader("Why Focus on Moderate and High Completers?")
    st.markdown("""
    - **Moderate Completers**:
        - Easier to re-engage compared to low completers.
        - They already see some value, so targeted nudges or content might work well.
    - **High Completers**:
        - They are the most likely to re-engage.
        - They already see significant value and may just need a reminder or new content.
    """)

    st.subheader("Solutions")
    st.write("- 🎯 Encouraging personalized nudges to continue learning content important to them.")
    st.write("- 🧩 Recommending complementary content to provide additional support to complete their learning.")

elif menu == "Interactive Prototype":
    # Interactive Prototype
    st.header("Interactive Prototype")
    st.subheader("1. Trigger for Next Module")
    st.write("""
    This feature identifies learners who have not interacted with the app for a while and nudges them to resume their in-progress courses. 
    Enter the user's progress and last login date to generate a personalized message.
    """)

    # Input Section for Triggers
    with st.expander("Enter User Details"):
        progress = st.slider("Course Progress (%)", 0, 100, 50)
        last_login = st.date_input("Last Login Date", datetime.now() - timedelta(days=30))

    # Generate Trigger Message
    if progress < 80:
        st.success(f"Trigger Message: You're {progress}% through your course! Complete Module 1 in just 10 minutes.")
    else:
        st.success(f"Trigger Message: Great work on Module 1! Start Module 2 to continue your journey.")

    st.subheader("2. Recommend Complementary Content")
    st.write("""
    This feature analyzes a user's current course and recommends related content that complements their learning. 
    Select a course from the dropdown to see suggestions.
    """)

    # Dropdown and Recommendations
    courses = ["Python Basics", "Data Science Intro", "ML Basics"]
    course = st.selectbox("Course in Progress", courses)

    recommendations = {
        "Python Basics": ["Hands-On Python Projects", "Python Data Types"],
        "Data Science Intro": ["Data Visualization Techniques", "Statistics for Data Science"],
        "ML Basics": ["Deep Learning Foundations", "ML Projects for Beginners"]
    }

    # Display Recommendations
    if course:
        st.success(f"Recommended Complementary Content for '{course}':")
        st.write(", ".join(recommendations[course]))
