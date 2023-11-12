import streamlit as st

from views.page1 import Page1
from views.page2 import Page2
from views.page3 import Page3

if "view" not in st.session_state:
    st.session_state.view = "page1" # Here, I am setting page 1 as the default page

if "views" not in st.session_state:
    st.session_state.views = {
        "page1": Page1(),
        "page2": Page2(),
        "page3": Page3(),
    }

st.session_state.views[st.session_state.view].render()