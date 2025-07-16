import streamlit as st
from google import genai
from google.genai import types


# STREAMLIT INTERFACE

st.set_page_config(page_title="Medical Assistant Chatbot", page_icon="🩺")
st.title("🩺 Medical Assistant Chatbot")
st.write("Developed By Abdur Rehman")
# API Key Input
api_key = st.text_input("Enter your Gemini API Key:", type="password")

# Input Question
user_question = st.text_area("Ask a medical question:", placeholder="e.g., What causes a sore throat?")

if st.button("Submit") and api_key and user_question:
    try:
        # Defining The System Prompt
        system_prompt = (
            "You are a helpful and friendly medical assistant. "
            "You do not provide any medical advice that could be harmful. "
            "Always recommend users consult a licensed doctor for treatment, prescriptions, or medical decisions."
        )

        # Calling API Key
        client = genai.Client(api_key=api_key)

        # Using Gemini Model
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=system_prompt),
            contents=user_question
        )

        st.success("Response from Chatbot:")
        st.write(response.text)

    except Exception as e:
        st.error(f"An error occurred: {e}")
