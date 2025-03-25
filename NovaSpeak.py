import streamlit as st
import speech_recognition as sr
import pyttsx3
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")
  
chat_history=ChatMessageHistory()
if "chat_history" not in st.session_state:
    st.session_state.chat_history=ChatMessageHistory()

engine=pyttsx3.init()
engine.setProperty("rate",240)
recognizer=sr.Recognizer()

# Custom CSS
st.markdown("""
     <style>
        /* Full-page background */
        .stApp {
            background-color: #0a1f44 !important; /* Dark Blue */
            color: white !important;
        }

        /* Text color */
        h1, h2, h3, h4, h5, h6, p {
            color: white !important;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #d81b60 !important; /* Dark Pink */
            color: white !important;
            font-size: 18px !important;
            border-radius: 8px !important;
            padding: 10px 15px !important;
            border: none !important;
            font-weight: bold !important;
        }

        /* Sidebar Styling */
        .stSidebar {
            background-color: #09203f !important; /* Slightly darker shade of blue */
        }
        </style>
        """,
        unsafe_allow_html=True
    )




def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        st.write("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
    try:
        query=recognizer.recognize_google(audio)
        st.write(f"👂 You Said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        st.write("🤖 Sorry, I couldn't understand. Try again!")
        return ""
    except sr.RequestError:
        st.write("⚠ Speech Recognition Service Unavailable")
        return ""
prompt=PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)

def run_chain(question):
    chat_history_text="\n".join([f"{msg.type.capitalize()}:{msg.content}" for msg in chat_history.messages])
    response=llm.invoke(prompt.format(chat_history=chat_history_text, question=question))

    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)
    return response

st.title("🎤NovaSpeak: Your Personal AI Voice Assistant")
st.write("🎙 Click the button below to speak to your AI assistant!")
st.write("Developed by: Saara and Neelmani ")
if st.button("🎙 Start listening"):
    user_query=listen()
    if user_query:
        ai_response=run_chain(user_query)
        st.write(f"**You:** {user_query}")
        st.write(f"**AI:** {ai_response}")
        speak(ai_response)

st.subheader("📜 Chat History")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")
