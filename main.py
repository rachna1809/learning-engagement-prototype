import streamlit as st
from datetime import datetime, timedelta

if menu == "About the Prototype":
    # About the Prototype Section
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">Improve Learner Engagement</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Helvetica Neue; font-size:24px;">Tell me and I forget, teach me and I may remember, involve me and I learn.</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    Personalization in learning embodies this principle, turning passive recipients into active participants by tailoring content to individual needs, preferences, and learning styles. 
    AI-powered personalization takes this further, leveraging data to analyze learner behavior, predict challenges, and deliver dynamic, adaptive content in real-time. 
    This not only enhances engagement but also boosts retention and motivation by making learning feel relevant and intuitive. For organizations, integrating AI into education ensures scalable personalization, fostering meaningful connections between learners and content, ultimately driving better outcomes.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    This prototype is an attempt to demonstrate how AI is used to target inactive users to encourage and improve engagement through personalized triggers and recommendations.
    </p>
    """, unsafe_allow_html=True)
    
    # Next Section Link
    st.markdown('<a href="#Problem and User Segments" style="font-size:16px; text-decoration:none; color:blue;">Next</a>', unsafe_allow_html=True)


# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigate",
    [
        "Problem and User Segments",
        "Hypothesis and Solutions",
        "Success Metrics",
        "Testing and Learnings",
        "Interactive Prototype",
    ],
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

elif menu == "Success Metrics":
    # Success Metrics
    st.header("Success Metrics")
    st.subheader("Re-engagement Rate")
    st.write("- 📈 **Percentage of users logging in after receiving a nudge.**")
    st.subheader("Engagement Metrics")
    st.write("- ⏱️ **Time spent per session, number of sessions per week.**")
    st.subheader("CTR on Recommendations")
    st.write("- 🖱️ **Percentage of clicks on advanced content or next-step recommendations.**")
    st.subheader("Completion Rate")
    st.write("- ✅ **Increase in content completion percentages among targeted users.**")

elif menu == "Testing and Learnings":
    # Testing and Learnings
    st.header("Testing and Learnings")
    
    st.subheader("How Was It Tested?")
    st.write("""
    To evaluate the effectiveness of personalized nudges and content recommendations, A/B testing was conducted:
    - **Control Group**: Did not receive personalized nudges or recommendations.
    - **Variant Group**: Received:
        - Personalized nudges to resume learning.
        - Recommendations for complementary content.
    - **Duration**: The test was conducted over a 4-week period to observe meaningful engagement patterns.
    """)

    st.subheader("Key Metrics Tracked")
    st.write("""
    - **Re-engagement Rate**: Percentage of users who logged in after receiving a nudge or recommendation.
    - **CTR on Recommendations**: Percentage of users who clicked on complementary content suggestions.
    - **Completion Rate**: Percentage of users who completed their in-progress courses.
    """)

    st.subheader("Model Success Metrics")
    st.write("""
    To evaluate the recommendation model's effectiveness, the following metrics were tracked:
    - **Precision@K**: Measures the relevance of the top-K recommendations.
    - **Recall@K**: Evaluates how well the model retrieves relevant recommendations from the dataset.
    - **F1 Score**: Balances precision and recall to provide an overall effectiveness score.
    - **CTR (Click-Through Rate)**: Measures user interaction with recommended content.
    """)

    st.subheader("What Did I Learn?")
    st.markdown("""
    - **Moderate Completers**:
        - Personalized nudges increased re-engagement by **15%**.
        - Recommendations drove a **12% increase** in course completion rates.
    - **High Completers**:
        - Complementary content recommendations had a **CTR of 22%**.
        - Users responded well to reminders about advanced or new content.
    - **General Learnings**:
        - Timing of nudges (e.g., sent during work hours) significantly impacted engagement.
        - Overly frequent nudges led to diminishing returns, emphasizing the need for balance.
    """)

    st.subheader("Model Learnings and Refinements")
    st.write("""
    Key insights from testing helped refine the model:
    - **Incorporating Time-Based Features**:
        - Factoring in recency improved recommendations for users with recent activity spikes.
    - **Adjusting Weighting for Popularity**:
        - Balancing personalized recommendations with popular courses increased CTR.
    - **User Segmentation for Recommendations**:
        - Providing different recommendation strategies for new vs. experienced learners boosted engagement.
    """)

    st.subheader("Data Adjustments")
    st.write("""
    Data changes implemented during the refinement process included:
    - **Enhanced Metadata**:
        - Added course tags, categories, and skill levels for better matching.
    - **User Activity Features**:
        - Added features such as last login time, course completion rates, and session durations.
    - **Filtered Outliers**:
        - Excluded users with anomalous behavior to prevent skewed recommendations.
    """)

    st.subheader("How Did I Iterate?")
    st.write("""
    Based on these learnings, I made the following changes:
    - **For Nudges**:
        - Optimized the timing and frequency of reminders.
        - Enhanced messaging to highlight user progress and the benefits of course completion.
    - **For Recommendations**:
        - Introduced more dynamic recommendations by incorporating user preferences and popular content among similar users.
    """)
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
