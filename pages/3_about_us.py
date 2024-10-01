import streamlit as st

# Function to set a background image
st.set_page_config(layout="wide")
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url();  /* Unsplash background image */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# CSS to make images round-shaped
def set_css_style():
    st.markdown("""
        <style>
        img {
            border-radius: 50%;
            border: 2px solid #ffffff;  /* Optional: Add a border around images */
        }
        .team-member {
            background-color: rgba(255, 255, 255, 0.8);  /* White background with transparency */
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);  /* Shadow for depth */
        }
        </style>
    """, unsafe_allow_html=True)

# Create an "About Us" page with columns and round images
def about_us():
    st.title("About Us")

    st.header("Meet the Team")
    st.write("""
    We are a group of four data enthusiasts working together on this data analysis project. Our goal is to deliver insights and solutions through effective data visualization and analysis.
    """)

    # Create a three-column layout
    cols = st.columns(3)  # Three columns for layout

    # Team Member 1: Mostafa Amin
    with cols[0]:
        st.markdown('<div class="team-member">', unsafe_allow_html=True)
        st.image("mostafa.jpg", width=150, caption="Mostafa Amin", use_column_width=False)
        st.markdown("<h5 style='color:#1E90FF;'>Mostafa Amin</h5>", unsafe_allow_html=True)  # Uniform color
        st.write("Power BI Specialist")
        if st.button("Learn More about Mostafa"):
            st.write("Mostafa specializes in crafting interactive dashboards using Power BI, delivering compelling visualizations for data insights.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Empty space in the second column
    with cols[1]:
        st.write("")  # Leave the second column empty for spacing

    # Team Member 2: Mazen Maher
    with cols[2]:
        st.markdown('<div class="team-member">', unsafe_allow_html=True)
        st.image("mazen2.jpg", width=150, caption="Mazen Maher", use_column_width=False)
        st.markdown("<h5 style='color:#1E90FF;'>Mazen Maher</h5>", unsafe_allow_html=True)  # Uniform color
        st.write("Power BI Specialist")
        if st.button("Learn More about Mazen"):
            st.write("Mazen is responsible for data visualization, contributing through detailed dashboards using Power BI.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Add space between rows
    st.write(" ")

    # Create a second row for the last two members with another three-column layout
    cols = st.columns(3)  # Three columns for layout

    # Team Member 3: Muhammad Jamal
    with cols[0]:
        st.markdown('<div class="team-member">', unsafe_allow_html=True)
        st.image("muhammad.jpg", width=150, caption="Muhammad Jamal", use_column_width=False)
        st.markdown("<h5 style='color:#1E90FF;'>Muhammad Jamal</h5>", unsafe_allow_html=True)  # Uniform color
        st.write("Data Scientist & Data Analyst")
        if st.button("Learn More about Muhammad"):
            st.write("Muhammad was responsible for data cleaning and visualization using Python, as well as performing in-depth data analysis.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Empty space in the second column
    with cols[1]:
        st.write("")  # Leave the second column empty for spacing

    # Team Member 4: Amr Mohammed
    with cols[2]:
        st.markdown('<div class="team-member">', unsafe_allow_html=True)
        st.image("amr.jpg", width=150, caption="Amr Mohammed", use_column_width=False)
        st.markdown("<h5 style='color:#1E90FF;'>Amr Mohammed</h5>", unsafe_allow_html=True)  # Uniform color
        st.write("Data Scientist & Machine Learning Engineer")
        if st.button("Learn More about Amr"):
            st.write("Amr was responsible for data cleaning and visualization using Python, focusing on preparing data for analysis.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Mission and Vision sections with backgrounds
    st.markdown("<h3 style='color:#6A5ACD;'>Our Mission</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 10px; border-radius: 10px; box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);">
        Our mission is to transform raw data into actionable insights. With diverse skills in data science, analysis, and visualization, we are committed to uncovering patterns and trends that can drive decisions.
    </div>
    """, unsafe_allow_html=True)

    st.write(" ")

    st.markdown("<h3 style='color:#6A5ACD;'>Our Vision</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 10px; border-radius: 10px; box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);">
        To leverage data as a powerful tool for solving real-world problems, inspiring businesses, and making informed decisions across different domains.
    </div>
    """, unsafe_allow_html=True)

# Run the CSS and function
set_background()
set_css_style()
about_us()
