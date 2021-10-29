"""Home page shown when the user enters the application"""
import streamlit as st
from pathlib import Path




#about project

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding="utf8")
#intro_markdown = read_markdown_file(r"C:\Users\talsughayyir\Desktop\pos 0.4\ABOUT.md")

# pylint: disable=line-too-long
def app():
    """Used to write the page in the app.py file"""
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    title = """
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic&display=swap" rel="stylesheet" type="text/css"/>
    <style> bdi {font-family: 'IBM Plex Sans Arabic';}
    div { direction: RTL;
    .css-hi6a2p {padding-top: 0rem;}

    </style>
    <div><h2><bdi>لوحة معلومات نقاط البيع السعودية</bdi></h2></div>
    """
    st.write(title , unsafe_allow_html=True, )
    with st.spinner("Loading Home ..."):
        intro_markdown = read_markdown_file('./ABOUT.md')
        st.markdown(intro_markdown, unsafe_allow_html=True)