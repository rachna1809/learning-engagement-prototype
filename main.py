import streamlit as st
from datetime import datetime, timedelta

# App Title
st.set_page_config(page_title="Learning Engagement Prototype", layout="wide")
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
    st.subheader("Problem")
    st.write("""
    **70% of users on my learning website are not active** (not active here is defined as not logging in within the last 30 days). These inactive users can be segmented into four groups:
    """)

    # User Segments
    segments = [
        {
            "name": "Low Completers",
            "who": "20% of users who have <20% content completed",
            "why": "These users likely didn’t find value or faced barriers in engaging.",
            "how_solved": "Ineffective onboarding flow.",
            "issues": "Poor onboarding, irrelevant content, or lack of motivation."
        },
        {
            "name": "Moderate Completers",
            "who": "30% of inactive users who have 20-49% content completed",
            "why": "These users showed initial interest but didn’t stay consistent.",
            "how_solved": "Emails about new content releases are sent but are not personalized.",
            "issues": "Content fatigue, lack of reminders or nudges, or no clear progression."
        },
        {
            "name": "High Completers",
            "who": "40% of inactive users who have 50-70% content completed",
            "why": "These users engaged significantly but didn’t complete their journey.",
            "how_solved": "No emails are sent to remind them; the website shows 'continue where you left off' but lacks incentives.",
            "issues": "No incentive to continue, lack of advanced content, or poor follow-ups."
        },
        {
            "name": "Super Completers",
            "who": "10% of inactive users who have >70% content completed",
            "why": "These users are near completion and may have finished all they were interested in.",
            "how_solved": "Limited new content is available.",
            "issues": "Lack of challenge or progression."
        }
    ]

    for segment in segments:
        st.subheader(segment["name"])
        st.write(f"**Who**: {segment['who']}")
        st.write(f"**Why**: {segment['why']}")
        st.write(f"**How it's solved today**: {segment['how_solved']}")
        st.write(f"**Issues**: {segment['issues']}")

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
