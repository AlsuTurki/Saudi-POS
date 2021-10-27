"""Home page shown when the user enters the application"""
import streamlit as st
from pathlib import Path

#about project

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding="utf8")
intro_markdown = read_markdown_file("./ABOUT.md")

# pylint: disable=line-too-long
def app():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        intro_markdown = read_markdown_file("./ABOUT.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)
