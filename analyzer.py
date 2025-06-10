# EmpathAI Core MVP - Advanced Version
# Structure: Multimodal-ready, clean, modular, GPT-integrated with sentiment + empathy tone classification

# File: analyzer.py

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


# File: app/modules/analyzer.py

from openai import OpenAI
import os
import openai
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text_emotion(text):
    prompt = f"""
You are a professional emotional intelligence analyst. Analyze the following message and classify:
- Dominant Emotion (happy, sad, angry, nervous, calm, etc.)
- Professional Tone (friendly, aggressive, formal, passive-aggressive, apologetic, neutral)
- Empathy Score (scale of 1 to 10)

Message:
"{text}"

Respond in JSON format: {{"emotion": ..., "tone": ..., "empathy_score": ...}}
"""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You analyze emotional tone in business communication."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    # Parse response JSON
    try:
        reply = response["choices"][0]["message"]["content"]
        cleaned = re.sub(r'```json|```', '', reply).strip()
        import json
        return json.loads(cleaned)
    except Exception as e:
        return {"emotion": "unknown", "tone": "unknown", "empathy_score": 5, "error": str(e)}
