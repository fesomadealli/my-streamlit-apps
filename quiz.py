# Define a list of questions, each as a dictionary with a question, options, and the correct answer
sport_questions = [
        {
        "question_number": 1, 
        "question": "How many OAU football athletes have won MOTM Awards in HiFL fixtures played away from Home?",
        "options": ["Three", "Four", "Five", "Six"],
        "correct_answer": "Four",
        "explanation": "Four OAU football athletes have won MOTM Awards in HiFL fixtures played away from Home: Oripelaye Kehinde, Afolabi Adekola, Adeyemi Opeyemi, and Olaniyi Muyiwa."
        },

        {
        "question_number": 2, 
        "question": "In which year did the OAU MFT concede 3 goals in a match against the University of Agriculture, Makurdi?",
        "options": ["2017", "2018", "2019", "2020"],
        "correct_answer": "2018",
        "explanation": "OAU MFT conceded 3 goals in a match in four different matches during CEO's time at the helm, and two of those were against the University of Agriculture, Makurdi. One such match was in HiFL2018 semifinals (first-leg) in Ile-Ife."
        },

        {
        "question_number": 3, 
        "question": "How many Finals did the OAU MFT lose (in regular time) in the period between 2003-2022?",
        "options": ["0", "1", "2", "3"],
        "correct_answer": "1",
        "explanation": "The OAU MFT only lost 1 out of 5 Finals (in regular time) in the period between 2003-2022, and it was the NUGA 2007 Finals vs. UNIMAID in Maiduguri."
        },

        {
        "question_number": 4, 
        "question": "How many times did Team UI score a goal in their two visits to the OAU MFT homeground between 2003-2022?",
        "options": ["0", "1", "2", "3"],
        "correct_answer": "0",
        "explanation": "Team UI never scored a goal in any of their two visits to the OAU MFT homeground (in competitions) between 2003-2022."
        },

        {
        "question_number": 5, 
        "question": "What are the records for most goals scored and conceded per match in all competitions (2003-2022)?",
        "options": ["Most Goals Conceded: 2, Most Goals Scored: 4", "Most Goals Conceded: 3, Most Goals Scored: 6", "Most Goals Conceded: 4, Most Goals Scored: 8", "Most Goals Conceded: 5, Most Goals Scored: 7"],
        "correct_answer": "Most Goals Conceded: 3, Most Goals Scored: 6",
        "explanation": "The records for most goals scored and conceded per match in all competitions are: Most Goals Conceded in a match - 3, Most Goals Scored in a match - 6."
        },

        {
        "question_number": 6, 
        "question": "What are the records for most goals scored and conceded per match on homeground (2003-2022)?",
        "options": ["Most Goals Conceded: 2, Most Goals Scored: 5", "Most Goals Conceded: 3, Most Goals Scored: 6", "Most Goals Conceded: 4, Most Goals Scored: 8", "Most Goals Conceded: 5, Most Goals Scored: 7"],
        "correct_answer": "Most Goals Conceded: 3, Most Goals Scored: 5",
        "explanation": "The records for most goals scored and conceded per match on homeground are: Most Goals Conceded in a match - 3, Most Goals Scored in a match - 5."
        },

        {
        "question_number": 7, 
        "question": "These OAU MFT players have all scored against three or more different teams in the HiFL EXCEPT?",
        "options": ["Olaniyi Muyiwa", "Muraina Toba", "Seyi Olumofe", "Esakpere Anthony"],
        "correct_answer": "Esakpere Anthony",
        "explanation": ("Esiakpere Anthony featured in two different HiFL squads for the OAU MFT but only recorded goals against "
                        "two different teams compared to Muraina Toba(3), Olaniyi Muyiwa(4) and Seyi Olumofe(3).")
        },

        {
        "question_number": 8, 
        "question": "What ended an unbeaten run of 10 games in all competitions and 7 games unbeaten in HiFL?",
        "options": ["0—3 defeat to UAM at HiFL 2018", "1—2 defeat to EKSU at HiFL 2022", "0—1 defeat to LASU at HiFL 2019", "None of the above"],
        "correct_answer": "1—2 defeat to EKSU at HiFL 2022",
        "explanation": "The 1—2 defeat to EKSU at HiFL 2022 ended an unbeaten run of 10 games in all competitions and 7 games unbeaten in HiFL."
        },

        {
        "question_number": 9, 
        "question": "How many times did OAU MFT only ever lose back-to-back games (2003-2022)?",
        "options": ["Once", "Twice", "Thrice", "Never"],
        "correct_answer": "Twice",
        "explanation": "OAU MFT only ever lost back-to-back games twice in the course of 2003—2022."
        },

        {
        "question_number": 10,
        "question": "How many goals did the OAU MFT score in games won (in all competitions) when facing the University of Ibadan under Chike Egbunu-Olimene?",
        "options": ["9", "15", "10", "None of the above"],
        "correct_answer": "None of the above",
        "explanation": ("The OAU MFT have a 6-0 aggregate score in games they won vs. UI (in all competitions) under Chike Egbunu-Olimene.")
        },

        {
        "question_number": 11, 
        "question": "Which one of these OAU Sport Council stakeholders has served in the capacity of the OAUSC Chairperson?",
        "options": ["Dr. Akinbiola", "Abu Adamu Lasisi", "Mrs. W.A Tijani", "Prof. Y.B Amusa"],
        "correct_answer": "Prof. Y.B Amusa",
        "explanation": "Prof. Y.B Amusa currently serves as the OAUSC Chairperson."
        },

        {
        "question_number": 12, 
        "question": "In which edition of the NUGA Games did OAU MFT attend but didn't play in the Finals under Chike Egbunu-Olimene?",
        "options": ["2007", "2011", "2015", "2019"],
        "correct_answer": "2011",
        "explanation": ("UNIBEN 2011 in Benin was the only edition of the NUGA Games the OAU MFT attended under "
                       "CEO and didn't play in the Finals courtesy of an early exit in the group stage.")
        },

        {
        "question_number": 13, 
        "question": "In how many games did Coach CEO avoid a defeat in the first half in his first 13 games in charge?",
        "options": ["6", "9", "10", "13"],
        "correct_answer": "13",
        "explanation": "Coach CEO never lost the first half in his first 13 games in charge of the OAU MFT (at competitions)."
        },

        {
        "question_number": 14, 
        "question": "What are the longest unbeaten runs at competitions attended under Chike Egbunu-Olimene?",
        "options": ["NUGA Games: 5, HiFL: 7, NUFOL Games: 3", "NUGA Games: 8, HiFL: 7, NUFOL Games: 5", "NUGA Games: 10, HiFL: 5, NUFOL Games: 7", "NUGA Games: 7, HiFL: 5, NUFOL Games: 3"],
        "correct_answer": "NUGA Games: 8, HiFL: 7, NUFOL Games: 5",
        "explanation": "Longest Unbeaten runs at competitions attended are: NUGA Games - 8, HiFL - 7, NUFOL Games - 5."
        },

        {
        "question_number": 15, 
        "question": "What is the record for the unbeatun run of the OAU MFT at HT under CEO?",
        "options": ["9", "43", "29", "13"],
        "correct_answer": "Most consecutive clean sheets",
        "explanation": "Since trailing 0-2 in Makurdi at HT (in 2018), the OAU MFT under CEO have enjoyed an impressive run of 29 first halves (in all comps) without going behind! A record that more than doubled the one initially set by CEO (13) when he first took charge."
        },

        {
        "question_number": 16, 
        "question": "In which match did OAU MFT only ever lost both halves in a game?",
        "options": ["UI in 2018", "UNIMAID in 2007", "UAM in 2019", "UNICAL in 2021"],
        "correct_answer": "UAM in 2018",
        "explanation": "OAU MFT under CEO only ever lost both halves in a game once, and it was in a 3-0 defeat (Away) to the University of Agriculture, Makurdi in 2018: 0-2 (L) in the First half, 0-1 (L) in the Second half."
        },

        {
        "question_number": 17,
        "question": "What are OAU MFT Longest Unbeaten Runs Per Half (all comps)?",
        "options": ["First-half: 25 Games, Second Half: 14 Games", "First-half: 29 Games, Second Half: 18 Games", "First-half: 20 Games, Second Half: 10 Games", "First-half: 24 Games, Second Half: 12 Games"],
        "correct_answer": "First-half: 29 Games, Second Half: 14 Games",
        "explanation": "OAU MFT Longest Unbeaten Runs Per Half (all comps) are: First-half: 29 Games, Second Half: 14 Games."
        },

        {
        "question_number": 18, 
        "question": "What happened in the 2-0 win over LASU at the mainbowl in 2019?",
        "options": ["OAU MFT won the NUGA Games", "Seyi Olumofe scored a hat-trick", "OAU MFT equalled their longest unbeaten run", "OAU MFT lost the match"],
        "correct_answer": "OAU MFT equalled their longest unbeaten run",
        "explanation": "OAU MFT equalled their longest unbeaten run (10 Games) under CEO in the 2-0 win over LASU at the mainbowl in 2019. Goals from Adeyemi Opeyemi and Olaniyi Muyiwa earned the team the deserved win."
        },

        {
        "question_number": 19, 
        "question": "Who is the visiting goalkeeper with the most Save Percentage in an HiFL match against OAU MFT on homeground?",
        "options": ["Seyi Olumofe", "Adeyemi Opeyemi", "Saka Abiola", "Olaniyi Muyiwa"],
        "correct_answer": "Saka Abiola",
        "explanation": "Following his heroics in 2019, Saka Abiola (LASU) is the visiting goalkeeper with the most Save Percentage (77.77%) in an HiFL match played against the OAU MFT on homeground."
        },

        {
        "question_number": 20, 
        "question": "What is the record regarding the OAU MFT never losing the second half of a fixture played on homeground under CEO?",
        "options": ["True", "False", "Partially True", "Not Specified"],
        "correct_answer": "True",
        "explanation": "The OAU MFT never lost the second half of a fixture played on homeground under CEO."
        },

        {
        "question_number": 21, 
        "question": "What did OAU MFT achieve despite enjoying Super 4 privileges in HiFL2019?",
        "options": ["Conceded the fewest goals", "Outscored every other SW geo-pol region university", "Won the NUGA Games", "Lost all group stage matches"],
        "correct_answer": "Outscored every other SW geo-pol region university",
        "explanation": "Despite enjoying Super 4 privileges and participating only in the KO stages of the HiFL2019, the OAU MFT under CEO outscored (8 Goals) every other University from the SW geo-pol region who started the tournament from the group stages."
        },

        {
        "question_number": 22, 
        "question": "How many changes did CEO make to his starting lineups at the HiFL2019 across the seven games played in that competition?",
        "options": ["5", "8", "10", "15"],
        "correct_answer": "10",
        "explanation": "In HiFL2019, CEO made a total of 10 changes to his starting lineups across the seven games played in that competition, and the OAU MFT featured a total of 15 different players in their starting-XI."
        },

        {
        "question_number": 23,
        "question": "What is the overall goal difference at competitions for the OAU MFT under CEO (excl. walkovers)?",
        "options": ["+47", "+18", "+56", "+24"],
        "correct_answer": "+47",
        "explanation": ("In all competitions under CEO, the team managed 96 goals and allowed 49 in total (excl. walkovers). "
                        "The overall goal difference at competitions for the OAU MFT under CEO is therefore +47.")
        },

        {
        "question_number": 24, 
        "question": "How many wins did the OAU MFT record at the 2016 PreNUGA tournament in Kwara?",
        "options": ["2", "0", "3", "1"],
        "correct_answer": "0",
        "explanation": "The team did not record a win at the 2016 PreNUGA tournament in Kwara."
        },

        {
        "question_number": 25,
        "question": "How many goals did the OAU MFT score at HiFL2019?",
        "options": ["15", "12", "9", "8"],
        "correct_answer": "8",
        "explanation": "OAU MFT scored eight (8) goals in the Higher Institutions' Football League in the year 2019."
        },

        {
        "question_number": 26, 
        "question": "Which of these teams did OAU MFT defeat to claim the Gold at the NUFOL Games?",
        "options": ["OOU", "UNILORIN", "UNIBEN", "UDUSOK"],
        "correct_answer": "OOU",
        "explanation": "OAU MFT defeated OOU 2-1 to claim the Gold medals at the 4th edition of the NUFOL Games, the final was recorded to have been played at Igbinedion University, Okada town"
        },

        {
        "question_number": 27,
        "question": "How many times did OAU MFT win the NUGA Gold medal under CEO?",
        "options": ["Once", "Twice", "Thrice", "Four times"],
        "correct_answer": "Once",
        "explanation": "OAU MFT won the NUGA Gold medal once under CEO, and it happened in 2014."
        },

        {
        "question_number": 28, 
        "question": "What was the score of the 2019 Peace Cup semi-final between OAU MFT and E-Springs FC?",
        "options": ["1-0", "2-0", "0-1", "0-2"],
        "correct_answer": "2-0",
        "explanation": "The score of the 2019 Peace Cup semi-final between OAU MFT and E-Springs FC was 2-0 in favor of OAU MFT."
        },

        {
        "question_number": 29, 
        "question": "'Drizzy, The Animal' were popular monickers for which of these OAU MFT players?",
        "options": ["Seyi Olumofe", "Adeyemi Opeyemi", "Akanfe Oyewale", "Adegoke Toheeb"],
        "correct_answer": "Seyi Olumofe",
        "explanation": "Seyi Olumofe's popular aliases are Drizzy and The Animal."
        },

        {
        "question_number": 30, 
        "question": "Who captained the OAU MFT to their only NUGA Gold medal under Chike Egbunu-Olimene?",
        "options": ["Seyi Olumofe", "Yengibiri Henry", "Addah Obubo", "Ayotunde Faleti"],
        "correct_answer": "Ayotunde Faleti",
        "explanation": "Ayotunde Faleti captained the OAU MFT to their only NUGA Gold medal under Chike Egbunu-Olimene in 2014."
        },

        {
        "question_number": 31,
        "question": "All of these people have served as the SU Director of Sports in Obafemi Awolowo University EXCEPT ?",
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
                        "\nthe Great Ife Students' Union Director of Sports unlike OluwaMicheal (2017/18), "
                        "\nOluwanooni (2022/23) and Sumbade Jnr (2023/24)")
        },

        {
        "question_number": 34,
        "question": "Which of these institutions is not one of the Top 5 teams faced by the OAU MFT under CEO?",
        "options": ["UNILORIN", "AAUA", "UAM", "ABU"],
        "correct_answer": "ABU",
        "explanation": "The OAU MFT under CEO only had three meetings with ABU in all competitions, compared to AAUA(4), UAM(4) and UNILORIN(5)."
        },

        {
        "question_number": 35,
        "question": "Which of these correctly describes the percentage distribution of full-time results of the OAU MFT under CEO (in all comps)?",
        "options": ["W(17.91%), D(38.81%), L(43.28%)", "W(50.75%), D(29.85%), L(19.40%)", "W(38.81%), D(52.24%), L(8.96%)", "Not Determinable"],
        "correct_answer": "W(50.75%), D(29.85%), L(19.40%)",
        "explanation": "The OAU MFT under CEO recorded 34/67 wins, 20/67 draws and 13 loses at FT (in all comps)."
        },

        {
        "question_number": 36,
        "question": "Which of these did not captain the OAU MFT under Chike?",
        "options": ["Kesh", "Adegoke Toheeb", "Seyi Olumofe", "Ayotunde Faleti"],
        "correct_answer": "Kesh",
        "explanation": "Kesh was the captain of the OAU FFT."
        },

        {
        "question_number": 37,
        "question": "Which of these is not in the Organization values of the OAUSC?",
        "options": ["None of the below", "Excellence", "Integrity", "Innovation"],
        "correct_answer": "None of the below",
        "explanation": "The OAUSC organizational values as listed on the University's sports website are as follows: Innovation, Integrity, Excellence and Efficiency."
        },

        {
        "question_number": 38,
        "question": "Obafemi Awolowo University did not host the NUGA Games in which of these years?",
        "options": ["1970", "1984", "2014", "None of the above"],
        "correct_answer": "None of the above)",
        "explanation": "Obafemi Awolowo University hosted the NUGA Games in 1970, 1984 and 2014, finishing 1st, 3rd and 3rd respectively on the final medals table."
        },

        {
        "question_number": 39,
        "question": "Which one these OAU MFT players has won honors at the NUGA Games, the HiFL and the Peace Cup?",
        "options": ["Addah Obubo", "Friday Ogboeba", "Akanfe Oyewale", "Akinsola Alarape"],
        "correct_answer": "Akanfe Oyewale",
        "explanation": "Akanfe Oyewale has won honors with the OAU MFT under CEO at the above listed competitions."
        },

        {
        "question_number": 40,
        "question": "One of these OAU MFT players is not famous for playing as a goalkeeper, who is it?",
        "options": ["Addah Obubo", "Chike Egbunu-Olimene", "Akanfe Oyewale", "Ebire Abiodun"],
        "correct_answer": "Addah Obubo",
        "explanation": "Unlike all who are listed above, Addah Obubo was a renowned midfield maestro during his time with the OAU MFT."
        },

        {
        "question_number": 41,
        "question": "The jersey #8 is synonymous to which OAU MFT athlete?",
        "options": ["Addah Obubo", "Seyi Olumofe", "Tella-Imam Abdulmalik", "Ebire Abiodun"],
        "correct_answer": "Seyi Olumofe",
        "explanation": "Seyi Olumofe was fond of the #8 jersey during his time with the OAU MFT."
        },

        {
        "question_number": 42,
        "question": "How many wins did the OAU MFT record at the NUGA Games under CEO at FT (excl. walkovers)?",
        "options": ["8", "7", "4", "6"],
        "correct_answer": "8",
        "explanation": "The OAU MFT under CEO won 8/19 games at the NUGA Games in all editions attended."
        },

        {
        "question_number": 43,
        "question": "How many FT clean sheets did the OAU MFT record at the NUGA Games in all editions attended under CEO?",
        "options": ["8", "7", "4", "6"],
        "correct_answer": "7",
        "explanation": "The OAU MFT under CEO recorded 7/19 clean sheets at the NUGA Games in all editions attended under CEO."
        },

        {
        "question_number": 44,
        "question": "In how games did the OAU MFT record a 1-1 draw at FT at the NUGA Games in all editions attended under CEO?",
        "options": ["1", "4", "3", "2"],
        "correct_answer": "2",
        "explanation": "The OAU MFT under CEO played a 1-1 draw at the NUGA Games only twice."
        },

        {
        "question_number": 45,
        "question": "At the UNIBEN 2011 NUGA Games, the OAU MFT were eliminated in the group stages but still scored more goals than they allowed, what were their goal averages at FT?",
        "options": ["GF Avg: 2.33, GA Avg: 1.67", "GF Avg: 1.63, GA Avg: 1.07", "GF Avg: 1.83, GA Avg: 0.77", "GF Avg: 1.93, GA Avg: 0.98"],
        "correct_answer": "GF Avg: 2.33, GA Avg: 1.67",
        "explanation": "The OAU MFT at the UNIBEN 2011 NUGA Games scored 7 times in three games and allowed 5 goals leading to their elimination at the group stages. Their FT goal averages were therefore GF Avg: 2.33 and GA Avg: 1.67"
        },

        {
        "question_number": 46,
        "question": "Based on second half results of games played at the 2006 NUGA Games in Maiduguri, what was the aggregate score throughout the tournament?",
        "options": ["5-4", "1-0", "0-1", "0-0"],
        "correct_answer": "0-0",
        "explanation": ("The OAU MFT played five games at the 2006 NUGA Games in Maiduguri, totalling three goalless draws, a 1-0 win and a 0-1 loss at FT. "
                        "In all these instances, no goals were scored or conceded in the second half.")
        },

        {
        "question_number": 47,
        "question": "Based on second half results of games played at the 2006 NUGA Games in Maiduguri, what was the aggregate score throughout the tournament?",
        "options": ["5-4", "1-0", "0-1", "0-0"],
        "correct_answer": "0-0",
        "explanation": ("The OAU MFT played five games at the 2006 NUGA Games in Maiduguri, totalling three goalless draws, a 1-0 win and a 0-1 loss at FT. "
                        "In all these instances, no goals were scored or conceded in the second half.")
        },

        {
        "question_number": 48,
        "question": "How many losses did the OAU MFT record in penalty shoot-outs in 2019?",
        "options": ["5", "0", "2", "3"],
        "correct_answer": "3",
        "explanation": ("The OAU MFT played three penalty shoot-outs (in all comps) in 2019 but failed to win any.")
        },

        {
        "question_number": 49,
        "question": "How many honors did the OAU MFT win on penalty shoot-outs under CEO?",
        "options": ["5", "0", "2", "3"],
        "correct_answer": "0",
        "explanation": ("The OAU MFT won 0/2 penalty shoot-outs in Finals and 0/1 in Third-Place matches under CEO (in all comps).")
        },

        {
        "question_number": 50,
        "question": "Against whom did the then OAU MFT captain, Toheebah, miss the decisive penalty in the Final of the NUGA Games in 2022?",
        "options": ["UNILAG", "ABU", "UI", "UNILORIN"],
        "correct_answer": "UNILORIN",
        "explanation": ("The OAU MFT contested honors in the Final of the 2022 NUGA Games in Lagos against the University of Ilorin.")
        },

        {
        "question_number": 51,
        "question": "How many honors did the OAU MFT win under Chike Egbunu-Olimene (in all comps)?",
        "options": ["8", "3", "5", "6"],
        "correct_answer": "6",
        "explanation": ("The OAU MFT won 6/8 contested honors under CEO.")
        },
]
