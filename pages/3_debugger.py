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

order = ['W', 'D', 'L']

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
h = h.rename(columns={'count' : 'Matches'})
st.dataframe(h)
for i in range(len(h)):
    finals_dict[str(h['Tie'][i] + ' Played')] = h['Matches'][i]
    
# Split dfs    
# Finals
finals_df = honors_df[(honors_df['Tie'] == 'Final')]

res_f = finals_df.FTR.value_counts().loc[order].reset_index()
res_f

for i in range(len(res_f)):
    finals_dict['Final ('+ str(res_f['FTR'][i]) +')'] = res_f['count'][i]


#  3rd Place Playoffs  
third_place_df = honors_df[(honors_df['Tie'] == '3rd Place')]   
third_place_df

res_3rd = third_place_df.FTR.value_counts().loc[order].reset_index()
res_3rd
# res_3rd.rename(columns={'count' : 'Matches'})

for i in range(len(res_3rd)):
    finals_dict['3rd Place ('+ str(res_3rd['FTR'][i]) +')'] = res_3rd['count'][i]   

# Adding Penalty Records
# Setting Order of Categories for PSHTR
psht_order = ['W','L']
f = finals_df.PSHTR.value_counts().loc[psht_order].reset_index()
# f.rename(columns={'count' : 'Matches'})

#  For PSHTR in Finals
for i in range(len(f)): # minus 1 cause we dont want to include nan based on the psht_order
    if i == 0:
        finals_dict['Final PSHT (' + str(f['PSHTR'][i] + ')')] = f['count'][i]
    else:
        finals_dict['Final PSHT (' + str(f['PSHTR'][i] + ')')] = f['count'][i]
        
#  For PSHTR in Third Place Contests
t = third_place_df.PSHTR.value_counts().loc[psht_order].reset_index()
# t.rename(columns={'count' : 'Matches'})

for i in range(len(t)): # minus 1 cause we dont want to include nan based on the psht_order
    if i == 0:
        finals_dict['3rd Place PSHT (' + str(t['PSHTR'][i] + ')')] = t['count'][i]
    else:
        finals_dict['3rd Place PSHT (' + str(t['PSHTR'][i] + ')')] = t['count'][i]

finals_dict

# #  Setting up Figure & Axes
# fig, ax = plt.subplots(figsize=(12, 4), facecolor=facecolor)
# ax.set(facecolor=facecolor, xticks=([]), yticks=([]))
# hide_spines(axes=ax, which_spine='all')

# # Creating the Podium 
# pod_third = Rectangle((0.2,.5),.2,.1, fc='grey', ec='grey')
# pod_first = Rectangle((0.4,.5),.2,.2, fc='grey', ec='grey')
# pod_second = Rectangle((0.6,.5),.2,.1, fc='grey', ec='grey')

# podium = [pod_third, pod_first, pod_second]
# for part in podium:
#     ax.add_patch(part)

# # Podium Labels
# ax.text(x=.3, y= .4, s='Silver', color='grey', ha='center',
#             va='center', font=b_font, fontsize=10, zorder=2)
# ax.text(x=.5, y= .4, s='Gold', color='grey', ha='center',
#             va='center', font=b_font, fontsize=10, zorder=2)
# ax.text(x=.7, y= .4, s='Bronze', color='grey', ha='center',
#             va='center', font=b_font, fontsize=10, zorder=2)

# # Annotations
# # Text for count Honors Won
# gold_medals = finals_dict['Final (W)'] + finals_dict['Final PSHT (W)']
# silver_medals = finals_dict['Final (L)'] + finals_dict['Final PSHT (L)']
# bronze_medals = finals_dict['3rd Place (W)'] + finals_dict['3rd Place PSHT (W)']

# ax.text(x=.3, y= .7, s=f'{silver_medals}', color=plot_color, ha='center',
#             va='center', font=t_font, fontweight='bold', fontsize=18, zorder=2)
# ax.text(x=.5, y= .8, s=f'{gold_medals}', color=plot_color, ha='center',
#             va='center', font=t_font, fontweight='bold', fontsize=18, zorder=2)
# ax.text(x=.7, y= .7, s=f'{bronze_medals}', color=plot_color, ha='center',
#             va='center', font=t_font, fontweight='bold', fontsize=18, zorder=2)

# # Title Text
# custom_space = " " #Needed cause of the behavioral ppts highlight-text on \n
# title_text = (f"A PODIUM PLOT OF THE <HONORS WON> BY {team} UNDER {coach.upper()}\n"
#                 f"\n\n{custom_space*30} ({data_span})")
# h_fig(x=.20, y=1.1, s=title_text, color=off_white, highlight_textprops=[{'color':plot_color}],
#     font=t_font, fontsize=13, fontweight='bold', zorder=2)

# # Total Honor Wons
# total_honors = gold_medals + silver_medals + bronze_medals
# t_hnr_txt = f'<Total Honors:> {total_honors}'
# # h_fig(x=.45, y=.90, s=t_hnr_txt, color='grey', highlight_textprops=[{'color':'grey'}],
# #        font=t_font, fontsize=13, fontweight='bold', zorder=2)

# # Additional Text
# brkdwn_txt = '\n'.join([f'{key} : {value}' for key, value in finals_dict.items()])
# # Split the string into four smaller parts
# parts = brkdwn_txt.split('\n')

# # Join in threes and format as strings
# brkdwn_txt_1 = '\n'.join(parts[:3])
# brkdwn_txt_2 = '\n'.join(parts[3:6])
# brkdwn_txt_3 = '\n'.join(parts[6:9])
# brkdwn_txt_4 = '\n'.join(parts[9:])

# brkdwn_txt1 = fig.text(x=0.25, y= 0.25, s=f'{brkdwn_txt_1}', color=off_white, linespacing= 2,
#                 ha='left', va='top', font=b_font, fontsize=10, zorder=2)
# brkdwn_txt2 = fig.text(x=0.42, y= 0.25, s=f'{brkdwn_txt_2}', color=off_white, linespacing= 2,
#                 ha='left', va='top', font=b_font, fontsize=10, zorder=2)
# brkdwn_txt3 = fig.text(x=0.54, y= 0.25, s=f'{brkdwn_txt_3}', color=off_white, linespacing= 2,
#                 ha='left', va='top', font=b_font, fontsize=10, zorder=2)
# brkdwn_txt4 = fig.text(x=0.67, y= 0.25, s=f'{brkdwn_txt_4}', color=off_white, linespacing= 2,
#                 ha='left', va='top', font=b_font, fontsize=10, zorder=2)

# brkdwn_txt1.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# brkdwn_txt2.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# brkdwn_txt3.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# brkdwn_txt4.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])

# #  Name Text
# name_text = fig.text(x=0.52, y= -.10, s=author, ha='center', va='center', 
#                 font=b_font, color=plot_color, alpha=.3, fontsize=10, zorder=2)
# name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])

# # Figure Paddings 
# # Pad Top 
# fig.text(x=0.5, y= 1.13, s=pad_top, color=off_white, linespacing= 2,
#                 ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
# # Pad Bottom
# fig.text(x=0.5, y= -.10, s=pad_end, color=off_white, linespacing= 2,
#                 ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

# return fig
