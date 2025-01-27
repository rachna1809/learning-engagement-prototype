import streamlit as st

# Set page configuration
st.set_page_config(page_title="Learning Engagement Prototype", layout="wide")

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "About the Prototype",
        "Challenge",
    ],
)

# Home Navigation
if menu == "Home":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">Welcome to the Learning Engagement Prototype</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Helvetica Neue; font-size:24px;">Navigate through the sections to explore the prototype.</h2>', unsafe_allow_html=True)

# About the Prototype Section
if menu == "About the Prototype":
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
    # Navigation Links
    st.markdown('<a href="#Home" style="font-size:16px; text-decoration:none; color:blue;">Home</a>', unsafe_allow_html=True)
    st.markdown('<a href="#Challenge" style="font-size:16px; text-decoration:none; color:blue;">Next</a>', unsafe_allow_html=True)

# Challenge Section
if menu == "Challenge":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">What is Our Situation?</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Helvetica Neue; font-size:24px;">70% of users on the platform have not logged in during the last 30 days.</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    We studied the behaviors of inactive users by dividing them into 4 distinctive groups based on the percentage of course completion. The patterns we identified are:
    </p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Low Completers (20%)</b>: These users completed less than 20% of the content due to poor onboarding, irrelevant content, or lack of motivation.</li>
        <li><b>Moderate Completers (30%)</b>: These users completed 20-49% but lost interest due to generic emails, content fatigue, or lack of reminders.</li>
        <li><b>High Completers (40%)</b>: These users engaged significantly (50-70% completed) but dropped off due to no follow-ups, limited advanced content, or insufficient incentives.</li>
        <li><b>Super Completers (10%)</b>: These users completed over 70% but didn’t return because of limited new content, no progression paths, or lack of challenge.</li>
    </ul>
    """, unsafe_allow_html=True)
    # Navigation Links
    st.markdown('<a href="#Home" style="font-size:16px; text-decoration:none; color:blue;">Home</a>', unsafe_allow_html=True)
    st.markdown('<a href="#Hypothesis" style="font-size:16px; text-decoration:none; color:blue;">Next</a>', unsafe_allow_html=True)
