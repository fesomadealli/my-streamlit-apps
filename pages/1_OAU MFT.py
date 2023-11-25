import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import glob
# import plost
import time
import io
import os

# import custom scripts
import oaumft_facts

# Global Elements
vspace = "\n"

# page layout
st.set_page_config(layout='centered', initial_sidebar_state='collapsed')

# styling the webpage
# Set custom CSS using the style.css file
def set_custom_style():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Call the function to set custom style
set_custom_style()

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
# Control endnote display per page
def display_endnote(page):
    if page == 'Home':
        st.write("**FAQ**")
        # Data Source
        with st.expander(label="Data Provider", 
                        expanded=True):
            exp_text = ("Data used for this App was made available by AlliNewsNigeria"
                        f"{vspace*2}[Contact AlliNews (Email)](mailto:allinewsnigeria@gmail.com)"
                        f"{vspace*2}[Follow AlliNews (Twitter)](twitter.com/allinewsnigeria)"
                        f"{vspace*2}[Follow AlliNews (Instagram)](instagram.com/allinewsnigeria)"
                        f"{vspace*2}[Listen to AlliNews Sports Podcasts](spotify.com/allinews-sports-podcast)")
            
            st.write(exp_text)

        with st.expander(label="Motive behind this Project?", 
                        expanded=False):
            exp_text = ("Community Value... affects real audience... educate University community.. and more...")
            st.write(exp_text)

        with st.expander(label="How was this data collected?", 
                        expanded=False):
            exp_text = ("I snatch am for hold-up...")
            st.write(exp_text)

        with st.expander(label="How was this data wrangled?", 
                        expanded=False):
            exp_text = ("With Omo and Dettol...")
            st.write(exp_text)

        with st.expander(label="Is the data public?", 
                        expanded=False):
            exp_text = ("Yes...")
            st.write(exp_text)
    else:
        nl(2)
# Customization file
def local_css(cssfile):
    with open(cssfile) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
# App Menu
with st.sidebar:
    selected = option_menu(
        menu_title="OAU MFT", #required
        options=["Home", "Dataset", "Analytics", "Featured Articles",
                 "Test Your Knowledge", "View Leaderboard", "Send Feedback", "Credits"], #required
        menu_icon="app-indicator",
        icons=["house", "database", "bar-chart", "pencil-square",
               "question-lg", "table", "chat-right", "award"],
        default_index=0
    )    
# sidebar contact
st.sidebar.markdown('''
---
Created by @fesomadealli\n
[Twitter](twitter.com/fesomadealli)
[Github](github.com/fesomadealli)
[Medium](medium.com/fesomade.alli)
                    ''')
st.sidebar.write(" ")

# Header
st.header("OAU MFT APP `v1.0`")
add_line(True)

# Placeholder will come in handy in the App
content_placeholder = st.empty()
body_placeholder = st.empty()

# layout of our landing pages of each section of the App
def set_landing_page(page_title = True):
    if page_title is False:
        content_placeholder.empty()
        body_placeholder.empty() 
    else:
        content_placeholder.empty()
        content_placeholder.header(page)
        body_placeholder.empty()

# Tracking the current page based on slection on Nav Bar
# (I used this to control what is displayed on the endnote)
page = "Home"

# Body
app_descr =(f"{vspace*2}What do you think of an App that tells you everything about your favorite sports team "
            f"and still gives you control over what information is delivered to you?"
            f"{vspace*2}Based on historical data collected about the Male Football team from 2003 to 2022 "
            f"and majoring on the tenure of the now retired veteran, Coach Chike Egbunu-Olimene (CEO), "
            f"this App covers all you need to know about the Male Football team of "
            f"Obafemi Awolowo University (recently aliased OAU Giants)."
            f"{vspace*2}**Happy Retirement CEO!**"
            f"{vspace*2}*Courtesy: 'The Conspirator'*"
            )
# Home page
set_landing_page()
body_placeholder.write(app_descr)
nl(1)

# Caching Dataset for download
@st.cache
# read the data from memory 
def read_data_from_memory():
    # Read .txt file
    csv_file = pd.read_csv("assets/OAUMFT_GOALS_2003_to_2022.csv")
    # Read .csv file
    txt_file_path = 'assets/OAUGIANTS_GAMES_2001_TO_2022_METADATA.txt'
    txt_file = " "
    with open(txt_file_path) as file:
        for line in file:
            txt_file += line
    return csv_file, txt_file

# Navigation Pages
def check_current_page():
    # Switching Pages on the Nav Bar
    if selected == "Dataset":
        dataset(True)
    if selected == "Analytics":
        analytics(True)
    if selected == "Featured Articles":
        featured_article(True)
    if selected == "Send Feedback":
        send_feedback(True)
    if selected == "Test Your Knowledge":
        test_your_knowledge(True)
    if selected == "View Leaderboard":
        view_leaderboard(True)
    if selected == "Credits":
        credits(True)
    elif selected == 'Home':
        add_line(True)
    
    # Adding Page specific feature for the endnote 
    display_endnote(page)

