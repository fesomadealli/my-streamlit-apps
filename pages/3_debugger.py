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

goals_df

# def process_string(input_str):
#     # Replace single quotes with escaped single quotes
#     processed_str = input_str.replace("'", "\\'")
#     return processed_str

# # Example usage
# original_string = "This is a string with a single quote ('), let's process it."
# processed_string = process_string(original_string)

# st.write("Original String:", original_string)
# st.write("Processed String:", processed_string)

selected_string = "I'm going to the park"

modified_string = selected_string.replace("'", r"\\'")
st.write(selected_string)
st.write(f"{modified_string}")


# # AllTime_Comp_Results(period):
# #  Order to specify the results
# order = ['W', 'D', 'L']

# # we dont need to remember these dfs so we can give them random names
# y = results_df.groupby('CompGroup')[f'{period}'].value_counts().unstack(fill_value=0)[order].reset_index()

# # Shortening Names of Some CompGroup Items
# y = y.replace(['NUFOL Games', 'NUGA Games'], ['NUFOL', 'NUGA'])

# # Getting a Unique List of Competitions played (now shortened)
# comp_list = y.CompGroup.unique()

# # setting up plot (grid) axes
# ncols = 3
# nrows = int(y.CompGroup.nunique()/ncols) #to remove decimals arising from division

# fig, axs = plt.subplots(nrows, ncols, figsize=(6,4), sharey='row',
#                         facecolor=facecolor, constrained_layout=True)

# # Define custom color palettes
# colors = {'W': '#E0CB8A',
#           'D': '#79A19D',
#           'L': 'grey'} #055A87 #923878 --Alt colors (blue & purple)

# # Dictionary to hold other plot valuables
# comp_dict = {}

# # Populating the Dictionary 
# for i in range(len(y)):
#     for j in range(len(order)):
#         comp_dict[f"{y.CompGroup[i]}({order[j]})"] = f"{y[order[j]][i]}"

# # Drawing the Subplots 
# for row in range(nrows):
#     for col in range(ncols):
#         # Access the current subplot using axs[row, col]
#         ax = axs[row, col]
#         # Axes customization
#         ax.set_yticks([])
#         ax.set_xticks([])
#         ax.set_ylim(0, 15)
#         ax.set(title="\n")
#         #specfiy axis labels
#         ax.set_facecolor(alt_color) #'#18191A'
#         plot_functions.hide_spines(axes=ax, which_spine='all')


# idx = 0
# idy = 0
# comp_list = y.CompGroup.unique()

# for i in range(len(comp_list)): 
#     # filter the dataframe for rows where CompGroup = comp_list[i]
#     new_df = y[y['CompGroup']==comp_list[i]]
#     # Set the 'CompGroup' column as the index for better plotting
#     new_df.set_index('CompGroup', inplace=True)
#     # Transpose the DataFrame for side-by-side bars
#     new_df = new_df.T.reset_index()
#     # Rename columns for Seaborn
#     new_df.columns = ['Outcome', 'Count']

#     # Check if we should switch to the next row  of subplots
#     if idy < ncols:
#         # plot on top subplot row
#         ax_plot = sns.barplot(ax=axs[idx,idy], data=new_df, x=new_df.Outcome, y=new_df.Count,
#                                 order=order, palette=colors, color=plot_color, zorder=2)
#         ax_plot.set(xlabel=None,
#                     ylabel=None,
#                     xticks=([]))

#         idy +=1

#     else:
#         if idy >= ncols:
#             idx +=1
#             idy -= ncols
#             # plot on bottom subplot row
#             ax_plot = sns.barplot(ax=axs[idx,idy], data=new_df, x=new_df.Outcome,
#                                     y=new_df.Count, order=order, palette=colors,
#                                     color=plot_color, zorder=2)
#             ax_plot.set(xlabel=None, ylabel=None, xticks=([]))

#             idy +=1

# # Name Text
# name_text = fig.text(x=0.51, y= -.22, s=author, ha='center', va='center', 
#                      font=b_font, color=plot_color, alpha=.3, fontsize=8, zorder=2)
# name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=plot_color), 
#                             path_effects.Normal()])

# # Figure Paddings  
# # Pad Top 
# fig.text(x=0.19, y= 1.08, s=pad_top, color=off_white, linespacing= 2,
#                 ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
# # Pad Bottom
# fig.text(x=0.51, y= -.20, s=pad_end, color=off_white, linespacing= 2,
#                 ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
# # Pad left
# fig.text(x=-.12, y= 1.15, s=hspace, color=off_white, linespacing= 2,
#                 ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
# # Pad Right 
# fig.text(x=1.12, y= 1.15, s=hspace, color=off_white, linespacing= 2,
#                 ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

