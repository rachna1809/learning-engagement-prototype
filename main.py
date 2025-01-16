import streamlit as st
from datetime import datetime, timedelta

# Website Title
st.set_page_config(page_title="Learning Engagement Prototype", layout="wide")
st.title("Learning Engagement Prototype")

# Solution 1: Trigger for Next Module
st.header("1. Trigger for Next Module")
st.write("Identify users with in-progress courses and remind them to complete or advance.")

# Input Section for Triggers
with st.expander("Enter User Details"):
    progress = st.slider("Course Progress (%)", 0, 100, 50)
    last_login = st.date_input("Last Login Date", datetime.now() - timedelta(days=30))

# Generate Trigger Message
if progress < 80:
    st.success(f"Trigger Message: You're {progress}% through your course! Complete Module 1 in just 10 minutes.")
else:
    st.success(f"Trigger Message: Great work on Module 1! Start Module 2 to continue your journey.")

# Solution 2: Recommend Complementary Content
st.header("2. Recommend Complementary Content")
st.write("Suggest content that complements the user’s current learning journey.")

# Input Section for Recommendations
with st.expander("Select a Course"):
    course = st.selectbox("Course in Progress", ["Python Basics", "Data Science Intro", "ML Basics"])

# Generate Recommendations
recommendations = {
    "Python Basics": ["Hands-On Python Projects", "Python Data Types"],
    "Data Science Intro": ["Data Visualization Techniques", "Statistics for Data Science"],
    "ML Basics": ["Deep Learning Foundations", "ML Projects for Beginners"]
}
if course:
    st.info(f"Recommended: {', '.join(recommendations[course])}")

# Engagement Metrics Placeholder
st.header("3. Engagement Metrics (Placeholder)")
st.write("In a real-world application, this section would display user engagement statistics.")
st.metric("Re-Engagement Rate", "45%", "5% increase")
st.metric("CTR for Recommendations", "32%", "8% increase")
