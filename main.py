if menu == "Problem and User Segments":
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
