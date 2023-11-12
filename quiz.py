# Define a list of questions, each as a dictionary with a question, options, and the correct answer
questions = [
    {
        "question": "How many second half Away goals have the OAUMFT scored in the knockout stages of the HiFL?",
        "options": ["5", "6", "2", "4"],
        "correct_answer": "2",
        "explanation": "In the knockout stages of HiFL tournament, OAU MFT have scored nine (9) second half goals (scoring 7 at their homeground)."
    },
    {
        "question": "When was the OAU Sports Council created?",
        "options": ["1956", "1986", "2001", "None of the above"],
        "correct_answer": "None of the above",
        "explanation": "My gee, me wey build the web App sef no remember. Just take am as work in progress...oti ye eh!."
    },
    {
        "question": "Which is the odd one?",
        "options": ["OluwaMicheal", "Oluwanooni", "Sido Maguire", "Sumbade Jnr"],
        "correct_answer": "Sido Maguire",
        "explanation": ("Out of the above named persons, only Sido Maguire has never been elected "
                        "\nthe Great Ife Students' Union Director of Sports unlike OluwaMicheal(2017/18), "
                        "\nOluwanooni(2022/23) and Sumbade Jnr(2023/24)")
    }
]

# Initialize variables to keep track of the current question and user's score
current_question = 0
user_score = 0

# Function to display a question
def display_question(question):
    st.write(f"**Question {current_question + 1}:** {question['question']}")
    for i, option in enumerate(question["options"]):
        option_selected = st.radio(f"Option {i + 1}:", options=question["options"])
        if option_selected == question["correct_answer"]:
            st.expander("CORRECT", question["explanation"])
        else:
            st.expander("INCORRECT", question["explanation"])

import streamlit as st

# Streamlit app
st.title("Quiz App")

# Check if the user has attempted all questions
if current_question < len(questions):
    display_question(questions[current_question])
    if st.button("Next Question"):
        current_question += 1
else:
    st.write("Quiz completed! Your score is: ", user_score)