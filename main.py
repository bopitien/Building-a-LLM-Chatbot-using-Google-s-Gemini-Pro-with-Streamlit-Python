import os
import streamlit as st
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Gemini-Pro Interactive Chat",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Retrieve Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key is available
if not GOOGLE_API_KEY:
    st.error("API key not found! Please set up your environment correctly.")
    st.stop()

# Function to send a request to the Gemini API
def send_gemini_request(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    response = requests.post(f"{url}?key={GOOGLE_API_KEY}", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"Error {response.status_code}: {response.json()}"

# Function to reset chat
def reset_chat():
    st.session_state.messages = []

# Initialize chat session and messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar options
with st.sidebar:
    st.header("Gemini-Pro Chat Options")
    if st.button("Reset Chat"):
        reset_chat()
        st.success("Chat reset successfully!")
    st.info("✨ Use this chatbot to explore Gemini-Pro's AI capabilities.")

# Main chatbot interface
st.title("🤖 Gemini-Pro Interactive Chat")
st.subheader("Powered by Google's Gemini AI")

# Display chat history dynamically
for message in st.session_state.messages:
    role, text = message
    with st.chat_message(role):
        st.markdown(text)

# Input area for the user's prompt
user_prompt = st.chat_input("Ask me anything about AI, tech, or life!")

# Process user's input and get AI response
if user_prompt:
    # Display user's message immediately
    st.session_state.messages.append(("User", user_prompt))
    st.chat_message("User").markdown(user_prompt)

    # Send user's message to Gemini-Pro and fetch the response
    with st.spinner("Gemini-Pro is thinking..."):
        assistant_reply = send_gemini_request(user_prompt)

    # Add AI's response to the chat history and display it
    st.session_state.messages.append(("Assistant", assistant_reply))
    with st.chat_message("Assistant"):
        st.markdown(assistant_reply)

# Footer for additional interactivity
st.divider()
st.caption("💡 Tip: Follow up on Gemini-Pro's responses to explore deeper insights!")
