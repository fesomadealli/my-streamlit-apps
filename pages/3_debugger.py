# # Import streamlit 
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# from matplotlib.patches import Arc, Rectangle, Circle

# # Universal Plot Elements
# # Text Detail
# team = 'OAU MFT'
# team_alias = 'OAU Giants'
# coach = 'Chike Egbunnu-Olimene'
# data_span = '2003-2022'
# author = 'Data by @allinewsnigeria' #'@fesomadealli'
# add_note = "(Walkover & Abandoned ties are excluded)"

# # Font
# b_font =  'Merriweather'
# t_font = 'Fira Code'
# b_fsize = 14
# t_fsize = 16

# # Colors for Dark Mode
# facecolor = '#242526' #18191A is an alternative choice
# ax_color = '#3A3B3C'  
# plot_color = '#E0CB8A'
# off_white = '#FAF9F6'
# alt_color = '#303233'

# # Text Customization & Fancy Legend Library
# import matplotlib.patheffects as path_effects
# import highlight_text
# h_axs = highlight_text.ax_text 
# h_fig = highlight_text.fig_text

# # # Customizing plot order (for results) from the start
# # order = ['W', 'D', 'L']

# # Figure Paddings         
# pad_top = "\n\n"
# pad_end = "\n\n"
# hspace  = " "
# vspace  = " "
# newline = '\n'

# # Loading Results Dataset
# def load_data():
#     # Results df
#     results = pd.read_csv('assets/results_df.csv')
#     #  Drop 'Unnamed:0' column
#     results = results.drop(columns=['Unnamed: 0'])
#     # Home Games df
#     home_games = pd.read_csv("assets/h_games.csv")
#     # Goals df
#     goals = pd.read_csv("assets/goals_df.csv")
    
#     return results, home_games, goals

# results_df, h_games, goals_df = load_data()

# import plot_functions

# select_opponent = "All_teams"
# select_period = "FTR"
# select_range = "All_Games"
# select_comp=None
# select_edition=None 
# select_category = None
# # select_comp = None

# # select_edition = None
# select_outcome = None

# # ------------------------------------------------------ #
# select_period = period = "HTR"

# # goals_df
