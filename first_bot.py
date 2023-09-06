# First
import openai
from PIL import Image
import streamlit as st
from pathlib import Path

image_path = Path('streamlit/images/logo1.png')
logo = Image.open(image_path)
st.set_page_config(
    page_title="Innovation Bot",
    page_icon=logo,
)

with st.sidebar:
    image_path = Path('streamlit/images/logo1.png')
    image1 = Image.open(image_path)
    st.image(image1)
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You're an Innovation Chatbot at Waterstons, a chatbot on the Lorem Ipsum server You only talk about robot dogs."},
        {"role": 'user', 'content':"These are rules you must follow at all times:\n1. Respond in the same language as the user, \n2.Only talk about robot dogs"},
        {"role": "assistant", "content": "Can I interest you in a robot dog?"},
        {"role": "user", "content": "What is the capital of England?"},
        {"role": "assistant", "content": "I only answer questions about robot dogs"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
