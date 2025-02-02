import streamlit as st
import datetime

# Initialize session state for menu navigation
if "menu" not in st.session_state:
    st.session_state["menu"] = "About the Prototype"

# Sidebar Navigation
menu = st.sidebar.radio(
    "Navigate",
    [
        "About the Prototype",
        "Challenge",
        "Hypothesis",
        "Solution",
        "Measure Success",
        "Interactive Prototype",
        "Testing",
        "Learnings",
        "Refining the Model",
        "Refining the Data",
        "Iteration",
    ],
    index=[
        "About the Prototype",
        "Challenge",
        "Hypothesis",
        "Solution",
        "Measure Success",
        "Interactive Prototype",
        "Testing",
        "Learnings",
        "Refining the Model",
        "Refining the Data",
        "Iteration",
    ].index(st.session_state["menu"]),
    key="menu",
)

# -----------------------------
# 🟢 About the Prototype Section
# -----------------------------
if menu == "About the Prototype":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">Improve Learner Engagement</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-family:Helvetica Neue; font-size:24px;">Tell me and I forget, teach me and I may remember, involve me and I learn.</h2>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    Personalization in learning embodies this principle, turning passive recipients into active participants by tailoring content to individual needs, preferences, and learning styles. <br><br>
    AI-powered personalization takes this further, leveraging data to analyze learner behavior, predict challenges, and deliver dynamic, adaptive content in real-time. <br><br>
    This not only enhances engagement but also boosts retention and motivation by making learning feel relevant and intuitive. For organizations, integrating AI into education ensures scalable personalization, fostering meaningful connections between learners and content, ultimately driving better outcomes.
    </p>
    """, unsafe_allow_html=True)

# -----------------------------
# 🟢 Challenge Section
# -----------------------------
elif menu == "Challenge":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">What is Our Situation?</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
   <b> 70% of users on the platform have not logged in during the last 30 days.</b> <br><br>We studied the behaviors of inactive users by dividing them into 4 distinctive groups based on the percentage of course completion.
    </p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Low Completers (20%):</b> Less than 20% of content completed due to poor onboarding, irrelevant content, or lack of motivation.</li>
        <li><b>Moderate Completers (30%):</b> 20-49% completed but lost interest due to generic emails, content fatigue, or lack of reminders.</li>
        <li><b>High Completers (40%):</b> 50-70% completed but dropped off due to no follow-ups, limited advanced content, or insufficient incentives.</li>
        <li><b>Super Completers (10%):</b> Over 70% completed but didn’t return due to limited new content, no progression paths, or lack of challenge.</li>
    </ul>
    """, unsafe_allow_html=True)

# -----------------------------
# 🟢 Hypothesis Section
# -----------------------------
elif menu == "Hypothesis":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">What is Our Hypothesis?</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    If we deliver highly personalized and effective learning experiences tailored to moderate and high completers, then users will achieve their goals more efficiently, leading to increased engagement, higher satisfaction, and improved completion rates.<br><br><u>Rationale:</u><br>
Focusing on moderate and high completers is strategic because they already see value in the content. Moderate completers (20-49%) are easier to re-engage with targeted nudges, while high completers (50-70%) are the most likely to return with new or advanced content. Tailoring efforts to these groups maximizes engagement and completion rates efficiently.</p>
    """, unsafe_allow_html=True)

# -----------------------------
# 🟢 Solution Section
# -----------------------------
elif menu == "Solution":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">What is Our Solution?</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    <b>Targeted Nudges and Tailored Recommendations to Drive Engagement and Completion.</b><br><br>
Our solution transforms the learning experience by leveraging personalization to keep users motivated and engaged. <br><br>
    <u><b>Through targeted nudges</b></u>, we encourage learners to focus on content that aligns with their goals, fostering consistent progress.  <br><br>
    Additionally, we <u><b>offer complementary content recommendations</b></u> to provide the extra support they need to complete their learning journey successfully. <br><br>This personalized approach not only enhances engagement but also helps users achieve their goals more efficiently, driving higher satisfaction and completion rates. 
    </p>
    """, unsafe_allow_html=True)
