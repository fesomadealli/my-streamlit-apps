import streamlit as st

from utils.utils import *

class Page1():
    def __init__(self):
        self.views = []

    def render(self):
        # define UI here
        st.header("You are in Page 1")
        st.button(" Go to Page 2", use_container_width=True, on_click=changeToPage2)
        st.button(" Go to Page 3", use_container_width=True, on_click=changeToPage3)
