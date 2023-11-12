import streamlit as st

# you can change the ui by changing the view. Note that the view must be a key in the dictionary
def changeToPage1():
    st.session_state.view = "page1"

def changeToPage2():
    st.session_state.view = "page2"

def changeToPage3():
    st.session_state.view = "page3"