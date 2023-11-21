# Define a list of questions, each as a dictionary with a question, options, and the correct answer
sport_questions = [
        {
        "question_number": 1, 
        "question": "Who won the FIFA World Cup in 2018?", 
        "options": ["France", "Croatia", "Brazil", "Germany"], 
        "correct_answer": "France", 
        "explanation": "France won the 2018 FIFA World Cup."
        },

        {
        "question_number": 2, 
        "question": "Which country has the most Olympic gold medals in total?", 
        "options": ["USA", "China", "Russia", "Germany"], 
        "correct_answer": "USA", 
        "explanation": "The USA has the most Olympic gold medals overall."
        },

        {
        "question_number": 3, 
        "question": "Who holds the record for the most goals in a single NBA game?", 
        "options": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Wilt Chamberlain"], 
        "correct_answer": "Wilt Chamberlain", 
        "explanation": "Wilt Chamberlain scored 100 points in a single NBA game."
        },

        {
        "question_number": 4, 
        "question": "Which tennis player has the most Grand Slam singles titles?", 
        "options": ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams"], 
        "correct_answer": "Margaret Court", 
        "explanation": "Margaret Court holds the record for the most Grand Slam singles titles."
        },

        {
        "question_number": 5, 
        "question": "In what year did Usain Bolt set the world record for the 100m?", 
        "options": ["2008", "2012", "2016", "2020"], 
        "correct_answer": "2009", 
        "explanation": "Usain Bolt set the 100m world record in 2009."
        },

        {
        "question_number": 6, 
        "question": "Which country hosted the first modern Olympic Games?", 
        "options": ["Greece", "France", "USA", "Germany"], 
        "correct_answer": "Greece", 
        "explanation": "Greece hosted the first modern Olympic Games in 1896."
        },

        {
        "question_number": 7, 
        "question": "Who is the all-time leading scorer in the NHL?", 
        "options": ["Wayne Gretzky", "Mario Lemieux", "Jaromir Jagr", "Alex Ovechkin"], 
        "correct_answer": "Wayne Gretzky", 
        "explanation": "Wayne Gretzky is the all-time leading scorer in the NHL."
        },

        {
        "question_number": 8, 
        "question": "Which team has won the most Super Bowls in NFL history?", 
        "options": ["New England Patriots", "Pittsburgh Steelers", "San Francisco 49ers", "Dallas Cowboys"], 
        "correct_answer": "Pittsburgh Steelers", 
        "explanation": "The Pittsburgh Steelers have won the most Super Bowls."
        },

        {
        "question_number": 9, 
        "question": "Who is considered the 'Greatest of All Time' (GOAT) in boxing?", 
        "options": ["Muhammad Ali", "Mike Tyson", "Floyd Mayweather", "Sugar Ray Robinson"], 
        "correct_answer": "Muhammad Ali", 
        "explanation": "Muhammad Ali is often regarded as the greatest boxer of all time."
        },

        {
        "question_number": 10,
        "question": "Which golf course is famous for hosting The Masters tournament?", 
        "options": ["Pebble Beach", "Augusta National", "St. Andrews", "Pinehurst"], 
        "correct_answer": "Augusta National", 
        "explanation": "Augusta National hosts The Masters tournament."
        },

        {
        "question_number": 11, 
        "question": "Who won the FIFA World Cup in 2006?", 
        "options": ["Italy", "Brazil", "France", "Germany"],
        "correct_answer": "Italy", 
        "explanation": "Italy won the 2006 FIFA World Cup."
        },

        {
        "question_number": 12, 
        "question": "Which country has won the most medals in Olympic gymnastics?", 
        "options": ["USA", "China", "Russia", "Romania"], 
        "correct_answer": "USA", 
        "explanation": "The USA has won the most Olympic gymnastics medals."
        },

        {
        "question_number": 13, 
        "question": "Who is the only player to have scored 100 points in an NBA game?", 
        "options": ["LeBron James", "Kobe Bryant", "Michael Jordan", "Wilt Chamberlain"], 
        "correct_answer": "Wilt Chamberlain", 
        "explanation": "Wilt Chamberlain is the only player to score 100 points in an NBA game."
        },

        {
        "question_number": 14, 
        "question": "Which female tennis player has won the most Grand Slam singles titles?", 
        "options": ["Serena Williams", "Steffi Graf", "Martina Navratilova", "Margaret Court"], 
        "correct_answer": "Margaret Court", 
        "explanation": "Margaret Court holds the record for the most Grand Slam singles titles."
        },

        {
        "question_number": 15, 
        "question": "In what year did the Chicago Bulls win their first NBA championship?", 
        "options": ["1991", "1989", "1993", "1987"], 
        "correct_answer": "1991", 
        "explanation": "The Chicago Bulls won their first NBA championship in 1991."
        },

        {
        "question_number": 16, 
        "question": "Who is the current Formula 1 World Champion?", 
        "options": ["Lewis Hamilton", "Max Verstappen", "Sebastian Vettel", "Valtteri Bottas"], 
        "correct_answer": "Max Verstappen", 
        "explanation": "Max Verstappen is the current Formula 1 World Champion."
        },

        {
        "question_number": 17,
        "question": "Which country has won the most Rugby World Cups?", 
        "options": ["New Zealand", "South Africa", "Australia", "England"], 
        "correct_answer": "New Zealand", 
        "explanation": "New Zealand has won the most Rugby World Cups."
        },

        {
        "question_number": 18, 
        "question": "Who holds the record for the most points scored in a single NBA game?",
        "options": ["Kobe Bryant", "LeBron James", "Wilt Chamberlain", "Michael Jordan"], 
        "correct_answer": "Wilt Chamberlain", 
        "explanation": "Wilt Chamberlain scored 100 points in a single NBA game."
        },

        {
        "question_number": 19, 
        "question": "Which country has the most Olympic gold medals in swimming?", 
        "options": ["USA", "Australia", "China", "Russia"],
        "correct_answer": "USA",
        "explanation": "The USA has the most Olympic gold medals in swimming."
        },

        {
        "question_number": 20, 
        "question": "Who won the FIFA World Cup in 1998?", 
        "options": ["Brazil", "Italy", "France", "Germany"], 
        "correct_answer": "France", 
        "explanation": "France won the 1998 FIFA World Cup."
        },

        {
        "question_number": 21, 
        "question": "Which athlete has the most Olympic gold medals?", 
        "options": ["Usain Bolt", "Michael Phelps", "Carl Lewis", "Simone Biles"], 
        "correct_answer": "Michael Phelps", 
        "explanation": "Michael Phelps holds the record for the most Olympic gold medals by an athlete."
        },

        {
        "question_number": 22, 
        "question": "In what year did the NHL expand to include the Vegas Golden Knights?", 
        "options": ["2015", "2017", "2019", "2021"], 
        "correct_answer": "2017", 
        "explanation": "The Vegas Golden Knights joined the NHL in the 2017-2018 season."
        },

        {
        "question_number": 23,
        "question": "Who is the all-time leading scorer in the Premier League?", 
        "options": ["Alan Shearer", "Wayne Rooney", "Thierry Henry", "Andy Cole"],
        "correct_answer": "Alan Shearer", 
        "explanation": "Alan Shearer is the all-time leading scorer in the Premier League."
        },

        {
        "question_number": 24, 
        "question": "Which country has won the most Copa America titles?",
        "options": ["Argentina", "Brazil", "Uruguay", "Chile"],
        "correct_answer": "Uruguay", 
        "explanation": "Uruguay has won the most Copa America titles."
        },

        {
        "question_number": 25,
        "question": "Who won the Ballon d'Or in 2021?",
        "options": ["Lionel Messi", "Cristiano Ronaldo", "Robert Lewandowski", "Mohamed Salah"], 
        "correct_answer": "Lionel Messi", 
        "explanation": "Lionel Messi won the Ballon d'Or in 2021."
        },

        {
        "question_number": 26, 
        "question": "Which country has won the most Ryder Cup titles?", 
        "options": ["USA", "Europe", "Great Britain", "Australia"], 
        "correct_answer": "USA",
        "explanation": "The USA has won the most Ryder Cup titles."
        },

        {
        "question_number": 27,
        "question": "Who is the All-time leading scorer in the NBA?", 
        "options": ["LeBron James", "Kareem Abdul-Jabbar", "Kobe Bryant", "Karl Malone"], 
        "correct_answer": "LeBron James", 
        "explanation": "LeBron James is the All-time leading scorer in the NBA."
        },

        {
        "question_number": 28, 
        "question": "In what year did the FIFA Women's World Cup start?",
        "options": ["1991", "1995", "2000", "2003"], "correct_answer": "1991", 
        "explanation": "The FIFA Women's World Cup started in 1991."
        },

        {
        "question_number": 29, 
        "question": "Which country has won the most Davis Cup titles in tennis?", 
        "options": ["USA", "Spain", "Australia", "France"], 
        "correct_answer": "USA", 
        "explanation": "The USA has won the most Davis Cup titles."
        },

        {
        "question_number": 30, 
        "question": "Who is the all-time leading scorer in MLB?",
        "options": ["Barry Bonds", "Hank Aaron", "Babe Ruth", "Alex Rodriguez"],
        "correct_answer": "Barry Bonds", 
        "explanation": "Barry Bonds is the all-time leading scorer in Major League Baseball (MLB)."
        },

        {
        "question_number": 31,
        "question": "Which is the odd one?",
        "options": ["OluwaMicheal", "Oluwanooni", "Sido Maguire", "Sumbade Jnr"],
        "correct_answer": "Sido Maguire",
        "explanation": ("Out of the above named persons, only Sido Maguire has never been elected "
                        "\nthe Great Ife Students' Union Director of Sports unlike OluwaMicheal(2017/18), "
                        "\nOluwanooni(2022/23) and Sumbade Jnr(2023/24)")
        },

        {
        "question_number": 32,
        "question": "When was the OAU Sports Council created?",
        "options": ["1956", "1986", "2001", "None of the above"],
        "correct_answer": "None of the above",
        "explanation": "My gee, me wey build the web App sef no remember. Just take am as work in progress...oti ye eh!."
        },

        {
        "question_number": 33,
        "question": "Which is the odd one?",
        "options": ["OluwaMicheal", "Oluwanooni", "Sido Maguire", "Sumbade Jnr"],
        "correct_answer": "Sido Maguire",
        "explanation": ("Out of the above named persons, only Sido Maguire has never been elected "
                        "\nthe Great Ife Students' Union Director of Sports unlike OluwaMicheal(2017/18), "
                        "\nOluwanooni(2022/23) and Sumbade Jnr(2023/24)")
        }
]

# Import statements
import random
import streamlit as st

@st.cache()
def load_questions():
    list_of_questions = random.sample(sport_questions, 10)
    return list_of_questions

# Main Streamlit app
def main(refresh=False):
    if refresh:
        load_questions.clear_cache()
        new_questions = load_questions()
    else:
        st.write("E no dey work")
