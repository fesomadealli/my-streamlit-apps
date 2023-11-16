# Import streamlit 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Arc, Rectangle, Circle

# Universal Plot Elements
# Text Detail
team = 'OAU MFT'
team_alias = 'OAU Giants'
coach = 'Chike Egbunnu-Olimene'
data_span = '2003-2022'
author = 'Data by @allinewsnigeria' #'@fesomadealli'
add_note = "(Walkover & Abandoned ties are excluded)"

# Font
b_font =  'Merriweather'
t_font = 'Fira Code'
b_fsize = 14
t_fsize = 16

# Colors for Dark Mode
facecolor = '#242526' #18191A is an alternative choice
ax_color = '#3A3B3C'  
plot_color = '#E0CB8A'
off_white = '#FAF9F6'
alt_color = '#303233'

# Text Customization & Fancy Legend Library
import matplotlib.patheffects as path_effects
import highlight_text
h_axs = highlight_text.ax_text 
h_fig = highlight_text.fig_text

# # Customizing plot order (for results) from the start
# order = ['W', 'D', 'L']

# Figure Paddings         
pad_top = "\n\n"
pad_end = "\n\n"
hspace  = " "
vspace  = " "
newline = '\n'

# Loading Results Dataset
def load_data():
    # Results df
    results = pd.read_csv('assets/results_df.csv')
    #  Drop 'Unnamed:0' column
    results = results.drop(columns=['Unnamed: 0'])
    # Home Games df
    home_games = pd.read_csv("assets/h_games.csv")
    # Goals df
    goals = pd.read_csv("assets/goals_df.csv")
    
    return results, home_games, goals

results_df, h_games, goals_df = load_data()

import plot_functions

select_opponent = "UNILAG"
select_period = "FTR"
select_range = "All_Games"
select_comp=None
select_edition=None 
select_category = None
# select_comp = None

# select_edition = None
select_outcome = None

import streamlit as st
import pandas as pd
import numpy as np


# ------------------------------------------------------ #
select_period = period = "HTR"

# goals_df

# Creating the Honors Dataframe
oau_giants = pd.read_csv("assets/oau-giants.csv")
honors_df = oau_giants[(oau_giants['CompGroup'] != 'PreNUGA') &
                        (oau_giants['Tie']=='Final') | (oau_giants['Tie']=='3rd Place') | 
                        (oau_giants['TieDescr']=='Final') | (oau_giants['TieDescr']=='3rd Place')]

honors_df.reset_index(drop=True, inplace=True)

# Create empty dictionary
finals_dict = {}

# populating the dictionary
#  Total Num of Finals Played - Main Finals & Third Place
finals_dict['Honors Contested'] = len(honors_df)

# Getting number of games played in Finals & 3rd Place contests
h = honors_df.Tie.value_counts().reset_index()
h = h.rename(columns={'index' : 'Outcome'})
st.dataframe(h)

index_list = h['Outcome'].to_list()
tie_list = h.Tie.to_list()
if len(index_list) == len(tie_list):
        for i in range(len(h)):
            # key = str(index_list[i])
            # value = str(tie_list[i])
            # finals_dict.update({key : value})
            finals_dict[str(h['Outcome'][i] + ' Played')] = h['Tie'][i]

else:
    st.write("Unequal Length of values... which would be totally strange!")
finals_dict
