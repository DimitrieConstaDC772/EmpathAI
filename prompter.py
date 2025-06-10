# EmpathAI Core MVP - Advanced Version
# Structure: Multimodal-ready, clean, modular, GPT-integrated with sentiment + empathy tone classification

# File: prompter.py

import streamlit as st
from app.modules.analyzer import analyze_text_emotion
from app.modules.prompter import generate_empathy_response
from app.modules.utils import load_openai_api_key
import os

st.set_page_config(page_title="EmpathAI - Intelligent Empathy Assistant", layout="centered")
st.title("🧠 EmpathAI — Real-Time Empathy & Communication Assistant")

st.markdown("""
EmpathAI helps professionals communicate with more empathy, clarity, and emotional intelligence. 
Paste a message or conversation below to get smart suggestions.
""")

# API KEY LOAD
load_openai_api_key()

# Text input
input_text = st.text_area("Paste a professional message or sentence:", height=200)

if st.button("Analyze and Suggest"):
    if input_text.strip():
        with st.spinner("Analyzing emotional tone and generating suggestions..."):
            analysis = analyze_text_emotion(input_text)
            suggestion = generate_empathy_response(input_text, analysis)

        st.subheader("🧠 Detected Emotion & Tone")
        st.json(analysis)

        st.subheader("💬 EmpathAI Suggestion")
        st.success(suggestion)
    else:
        st.warning("Please enter a message to analyze.")


# File: app/modules/prompter.py

def generate_empathy_response(text, analysis):
    emotion = analysis.get("emotion", "neutral")
    tone = analysis.get("tone", "neutral")
    empathy_score = analysis.get("empathy_score", 5)

    # Custom logic based on emotion/tone
    if tone == "aggressive" or empathy_score < 4:
        return "Try softening your message and acknowledging the other person's point of view."
    elif tone == "formal" and emotion == "sad":
        return "Consider adding a supportive statement to show understanding."
    elif tone == "neutral" and emotion == "nervous":
        return "You might help the other person feel at ease by expressing reassurance."
    elif tone == "friendly" and empathy_score >= 8:
        return "Your message already shows strong empathy — well done!"
    else:
        return "Try to rephrase with a bit more warmth or clarity to improve connection."
