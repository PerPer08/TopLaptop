from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google API key for Generative AI
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def get_gemini_recommendation(prompt):
    """
    Queries Gemini for laptop recommendations based on user input.

    Args:
        prompt (str): The prompt containing user specifications for the laptop.

    Returns:
        str: The response from Gemini with laptop recommendations.
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Set the page configuration
st.set_page_config(page_title="TopLaptop: Ask your AI Laptop Expert")

# Header for the app
st.header("TopLaptop: AI laptop expert")

# Sidebar for collecting user inputs
with st.sidebar:
    st.header("Laptop Requirements")
    primary_use = st.selectbox(
        "Primary Use",
        ["Work", "Browsing", "Schoolwork", "Creative Tasks (Photo/Video Editing)", "Gaming", "Other"]
    )

    specific_programs = st.text_area(
        "Specific Programs (e.g., Photoshop, heavy spreadsheets)",
        "Photoshop, Microsoft Office"
    )

    portability = st.selectbox(
        "Portability",
        ["Very Important", "Somewhat Important", "Not Important"]
    )

    budget = st.slider(
        "Budget (Pesos)",
        5000, 300000, (20000, 60000)
    )


    operating_system = st.selectbox(
        "Operating System",
        ["Windows", "macOS", "ChromeOS", "Linux", "No Preference"]
    )

    battery_life = st.slider(
        "Battery Life (hours)",
        1, 24, 8
    )

    screen_size = st.selectbox(
        "Screen Size",
        ["13 inches", "14 inches", "15 inches", "17 inches"]
    )

    storage = st.selectbox(
        "Storage",
        ["256GB SSD", "512GB SSD", "1TB SSD", "1TB HDD", "2TB HDD"]
    )

    specific_features = st.multiselect(
        "Specific Features",
        ["Touchscreen", "Backlit Keyboard", "Good Quality Webcam", "Other"]
    )

    additional_info = st.text_area(
        "Additional Information",
        "Replacing an old laptop that is slow and often overheats."
    )

# Craft the prompt for Gemini based on user input
prompt = f"""
I need a laptop primarily for {primary_use}. 
It must run {specific_programs} smoothly. 
Portability is {portability} as I’ll carry it frequently, with a budget between {budget[0]}pesos and {budget[1]}pesos.
I prefer {operating_system} for its software compatibility and need at least {battery_life} hours of battery life. 
A screen size {screen_size} is ideal, with a {storage} for storage.
Specific features: {', '.join(specific_features)}
Additional info: {additional_info}
"""

# Submit button and response display
submit = st.button("Recommend a Laptop")

if submit:
    recommendation = get_gemini_recommendation(prompt)
    st.subheader("Here's your personalized laptop recommendation:")
    st.write(recommendation)
    st.markdown(
        """**Note:** Due to limitations in factual accuracy of generative models, it's recommended to double-check specifications and reviews before making a purchase."""
    )
