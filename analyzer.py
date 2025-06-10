# File: app/modules/analyzer.py

import os
import openai
import re
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text_emotion(text):
    prompt = f"""
You are a professional emotional intelligence analyst. Analyze the following message and classify:
- Dominant Emotion (happy, sad, angry, nervous, calm, etc.)
- Professional Tone (friendly, aggressive, formal, passive-aggressive, apologetic, neutral)
- Empathy Score (scale of 1 to 10)

Message:
\"{text}\"

Respond ONLY in JSON format:
{{"emotion": "...", "tone": "...", "empathy_score": ...}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You analyze emotional tone in business communication."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    try:
        reply = response["choices"][0]["message"]["content"]
        cleaned = re.sub(r'```json|```', '', reply).strip()
        return json.loads(cleaned)
    except Exception as e:
        return {"emotion": "unknown", "tone": "unknown", "empathy_score": 5, "error": str(e)}
