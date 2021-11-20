"""Main module for the streamlit app"""
import streamlit as st
from multipage import MultiPage
from src.pages import home, about, posbycity, posbysector,histposbysector


st.set_page_config(
    page_title="نقاط البيع السعودية")    


# Create an instance of the app 
app = MultiPage()

# Title of the main page
#st.title("لوحة معلومات نقاط البيع السعودية")

# Add all your applications (pages) here
app.add_page("الصفحة الرئيسة", home.app)
app.add_page("تقنيات المشروع", about.app)
app.add_page("نقاط البيع الاسبوعية لكل مدينة", posbycity.app)
app.add_page("نقاط البيع الاسبوعية لكل قطاع",posbysector.app)
app.add_page("نقاط البيع الشهرية لكل قطاع",histposbysector.app)




# The main app
app.run()