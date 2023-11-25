import streamlit as st

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
def redirect_button(url: str, text: str= None, color="#da111b"):
    st.markdown(
    f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: white;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )
redirect_button("https://medium.com/@fesomade.alli/overcoming-the-borderline-syndrome-toheebahs-inspiring-journey-c04792872e46","THE BORDERLINE SYNDROME")