elif menu == "Measure Success":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">How Do We Measure?</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    We track re-engagement, engagement, and completion metrics and study the impact created. And the model success metrics!
    </p>
    <table style="font-family:Arial; font-size:16px; border-collapse: collapse; width:100%; border: 1px solid black;">
        <tr>
            <th style="border: 1px solid black; padding: 8px; text-align:left; width:50%;">Business Outcomes</th>
            <th style="border: 1px solid black; padding: 8px; text-align:left; width:50%;">Model Outcomes</th>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 8px;">
                <ul>
                    <li><b>Re-engagement Rate:</b> Percentage of users logging in after receiving personalized nudges.</li>
                    <li><b>Engagement Metrics:</b> Time spent per session and the number of sessions per week to evaluate sustained interest.</li>
                    <li><b>CTR on Recommendations:</b> Click-through rate on advanced content or next-step recommendations to assess the effectiveness of tailored suggestions.</li>
                    <li><b>Completion Rate:</b> Monitoring the increase in content completion percentages among targeted users.</li>
                </ul>
            </td>
            <td style="border: 1px solid black; padding: 8px;">
                <ul>
                    <li><b>Precision@K:</b> Measures the relevance of the top-K recommendations.</li>
                    <li><b>Recall@K:</b> Evaluates how well the model retrieves relevant recommendations from the dataset.</li>
                    <li><b>F1 Score:</b> Balances precision and recall to provide an overall effectiveness score.</li>
                    <li><b>CTR:</b> User interaction with recommended content.</li>
                </ul>
            </td>
        </tr>
    </table>
    """, unsafe_allow_html=True)


# -----------------------------
# 🟢 Interactive Prototype Section (Fully Functional)
# -----------------------------
elif menu == "Interactive Prototype":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">Interactive Prototype</h1>', unsafe_allow_html=True)

    ### Feature 1: Trigger for Next Module
    st.markdown('<h2 style="font-family:Arial; font-size:24px;">Feature 1 - Trigger for Next Module</h2>', unsafe_allow_html=True)
    progress = st.slider("Your current course progress (%)", 0, 100, 50)
    last_login = st.date_input("Last login date", datetime.date.today())

    # Personalized message logic
    if progress < 80:
        st.success(f"🔔 You last logged in on {last_login}. You're {progress}% through your course. Resume now to stay on track!")
    else:
        st.info(f"🎯 Great job! You're {progress}% done. Start the next module to keep progressing!")

    ### Feature 2: Recommend a Complementary Course
    st.markdown('<h2 style="font-family:Arial; font-size:24px;">Feature 2 - Recommend a Complementary Course</h2>', unsafe_allow_html=True)
    course_options = {
        "Python for Beginners": ["Advanced Python", "Data Structures in Python"],
        "Machine Learning Basics": ["Deep Learning Intro", "ML Model Evaluation"],
        "Project Management": ["Agile Fundamentals", "Product Strategy"],
        "Cloud Computing": ["AWS for Beginners", "Azure Cloud Services"],
    }

    selected_course = st.selectbox("Select your current course", list(course_options.keys()))
    recommended_courses = course_options[selected_course]

    st.markdown(f"<p style='font-size:16px;'>📚 Recommended for you: <b>{', '.join(recommended_courses)}</b></p>", unsafe_allow_html=True)

# -----------------------------
# 🟢 Testing Section
# -----------------------------
elif menu == "Testing":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">How Did We Test It?</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    We used A/B Testing to measure engagement and effectiveness. Two groups were tested:
    </p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Control Group:</b> Did not receive personalized nudges or recommendations.</li>
        <li><b>Variant Group:</b> Received personalized nudges to resume learning and recommendations for complementary content.</li>
    </ul>
    <p style="font-family:Arial; font-size:16px;">
    The test ran for a 4-week period, observing meaningful engagement patterns and assessing the impact on user behavior.
    </p>
    """, unsafe_allow_html=True)

# -----------------------------
# 🟢 Learnings Section
# -----------------------------
elif menu == "Learnings":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">What Did We Learn?</h1>', unsafe_allow_html=True)
    st.markdown("""<p><b>Personalized nudges and content recommendations significantly boost engagement and completion rates, with optimal timing and a balanced approach being key to maintaining their effectiveness.</b></p>
    <p style="font-family:Arial; font-size:16px;">
    Key findings from our testing:
    </p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Re-engagement:</b> Personalized nudges increased re-engagement by 15%.</li>
        <li><b>Completion Rates:</b> Moderate completers achieved a 12% improvement in completion rates.</li>
        <li><b>CTR:</b> High completers demonstrated a 22% click-through rate on recommended content.</li>
    </ul>
    """, unsafe_allow_html=True)
elif menu == "Refining the Model":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">How Did We Refine the Model?</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-family:Arial; font-size:16px;">
    <b>Tailoring recommendations based on user activity, course popularity, and experience level significantly boosts engagement and click-through rates.</b>
    </p>
    <p style="font-family:Arial; font-size:16px;">
    The following insights helped us refine the model:
    </p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Time-Based Features:</b> Factoring in recent activity spikes improved recommendations for active users.</li>
        <li><b>Popularity Weighting:</b> Balancing personalized suggestions with popular courses enhanced click-through rates.</li>
        <li><b>Segmentation:</b> Different recommendation strategies for new and experienced learners increased engagement.</li>
    </ul>
    """, unsafe_allow_html=True)


elif menu == "Refining the Data":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">How Did We Refine the Data?</h1>', unsafe_allow_html=True)
    st.markdown("""<p><b>Refining data by enhancing metadata, incorporating user activity features, and filtering outliers improved the accuracy and relevance of recommendations.</b><br><br>The following insights helped us refine the model:<br></p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Enhanced Metadata:</b> Adding detailed course tags, categories, and skill levels improved matching accuracy.</li>
        <li><b>User Activity Features:</b> Integrated features like session duration, last login time, and completion rates.</li>
        <li><b>Filtered Outliers:</b> Excluded users with anomalous activity patterns to maintain reliable recommendations.</li>
    </ul>
    """, unsafe_allow_html=True)

elif menu == "Iteration":
    st.markdown('<h1 style="font-family:Arial; font-size:40px;">How Did We Iterate?</h1>', unsafe_allow_html=True)
    st.markdown(""" 
    <p style="font-family:Arial; font-size:16px;">
    <b>Adjustments were made to optimize and refine the timing and messaging of nudges, while making content recommendations more relevant and personalized based on user preferences and behaviors.</b><br><br>
    Based on these insights, I implemented the following adjustments:<br>
    </p>
    <ul style="font-family:Arial; font-size:16px;">
        <li><b>Nudges:</b> Adjusted timing and messaging to highlight user progress and benefits of course completion.</li>
        <li><b>Recommendations:</b> Factored in user preferences and popular content among similar users for better relevance.</li>
    </ul>
    """, unsafe_allow_html=True)


