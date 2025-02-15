import streamlit as st
import os
from utils.stt import speech_to_text
from utils.translate import translate_text
from utils.chatbot import get_chatbot_response
from utils.tts import text_to_speech

st.title("🌍 Multi-Language Real-Time Translation Chatbot")

# Language options
language_options = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "Japanese": "ja"
}

# Dropdown for selecting input and output languages
input_language = st.selectbox("Select Input Language", list(language_options.keys()))
output_language = st.selectbox("Select Output Language", list(language_options.keys()))

# Get language codes
input_lang_code = language_options[input_language]
output_lang_code = language_options[output_language]

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload or record audio
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
record_button = st.button("🎙 Record Voice")

# Handle audio input
if record_button:
    st.info("Recording... Speak now!")
    user_input = speech_to_text()

    if user_input:
        st.success(f"Recognized Speech: {user_input}")

        # Translate input text if the input language is not English
        if input_lang_code != "en":
            user_input = translate_text(user_input, src=input_lang_code, dest="en")
            st.write(f"🈳 Translated to English: {user_input}")

        # Get chatbot response in English
        response = get_chatbot_response(user_input)

        # Translate chatbot response if output language is not English
        if output_lang_code != "en":
            translated_response = translate_text(response, src="en", dest=output_lang_code)
            st.write(f"🤖 Chatbot Response ({output_language}): {translated_response}")
        else:
            translated_response = response
            st.write(f"🤖 Chatbot Response (English): {translated_response}")

        # Store chat history
        st.session_state.chat_history.append((user_input, translated_response))

        # Convert chatbot response to speech in the selected output language
        text_to_speech(translated_response, lang=output_lang_code)
        st.audio("output.mp3", format="audio/mp3")

    else:
        st.error("No speech detected. Please try again.")

# Display chat history
st.subheader("📝 Chat History")
for i, (user_msg, bot_msg) in enumerate(st.session_state.chat_history):
    st.write(f"**You:** {user_msg}")
    st.write(f"**Bot:** {bot_msg}")
    st.write("---")  # Separator for readability
