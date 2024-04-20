import streamlit as st

def page_home():
    st.title('Counsello')
    st.write('Welcome to Counsello!')

    st.header('About Course Counseller')
    st.write('Course Counseller is a platform designed to help you discover and explore various courses across different domains. Whether you are a beginner or an experienced learner, Course Counseller provides personalized recommendations to help you achieve your learning goals.')

    # Add navbar with poll for user satisfaction with Counsello
    st.sidebar.title('User Satisfaction Poll')
    st.sidebar.subheader('Counsello')
    counsello_satisfaction = st.sidebar.radio('Are you satisfied with Counsello?', ('Yes', 'No'))

    # Submit button for Counsello poll
    if st.sidebar.button('Submit (Counsello)'):
        # Logic to save user satisfaction for Counsello
        st.write('User satisfaction for Counsello:', counsello_satisfaction)

    # Add navbar with poll for user satisfaction with College Mentors
    st.sidebar.subheader('College Mentors')
    college_mentors_satisfaction = st.sidebar.radio('Are you satisfied with College Mentors?', ('Yes', 'No'))

    # Submit button for College Mentors poll
    if st.sidebar.button('Submit (College Mentors)'):
        # Logic to save user satisfaction for College Mentors
        st.write('User satisfaction for College Mentors:', college_mentors_satisfaction)

    # Display the "Start" button
    if st.button('Start'):
        # Set session state to navigate to the user details page
        st.session_state['page'] = 'User Details'

def page_user_details():
    st.title('User Details')
    st.write('Please provide further details.')

    # Input fields for user details
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    part_time_job = st.selectbox('Do you have a part-time job?', ['Yes', 'No'])
    absence_days = st.number_input('Number of absence days', min_value=0, max_value=30, value=0)
    extracurricular_activities = st.selectbox('Do you participate in extracurricular activities?', ['Yes', 'No'])
    weekly_self_study_hours = st.selectbox('Weekly self-study hours', list(range(0, 41)))

    # Button to proceed to the next step
    if st.button('Proceed to Academic Details'):
        # Set session state to navigate to the academic details page
        st.session_state['page'] = 'Academic Details'

def page_academic_details():
    st.title('Academic Details')
    st.write('Please provide your academic details.')

    # Dropdown menu for stream selection
    stream = st.selectbox('Select Stream', ['Science', 'Commerce', 'Arts'])

    # Input fields for subject marks based on selected stream
    if stream == 'Science':
        st.write('Enter marks for Science stream subjects')
        physics_marks = st.number_input('Physics', min_value=0, max_value=100, value=0)
        chemistry_marks = st.number_input('Chemistry', min_value=0, max_value=100, value=0)
        mathematics_marks = st.number_input('Mathematics', min_value=0, max_value=100, value=0)
        biology_marks = st.number_input('Biology', min_value=0, max_value=100, value=0)
    elif stream == 'Commerce':
        st.write('Enter marks for Commerce stream subjects')
        accounts_marks = st.number_input('Accounts', min_value=0, max_value=100, value=0)
        business_studies_marks = st.number_input('Business Studies', min_value=0, max_value=100, value=0)
        economics_marks = st.number_input('Economics', min_value=0, max_value=100, value=0)
    elif stream == 'Arts':
        st.write('Enter marks for Arts stream subjects')
        history_marks = st.number_input('History', min_value=0, max_value=100, value=0)
        geography_marks = st.number_input('Geography', min_value=0, max_value=100, value=0)
        political_science_marks = st.number_input('Political Science', min_value=0, max_value=100, value=0)

    # Button to proceed
    if st.button('Proceed'):
        # Logic to proceed to the next step or generate course recommendations
        st.write('Proceeding to the next step...')

# Define a dictionary to map page names to their corresponding functions
pages = {
    'Home': page_home,
    'User Details': page_user_details,
    'Academic Details': page_academic_details
}

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

# Display the selected page
pages[st.session_state['page']]()
