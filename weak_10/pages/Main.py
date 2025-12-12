import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Homepage", page_icon="^", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the Homepage.")
    if st.button("Go to login page"):
        # Switch by the path relative to the main app (root). Do NOT use absolute paths.
        # From a file inside `pages/`, the main app is one level up.
        st.switch_page("../Login.py")   # back to the first page
    st.stop()

# If logged in, show dashboard content
st.title("Homepage")
st.success(f"Hello, **{st.session_state.username}**! You are logged in.")
name = st.chat_input("Enter your name here")
prompt = st.chat_input("Select your dashboard: Cybersecurity, Data science, IT")
if name:
    st.write(f"Your Name: {name}")
st.markdown("""
# Choose the Dashboard:
- Cybersecurity
- Data Science
- IT
""")
if prompt=="Cybersecurity":
    st.write("You have selected Cybersecurity Dashboard")
    st.switch_page("pages/Cybersecurity.py")
elif prompt=="Data science":
    st.write("You have selected Data Science Dashboard")
    st.switch_page("pages/Data_science.py")
elif prompt=="IT":
    st.write("You have selected IT Dashboard")
    st.switch_page("pages/IT.py")
else:
    st.write("Please select a valid dashboard from the menu on the left or type here")

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("You have been logged out.")
    st.switch_page("../Login.py")

