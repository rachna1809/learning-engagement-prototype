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
    
    # User Segments
    st.subheader("User Segments")
    st.write("The 70% of inactive users can be divided into four distinct groups:")

    # Segment 1
    st.markdown("### 1. Low Completers")
    st.write("""
    - **Who**: 20% of users who have completed less than 20% of their enrolled content.
    - **Why**: These users likely struggled to find value or faced barriers in engaging.
    - **Current Approach**: Ineffective onboarding flow.
    - **Issues Identified**:
        - Poor onboarding experience.
        - Irrelevant content recommendations.
        - Lack of motivation or clarity on how to proceed.
    """)

    # Segment 2
    st.markdown("### 2. Moderate Completers")
    st.write("""
    - **Who**: 30% of inactive users who have completed 20-49% of their enrolled content.
    - **Why**: These users showed initial interest but failed to sustain engagement.
    - **Current Approach**: Generic email campaigns about new content releases.
    - **Issues Identified**:
        - Generic, non-personalized communication.
        - Content fatigue from lack of variety.
        - Absence of timely nudges or reminders.
    """)

    # Segment 3
    st.markdown("### 3. High Completers")
    st.write("""
    - **Who**: 40% of inactive users who have completed 50-70% of their enrolled content.
    - **Why**: These users engaged significantly but dropped off before completing their courses.
    - **Current Approach**: Limited reminders and no advanced incentives.
    - **Issues Identified**:
        - Lack of advanced or motivating content.
        - No follow-up emails or reminders.
        - Limited incentives for returning to the platform.
    """)

    # Segment 4
    st.markdown("### 4. Super Completers")
    st.write("""
    - **Who**: 10% of inactive users who have completed more than 70% of their enrolled content.
    - **Why**: These users may have completed the content they were interested in and see little value in returning.
    - **Current Approach**: No clear progression paths or incentives to re-engage.
    - **Issues Identified**:
        - Limited availability of new, challenging content.
        - Lack of clear progression paths after completion.
        - No incentives to explore additional topics or engage further.
    """)

elif menu == "Hypothesis and Solutions":
    # Hypothesis and Solutions
    st.header("Hypothesis and Solutions")
    st.write("""
    **Hypothesis**:  
    If we deliver highly effective and personalized learning experiences for moderate and high completers, users will achieve their learning goals more efficiently by engaging with relevant content, resulting in increased engagement, satisfaction, and completion rates.
    """)
    st.subheader("Solutions")
    st.write("- Encouraging personalized nudges to continue learning content important to them.")
    st.write("- Recommending complementary content to provide additional support to complete their learning.")

elif menu == "Success Metrics":
    # Success Metrics
    st.header("Success Metrics")
    st.subheader("Re-engagement Rate")
    st.write("- Percentage of users logging in after receiving a nudge.")
    st.subheader("Engagement Metrics")
    st.write("- Time spent per session, number of sessions per week.")
    st.subheader("CTR on Recommendations")
    st.write("- Percentage of clicks on advanced content or next-step recommendations.")
    st.subheader("Completion Rate")
    st.write("- Increase in content completion percentages among targeted users.")

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
