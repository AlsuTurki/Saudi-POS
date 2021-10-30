"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries 
import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        # Drodown to select the page to run  
        st.sidebar.title("القائمة")
        page = st.sidebar.selectbox(
            'اختر الصفحة', 
            self.pages, 
            format_func=lambda page: page['title']
        )

        st.sidebar.title("Contribute")
        st.sidebar.info(
            "This an open source project and you are very welcome to **contribute** your awesome "
            "comments, questions, resources and apps as "
            "[issues](https://github.com/AlsuTurki/SaudiPointOfSales/issues) of or "
            "[pull requests](https://github.com/AlsuTurki/SaudiPointOfSales/pulls) "
            "to the [source code](https://github.com/AlsuTurki/SaudiPointOfSales). ")
            
        st.sidebar.info(
            """
            This app is maintained by Turki Alsughayyir.""")
        # run the app function     
        page['function']()