# functions of each page asides homepage
def dataset(val=False):
    if val==True:
        global page 
        page = "Dataset"
        set_landing_page()
        nl(1)
        st.write(f"{vspace*2} This dataset was provided by @allinewsnigeria "
                "and is publicly available."
                f"{vspace*2}You may also share further actions performed on this "
                "dataset with the brand via any of their social handles or their email address.")
        nl(2)

        download_btn = """
                <!-- Add icon library -->
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <!-- Auto width -->
                <button class="btn"><i class="fa fa-download"></i> Download Files</button>
                """
        st.markdown(download_btn, unsafe_allow_html=True)
        local_css("style.css")

        # add_line(True)

        nl(2)
        with st.expander(label="WHAT IS INCLUDED IN THE DOWNLOAD ?", 
                         expanded=False):
            exp_text = (f"{vspace*2}Downloadable files contains the **metadata** and a **csv** "
                        "of the match records in a zip file. In the spirit of fostering a data "
                        "conscious society, the dataset has been freely released so interested "
                        "enthusiasts may continue to update the records and perform further analysis.")
            nl(1)
            st.write(exp_text)
        nl(1)    
        with st.expander(label="READ METADATA", 
                         expanded=False):
            txt_file_path = 'assets/OAUGIANTS_GAMES_2001_TO_2022_METADATA.txt'
            nl(1)
            with open(txt_file_path) as file:
                for line in file:
                    st.write(line)
        nl(2)
        # # Adding Download Button
        # st.download_button(label='Download Files',
        #                    data= create_zip(),
        #                    file_name='OAUMFT_FILES_2003_TO_2022', mime='.zip', 
        #                    help='click here to download the dataset and the metadata')

def featured_article(val=False):
    if val==True:
        global page 
        page = "Featured Articles"
        set_landing_page()
        nl(1)
        st.write(f"{vspace*2}There are a few articles featured in this App "
                "and both centered around key members of the University team. "
                "First, is about the retired veteran, Chike Egbunu-Olimene (CEO) "
                "and the other on the last appointed captain by the Coach (Toheebah).")
        # add_line(True)

        nl(1)
        with st.expander(label="READ THE BIOGRAPHY OF CHIKE EGBUNU-OLIMENE (CEO)", 
                         expanded=False):
            exp_text = (f"{vspace*2}Komolafe Tolulope Joshua ([Toluano](www.twitter.com/iamtoluano)) did a story on the biography "
                        "of Coach Chike Egbunu-Olimene and zoomed in on his time at "
                        "Oba Awon Universities. His detail on the story was scattered "
                        "across his social networks, so, I have reworked the story and "
                        "compiled them for you, so you can read over six decades of Coach Chike's "
                        "life experiences in just a few minutes.")
            nl(1)
            st.write(exp_text)
            
            nl(1)
            biography_article = "Celebrating the Remarkable Journey of Coach Chike: A Legacy in Sports and Education"
            biography_url = "https://medium.com/#"
            if st.button(biography_article):
                webbrowser.open(biography_url)
            nl(1)

        with st.expander(label="READ TOHEEBAH'S JOURNEY AS AN OAU ATHLETE", 
                         expanded=False):
            exp_text = (f"{vspace*2}Adegoke Toheeb (Toheebah) was the last appointed captain "
                         "of the CEO era and this article focuses on the events peculiar to "
                         "his period as a football athlete on OAU campus.")
            nl(1)
            st.write(exp_text)
            
            nl(1)
            borderline_article = "Overcoming The Borderline Syndrome : Toheebah's Inspiring Journey"
            borderline_url = "https://medium.com/@fesomade.alli/c04792872e46"
            redirect_button(borderline_url, borderline_article)
            nl(1)

        with st.expander(label="WILL ANALYTICS THRIVE IN COLLEGIATE (WOMEN) FOOTBALL ?", 
                         expanded=False):
            exp_text = (f"{vspace*2}Giantess Action Plots.")
            nl(1)
            st.write(exp_text)
            
            nl(1)
            giantess_article = "Video Analytics In Nigerian Collegiate Sports: A Peek Into The Future of Women's Football"
            giantess_url = "https://medium.com/#"
            if st.button(giantess_article):
                webbrowser.open(biography_url)
            nl(1)

def send_feedback(val=False):
    feedback_form ="""
                    <form action="https://formsubmit.co/f2d54bc4e3d405a747ffef6941c28891" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="name" placeholder= "Your Name " required>
                        <input type="email" name="email" placeholder= "Your Email Address" required>
                        <textarea name="message" placeholder="Your Message Here.."></textarea>
                        <button type="submit">Send</button>
                    </form>
                    """
    if val==True:
        global page 
        page = "Send Feedback"
        set_landing_page()
        nl(1)
        st.write(f"{vspace*2}If you have anything to say about "
                "the App: maybe it's a correction, a question, a suggestion "
                "or anything else, kindly leave a message for me using the form below."
                f"{vspace*2}I'll appreciate your message!")
        # add_line(True)
        
        nl(1)
        st.markdown(feedback_form, unsafe_allow_html=True)
        local_css("style.css")

