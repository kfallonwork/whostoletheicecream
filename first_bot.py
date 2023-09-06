# First
import openai
from PIL import Image
import streamlit as st
from pathlib import Path

image_path = Path('streamlit/images/logo.png')
logo = Image.open(image_path)
st.set_page_config(
    page_title="Innovation Bot",
    page_icon=logo,
)


image_path = Path('streamlit/images/banner1.png')
image1 = Image.open(image_path)
st.image(image1)
st.markdown("Welcome to the Waterstons Innovation bot! This chatbot will answer all of your queries relating to robot dogs.")

st.title("") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You're an Innovation Chatbot at Waterstons, a chatbot on the Lorem Ipsum server You only talk about robot dogs."},
        {"role": 'user', 'content':"These are rules you must follow at all times:\n1. Respond in the same language as the user, \n2.Only talk about robot dogs"},
        {"role": "user", "content": "What is the capital of England?"},
        {"role": "assistant", "content": "I only answer questions about robot dogs"},
    ]

#for msg in st.session_state.messages:
st.chat_message("assistant").write("Can I interest you in a robot dog?")

if prompt := st.chat_input():

    openai.api_key = st.secrets.api_credentials.api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
