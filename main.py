import streamlit as st
from datetime import datetime, timedelta

# App Title and Description
st.title("Learning Engagement Prototype")
st.markdown("""
This prototype addresses **learner engagement challenges** by using **personalized triggers** and **content recommendations**:
1. **Trigger for Next Module**: Re-engages users to resume or complete in-progress courses.
2. **Recommend Complementary Content**: Suggests related content to enhance the learning experience.

Explore the features below to see how they work!
""")

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigate", ["Home", "Trigger for Next Module", "Recommend Complementary Content"])

if menu == "Home":
    st.header("Welcome to the Learning Engagement Prototype")
    st.markdown("""
    This app demonstrates solutions to improve learner engagement:
    - **Trigger for Next Module**: Personalized nudges to help users resume their courses.
    - **Recommend Complementary Content**: Related content suggestions to complement learning.
    
    Use the navigation menu on the left to explore these features.
    """)

elif menu == "Trigger for Next Module":
    # Section: Trigger for Next Module
    st.header("1. Trigger for Next Module")
    st.write("""
    This feature identifies learners who have not interacted with the app for a while and nudges them to resume their in-progress courses. 
    Enter the user's progress and last login date to generate a personalized message.
    """)

    # Input Section
    with st.expander("Enter User Details"):
        progress = st.slider("Course Progress (%)", 0, 100, 50)
        last_login = st.date_input("Last Login Date", datetime.now() - timedelta(days=30))

    # Generate Trigger Message
    if progress < 80:
        st.success(f"Trigger Message: You're {progress}% through your course! Complete Module 1 in just 10 minutes.")
    else:
        st.success(f"Trigger Message: Great work on Module 1! Start Module 2 to continue your journey.")

elif menu == "Recommend Complementary Content":
    # Section: Recommend Complementary Content
    st.header("2. Recommend Complementary Content")
    st.write("""
    This feature analyzes a user's current course and recommends related content that complements their learning. 
    Select a course from the dropdown to see suggestions.
    """)

    # Dropdown and Recommendations
    st.subheader("Select a Course")
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

# Placeholder for engagement metrics
st.sidebar.write("Engagement Metrics (coming soon)")