def test_your_knowledge(val=False):
    if val == True:
        global page
        page = "Test Your Knowledge"  
        set_landing_page()
        import quiz
        nl(1)

        st.markdown(f"""
        *How conversant are you with OAU Sports ?
        What do you know about the history of sports on OAU campus ?*
        *How current and up-to-date are you? Test your knowledge with ten (10) randomly generated questions!*
        \n*At the end of the quiz, you can see how you rank on the leaderboard.*
        
        Instructions:
        1. The questions load with all answers default to Option A, kindly
           select your answers by changing clicking on the radio button or 
           leaving it at the default (if applicable)
            
        2. The question pool contain 1000+ questions on OAU Sports cutting
           across Football (majorly), other sports and general questions.
        
        3. All Questions do not carry equal points:
           General Questions(5pts)     Women Sports(3pts)   
           Football Questions(2.5pts)  Other Sports(2.5pts)
            
        4. To upload your score to the leaderboard, you need to create an account.     
        
        """)
      
        scorecard_placeholder = st.empty()
        add_line(True)
        nl(2)

        # Initializing Session States
        if 'counter' not in st.session_state:
            st.session_state['counter'] = 0
        if 'start' not in st.session_state:
            st.session_state['start'] = False
        if 'stop' not in st.session_state:
            st.session_state['stop'] = False
        if 'refresh' not in st.session_state:
            st.session_state['refresh'] = False
        if "button_label" not in st.session_state:
            st.session_state['button_label'] = "START"
        if 'current_quiz' not in st.session_state:
            st.session_state['current_quiz'] = {}
        if 'user_answers' not in st.session_state:
            st.session_state['user_answers'] = []
        if 'grade' not in st.session_state:
            st.session_state['grade'] = 0

        # Function to update current session
        def update_session_state():
            if st.session_state.counter == 1:
                st.session_state['start'] = True
                st.session_state['button_label'] = "SUBMIT"
                st.session_state.current_quiz = random.sample(quiz.sport_questions, 10)

            elif st.session_state.counter == 2:
                # Set start to False
                st.session_state['start'] = True 
                # Set stop to True
                st.session_state['stop'] = True
                # Rename button text
                st.session_state['button_label'] = "RELOAD"

            elif st.session_state.counter == 3:
                # Deactivate start & stop by setting them to False
                st.session_state['start'] = st.session_state['stop'] = False
                # Activate refresh to True
                st.session_state['refresh'] = True
                st.session_state.clear()

        # Function to display a question
        def quiz_app():
            # create container
            with st.container():
                if (st.session_state.start):
                    for i in range(len(st.session_state.current_quiz)):
                        number_placeholder = st.empty()
                        question_placeholder = st.empty()
                        options_placeholder = st.empty()
                        results_placeholder = st.empty()
                        expander_area = st.empty()
                        
                        # Add '1' to current_question tracking variable cause python starts counting from 0
                        current_question = i+1
                        # display question_number
                        number_placeholder.write(f"*Question {current_question}*")
                        # display question based on question_number
                        question_placeholder.write(f"**{st.session_state.current_quiz[i].get('question')}**") 
                        # list of options
                        options = st.session_state.current_quiz[i].get("options")
                        # track the user selection
                        options_placeholder.radio("", options, index=1, key=f"Q{current_question}")
                        nl(1)

                        if st.session_state.stop:
                            # comparing answers to track score
                            if st.session_state[f'Q{current_question}'] == st.session_state.current_quiz[i].get("correct_answer"):
                                st.session_state.user_answers.append(True)
                            
                            else:
                                st.session_state.user_answers.append(False)

                            # Results Feedback
                            if st.session_state.user_answers[i] == True:
                                results_placeholder.success("CORRECT")
                            else:
                                results_placeholder.error("INCORRECT")

                            # Explanation of the Answer
                            expander_area.write(f"*{st.session_state.current_quiz[i].get('explanation')}*")

            # calculate score
            if st.session_state.stop:  
                st.session_state['grade'] = st.session_state.user_answers.count(True)           
                scorecard_placeholder.write(f"### **Your Final Score : {st.session_state['grade']} / {len(st.session_state.current_quiz)}**")

        # Initializing Button Text
        button = st.button(label=st.session_state['button_label'], key='button_press')

        if button:
            st.session_state.counter += 1
            update_session_state()
            with st.spinner("*this may take a while*"):
                time.sleep(2)
            st.experimental_rerun()

        nl(3)
        # Run Main App
        quiz_app()
        nl(1)

