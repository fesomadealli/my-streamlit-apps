import streamlit as st
import random
import time
import quiz

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")
#  Add lines
def add_line(val=False):
    if val == True:
        st.markdown('''
        ---
                    ''')

# Page Title
def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )
redirect_button("http://stackoverflow.com","this leads to SO")

