import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

MODEL_NAME = "models/gemini-1.5-flash"

st.set_page_config(
    page_title="DataPod Assistant",
    page_icon="robot",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load only the AI assistant page for managing personal data pods
with open("_pages/home.py", encoding="utf-8") as file:
    exec(file.read())
