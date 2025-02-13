import streamlit as st
import os
from utils.stt import speech_to_text
from utils.translate import translate_text
from utils.chatbot import get_chatbot_response
from utils.tts import text_to_speech


st.title("🎤 Real-Time Language Translation Chatbot")

# Initialize session state to track previous inputs and responses
if 'previous_input' not in st.session_state:
    st.session_state.previous_input = None
if 'previous_response' not in st.session_state:
    st.session_state.previous_response = None

# Upload or record audio
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
record_button = st.button("🎙 Record Voice")

# Handle audio input
if record_button:
    st.info("Recording... Speak now!")
    user_input = speech_to_text()
    
    if user_input:
        st.success(f"Recognized Speech: {user_input}")

        # Translate input text (only if there is valid user input)
        if user_input.strip():  # Ensure non-empty input
            translated_text = translate_text(user_input, src="en", dest="hi")
            st.write(f"🈳 Translated Text (English → Hindi): {translated_text}")

            # Check if the new question is the same as the previous one
            if user_input == st.session_state.previous_input:
                response = st.session_state.previous_response
                st.write(f"🤖 Repeating response: {response}")
            else:
                # Get chatbot response
                response = get_chatbot_response(translated_text)
                st.session_state.previous_input = user_input
                st.session_state.previous_response = response
                st.write(f"🤖 Chatbot Response: {response}")

            # Convert chatbot response to speech
            text_to_speech(response, lang="hi")
            st.audio("output.mp3", format="audio/mp3")
        else:
            st.warning("Please speak something for translation.")
    
    else:
        st.error("No speech detected. Please try again.")
