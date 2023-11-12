import streamlit as st

from utils.utils import *

class Page2():
    def __init__(self):
        self.views = []

    def render(self):
        # define UI here
        st.header("You are in Page 2")
        st.button(" Go to Page 1", use_container_width=True, on_click=changeToPage1)
        st.button(" Go to Page 3", use_container_width=True, on_click=changeToPage3)