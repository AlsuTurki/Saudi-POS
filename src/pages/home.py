"""Home page shown when the user enters the application"""
import streamlit as st
from pathlib import Path





def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding="utf8")

intro_markdown = read_markdown_file("./ABOUT.md")

def app():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.markdown(intro_markdown, unsafe_allow_html=True)