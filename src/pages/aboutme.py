
import streamlit as st
from pathlib import Path

#about project

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding="utf8")

# pylint: disable=line-too-long
def app():
    """Used to write the page in the app.py file"""
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    intro_markdown = read_markdown_file('./ABOUT.md')
    st.markdown(intro_markdown, unsafe_allow_html=True,)
