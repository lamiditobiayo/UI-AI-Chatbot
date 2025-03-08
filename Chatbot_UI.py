import streamlit as st
import requests

# Set up Streamlit page configuration
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stTextInput, .stTextArea {
            border-radius: 10px;
            border: 2px solid #6c63ff;
            padding: 10px;
        }
        .stButton>button {
            background-color: #6c63ff;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 8px 16px;
        }
        .stButton>button:hover {
            background-color: #5147d9;
        }
        .chat-container {
            padding: 15px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Chatbot Header
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.write("Chat with an AI-powered assistant!")

# Create a chat container
chat_container = st.container()

# User Input
user_input = st.text_input("Type your message and press Enter:", "")

# Chat Button
if st.button("Send"):
    if user_input:
        try:
            # Send request to the backend API
            response = requests.post(
                "http://127.0.0.1:5000/chat",  # Change this URL when deploying
                json={"message": user_input}
            )

            if response.status_code == 200:
                bot_response = response.json().get("response", "No response received.")
                
                # Display chat messages
                with chat_container:
                    st.markdown(f"**You:** {user_input}")
                    st.markdown(f"**Chatbot:** {bot_response}")

            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error occurred.')}")
        except Exception as e:
            st.error(f"Connection Error: {e}")
    else:
        st.warning("Please type a message before sending.")
