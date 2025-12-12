import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
st.title("Welcome to Data Science Dashboard")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY not found. Add it to Streamlit secrets or .env")
    st.stop()

client = OpenAI(api_key=api_key)
st.write("I'm a Data Science expert assistant!")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a Data Science expert assistant."}]

user_input = st.chat_input("Enter your Data Science query here")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["messages"])

    assistant_message = completion.choices[0].message.content
    st.session_state["messages"].append(
        {"role": "assistant", "content": assistant_message})

    with st.chat_message("assistant"):
        st.markdown(assistant_message)