# # Title Text
# title = (f"<WINS>, <DRAWS> AND <LOSSES> BY {team} PER TOURNAMENT UNDER {coach.upper()}\n\n" +
#             f"                                ({data_span})")
# h_fig(x=-.03, y=1.15, s=title, color=off_white, highlight_textprops=[{'color':'#E0CB8A'},
#                                                                      {'color':'#79A19D'},
#                                                                      {'color':'grey'}],
#         font=t_font, fontsize=10, linespacing=1.75, fontweight='bold', zorder=2)

# #  Total Games played Per CompGroup
# def calc_sum(comp_list):
#     gms_plyd = int(comp_dict[f'{comp_list}(W)']) + int(comp_dict[f'{comp_list}(D)']) + int(comp_dict[f'{comp_list}(L)'])
#     return gms_plyd

# # """ This portion of code is not totally dynamic and may need a review/update in future versions """
# # Subplot labels
# t_one = (f"{comp_list[0]} | W{comp_dict[f'{comp_list[0]}({order[0]})']} "
#             f"D{comp_dict[f'{comp_list[0]}({order[1]})']} "
#             f"L{comp_dict[f'{comp_list[0]}({order[2]})']}   ({calc_sum(comp_list[0])})")

# t_two = (f"{comp_list[1]} | W{comp_dict[f'{comp_list[1]}({order[0]})']} "
#             f"D{comp_dict[f'{comp_list[1]}({order[1]})']} "
#             f"L{comp_dict[f'{comp_list[1]}({order[2]})']}   ({calc_sum(comp_list[1])})")

# t_three = (f"{comp_list[2]} | W{comp_dict[f'{comp_list[2]}({order[0]})']} "
#             f"D{comp_dict[f'{comp_list[2]}({order[1]})']} "
#             f"L{comp_dict[f'{comp_list[2]}({order[2]})']}   ({calc_sum(comp_list[2])})")

# b_one = (f"{comp_list[3]} | W{comp_dict[f'{comp_list[3]}({order[0]})']} "
#             f"D{comp_dict[f'{comp_list[3]}({order[1]})']} "
#             f"L{comp_dict[f'{comp_list[3]}({order[2]})']}   ({calc_sum(comp_list[3])})")

# b_two = (f"{comp_list[4]} | W{comp_dict[f'{comp_list[4]}({order[0]})']} "
#             f"D{comp_dict[f'{comp_list[4]}({order[1]})']} "
#             f"L{comp_dict[f'{comp_list[4]}({order[2]})']}   ({calc_sum(comp_list[4])})")

# b_three = (f"{comp_list[5]} | W{comp_dict[f'{comp_list[5]}({order[0]})']} "
#             f"D{comp_dict[f'{comp_list[5]}({order[1]})']} "
#             f"L{comp_dict[f'{comp_list[5]}({order[2]})']}   ({calc_sum(comp_list[5])})")

# # idx = 0
# top_1 = fig.text(x=0.01, y= 0.93, s=f"{t_one}", color=off_white, fontweight='medium',
#                     ha='left', va='center', font=b_font, fontsize=8, zorder=2)
# top_2 = fig.text(x=0.34, y= 0.93, s=f"{t_two}", color=off_white, fontweight='medium',
#                     ha='left', va='center', font=b_font, fontsize=8, zorder=2)
# top_3 = fig.text(x=0.67, y= 0.93, s=f"{t_three}", color=off_white, fontweight='medium',
#                     ha='left', va='center', font=b_font, fontsize=8, zorder=2)
# # # idx = 1 
# bottom_1 = fig.text(x=0.01, y= 0.43, s=f"{b_one}", color=off_white, fontweight='medium',
#                     ha='left', va='center', font=b_font, fontsize=8, zorder=2)
# bottom_2 = fig.text(x=0.34, y= 0.43, s=f"{b_two}", color=off_white, fontweight='medium',
#                     ha='left', va='center', font=b_font, fontsize=8, zorder=2)
# bottom_3 = fig.text(x=0.67, y= 0.43, s=f"{b_three}", color=off_white, fontweight='medium',
#                     ha='left', va='center', font=b_font, fontsize=8, zorder=2)


# top_1.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# top_2.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# top_3.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# bottom_1.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# bottom_2.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])
# bottom_3.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])

# # Endnotes
# if period == 'FTR':
#     endnote_text = (f"Breakdown of full-time results per tournament.\n" 
#                         "(Walkover & Abandoned ties are excluded)")
# if period == 'HTR':
#     endnote_text = (f"Breakdown of half-time results per tournament.\n" 
#                         "(Walkover & Abandoned ties are excluded)")
# if period == 'SHR':
#     endnote_text = (f"Breakdown of second-half results per tournament.\n" 
#                         "(Walkover & Abandoned ties are excluded)")

# endnote = fig.text(x=0.51, y= -.12, s=endnote_text, color=off_white, linespacing= 2,
#                     ha='center', va='center', font=b_font, fontsize=9, zorder=2)
# endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
#                             path_effects.Normal()])

# fig