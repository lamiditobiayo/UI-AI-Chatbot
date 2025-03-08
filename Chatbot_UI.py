import streamlit as st
import requests
import time

# Set up Streamlit page
st.set_page_config(page_title="BGO AI Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .chat-container {
            width: 70%;
            margin: auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .user-message {
            background-color: #0056b3;
            color: white;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
            margin-left: auto;
            margin-bottom: 10px;
        }
        .bot-message {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
            max-width: 80%;
            margin-right: auto;
            margin-bottom: 10px;
        }
        .stButton>button {
            background-color: #ffcc00;
            color: black;
            border-radius: 10px;
            font-size: 16px;
            padding: 8px 16px;
        }
        .stButton>button:hover {
            background-color: #ffaa00;
        }
        .logo-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .logo-container img {
            width: 200px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: gray;
            margin-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# Display BGO logo
st.markdown("<div class='logo-container'><img src='https://your-logo-url.com/logo.png' alt='BGO Logo'></div>", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #ffcc00;'>🤖 BGO AI Chatbot</h1>", unsafe_allow_html=True)
st.write("Chat with BGO's AI-powered assistant. Type your message below!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
with st.container():
    for role, text in st.session_state.messages:
        if role == "user":
            st.markdown(f"<div class='user-message'>{text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>{text}</div>", unsafe_allow_html=True)

# User input
user_input = st.text_input("Type your message and press Enter:")

if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append(("user", user_input))

        # Simulate a typing effect
        with st.spinner("BGO AI is thinking..."):
            time.sleep(1.5)

            # Placeholder bot response (Replace with API request)
            bot_response = "Hello! I am BGO AI Chatbot. How can I assist you today?"
            st.session_state.messages.append(("bot", bot_response))

        # Refresh page to show new messages
        st.rerun()

# Footer
st.markdown("<div class='footer'>Bill Gosling Outsourcing - Powered by AI</div>", unsafe_allow_html=True)
