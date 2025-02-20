import streamlit as st
import time
import google.generativeai as genai
from PIL import Image
import base64

# Configure Google Gemini API Key
genai.configure(api_key="AIzaSyC7op0zN_EESTSFhXGtzHRYImp5nhvDz-c")

# Custom CSS for advanced styling
st.markdown("""
    <style>
        body, .stApp {background-color: #F5C6C6 !important; color: #000000 !important;}
        .main-title {text-align: center; font-size: 45px; font-weight: bold; color: #000000 !important;}
        .sub-header {text-align: center; font-size: 28px; font-weight: bold; color: #000000 !important;}
        .stTextArea textarea {background-color: #000000 !important; color: #FFFFFF !important; border-radius: 12px;}
        .stButton button {background-color: #FF4500; color: white; font-size: 20px; border-radius: 12px;}
        .stDownloadButton button {background-color: #32CD32; color: white; font-size: 20px; border-radius: 12px;}
    </style>
""", unsafe_allow_html=True)

# Function to display animated text
def animated_text(text, speed=0.07):
    placeholder = st.empty()
    displayed_text = ""
    for letter in text:
        displayed_text += letter
        placeholder.markdown(f'<h1 class="main-title">{displayed_text} ✨</h1>', unsafe_allow_html=True)
        time.sleep(speed)

# Animated Welcome Text
animated_text("🚀 Welcome to CodeFix Pro - AI Debug & Optimize! 💡")

# Streamlit Layout
st.markdown("<h2 class='sub-header'>🤖 Smart AI-Powered Code Debugger & Enhancer</h2>", unsafe_allow_html=True)

# User Input for Buggy Code
buggy_code = st.text_area("🐞 Enter your buggy code here:", height=250)

# Function to debug code
def debug_code_with_gemini(code):
    prompt = f"Debug the following code and provide the corrected version:\n\n{code}"
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ Error in AI response."

# Function to get suggestions for improvement
def get_suggestions_with_gemini(code):
    prompt = f"Suggest improvements for the following code, focusing on best practices, performance optimization, and readability:\n\n{code}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text if response.text else "⚠️ No suggestions available."

# Processing user input
if buggy_code:
    with st.spinner("🔍 Analyzing and fixing your code... 🛠️"):
        fixed_code = debug_code_with_gemini(buggy_code)
    
    with st.spinner("✨ Enhancing your code with best practices..."):
        suggestions = get_suggestions_with_gemini(fixed_code)

    # Display Debugged Code
    st.markdown("<h2 class='sub-header'>✅ Your Debugged Code:</h2>", unsafe_allow_html=True)
    st.code(fixed_code, language="python")
    
    # Download button for Fixed Code
    st.download_button(
        label="📥 Download Corrected Code",
        data=fixed_code,
        file_name="corrected_code.py",
        mime="text/plain"
    )
    
    # Display AI Suggestions
    st.markdown("<h2 class='sub-header'>💡 Smart AI Suggestions:</h2>", unsafe_allow_html=True)
    st.write(suggestions)
