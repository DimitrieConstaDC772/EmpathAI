# File: app/modules/utils.py

import os
import openai
import streamlit as st

def load_openai_api_key():
    """
    Loads the OpenAI API key from environment variables and initializes the OpenAI client.
    Displays a warning if the key is missing.
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        st.warning("⚠️ OPENAI_API_KEY not found in environment variables. Please set it to use EmpathAI.")
    else:
        openai.api_key = key
