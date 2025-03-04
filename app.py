import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

MODEL_NAME = "models/gemini-1.5-flash"

st.set_page_config(
    page_title="Nate's Portfolio",
    page_icon="desktop_computer",
    layout="wide",
    initial_sidebar_state="collapsed",  # Sidebar is now collapsed
)

# Load only the Lucy chatbot page
with open("_pages/home.py", encoding="utf-8") as file:
    exec(file.read())
