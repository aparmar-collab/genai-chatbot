import os;

from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title = "Chatbot",
    page_icon = "🤖",
    layout = "centered",
)
st.title("💬 Generative AI Chatbot")

#intitate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show chat history    
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#llm intiate
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature=0.7)        

user_prompt = st.chat_input("Ask chatbot...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant"}, *st.session_state.chat_history]
    )
    st.session_state.chat_history.append({"role": "assistant", "content": response.content})

    with st.chat_message("assistant"):
        st.markdown(response.content)
    