import streamlit as st
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")  # ✅ Now 'st' is defined
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        st.error("Error connecting to speech recognition service.")
        return ""