def view_leaderboard(val=False):
    if val == True:
        global page
        page = "Quiz Leaderboard"
        set_landing_page()
        import random

        # Sample data for ten users
        users = [
            {"username" : "@sidomaguire", "ATTQ": 100, "XP": 500},
            {"username" : "@unagocshege", "ATTQ": 95, "XP": 480},
            {"username" : "@drnooni", "ATTQ": 90, "XP": 450},
            {"username" : "@olakunleyy", "ATTQ": 85, "XP": 420},
            {"username" : "@stellamaris", "ATTQ": 80, "XP": 400},
            {"username" : "@kingqber", "ATTQ": 75, "XP": 380},
            {"username" : "@carlospeter", "ATTQ": 70, "XP": 360},
            {"username" : "@danielmoneyyhakimi", "ATTQ": 65, "XP": 340},
            {"username" : "@captainkesh", "ATTQ": 60, "XP": 320},
            {"username" : "@pablomicrolab", "ATTQ": 55, "XP": 300},
            {"username" : "@dfasesin4", "ATTQ": 75, "XP": 380},
            {"username" : "@toheebahh", "ATTQ": 70, "XP": 360},
            {"username" : "@babarahman", "ATTQ": 65, "XP": 340},
            {"username" : "@mullerofoau", "ATTQ": 60, "XP": 320},
            {"username" : "@slimcardi", "ATTQ": 55, "XP": 300},
            {"username" : "@ebu_bianu", "ATTQ": 75, "XP": 380},
            {"username" : "@yengibs10", "ATTQ": 70, "XP": 360},
            {"username" : "@aurora_of_giantess", "ATTQ": 65, "XP": 340},
            {"username" : "@mactarzan", "ATTQ": 60, "XP": 320},
            {"username" : "@profawolowo", "ATTQ": 55, "XP": 300},
        ]

        # Create a DataFrame from the sample data
        leaderboard = pd.DataFrame(users)

        # Function to update ranks with random delta values
        def update_ranks(dataframe):
            for _ in range(20):
                index = random.randint(0, 19)
                delta = random.randint(-5, 5)
                leaderboard.loc[index, "XP"] += delta

        leaderboard_area = st.empty()

        # Initial display of the leaderboard
        leaderboard_area.table(leaderboard)

        st.markdown(""" ATTQ ---- Attempted Questions \n\nXP ---- Points Accrued """)
        # Button to update ranks with random delta values
        if st.button("Refresh Leaderboard"):
            update_ranks(leaderboard)
            leaderboard = leaderboard.sort_values(by=["XP", "ATTQ"], ascending=False)
            leaderboard_area.table(leaderboard)

# Credits Section
def credits(val=False):
    if val == True:
        global page
        page = "Credits"
        set_landing_page()
        st.markdown(f""" {vspace*2}As with any great projet, people are of immense importance!
            In light of this, special gratitude goes out to everyone who helped out 
            in one way or another to guarantee the success of the version 1.0 of this project
            especially on the Quiz Section! In no particular order, the expanders below highlights
            all who played a critical role in the success on the project.
                                     """)
        nl(2)
        with st.expander(label = 'AlliNewsNigeria',
                         expanded = False):
            nl(1)
            st.write("*APPRECIATION FILE GOES HERE*")
            nl(1)
        with st.expander(label = 'Chibuze',
                         expanded = False):
            nl(1)
            st.write("*APPRECIATION FILE GOES HERE*")
            nl(1)
        with st.expander(label = 'Daniel Moneyy',
                         expanded = False):
            nl(1)
            st.write("*APPRECIATION FILE GOES HERE*")
            nl(1)
        with st.expander(label = 'Chief Chike Egbunu-Olimene',
                         expanded = False):
            nl(1)
            st.write("*APPRECIATION FILE GOES HERE*")
            nl(1)
        with st.expander(label = 'Coach Fasugba Toyin',
                         expanded = False):
            nl(1)
            st.write("*APPRECIATION FILE GOES HERE*")
            nl(1)
        with st.expander(label = 'Group of Coaches, Old Players etc.',
                         expanded = False):
            nl(1)
            st.write("*APPRECIATION FILE GOES HERE*")
            nl(1)

