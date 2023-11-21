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
st.header("**QUIZ**")
st.markdown(f"""
        *How conversant are you with OAU Sports ?
        What do you know about the history of sports on OAU campus ?*
        *How current and up-to-date are you? Test your knowledge with ten (10) randomly generated questions!*
        \n*At the end of the quiz, you can see how you rank on the leaderboard.*
        """)


# placeholders
# scorecard_placeholder = st.empty()
# def add_placeholders():
number_placeholder = st.empty()
question_placeholder = st.empty()
options_placeholder = st.empty()
results_placeholder = st.empty()

# Select Question
list_of_questions = quiz.load_questions()

# Initialize variables to keep track of the current question and user's score
user_answers = [] 
options_archive = []
user_score = 0        

scorecard_placeholder = st.empty()
add_line(True)
nl(2)

# Function to display a question
def display_questions(questions=True, answers=False):
    for i in range(len(list_of_questions)):
        current_question = i+1
        with st.container():
            number_placeholder = st.empty()
            question_placeholder = st.empty()
            options_placeholder = st.empty()
            results_placeholder = st.empty()
            expander_area = st.empty()

            # print
            number_placeholder.write(f"*Question {current_question}*")
            question_placeholder.write(f"**{list_of_questions[i].get('question')}**")
            # list of options
            options = list_of_questions[i].get("options")
            # track the selected option
            selected_option = options_placeholder.radio("",options=options)
            user_selection = options.index(selected_option)
            options_archive.append(user_selection)

            # comparing answers to track score
            if selected_option == list_of_questions[i].get("correct_answer"):
                user_answers.append(True)
            else:
                user_answers.append(False)

            if answers == True:
                # Results Feedback
                if user_answers[i] == True:
                    results_placeholder.success("CORRECT")
                else:
                    results_placeholder.error("INCORRECT")

                # Explanation of the Answer
                expander_area.write(f"*{list_of_questions[i].get('explanation')}*")
           
            nl(1)

    #  calculate score
    global user_score
    if answers == True:
        user_score += user_answers.count(True)            
        scorecard_placeholder.write(f"### **Your Final Score : {user_score}**")

        refresh = st.button("Refresh Quiz")
        if refresh:
            quiz.main(True)


# Check if the counter is not in session_state, initialize it to 0
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Main Streamlit app
def main():
    # Button to start/stop loading questions
    if st.button("START / STOP QUIZ"):
        with st.spinner("*this may take a while*"):
            time.sleep(2)
        # Toggle between True and False on each button click
        st.session_state.counter += 1
        if st.session_state.counter % 2 == 0:
            button_state = True
        else:
            button_state = False
        # checking button state
        st.write(f"Button State is {button_state}")
        display_questions(answers=button_state)

if __name__ == "__main__":
    main()
