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


st.markdown(""" ### NOTHING TO SEE HERE, SO DON'T BOTHER READING

So this year I met Soccermatics, Chelsea Disseldorp and Victory Ogbebor (amongst others) and I've been thinking differently. What a journey it's been since March... *whew!*

I'm thinking of putting some of my end-to-end sport projects or data collection exercises here (or maybe not). Though some of them are not very good/successful projects but I can just dump them here and document my journey with sports data collection and/or analysis with them — I could even write a medium post for it later (or maybe not)

\nSome of the said projects include **2021 FIBA Women's Afrobasket Shotmap, NUGA2022 Basketball Shot data (Shotmap) between OAU & UNILAG, Sporting Lagos' Shotmap for some of their matches in the 2023/24 season, OAU Giantess corners from some of their matches in 2022, WAFCON2022 self collected event data for the match between Nigeria and Botswana (First Half)**. I'm also currently collecting data on the **NWFL (2000—2023)**. Maybe I'll do something with that as well (or not 😔)

\nI hope one day I can build a company that doesn't just do sports media at a global scale (esp. collegiate sports) but also focuses on sports data and other cool stuff like gaming and co. I also want to build sports devices like wearables, boards and stuff (PS: I know a thing or two about Hardware). I also hope I can transform the African sports data space but at this time, I'm still building myself, who knows, maybe I'll get into Statsbomb or Opta or Wyscout (or maybe not). I could even go into sports administration — I mean, I like it, but partly because it's where you can make real changes 😄

\nA good number of these projects were just me trying my hands on data collection and then daring to see if I could go end-to-end with some of them. I believe if Analytics survived in global sports, it should in local sports or at any other level as well (even collegiate sports). I'm a big fan of Womens sports (you can probably tell if you consider the datasets I've collected or still working on) and I was looking for what could be the challenges and if there was any walk-around so I did some of these stuffs. I'm not even proud of some of them but it's okay. 

\nThis App is probably going to be renamed but I currently use it to debug my other Streamlit Apps hence it's name (debugger). As a matter of fact, the next time you reload, you may not even see this text here.

\nIncase you read this and you're disappointed or something,  that's on you cause I already told you not to bother (I even wrote it in ALL CAPS)

\nAnyway, thanks for coming to my Ted talk 🤝🏾""")