# Analytics Section!
def analytics(val=False):
    if val==True:
        global page 
        page = "Analytics"
        set_landing_page(page_title=False)
        selected = option_menu(
            menu_title="Analytics", #required
            options=["All Time", "Head-to-Head", "Competitions", "DYKs"], #required
            menu_icon="bar-chart",
            icons=["graph-down", "people", "trophy", 'blockquote-right'], #"pie-chart"
            default_index=3,
            orientation="horizontal")

        # import plot script
        import plot_functions

        # functions of each nav page
        def all_time():
            # Default seting for Opponent selection
            select_opponent = "All_teams"
            # Column availability for dropdowns
            disable_col1 = disable_col2 = disable_col3 = False
            with st.container():
                # Create a dropdown select box
                selected_option = st.selectbox("Select an option:", 
                                              ["Honors Won", "Form Guide", "Games Played",
                                               "Goals Chart", "Match Results", "Teams Faced"])
                nl(1)

                with st.container():
                    # ---- HONORS WON ----
                    if selected_option == "Honors Won":
                            plot_functions.display_plot(plot_type="Honors Won")
                            nl(1)

                    # ---- MATCH RESULTS ----
                    elif selected_option == "Match Results":
                        col1, col2, col3 = st.columns(3)
                        # for args/parameters in each plot functions
                        params = {}
                        with col1:
                            selected_games = st.selectbox("Select Games", 
                                                          options=["All Matches", "Home Matches"],
                                                          disabled=disable_col1)  
                        with col3:
                            selected_plot = st.selectbox("Select Stat", 
                                                         options=["Result Percentages", "Result Correlation", "Runs"],
                                                         disabled=disable_col3)
                        with col2:
                            if selected_plot == "Result Correlation":
                                disable_col2 = True
                            selected_period= st.selectbox("Select Period", 
                                                          options=["Full Time", "First Half", "Second Half"],
                                                          disabled=disable_col2)
    
                        # Adding Filters
                        # checking data range
                        if selected_games == "All Matches":
                            select_range = "All_Games"
                        elif selected_games == "Home Matches":
                            select_range = "Home_Games"
                        # checking period
                        if selected_period == "Full Time":
                            select_period = "FTR"
                        if selected_period == "First Half":
                            select_period = "HTR"
                        if selected_period == "Second Half":                                                   
                            select_period = "SHR"
                        
                        # checking plot type
                        if selected_plot == "Result Percentages":
                            params.update({'select_opponent' : select_opponent, 
                                           'select_period' : select_period, 
                                           'select_range' : select_range}) 
                        
                        elif selected_plot == "Result Correlation":
                            params.update({'select_range' : select_range})
                        
                        elif selected_plot == "Runs":
                            with col3:
                                run_type = st.selectbox("Select Run Type",
                                                        options=["Unbeaten Runs", "Winning Runs",
                                                                 "Draw Runs", "Losing Runs"])
                            if run_type == "Unbeaten Runs":
                                streak_type = "Unbeaten_Run"
                            elif run_type == "Winning Runs":
                                streak_type = "Win_Streak"
                            elif run_type == "Draw Runs":
                                streak_type = "Draw_Streak"
                            elif run_type == "Losing Runs":
                                streak_type = "Loss_Streak"

                            params.update({'streak_type' : streak_type,
                                           'select_range' : select_range,
                                           'select_period' : select_period,
                                           'run_type' : run_type})
                        # Proceed to actually plotting the viz
                        plot_functions.display_plot(plot_type="Match Results", 
                                                    plot_alt=selected_plot, 
                                                    args=params) 
                        nl(1)      

                    # ---- GAMES PLAYED ----
                    elif selected_option == "Games Played":
                            plot_functions.display_plot(plot_type="Games Played")
                            nl(1)
                    
                    # ---- GOALS CHART ----
                    elif selected_option == "Goals Chart":
                        col1, col2, col3 = st.columns(3)
                        # for args/parameters in each plot functions
                        params = {}
                        with col1:
                            selected_games = st.selectbox("Select Games", 
                                                          options=["All Matches", "Home Matches"],
                                                          disabled=disable_col1)
                        with col3:
                            selected_plot = st.selectbox("Select Stat", 
                                                         options=["Goals Ratio", "Goals Allowed (Top 10)", 
                                                                  "Goals For (Top 10)", "Common Scorelines", 
                                                                  "Goals Correlation"],
                                                         disabled=disable_col3)
                        with col2:
                            if (selected_plot == "Goals Correlation" or selected_plot == "Goals Allowed (Top 10)" or selected_plot == "Goals For (Top 10)"):
                                disable_col2 = True
                            selected_period = st.selectbox("Select Period", 
                                                            options=["Full Time", "First Half", "Second Half"],
                                                            disabled=disable_col2) 
                        
                        # Adding Filters
                        # checking data range
                        if selected_games == "All Matches":
                            select_range = "All_Games"
                        elif selected_games == "Home Matches":
                            select_range = "Home_Games"
                        # checking period
                        if selected_period == "Full Time":
                            select_period = "FTR"
                        if selected_period == "First Half":
                            select_period = "HTR"
                        if selected_period == "Second Half":                                                   
                            select_period = "SHR"
                        
                        # checking plot type
                        if selected_plot == "Goals Ratio":
                            # Since we are running All Time Analysis
                            # We need to set the opponent to `None`
                            select_opponent = None
                            # The above is based on the behavior of the 
                            # Goals_Plot() function which runs analysis
                            # against All_teams by default.
                            
                            # New dropdown selectbox for extra filter
                            with col3:
                                selected_outcome = st.selectbox("Filter by Match Outcome",
                                                                options=["All Outcomes", "Wins", 
                                                                         "Draws", "Losses"],
                                                                disabled=False)
                            # adjusting for the enlisted outcomes
                            if selected_outcome == "All Outcomes":
                                select_outcome = None # We set this to `None` in order to make it equivalent to the 
                                                      # default All_Outcomes selection which the Goals_Plot() runs
                            elif selected_outcome == "Wins":
                                select_outcome = "W" 
                            elif selected_outcome == "Draws":
                                select_outcome = "D"
                            elif selected_outcome == "Losses":
                                select_outcome = "L" 
                            # checking outcome filters
                            if select_range == "All_Games":
                                if selected_outcome != "All Outcomes":
                                    select_category = "Per_Outcome_All_Games"
                                else:
                                    select_category = "All_Time"        
                            if select_range == "Home_Games":
                                    if selected_outcome != "All Outcomes":
                                        select_category = "Per_Outcome_Homeground_Fixtures"
                                    else:
                                        select_category = "Homeground_Fixtures"
                            # updating the dictionary
                            params.update({'select_opponent' : select_opponent, 
                                           'select_period' : select_period,
                                           'select_category' : select_category, 
                                           'select_outcome' : select_outcome})  

                        if selected_plot == "Goals Allowed (Top 10)":
                            params.update({'select_range' : select_range})

                        if selected_plot == "Goals For (Top 10)":
                            params.update({'select_range' : select_range})

                        elif selected_plot == "Common Scorelines":
                            params.update({'select_opponent' : select_opponent, 
                                           'select_period' : select_period, 
                                           'select_range' : select_range}) 
                            
                        elif selected_plot == "Goals Correlation":
                            params.update({'select_range' : select_range})
                        
                        # Proceed to actually plotting the viz
                        plot_functions.display_plot(plot_type="Goals Chart", 
                                                    plot_alt=selected_plot, 
                                                    args=params) 
                        nl(1)                              

                    # ---- FORM GUIDE ----
                    elif selected_option == "Form Guide":
                        # for args/parameters in each plot functions
                        params = {}
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            selected_games = st.selectbox("Select Games", 
                                                          options=["All Matches", "Home Matches"])
                        with col2:
                            selected_period = st.selectbox("Select Period", 
                                                           options=["Full Time", "First Half", "Second Half"])
                        
                        # checking range
                        if selected_games == "All Matches":
                            select_range = 'All_Games'
                        elif selected_games == "Home Matches":
                            select_range = 'Home_Games'
                        # checking period
                        if selected_period == "Full Time":
                            select_period = "FTR"
                        if selected_period == "First Half":
                            select_period = "HTR"
                        if selected_period == "Second Half":                                                   
                            select_period = "SHR" 
                        # updating the dictionary
                        params.update({'select_opponent' : select_opponent,
                                       'select_range' : select_range, 
                                       'select_period' : select_period}) 
                        
                        # Proceed to actually plotting the viz
                        plot_functions.display_plot(plot_type="Form Guide", args=params)
                        nl(1)

                    # ---- TEAMS FACED ----                    
                    elif selected_option == "Teams Faced":
                        plot_functions.display_plot(plot_type="Teams Faced")
                        nl(1)
                    
                    # Text under button to inform user of currently selected item
                    st.write(f"You Selected **{selected_option}**")
                    
                nl(1)                    

        def head_to_head():
            # Column availability for dropdowns
            # disable_col1 = disable_col2 = disable_col3 = False
            goals_df = plot_functions.load_data(pref_df="goals")
            opp_var = goals_df.Opponent.to_list()
            list_of_opponents = sorted(list(set(opp_var)))

            nl(1)
            with st.container():
                col1, col2 = st.columns(2)
                # for args/parameters in each plot functions
                params = {}
                with col1:
                    # Create a dropdown select box
                    select_opponent = st.selectbox("Select Opponent", 
                                                    options=list_of_opponents)
                    # Create a dropdown select box
                    selected_plot= st.selectbox("Select Stat", 
                                                options=["Result Percentages", "Form Guide",
                                                         "Goals Ratio", "Common Scorelines"]) 
                    # Select Range of Games
                    selected_games = st.selectbox("Select Games", 
                                                  options=["All Matches", "Home Matches"],
                                                  disabled=False)  
                    #  Select Period
                    selected_period= st.selectbox("Select Period", 
                                                  options=["Full Time", "First Half", "Second Half"],
                                                  disabled=False)
                    
                # Control the availability of the tournament filter
                if (selected_plot == "Form Guide") or (selected_plot == "Goals Ratio"):
                    disable_sub_col2 = False
                else:
                    disable_sub_col2 = True

                # Control the availability of the match outcome filter
                if (selected_plot != "Goals Ratio"):
                    disable_sub_col1 = True
                else:
                    disable_sub_col1 = False

                # specifying the sub-columns
                sub_col1, sub_col2, sub_col3, sub_col4 = st.columns(4)
                with sub_col1:
                    selected_outcome = st.selectbox("Filter by Match Outcome",
                                                    options=["All Outcomes", "Wins", 
                                                             "Draws", "Losses"],
                                                    disabled=disable_sub_col1)
               
                with sub_col2:
                    comp_var = goals_df.CompGroup.to_list()
                    list_of_comps = sorted(list(set(comp_var)))
                    list_of_comps.append("All Competitions")
                    selected_comp = st.selectbox("Filter by Tournament",
                                                 options=list_of_comps,
                                                 index= len(list_of_comps)-1,
                                                 disabled=disable_sub_col2)
                    
                with col2:
                    # Print H2H summary text
                    summary = plot_functions.get_All_time_record(select_opponent=select_opponent)
                    
                    # Create a DataFrame from the dictionary
                    df = pd.DataFrame.from_dict(summary, orient='index')
                    # Set the column name to "Summary" for the first column
                    df.columns = ['H2H SUMMARY']
                    # Display the DataFrame in a Streamlit table
                    st.table(df)

                # checking selected category
                if selected_plot == "Goals Ratio":
                    select_category = "Per_Opponent"
                else:
                    select_category = None
                # checking range of games involved
                if selected_games == "All Matches":
                    select_range = "All_Games"
                elif selected_games == "Home Matches":
                    select_range = "Home_Games" 
                # checking period
                if selected_period == "Full Time":
                    select_period = "FTR"
                if selected_period == "First Half":
                    select_period = "HTR"
                if selected_period == "Second Half":
                    select_period = "SHR"  
                # Adjust for outcomes
                if selected_outcome == "Wins":
                    select_outcome = "W"
                elif selected_outcome == "Draws":
                    select_outcome = "D"
                elif selected_outcome == "Losses":
                    select_outcome = "L"
                else:
                    select_outcome = None #"All_Outcomes" 
                #  Adjust for selected competitions
                if selected_comp == "All Competitions":
                    select_comp = None
                else:
                    select_comp = selected_comp

                params.update({'select_opponent' : select_opponent,
                               'select_range' : select_range,
                               'select_period' : select_period,
                               'select_outcome' : select_outcome,
                               'select_comp' : select_comp,
                               'select_category' : select_category,
                               'select_edition' : None})
                # Proceed to actually plotting the viz
                plot_functions.display_plot(plot_type="Head-to-Head", 
                                            plot_alt=selected_plot, 
                                            args=params) 
                # Text under button to inform user of currently selected item
                st.write(f"You Selected **{select_opponent}**")
                    
                nl(1) 
        def per_comp():
            # Column availability for dropdowns
            disable_comp = disable_edtn = disable_gms = disable_outcome = False
            goals_df = plot_functions.load_data(pref_df="goals")
            h_games = plot_functions.load_data(pref_df="home_games")
            comp_var = goals_df.CompGroup.to_list()
            list_of_comps = sorted(list(set(comp_var)))
            list_of_comps.append("All Tournaments")
            default_tournament = len(list_of_comps)-1 #select All Tournaments by default

            nl(1)
            with st.container():
                col1, col2 = st.columns(2)
                # for args/parameters in each plot functions
                params = {}
                with col1:
                    # Create a dropdown select box
                    selected_plot= st.selectbox("Select Stat", 
                                                options=["Result Aggregate", "Form Guide",  
                                                         "Goals Ratio", "Common Scorelines"]) 
                    # checking selected category
                    if selected_plot == "Result Aggregate":
                        disable_comp = disable_edtn = disable_gms = disable_outcome = True

                    #  checking selected category
                    if selected_plot == "Goals Ratio":
                        select_opponent = None
                        list_of_comps.pop()
                        default_tournament = 2 #select NUGA by default
                        select_category = "Per_Tournament"
                        disable_gms = True
                    else:
                        select_category = None

                    # Create a dropdown select box
                    selected_comp = st.selectbox("Select Tournament", 
                                                 options=list_of_comps,
                                                 index=default_tournament,
                                                 disabled=disable_comp)
                    # Create a dropdown select box
                    if selected_comp != "All Tournaments":
                        temp_df = goals_df[(goals_df.CompGroup == selected_comp)]
                        temp_df.reset_index()
                        edtn_var = temp_df.Competition.to_list()
                        list_of_edtns = sorted(list(set(edtn_var)))
                        list_of_edtns.append("All Editions")
                        default_selection = len(list_of_edtns)-1
                    else:
                        list_of_edtns = ["All Editions"]
                        default_selection = 0 #index of single item list

                    if (selected_plot == "Form Guide") or (selected_plot == "Common Scorelines"):
                        disable_edtn = disable_outcome = True
                    selected_edition= st.selectbox("Select Edition", 
                                                   options=list_of_edtns,
                                                   index=default_selection,
                                                   disabled=disable_edtn) 
                    #  Select Period
                    selected_period= st.selectbox("Select Period", 
                                                  options=["Full Time", "First Half", "Second Half"],
                                                  disabled=False)
                
                # specifying the sub-columns
                sub_col1, sub_col2, sub_col3, sub_col4= st.columns(4)    
                with sub_col1:
                    # Select Range of Games
                    selected_games = st.selectbox("Select Games", 
                                                  options=["All Matches", "Home Matches"],
                                                  disabled=disable_gms)
                with sub_col2:
                    if selected_plot == "Goals Ratio":
                        if selected_edition != "All Editions":
                            disable_outcome = True
                            select_category = "Per_Comp_Edition"
                            select_edition = selected_edition
                            # # Shred Edition of certain formattings
                            # select_edition = select_edition.replace("'", r"\\'")

                    #  Select Match Outcome
                    selected_outcome = st.selectbox("Select Outcome",
                                                    options=["All Outcomes", "Wins", 
                                                             "Draws", "Losses"],
                                                    disabled=disable_outcome)  
                    
                # checking selected competition
                if selected_comp != "All Tournaments":
                    select_comp = selected_comp
                else:
                    select_comp = None 
                # checking selected editions
                if selected_edition != "All Editions":
                    select_edition = selected_edition
                else:
                    select_edition = None
                    
                with col2:
                        # Print Comp summary text
                        summary = plot_functions.get_Competition_record(select_comp=select_comp,
                                                                        select_edition=select_edition)
                        if type(summary) == str:
                            st.write(summary)
                        else:  
                            # Create a DataFrame from the dictionary
                            df = pd.DataFrame.from_dict(summary, orient='index')
                            # Set the column name to "Summary" for the first column
                            df.columns = ['COMPETITION RECORD']
                            # Display the DataFrame in a Streamlit table
                            st.table(df)
               
                # adjusting goals ratio by Editions
                # if selected_plot == "Goals Ratio":
                #     if selected_edition != "All Editions": 
                #         select_category = "Per_Comp_Edition"
                    
                if selected_plot == "Form Guide":
                    select_opponent = "All_teams"
                    if selected_comp != "All Tournaments":
                        stack = 10
                    else:
                        stack = 15
                else:
                    select_opponent = None
                    stack = None
                if selected_plot == "Common Scorelines":
                    select_opponent = "All_teams"
                    
                # checking range of games involved
                if selected_games == "All Matches":
                    select_range = "All_Games"
                elif selected_games == "Home Matches":
                    select_range = "Home_Games" 
                # checking period
                if selected_period == "Full Time":
                    select_period = "FTR"
                if selected_period == "First Half":
                    select_period = "HTR"
                if selected_period == "Second Half":
                    select_period = "SHR"  
                # Adjust for outcomes
                if selected_outcome == "Wins":
                    select_outcome = "W"
                elif selected_outcome == "Draws":
                    select_outcome = "D"
                elif selected_outcome == "Losses":
                    select_outcome = "L"
                else:
                    select_outcome = None #"All_Outcomes"

                # Adjusting parameters accordingly
                params.update({'select_opponent' : select_opponent,
                               'select_range' : select_range,
                               'select_period' : select_period,
                               'select_outcome' : select_outcome,
                               'select_comp' : select_comp,
                               'select_category' : select_category,
                               'select_edition' : select_edition,
                               'stack' : stack})
                
                # Proceed to actually plotting the viz
                plot_functions.display_plot(plot_type="Competitions", 
                                            plot_alt=selected_plot, 
                                            args=params) 
        def dyk():
            nl(1)
            # create container
            container = st.container()
            nl(1)
            
            with container:
                oaumft_facts.display_random_fact()  
            add_line(True)           
            
            nl(1)
            with st.expander(label="WHAT ARE DYKs ?", expanded=False):
                st.markdown("""DYKs are 60 things you may not know about the OAU MFT.""")
            nl(1)
            with st.expander(label="DISCLAIMER", expanded=False):
                st.markdown("""
                    ***DISCLAIMER**: The report gotten from using the features on the other Analytics 
                    pages is of a higher integrity than the excerpts dropped here. Therefore, 
                    should you have anything to inspect or verify, you may adjust the settings on the 
                    other pages. For further inspection or verification, kindly DYOR. You may start by downloading the 
                    data provided (or otherwise).*
                            """)
            
        # page specific programs for different 
        # sections of the Analytics Page
        if selected == "DYKs":
            dyk()
        if selected == "All Time":
            all_time()
        if selected == "Head-to-Head":
            head_to_head()
        if selected == "Competitions":
            per_comp()

        
# track user navigation
check_current_page()
