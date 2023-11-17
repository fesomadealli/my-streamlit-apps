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

select_opponent = "All_teams"
select_period = "FTR"
select_range = "All_Games"
select_comp=None
select_edition=None 
select_category = None
# select_comp = None

# select_edition = None
select_outcome = None

# ------------------------------------------------------ #
select_period = period = "HTR"

# goals_df

order = ['W', 'D', 'L']
"""
Possible Func Mods: select_opponent, select_period (optional: select_df to Use)

select_opponent: All_teams | Oppnt_name
select_period: FTR | HTR | SHR
select_range: All_Games | Home_Games
"""
plot_results = True

if select_range == 'Home_Games':
    if select_opponent != 'All_teams':
        if plot_functions.confirm_fixture_on_homeground(select_opponent) is False:
            st.write(f"No Meetings With {select_opponent} on Homeground")
            # return(f"No Meetings With {select_opponent} on Homeground")
            # plot_results = False
        else:
            df = h_games[h_games['Opponent'] == select_opponent]
    else:
        df = h_games
    
elif select_range == 'All_Games':
    df = goals_df
    if select_opponent != 'All_teams':
        df = goals_df[(goals_df.Opponent == select_opponent)]

# Making Plot
if plot_results is True:
    #Filter the goals_df
    # Check for possible missing categorical variables 'W', 'D' or 'L' in select_period column
    # ...using reindex() with the fill_values argument/parameter passed into the method
    cum_df = df[f'{select_period}'].value_counts().reindex(order, fill_value=0).reset_index()
    cum_df
    
    # Data for the donut chart
    total_games_played = cum_df['count'].sum()

    #  Setting up Figure & Axes
    fig, ax = plt.subplots(1,3, figsize=(12, 4), facecolor=facecolor, constrained_layout=True)

    # dictionary to access the contents of the Cumulative Results Column
    emp = {}
    for i in range(len(cum_df)):   #Can't put this block of code in the second for loop because we need  
        emp[cum_df[f'{select_period}'][i]] = cum_df['count'][i] #to fill the dctionary first before accessing it.
    
    emp

    for i in range(len(cum_df)):
        if order[i] == 'W':
            colors = [ax_color, plot_color]
            num_wins = str(emp.get(f'{order[i]}', 0))
        if order[i] == 'D':
            colors = [ax_color, plot_color]
            num_draws = str(emp.get(f'{order[i]}', 0))
        if order[i] == 'L':
            colors = [ax_color, plot_color]
            num_loss = str(emp.get(f'{order[i]}', 0))
        ax[i].set_yticks([])
        ax[i].set_xticks([])
        ax[i].set_facecolor(ax_color)
        plot_functions.hide_spines(axes=ax[i], which_spine="all")
       
        # Calculate % of that portion/selection
        pct = (emp[order[i]] / total_games_played) * 100 
        # Create the donut chart
        ax[i].pie([total_games_played - int(emp[order[i]]), int(emp[order[i]])], colors=colors, 
                  startangle=90, wedgeprops={'width': 1.5})
        # Highlight the variable of interest in the center
        center_circle = plt.Circle((0, 0), 0.62, color=facecolor)
        ax[i].add_artist(center_circle)
        # Add the corresponding percentage text in the center
        # Pct Labels
        h_axs(ax=ax[i], x=-.38, y=.05, s=f'{pct: .2f}%', color=off_white, 
              font=t_font, fontsize=18, fontweight='bold', zorder=2)

    # Wins% Label
    h_axs(ax=ax[0], x=-.23, y=-.15, s='<Win %>', color=off_white, 
          highlight_textprops=[{'color':plot_color}], font=b_font,
          fontsize=b_fsize, fontweight='bold', zorder=2)
    # Draws% Label
    h_axs(ax=ax[1], x=-.21, y=-.15, s='<Draw %>', color=off_white,
          highlight_textprops=[{'color':plot_color}], font=b_font,
          fontsize=b_fsize, fontweight='bold', zorder=2) 
    # Loss% Label
    h_axs(ax=ax[2], x=-.21, y=-.15, s='<Loss %>', color=off_white,
          highlight_textprops=[{'color':plot_color}], font=b_font,
          fontsize=b_fsize, fontweight='bold', zorder=2)

    # Title Text x-location on Figure if the Opponent Name is to be printed on the Title
    title_xloc=.25
    ttl_space = hspace*4
    oppnt_name_char = len(select_opponent)
    if select_opponent != 'All_teams':
        if select_opponent != 'Successful Christian Mission FC':
            if oppnt_name_char>3 & oppnt_name_char<=15:
                title_xloc=.21
                ttl_space = hspace*5
        else: 
            select_opponent = 'Successful CMFC'
            title_xloc=.21
            ttl_space = hspace*10

    # Title Text
    title_text=" "
    if select_period == 'FTR':
        if select_opponent != 'All_teams':
            if select_range == 'Home_Games':
                title_text = (f"{team} <FT MATCH RESULTS%> vs. {select_opponent.upper()} IN HOME GAMES\n"
                              f"{ttl_space}UNDER {coach.upper()} ({data_span})")
            elif select_range == "All_Games":
                title_text = (f"{team} <FT MATCH RESULTS%> vs. {select_opponent.upper()} IN ALL MEETINGS\n"
                              f"{ttl_space}UNDER {coach.upper()} ({data_span})")
        # No Particular Opponent Selected        
        elif select_opponent == "All_teams":
            if select_range == 'Home_Games':
                title_text = (f"{team} <FT MATCH RESULTS%> IN ALL HOME GAMES UNDER\n"
                              f"{hspace*8}{coach.upper()} ({data_span})")
            elif select_range == "All_Games":
                title_text = f"{team} <FT MATCH RESULTS%> UNDER {coach.upper()} ({data_span})"
                title_xloc=.14

    if select_period == 'HTR':
        if select_opponent != 'All_teams':
            if select_range == 'Home_Games':
                title_text = (f"{team} <HT MATCH RESULTS%> vs. {select_opponent.upper()} IN HOME GAMES\n"
                              f"{ttl_space}UNDER {coach.upper()} ({data_span})")
            elif select_range == "All_Games":
                title_text = (f"{team} <HT MATCH RESULTS%> vs. {select_opponent.upper()} IN ALL MEETINGS\n"
                              f"{ttl_space}UNDER {coach.upper()} ({data_span})")
        # No Particular Opponent Selected        
        elif select_opponent == "All_teams":
            if select_range == 'Home_Games':
                title_text = (f"{team} <HT MATCH RESULTS%> IN ALL HOME GAMES UNDER\n"
                              f"{hspace*8}{coach.upper()} ({data_span})")
            elif select_range == "All_Games":
                title_text = f"{team} <HT MATCH RESULTS%> UNDER {coach.upper()} ({data_span})"
                title_xloc=.14

    if select_period == 'SHR':
        if select_opponent != 'All_teams':
            if select_range == 'Home_Games':
                title_text = (f"{team} <2ND HALF MATCH RESULTS%> vs. {select_opponent.upper()}"
                              f" IN HOME GAMES\n{ttl_space}UNDER {coach.upper()} ({data_span})")
            elif select_range == "All_Games":
                title_text = (f"{team} <2ND HALF MATCH RESULTS%> vs. {select_opponent.upper()}"
                              f" IN ALL MEETINGS\n{ttl_space}UNDER {coach.upper()} ({data_span})")
        # No Particular Opponent Selected       
        elif select_opponent == "All_teams":
            if select_range == 'Home_Games':
                title_text = (f"{team} <2ND HALF MATCH RESULTS%> IN ALL HOME GAMES UNDER\n"
                              f"{hspace*8}{coach.upper()} ({data_span})")
            elif select_range == "All_Games":
                    title_text = f"{team} <2ND HALF MATCH RESULTS%> UNDER {coach.upper()} ({data_span})"
                    title_xloc=.14

    # Set titles for the figure and the subplot respectively
    h_fig(x=title_xloc, y=1.18, s=title_text, color=off_white, highlight_textprops=[{'color':plot_color}],
           font=t_font, fontsize=t_fsize, fontweight='bold', zorder=2)

    # FT Results Breakdown
    txt = f"<Games Played:> " + str(len(df)) + f" <| Wins:> {num_wins}" + f" <| Draws:> {num_draws}" + f" <| Loss:> {num_loss}"

    h_fig(x=.22, y=-.08, s=txt, color=off_white, highlight_textprops=[{'color':plot_color}, 
                                                                      {'color':plot_color},
                                                                      {'color':plot_color},
                                                                      {'color':plot_color}],
           font=t_font, fontsize=t_fsize, fontweight='bold', zorder=2)

    # Endnotes
    gms_incl = plot_functions.get_comps(df)
    endnote_text = (f"Matches Included: {gms_incl}\n" 
                    f"{add_note}")
    endnote = fig.text(x=0.51, y= -.38, s=endnote_text, color=off_white, linespacing= 2,
                       ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    # Name Text
    name_text = fig.text(x=0.51, y= -.55, s=author, ha='center', va='center', 
                       font=b_font, color=plot_color, alpha=.3, fontsize=b_fsize, zorder=2)

    # Path Effects for texts
    endnote.set_path_effects([path_effects.Stroke(linewidth=.018, foreground=off_white),
                              path_effects.Normal()])
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=plot_color), 
                                path_effects.Normal()])

    # Figure Paddings         
    fig.text(x=0.19, y= 1.20, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    fig.text(x=0.51, y= -.50, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    # plt.tight_layout()
    fig
    # return fig

else:
    error_msg = ("No Plot to Display")
    error_msg
    # return error_msg
