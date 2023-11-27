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


st.markdown("""I'm thinking of putting some end-to-end sport projects or data collection exercises here (or maybe not). Though some of them are not very good/successful projects but I can just dump them here and document my journey with sports data collection and/or analysis with them — I could even write a medium post for it later. Some of the said projects include 2021 FIBA Women's Afrobasket Shotmap, NUGA2022 Basketball Shot data (Shotmap) between OAU & UNILAG, Sporting Lagos' Shotmap for some of their matches in the 2023/24 season, OAU Giantess corners from some of their matches in 2022, WAFCON2022 self collected event data for the match between Nigeria and Botswana (First Half). 

\nA good number of these projects was just me trying my hands on data collection and then daring to see if I could go end to end with some of them. I believe if Analytics survived in global sports, it should in local sports as well. I was looking for what could be the challenges and if there was any walk-around so I did some of these stuffs. I'm not even proud of some of them but it's okay. \n This App is probably going to be renamed but I currently use it to debug my other Streamlit Apps hence why it's currently called a debugger.""")