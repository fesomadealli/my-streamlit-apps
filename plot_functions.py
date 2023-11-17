# Import streamlit 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Arc, Rectangle, Circle

# newline char
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

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

# Customizing plot order (for results) from the start
order = ['W', 'D', 'L']

# Figure Paddings         
pad_top = "\n\n"
pad_end = "\n\n"
hspace  = " "
vspace  = " "
newline = '\n'

# Define a function to extract the first four digits from the Date column 
# this is to enable us get the year alone and put it in a separate column 
import re
def extract_year(date_string):
    match = re.match(r"\d{4}", date_string)
    if match:
        return match.group()
    else:
        return None
    
# Reorder Columns 
def reorder_columns(dataframe, col_name, new_position):
    """Reorder a dataframe's column.

    Args:
        dataframe (pd.DataFrame): dataframe to use
        col_name (string): column name to move
        position (0-indexed position): where to relocate column to

    Returns:
        pd.DataFrame: re-assigned dataframe
    """
    temp_col = dataframe[col_name]
    dataframe = dataframe.drop(columns=[col_name])
    dataframe.insert(loc=new_position, column=col_name, value=temp_col)

    return dataframe

# Import Dataset
@st.cache(allow_output_mutation=False)
def load_dataset():
    df = pd.read_csv("assets/oau-giants.csv")
    #  Drop 'Unnamed:0' column
    df = df.drop(columns=['Unnamed: 0'])
    # String Variables
    df[['Date','Time','Venue','CompID','Competition',
                'Tie','TieDescr','MatchID','HomeTeam','AwayTeam',
                'MatchRemarks', 'Note', 'GScorers(Info)', 'MOTM']] = df[['Date','Time','Venue','CompID','Competition',
                                                                                'Tie','TieDescr','MatchID','HomeTeam','AwayTeam',
                                                                                'MatchRemarks', 'Note', 'GScorers(Info)', 'MOTM']].astype(str)
    # Categorical Variables
    df[['CompGroup','HTR','FTR','PSHTR']] = df[['CompGroup','HTR','FTR','PSHTR']].astype("category")
    # Numeric Variables
    df[['HTHG','HTAG','FTHG','FTAG','PENHG','PENAG']] = df[['HTHG','HTAG','FTHG','FTAG','PENHG','PENAG']].astype('int32')
    
    # Apply the function to the 'Date' column and create a new column called 'Year'
    df['Year'] = df['Date'].apply(extract_year)
    # put the Year column in front of the Date column
    df = reorder_columns(dataframe=df, col_name='Year', new_position=0)

    return df

oau_giants = load_dataset()

# Hide Spines in Streamlit
def hide_spines(axes, which_spine):
    spines = ['top', 'bottom', 'left', 'right']
    error_msg = (f"**Invalid spine selection:** '{which_spine}'. Please select from: {spines}")
                
    if which_spine != 'all':
        if type(which_spine) == list:
            for i in range(len(which_spine)):
                spine = which_spine[i]
                if spine in spines:
                    # Hide the enlisted spines
                    axes.spines[spine].set_visible(False)
                else:
                    st.write(error_msg)

        elif type(which_spine) == str:
            if which_spine in spines:
                axes.spines[which_spine].set_visible(False)
            else:
                st.write(error_msg)
    else:
        # Hide all spines
        for spine in range(len(spines)):
            axes.spines[spines[spine]].set_visible(False)

# Honors Won
def Honors_Won():
    # Creating the Honors Dataframe
    honors_df = oau_giants[(oau_giants['CompGroup'] != 'PreNUGA') &
                            (oau_giants['Tie']=='Final') | (oau_giants['Tie']=='3rd Place') | 
                            (oau_giants['TieDescr']=='Final') | (oau_giants['TieDescr']=='3rd Place')]
    
    honors_df.reset_index(drop=True, inplace=True)
    # Tidying some ends for data consistency
    #Changing Ties to 3rd Place at rows 4 & 6 respectively
    honors_df.at[4, 'Tie'] = '3rd Place'
    honors_df.at[6, 'Tie'] = '3rd Place'
    #Changing TieDescr to Super 4 at rows 4 & 6 respectively
    honors_df.at[4, 'TieDescr'] = 'Super 4'
    honors_df.at[6, 'TieDescr'] = 'Super 4'
    
    # Create empty dictionary
    finals_dict = {}
    
    # populating the dictionary
    #  Total Num of Finals Played - Main Finals & Third Place
    finals_dict['Honors Contested'] = len(honors_df)
    
    # Getting number of games played in Finals & 3rd Place contests
    h = honors_df.Tie.value_counts().reset_index()
    h = h.rename(columns={'count' : 'Matches'})
    
    for i in range(len(h)):
        finals_dict[str(h['Tie'][i] + ' Played')] = h['Matches'][i]
        
    # Split dfs    
    # Finals
    finals_df = honors_df[(honors_df['Tie'] == 'Final')]
    
    res_f = finals_df.FTR.value_counts().loc[order].reset_index()
    for i in range(len(res_f)):
        finals_dict['Final ('+ str(res_f['FTR'][i]) +')'] = res_f['count'][i]
    
    
    #  3rd Place Playoffs  
    third_place_df = honors_df[(honors_df['Tie'] == '3rd Place')]   
    
    res_3rd = third_place_df.FTR.value_counts().loc[order].reset_index()
    for i in range(len(res_3rd)):
        finals_dict['3rd Place ('+ str(res_3rd['FTR'][i]) +')'] = res_3rd['count'][i]   
    
    # Adding Penalty Records
    #  For PSHTR in Finals
    f = finals_df.PSHTR.value_counts().reset_index()
    for i in range(len(f)): 
            finals_dict['Final PSHT (' + str(f['PSHTR'][i] + ')')] = f['count'][i]
            
    #  For PSHTR in Third Place Contests
    t = third_place_df.PSHTR.value_counts().reset_index()
    for i in range(len(t)):
            finals_dict['3rd Place PSHT (' + str(t['PSHTR'][i] + ')')] = t['count'][i]
    
    # Just a check
    # finals_dict
    
    #  Setting up Figure & Axes
    fig, ax = plt.subplots(figsize=(12, 4), facecolor=facecolor)
    ax.set(facecolor=facecolor, xticks=([]), yticks=([]))
    hide_spines(axes=ax, which_spine='all')
    
    # Creating the Podium 
    pod_second = Rectangle((0.2,.5),.2,.15, fc='grey', ec='grey')
    pod_first = Rectangle((0.4,.5),.2,.25, fc='grey', ec='grey')
    pod_third = Rectangle((0.6,.5),.2,.1, fc='grey', ec='grey')
    
    podium = [pod_third, pod_first, pod_second]
    for part in podium:
        ax.add_patch(part)
    
    # Podium Labels
    ax.text(x=.3, y= .4, s='Silver', color='grey', ha='center',
                va='center', font=b_font, fontsize=10, zorder=2)
    ax.text(x=.5, y= .4, s='Gold', color='grey', ha='center',
                va='center', font=b_font, fontsize=10, zorder=2)
    ax.text(x=.7, y= .4, s='Bronze', color='grey', ha='center',
                va='center', font=b_font, fontsize=10, zorder=2)
    
    # Annotations
    # Text for count Honors Won (get() method has been set to return 0 for absent keys)
    gold_medals = finals_dict.get('Final (W)', 0) + finals_dict.get('Final PSHT (W)', 0)
    silver_medals = finals_dict.get('Final (L)', 0) + finals_dict.get('Final PSHT (L)', 0)
    bronze_medals = finals_dict.get('3rd Place (W)', 0) + finals_dict.get('3rd Place PSHT (W)', 0)
    
    ax.text(x=.3, y= .7, s=f'{silver_medals}', color=plot_color, ha='center',
                va='center', font=t_font, fontweight='bold', fontsize=18, zorder=2)
    ax.text(x=.5, y= .8, s=f'{gold_medals}', color=plot_color, ha='center',
                va='center', font=t_font, fontweight='bold', fontsize=18, zorder=2)
    ax.text(x=.7, y= .7, s=f'{bronze_medals}', color=plot_color, ha='center',
                va='center', font=t_font, fontweight='bold', fontsize=18, zorder=2)
    
    # Title Text
    custom_space = " " #Needed cause of the behavioral ppts highlight-text on \n
    title_text = (f"A PODIUM PLOT OF THE <HONORS WON> BY {team} UNDER {coach.upper()}\n"
                    f"\n\n{custom_space*30} ({data_span})")
    h_fig(x=.20, y=1.1, s=title_text, color=off_white, highlight_textprops=[{'color':plot_color}],
        font=t_font, fontsize=13, fontweight='bold', zorder=2)
    
    # Total Honor Wons
    total_honors = gold_medals + silver_medals + bronze_medals
    t_hnr_txt = f'<Total Honors:> {total_honors}'
    # h_fig(x=.45, y=.90, s=t_hnr_txt, color='grey', highlight_textprops=[{'color':'grey'}],
    #        font=t_font, fontsize=13, fontweight='bold', zorder=2)
    
    # Additional Text
    brkdwn_txt = '\n'.join([f'{key} : {value}' for key, value in finals_dict.items()])
    # Split the string into four smaller parts
    parts = brkdwn_txt.split('\n')
    
    # Join in threes and format as strings
    brkdwn_txt_1 = '\n'.join(parts[:3])
    brkdwn_txt_2 = '\n'.join(parts[3:6])
    brkdwn_txt_3 = '\n'.join(parts[6:9])
    brkdwn_txt_4 = '\n'.join(parts[9:])
    
    brkdwn_txt1 = fig.text(x=0.25, y= 0.25, s=f'{brkdwn_txt_1}', color=off_white, linespacing= 2,
                    ha='left', va='top', font=b_font, fontsize=10, zorder=2)
    brkdwn_txt2 = fig.text(x=0.42, y= 0.25, s=f'{brkdwn_txt_2}', color=off_white, linespacing= 2,
                    ha='left', va='top', font=b_font, fontsize=10, zorder=2)
    brkdwn_txt3 = fig.text(x=0.54, y= 0.25, s=f'{brkdwn_txt_3}', color=off_white, linespacing= 2,
                    ha='left', va='top', font=b_font, fontsize=10, zorder=2)
    brkdwn_txt4 = fig.text(x=0.67, y= 0.25, s=f'{brkdwn_txt_4}', color=off_white, linespacing= 2,
                    ha='left', va='top', font=b_font, fontsize=10, zorder=2)
    
    brkdwn_txt1.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    brkdwn_txt2.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    brkdwn_txt3.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    brkdwn_txt4.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    
    #  Name Text
    name_text = fig.text(x=0.52, y= -.10, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=10, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    
    # Figure Paddings 
    # Pad Top 
    fig.text(x=0.5, y= 1.13, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    fig.text(x=0.5, y= -.10, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

# Loading Results Dataset
def load_data(pref_df=None):
    # Results df
    results = pd.read_csv('assets/results_df.csv')
    #  Drop 'Unnamed:0' column
    results = results.drop(columns=['Unnamed: 0'])
    # Home Games df
    home_games = pd.read_csv("assets/h_games.csv")
    # Goals df
    goals = pd.read_csv("assets/goals_df.csv")
    
    if pref_df is not None:
        if pref_df == "results":
            return results
        elif pref_df == "home_games":
            return home_games
        elif pref_df == "goals":
            return goals
    else:
        return results, home_games, goals

results_df, h_games, goals_df = load_data()

# Oppositions Faced
def Teams_Faced():
    # Further Processing for Plotting
    h_teams = results_df.HomeTeam.to_list()
    a_teams = results_df.AwayTeam.to_list()

    # Value Counts 
    results_df.HomeTeam.value_counts().reset_index()
    results_df.AwayTeam.value_counts().reset_index()

    # Remove leading and trailing whitespaces from 'HomeTeam' column
    results_df['HomeTeam'] = results_df.HomeTeam.str.strip()
    results_df.HomeTeam.value_counts()

    # Remove leading and trailing whitespaces from 'AwayTeam' column
    results_df['AwayTeam'] = results_df.AwayTeam.str.strip()
    results_df.AwayTeam.value_counts()

    # Define a dictionary to map the items to the common name
    replacement_dict = {'UAM Tillers' : 'UAM'  ,      
                        'UNILORIN Warriors' : 'UNILORIN',   
                        'UI Pioneers' : 'UI',
                        'LASU Blazers' : 'LASU'  ,       
                        'AAUA Luminaries' : 'AAUA'
                        }

    # Replace the items in 'AwayTeam' Column with the common name using replace
    results_df['AwayTeam'] = results_df['AwayTeam'].replace(replacement_dict)

    # Replace the items in 'HomeTeam' Column with the common name using replace
    results_df['HomeTeam'] = results_df['HomeTeam'].replace(replacement_dict) 

    # A comprehensive list of all teams featured in the dataset (approved matches)
    teams_list = results_df.HomeTeam.to_list() + results_df.AwayTeam.to_list()

    # Teams in the Dataset
    teams = set(teams_list) 

    # Total Num of Teams Faced
    opp_faced = len(teams) - 1

    # Filter the list to only include items that occur more than once
    opp_freq = [team for team in teams_list if (teams_list.count(team) > 2) & (team != 'OAU Giants')]
    teams_face_more_than2 = set(opp_freq)

    # Let's save a list of Top 10 Teams faced, we will need it later
    top_ten_oppnt = list(teams_face_more_than2)

    # Setting up the Figure
    fig, ax = plt.subplots(1,1, figsize=(12,8), facecolor=facecolor)

    # Axes customization
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_xlim(-4, 12)
    ax.axis('off')

    # Specfiy axis labels
    ax.set_facecolor(facecolor) #'#18191A' '#303233'
    # ax.spines[['top','bottom','left','right']].set_visible(False)

    # Calculating the number of meetings with each team in the list
    unique_items, item_counts = np.unique(opp_freq, return_counts=True)

    # Sort Teams descending order of meetings
    sorted_indices = np.argsort(item_counts)[::-1]
    unique_items = unique_items[sorted_indices]
    item_counts = item_counts[sorted_indices]

    # Adding Plot
    sns.countplot(ax=ax, y=opp_freq, order=unique_items,
                facecolor='grey', edgecolor="none", linewidth=.5, alpha=.7);

    title_text = (f"TOP 10 <MOST FACED TEAMS> IN ALL COMPS BY {coach.upper()} WITH {team}\n"
                f"\n\n{hspace*30} ({data_span})")
    h_fig(x=0.13, y=1.03, s=title_text, color=off_white, highlight_textprops=[{'color':plot_color}],
        font=t_font, fontsize=15, fontweight='bold', zorder=2)

    #  Alt Name Text
    name_text = ax.text(x=9.0, y= 8.8, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=13, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    #  FIGURE PADDING
    # Pad Top 
    fig.text(x=0.5, y= 1.01, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    fig.text(x=0.5, y= 0.2, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    ## Pad left
    fig.text(x=-.01, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Right 
    fig.text(x=0.97, y=0, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    # ANNOTATIONS
    # The Teams to be labelled on the left of the Spines
    tten_opp = list(unique_items)
    
    txt_offset = .4 # Distance of the text from the height of the bar
    x_origin = 0
    vspacing = 0

    for i in range(len(tten_opp)):
        label = ax.text(x=-.5, y= vspacing, s=f'{tten_opp[i]}', ha='right', va='center', fontweight='medium',
                    font=b_font, color=plot_color, fontsize=12, zorder=2)
        label.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=plot_color), 
                                path_effects.Normal()])
        # Text to the rightmost part of the plot
        bar_height = opp_freq.count(tten_opp[i])
        num_of_meetings = bar_height # Since the plot was made by how many times they faced each other
        hspacing = x_origin + bar_height + txt_offset
        meetings = ax.text(x=hspacing, y=vspacing, s=f'{num_of_meetings}', ha='left', va='center',
                        fontweight='medium', font=b_font, color=off_white, fontsize=12, zorder=2)
        meetings.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
        
        vspacing +=1

    # Create custom left spine   
    custom_lspine = plt.Rectangle((0,-1), 0, 12, edgecolor='grey', linewidth=.8)
    opp_count_circle = plt.Circle((9,6), .7, edgecolor='grey', facecolor=facecolor, linewidth=.8)

    Patches = [custom_lspine, opp_count_circle]
    for patch in Patches:
        ax.add_patch(patch)

    # In-Circle Text
    crc_text = ax.text(x=9, y=6.0, s=opp_faced, ha='center', va='center', fontweight='bold',
                    font=t_font, color=plot_color, fontsize=18, zorder=2)
    crc_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Circle label 
    circle_label_txt = "Total Number of Teams Faced\n(Walkover & Abandoned ties are excluded)"
    crc_lbl = ax.text(x=9, y=7.5, s=circle_label_txt, ha='center', va='center', fontweight='medium',
                    font=b_font, color=off_white, fontsize=12, zorder=2) 
    crc_lbl.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    return fig

# 
def Games_Played():
    # Games Played Each Year
    gms_per_year = oau_giants['Year'].value_counts().reset_index()

    # Figure
    fig, ax = plt.subplots(1,1, figsize=(8,3), facecolor=facecolor)#, layout= 'constrained')

    ax.set_ylim(0, 20)
    ax.set_facecolor(ax_color)
    # ax.axis('off')
    ax.tick_params(axis='both', colors=off_white)
        
    #specify axis labels
    ax.set_facecolor(facecolor)
    hide_spines(axes=ax, which_spine='all')

    # Create a horizontal barplot with Seaborn on the ax 
    ax_plt = sns.barplot(y=gms_per_year['count']*.5, x=gms_per_year['Year'], ax=ax, color=plot_color)

    # Axes customization
    ax_plt.set(xlabel=None,  ylabel=None, yticks=([]))

    # # Add values at the end of each bar
    for i, v in enumerate(gms_per_year['count']*.5):
        gms_cnt = ax.text(i-.1, v+1.25, str(int(v*2)), va='center', color=off_white, fontweight='semibold',
                        font=t_font, fontsize=12);
        gms_cnt.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Adding Plot
    title_text = (f"<GAMES PLAYED IN COMPS> PER YEAR BY {team} ({data_span})")
    h_fig(x=0.16, y=1.03, s=title_text, color=off_white, highlight_textprops=[{'color':plot_color}],
        font=t_font, fontsize=12, fontweight='bold', zorder=2)

    #  Alt Name Text
    name_text = ax.text(x=9.0, y= 12.8, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=9, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    #  FIGURE PADDING
    # Pad Bottom
    fig.text(x=0.5, y= 0.2, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad left
    fig.text(x=-.01, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Right 
    fig.text(x=0.97, y=0, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    
    plt.tight_layout()

    return fig

# Confirm that a fixture (agains an opponent) was played on Homeground
def confirm_fixture_on_homeground(select_opponent):
    fixture = False
    teams_faced_at_home = list(h_games.Opponent.unique())
    
    for i in range(len(teams_faced_at_home)):
        if teams_faced_at_home[i] == select_opponent:
            fixture = True
            break
        else:
            i +=1
            
    return fixture

# Competitions involved in Result Percentage Plots
def get_comps(df):
    comps = " "
    x = df.CompGroup.unique()
    for i in range(len(x)):
        if i != len(x) - 1:
            comps += str(x[i]) + ', '
        else:
            comps += str(x[i]) + '.'
    #print('Games played at competitions include:', comps) #Uncomment to test success
    return comps

# Result Percentages
def Results_Pct(select_opponent, select_period, select_range):
    """
    Possible Func Mods: select_opponent, select_period (optional: select_df to Use)

    select_opponent: All_teams | Oppnt_name
    select_period: FTR | HTR | SHR
    select_range: All_Games | Home_Games
    """
    plot_results = True
    
    if select_range == 'Home_Games':
        if select_opponent != 'All_teams':
            if confirm_fixture_on_homeground(select_opponent) is False:
                return(f"No Meetings With {select_opponent} on Homeground")
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
            hide_spines(axes=ax[i], which_spine="all")
           
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
        gms_incl = get_comps(df)
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
        return fig

    else:
        error_msg = ("No Plot to Display")
        return error_msg

# Further processing for correlation analysis
def prep_corr_data(df):
    # Full Time
    ft_conditions = [#When FTR is W  | #When FTR is D  | #When FTR is L
                     (df['FTR']=='W'), (df['FTR']=='D'), (df['FTR']=='L')
                    ]
    # Halftime
    ht_conditions = [#When HTR is W  | #When HTR is D  | #When HTR is L
                     (df['HTR']=='W'), (df['HTR']=='D'), (df['HTR']=='L')
                    ]
    # Second Half
    sh_conditions = [#When SHR is W  | #When SHR is D  | #When SHR is L
                     (df['SHR']=='W'), (df['SHR']=='D'), (df['SHR']=='L')
                    ]

    # Wins=1, Draws=0.5 and Losses=0
    values = [1, .5, 0]

    # Creating the columns for Results
    df['Ftr'] = np.select(ft_conditions, values)
    df['Htr'] = np.select(ht_conditions, values)
    df['Shr'] = np.select(sh_conditions, values)

    return df

# Correlation Heatmap
def Corr_Heatmap(select_range, corr_type):
    """
    select_range: All_Games or Home_Games (Based on selection, Corr. is computed across All Comps)
    corr_type: goals_corr or results_corr
    """
    if not isinstance(select_range, str):
        raise ValueError("Correlation range must be a string. Please enter a string only.")
    
    # Checking what range was added
    if select_range == 'Home_Games':
        df = h_games.copy()
        corr_title = f'CORRELATION HEATMAP OF {team} MATCHES ON HOMEGROUND'
        
    elif select_range == 'All_Games':
        df = goals_df.copy()
        corr_title = f'CORRELATION HEATMAP OF {team} MATCHES'
        
    df = prep_corr_data(df)


    # Create Figure & Subplots
    fig, ax = plt.subplots(1,1, figsize=(6,6), facecolor=facecolor)
    fig.tight_layout(h_pad=6.5)
    
    # Correlation Type
    if corr_type == "goals_corr":
        # Correlation Heatmap of Goals in Each Half & the Fulltime Results
        gls_corr = df[['HTTG', 'HTOG', 'SHTG', 'SHOG', 'Ftr']].corr()
        sns.heatmap(gls_corr, ax=ax, annot=True, cmap='Blues', cbar=False)
        endnote_text = (f"ALL COMPS ({data_span})\n"
                        f"{add_note}\n"
                         "Ftr — Fulltime Results\n"
                         "SHTG: Second Half Team Goals | HTTG: Halftime Team Goals\n"
                         "SHOG: Second Half Opponent Goals | HTOG: Halftime Opponent Goals")
        # Axes Title
        ax_title = 'Goals Per Half & Fulltime Result'
            
    elif corr_type == "results_corr":
        # Correlation Heatmap of Results in Each Half & the Fulltime Results
        half_corr = df[['Htr', 'Shr', 'Ftr']].corr()
        sns.heatmap(half_corr, ax=ax, annot=True, cmap='Blues', cbar=False)  
        endnote_text = (f"ALL COMPS ({data_span})\n"
                        f"{add_note}\n"
                        f"Ftr — Fulltime Results{vspace*2}|"
                        f"{vspace*3}Htr — Halftime Results{vspace*2}|"
                        f"{vspace*2}Shr — Second Half Results")
        # Axes Title
        ax_title = 'Outcome Per Half & Fulltime Result'
        
    # Positioning Title
    axes_title = ax.set_title(ax_title, color=off_white,
                                fontsize=10, font=b_font, fontweight='medium')
    axes_title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    # ax tick text colors
    ax.tick_params(axis='both', colors=off_white)

    # ANNOTATIONS
    # Title
    title = fig.text(x=0.51, y= 1.08, s=corr_title.upper(), ha='center', va='center', linespacing=2.2,
                        font=t_font, color=off_white, fontweight='semibold', fontsize=12, zorder=2)
    title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                            path_effects.Normal()])

    # Endnote Text
    endnote = fig.text(x=0.51, y=-.13, s=endnote_text, ha='center', va='center',
                       font=b_font, linespacing=2.3, color='grey', alpha=1, fontsize=10, zorder=2)
    endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])       

    # FIGURE PADDING
    # Pad Top 
    fig.text(x=0.5, y= 1.09, s=pad_top, color=off_white, linespacing= 2, ha='center',
                                            va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    fig.text(x=0.5, y= -0.28, s=pad_end, color=facecolor, linespacing= 2, ha='center',
                                            va='center', font=b_font, fontsize=b_fsize, zorder=2)
    ## Pad left
    fig.text(x=-.01, y= 1.15, s=hspace, color=facecolor, linespacing= 2, ha='center',
                                            va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Right 
    fig.text(x=1.03, y=1.15, s=hspace, color=facecolor, linespacing= 2, ha='center',
                                            va='center', font=b_font, fontsize=b_fsize, zorder=2)

    #  Name Text
    name_text = fig.text(x=0.51, y= -.28, s=author, ha='center', va='center', 
                        font=b_font, color=plot_color, alpha=.3, fontsize=10, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    return fig

def confirm_comp_on_homeground(select_comp):
    home_match_in_comp = False
    comps_playd_at_home = list(h_games.CompGroup.unique())
    
    for i in range(len(comps_playd_at_home)):
        if comps_playd_at_home[i] == select_comp:
            home_match_in_comp = True
            break
        else:
            i +=1
            
    return home_match_in_comp

def Common_Scoreline(select_opponent, select_period, select_range, select_comp=None):
    # Error checking
    if not isinstance(select_opponent, str):
        raise ValueError("Opponent name must be a string. Please enter a string only.")
    if not isinstance(select_period, str):
        raise ValueError("Period must be a string. Please enter a string only.")
    if not isinstance(select_range, str):
        raise ValueError("select_df must be a string. Please enter a string only.")
    
    # Check range of data to use
    if select_range == 'Home_Games':
        gls_df = h_games.copy()
        
    elif select_range == 'All_Games':
        gls_df = goals_df.copy()
        
        
    # Check if an Opponent is selected
    if select_opponent != 'All_teams':
        gls_df = gls_df[gls_df['Opponent'] == select_opponent].reset_index(drop=True)
        select_comp = None
    
    # Check if a Competition is specified
    if select_comp is not None:
        if select_range == 'Home_Games':
            if confirm_comp_on_homeground(select_comp) is True:
                gls_df = gls_df[gls_df['CompGroup'] == select_comp].reset_index(drop=True)
            else:
                return (f'No Fixture was held on the {team} Homeground at the {select_comp}')
        else:
            gls_df = gls_df[gls_df['CompGroup'] == select_comp].reset_index(drop=True)

    # Check to see which period we're working with
    if select_period =='HTR':
        # affected df cols
        team_col = 'HTTG'
        oppnt_col = 'HTOG'
        # cols to fetch data
        team_data = gls_df['HTTG']
        opp_data = gls_df['HTOG']
        # Get the maximum values of FTTG and FTOG
        max_fttg = max(gls_df['HTTG'])
        max_ftog = max(gls_df['HTOG'])
        #Get Threshold for Text Label Color
        threshold_df = gls_df[['HTTG', 'HTOG']].value_counts().reset_index()        
        
    elif select_period == 'SHR':
        # affected df cols
        team_col = 'SHTG'
        oppnt_col = 'SHOG'
        # cols to fetch data
        team_data = gls_df['SHTG']
        opp_data = gls_df['SHOG']
        # Get the maximum values of FTTG and FTOG
        max_fttg = max(gls_df['SHTG'])
        max_ftog = max(gls_df['SHOG'])
        # Get Threshold for Text Label Color
        threshold_df = gls_df[['SHTG', 'SHOG']].value_counts().reset_index()

    else:
        # affected df cols
        team_col = 'FTTG'
        oppnt_col = 'FTOG'
        # cols to fetch data
        team_data = gls_df['FTTG']
        opp_data = gls_df['FTOG']
        # Get the maximum values of FTTG and FTOG
        max_fttg = max(gls_df['FTTG'])
        max_ftog = max(gls_df['FTOG'])
        # Get Threshold for Text Label Color
        threshold_df = gls_df[['FTTG', 'FTOG']].value_counts().reset_index()
         
    # Create the figure 
    fig, ax = plt.subplots(1,1, figsize=(10, 6), facecolor=facecolor)
    # Create a 2D histogram
    heatmap, xedges, yedges = np.histogram2d(team_data, opp_data,
                                             bins=(np.arange(max_fttg + 2), np.arange(max_ftog + 2)))

    # Define a custom colormap with darkgreen
    cmap = plt.get_cmap('Blues')#.copy()
    #cmap.set_under(color=ax_color)
    
    # ax tick text xolors
    ax.tick_params(axis='both', colors=off_white)
    hide_spines(axes=ax, which_spine="all")
    
    # Plot the heatmap
    plt.imshow(heatmap.T, cmap=cmap, vmin=0, vmax=np.max(heatmap), origin='lower', interpolation='none')
        
    # Set xticks and yticks to match the range of possible scorelines
    plt.xticks(np.arange(max_fttg + 1))
    plt.yticks(np.arange(max_ftog + 1))

    
    # Show the colorbar with reversed intensity
    cbar = plt.colorbar(label='Frequency', orientation='vertical', extend='max')
    # Set text properties for colorbar labels
    cbar.ax.set_ylabel('Num of Matches', rotation=270, labelpad=20,
                       fontsize=12, font=t_font, color=off_white)
    
    cbar.ax.tick_params(axis='y', colors=off_white)
    cbar_spines = ['top','bottom','left','right']
    for spine in cbar_spines:
        cbar.ax.spines[spine].set_visible(False)
    
    # Geting the cbar ticks  
    tick_values = cbar.get_ticks()
    # Threshold for adjusting text color based on intensity of cell
    threshold = int(max(tick_values)/2)
       
    # Print the frequency on top of each cell
    for i in range(len(xedges) - 1):
        for j in range(len(yedges) - 1):
            if len(gls_df[(gls_df[f'{team_col}'] == i) & (gls_df[f'{oppnt_col}'] == j)]) < threshold:
                cnt_color = 'black'
            else:
                cnt_color = off_white
            if heatmap[i, j] != 0:
                match_cnt = ax.text(i+0.03, j+0.03, int(heatmap[i, j]), color=cnt_color,
                                    ha='center', va='center', fontsize=14, font=b_font, fontweight='bold')
                match_cnt.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                                path_effects.Normal()])

    
   # Add labels and title
    _ylabel = ' '
    _xlabel = 'Goals Scored (Team OAU)'
    
    if select_range == 'Home_Games':
        if select_opponent != 'All_teams':
            _ylabel = f'Goals Scored\n({select_opponent})'
            title_text = (f'COMMON {select_period} BETWEEN TEAM OAU AND {select_opponent.upper()}\n'
                          f'{hspace*5} IN GAMES PLAYED AT THE {team} HOMEGROUND')
    
        elif select_opponent == 'All_teams':
            _ylabel = 'Goals\nConceeded'
            if select_comp is not None:
                title_text = (f'COMMON {select_period} AT THE {team} HOMEGROUND BETWEEN TEAM OAU AND\n'
                              f'ALL TEAMS FACED AT THE {select_comp.upper()} ({data_span})')
            else:
                title_text = f'COMMON {select_period} ON HOMEGROUND BETWEEN TEAM OAU AND\n ALL TEAMS FACED ({data_span})'
    
    if select_range == 'All_Games':
        if select_opponent != 'All_teams':
            _ylabel = f'Goals Scored\n({select_opponent})'
            title_text = (f'COMMON {select_period} BETWEEN {team} AND {select_opponent.upper()}\n'
                          f'{hspace*5} IN ALL MEETINGS EVER')
    
        elif select_opponent == 'All_teams':
            _ylabel = 'Goals\nConceeded'
            if select_comp is not None:
                title_text = (f'COMMON {select_period} BETWEEN {team} AND ALL TEAMS FACED AT\n'
                              f'{hspace*5}THE {select_comp.upper()} ({data_span})')
            else:
                title_text = (f'COMMON {select_period} BETWEEN TEAM OAU AND ALL TEAMS FACED\n'
                             f'{hspace*2}IN ALL COMPETITIONS ({data_span})')
    
    # ANNOTATIONS    
    # ylabel Text
    ylabel_text= fig.text(x=0.02, y= .50, s=_ylabel, ha='center', va='center', linespacing=2.2,
                   font=t_font, color=off_white, fontweight='semibold', fontsize=12, zorder=2)
    ylabel_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                            path_effects.Normal()])    
    
    # xlabel Text
    xlabel_text= fig.text(x=.45, y=0, s=_xlabel, ha='center', va='center', linespacing=2.2,
                   font=t_font, color=off_white, fontweight='semibold', fontsize=12, zorder=2)
    xlabel_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                            path_effects.Normal()])    
        
    # Title Text
    title = fig.text(x=0.48, y=1.0, s=title_text, ha='center', va='center', linespacing=2.2,
                   font=t_font, color=off_white, fontweight='semibold', fontsize=14, zorder=2)
    title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                            path_effects.Normal()])
    
    # Endnote Text
    if select_period == 'HTR':
        endnote_text = (f"HTR — Halftime Results\n{add_note}")
    elif select_period == 'SHR':
        endnote_text = (f"SHR — Second Half Results\n{add_note}")
    else:
        endnote_text = (f"FTR — Fulltime Results\n{add_note}") 
    
    endnote = fig.text(x=0.45, y=-.13, s=endnote_text, ha='center', va='center',
                       font=b_font, linespacing=2, color='grey', alpha=1, fontsize=12, zorder=2)
    endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                            path_effects.Normal()])
        
    #  Name Text
    name_text = fig.text(x=0.45, y=-.22, s=author, ha='center', va='center', 
                       font=b_font, color=plot_color, alpha=.3, fontsize=12, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Pad Top 
    fig.text(x=0.5, y= 0.01, s=pad_top, color=off_white, linespacing= 2, ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    fig.text(x=0.5, y= -.25, s=pad_end, color=facecolor, linespacing= 2, ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    ## Pad left
    fig.text(x=-.15, y= 1.15, s=hspace, color=facecolor, linespacing= 2, ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Right 
    fig.text(x=1.06, y=0, s=hspace, color=facecolor, linespacing= 2, ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

# Useful in Goals_Plot()
def reset_to_none(category, reset_others):
        if reset_others is True:
            if (category == 'All_Time') | (category == 'Homeground_Fixtures'):
                select_comp = select_opponent = select_edition = select_outcome = None

            if category == 'Per_Tournament':
                select_opponent = select_edition = None
                
            if category == 'Per_Comp_Edition':
                select_comp = select_opponent = select_outcome = None

            if category == 'Per_Opponent':
                select_edition = None #select_comp = select_outcome = None
        
            if (category == 'Per_Outcome_All_Games') | (category == 'Per_Outcome_Homeground_Fixtures'):
                select_comp = select_opponent = select_edition = None

def Goals_Plot(select_period, select_category, 
               select_comp=None, select_opponent=None, 
               select_edition=None, select_outcome=None):
    """
    Plot of Goals Scored against Goals Allowed with their respective Averages
    
    select_category: All_Time | Homeground_Fixtures | Per_Tournament | Per_Comp_Edition 
                     Per_Opponent | Per_Outcome_All_Games | Per_Outcome_Homeground_Fixtures
    select_opponent: All_teams | Oppnt_name
    select_period: FTR | HTR | SHR
    select_range: All_Games | Home_Games (--No real need to pass this in, `select_category` 
                                          --already covers for its (possible) unique occurences)
    select_outcome: All_Outcomes (default)| in_Wins (W) | in_Draws (D) | in_Losses (L)
    """
    
    proceed_to_plot = False
    bar_color = '#79A19D'
    
    if select_outcome == 'W':
        outcome = 'WINS'
    if select_outcome == 'D':
        outcome = 'DRAWS'
    if select_outcome == 'L':
        outcome = 'LOSSES'

    # ---------- ALL GAMES -----------     
    if select_category == 'All_Time':
        gls_plt_df = goals_df.copy()
        proceed_to_plot = True
        reset_to_none(category=select_category, reset_others=proceed_to_plot)
        title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} BASED ON {select_period}\n'
                     f'OF ALL MATCHES IN ALL COMPS')
    # ---------- HOMEGROUND FIXTURES -----------     
    if select_category == 'Homeground_Fixtures':
        gls_plt_df = h_games.copy()
        proceed_to_plot = True
        reset_to_none(category=select_category, reset_others=proceed_to_plot)
        title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} BASED ON {select_period}\n'
                     f'OF MATCHES PLAYED ON THEIR HOMEGROUND')
    # ---------- PER TOURNAMENT -----------     
    if select_category == 'Per_Tournament':
        if select_comp is not None:
            gls_plt_df = goals_df[goals_df['CompGroup']==select_comp]
            reset_to_none(category=select_category, reset_others=proceed_to_plot)
            if (select_outcome == "All_Outcomes") or (select_outcome==None):
                proceed_to_plot = True
                title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} BASED ON {select_period}\n'
                            f'AT THE {select_comp.upper()}')
            elif select_outcome is not None:
                gls_plt_df = gls_plt_df[gls_plt_df[f'{select_period}']==select_outcome]
                proceed_to_plot = True
                title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} (BASED ON {select_period})\n'
                            f'IN {outcome} AT THE {select_comp.upper()}')
                
        else:
            return ("No Competition Selected")
    # ---------- PER EDITION -----------
    if select_category == 'Per_Comp_Edition':
        if select_edition is not None:
            gls_plt_df = goals_df[goals_df['Competition']==select_edition]
            proceed_to_plot = True
            reset_to_none(category=select_category, reset_others=proceed_to_plot)
            title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} BASED ON {select_period}\n'
                         f'AT THE {select_edition}')
        else:
            return ("No Edition Selected")
    # ---------- PER OPPONENT ----------- 
    if select_category == 'Per_Opponent':
        if select_opponent is not None:
            #Games Versus Opponent Considering All Outcomes In All Competitions
            gls_plt_df = goals_df[goals_df['Opponent']==select_opponent] 
            proceed_to_plot = True
            reset_to_none(category=select_category, reset_others=proceed_to_plot)

            # checking for more filters
            if (select_comp is None) and (select_outcome is None): # same as default
                proceed_to_plot = True
                title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} BASED ON\n'
                            f'{select_period} IN ALL MATCHES AGAINST {select_opponent}')
            
            if select_comp is not None: #User has selected a Competition
                if select_comp in list(set(gls_plt_df.CompGroup.to_list())):
                    gls_plt_df = gls_plt_df[gls_plt_df['CompGroup'] == select_comp]
                    proceed_to_plot = True
                    if select_outcome is None: #User wants All Outcomes at that Competition
                        title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} AGAINST {select_opponent}\n'
                                    f'BASED ON {select_period} IN ALL MATCHES AT THE {select_comp}')
                    elif select_outcome is not None: #User wants a Preferred Outcome at that Competition
                        if select_outcome in list(set(gls_plt_df[f'{select_period}'].to_list())):
                            gls_plt_df = gls_plt_df[gls_plt_df[f'{select_period}'] == select_outcome]
                            proceed_to_plot = True
                            title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} IN {outcome} AGAINST {select_opponent}\n'
                                        f'BASED ON {select_period} OF MATCHES AT THE {select_comp}')
                        else:
                            proceed_to_plot = False
                            error_msg = (f'The {team} did not record any {outcome.lower()} in meetings with {select_opponent} at the {select_comp}')
                            return error_msg
                else:
                    proceed_to_plot = False
                    error_msg = (f"No meeting between {team} and {select_opponent} at the {select_comp}")
                    return error_msg
                                
            elif select_comp is None: #User has selected All Competitions
                if select_outcome is not None: #A Preferred Outcome has been selected
                    gls_plt_df = gls_plt_df[gls_plt_df[f'{select_period}'] == select_outcome]
                    proceed_to_plot = True
                    title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} IN {outcome} AGAINST {select_opponent}\n'
                                    f'BASED ON {select_period} OF MATCHES IN ALL COMPS')
        else:
            return("No Opponent Selected")   
    # ---------- PER OUTCOME IN ALL GAMES -----------     
    if select_category == 'Per_Outcome_All_Games':
        if select_outcome is not None:
            gls_plt_df = goals_df[goals_df[f'{select_period}']==select_outcome]
            proceed_to_plot = True
            reset_to_none(category=select_category, reset_others=proceed_to_plot)
            title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} IN {outcome}\n'
                         f'BASED ON {select_period} OF MATCHES IN ALL COMPS')
        else:
            return ("No Match Outcome Selected")
    # ---------- PER OUTCOME ON HOMEGROUND ----------- 
    if select_category == 'Per_Outcome_Homeground_Fixtures':
        if select_outcome is not None:
            gls_plt_df = h_games[h_games[f'{select_period}']==select_outcome]
            proceed_to_plot = True
            reset_to_none(category=select_category, reset_others=proceed_to_plot)
            title_txt = (f'GOALS SCORED vs. GOALS CONCEEDED BY {team} IN {outcome}\n'
                         f'BASED ON {select_period} OF GAMES PLAYED ON HOMEGROUND')
        else:
            return ("No Match Outcome Selected")
        
        
    if select_period == 'FTR':
        team_col = 'FTTG'
        opp_col =  'FTOG'
        add_descr = 'FTR — Full Time Results'
        
    if select_period == 'HTR':
        team_col = 'HTTG'
        opp_col =  'HTOG'
        add_descr = 'HTR — Halftime Results'
        
    if select_period == 'SHR':
        team_col = 'SHTG'
        opp_col =  'SHOG'
        add_descr = 'SHR — Second Half Results'
        
        
    if proceed_to_plot is True:    
        #figure parameters
        fig, ax = plt.subplots(1,1, figsize=(12,4), facecolor=facecolor)
            
        num_of_gms = len(gls_plt_df)
        # Goals Scored Vs Goals Conceeded
        label = ['Goals Scored', 'Goals Conceded']
        value = [(gls_plt_df[f'{team_col}'].sum())*.5, (gls_plt_df[f'{opp_col}'].sum())*.5]

        # Create a horizontal barplot with Seaborn on the ax with adjusted bar height
        sns.barplot(x=value, y=label, ax=ax, color=bar_color)

        # Add values at the end of each bar
        for i, v in enumerate(value):
            gls_cnt = ax.text(v+1, i, str(int(v*2)), va='center', color=off_white, fontweight='semibold',
                              font=t_font, fontsize=t_fsize);
            gls_cnt.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                      path_effects.Normal()])

        # Customize axis limits so plot can shrink sort of
        ax.set_xlim(0,50);
        # Shift the left spine (x-axis) to the right
        ax.spines['left'].set_position(('outward', 10))
        # ax tick text colors
        ax.tick_params(axis='y', colors=off_white, labelsize=b_fsize)
        # set facecolor for plot
        ax.set_facecolor(facecolor);
        # Turn off top and right spines
        spines = ['top', 'bottom', 'right','left']
        for spine in spines:
            ax.spines[spine].set_visible(False);
        # Set labels and title
        ax.set_xlabel('Num of Goals', color='grey', font=t_font, fontsize=b_fsize);
        ax.set_xticks([])
        ax.set_ylabel(' ');

        # Calculating Goals Scored & Goals Allowed Avg (Per Game)
        try:
            GF_Avg = round(int(value[0]*2)/len(gls_plt_df), 2)
            GA_Avg = round(int(value[1]*2)/len(gls_plt_df), 2)
        except ZeroDivisionError:
            return ("No match for this selection!")

        # Printing Goal Avgs
        if num_of_gms > 1:
            game_cnt_text = 'Games'
        else:
            game_cnt_text = 'Game'

        gls_text = (f'<Goals Scored Average:> {GF_Avg} | <Goals Allowed Average:> {GA_Avg}{newline*4}'
                    f'{hspace*22}({num_of_gms} {game_cnt_text})')
        h_fig(x=.20, y=-.23, s=gls_text, color=off_white, highlight_textprops=[ {'color': bar_color},
                                                                                {'color': bar_color}],
           font=t_font, fontsize=t_fsize, fontweight='bold', va='center', zorder=2)

        # ANOTATIONS
        # Title Text
        title = fig.text(x=0.51, y= 1.08, s=title_txt, ha='center', va='center', linespacing=2.2,
                                   font=t_font, color=off_white, fontweight='semibold', fontsize=t_fsize, zorder=2)
        title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                    path_effects.Normal()])
        # Endnote Text
        endnote_text = (f"{add_descr} ({data_span}){newline}{add_note}")
        endnote = fig.text(x=0.51, y=-.62, s=endnote_text, ha='center', va='center',
                               font=b_font, linespacing=2.3, color='grey', fontsize=b_fsize, zorder=2)
        endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                    path_effects.Normal()]) 
        #  Name Text
        name_text = fig.text(x=0.51, y= -.83, s=author, ha='center', va='center', 
                           font=b_font, color=plot_color, alpha=.3, fontsize=b_fsize, zorder=2)
        name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                    path_effects.Normal()])
        
        # PADDINGS
        # Figure Paddings
        fig.text(x=.51, y=1.12, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
        # Pad Right 
        fig.text(x=1.03, y=1.15, s=hspace, color=facecolor, linespacing= 2, ha='center',
                 va='center', font=b_font, fontsize=b_fsize, zorder=2)
        # Pad left
        fig.text(x=-.01, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
        # Pad Bottom
        fig.text(x=0.5, y= -0.84, s=pad_end, color=facecolor, linespacing= 2, ha='center',
                 va='center', font=b_font, fontsize=b_fsize, zorder=2)
       
        return fig
    
    else:
        error_msg = ("Please make a valid selection")
        return error_msg

def Goals_For_Top10():
    top_10_gf = goals_df.groupby('Opponent')['FTTG'].sum().reset_index(name='GF')
    # Sort the DataFrame by 'GF' column in descending order and select the top 10 rows
    top_10_gf = top_10_gf.sort_values(by='GF', ascending=False).head(10)

    x_col = top_10_gf['Opponent']
    y_col = top_10_gf['GF']*.5

    # Create a horizontal barplot
    fig = plt.figure(figsize=(8, 6), facecolor=facecolor)
    bars = plt.barh(x_col, y_col, color='grey')

    # Add count values at the end of each bar
    for i, v in enumerate(y_col):
        count = plt.text(v + .2, i, str(int(v*2)), va='center', color=off_white, font=b_font)
        count.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
        
    # Customize the appearance
    plt.xlabel(' ')
    plt.ylabel(' ')
    plt.gca().invert_yaxis()  # Invert the y-axis to display the highest value at the top
    plt.xlim(0, 10)  # Set the x-axis limits
    plt.gca().set_facecolor(facecolor)  # Set the facecolor to black
    plt.axis('on')
    spines = ['top','bottom','left','right']
    for spine in spines:
        plt.gca().spines[spine].set_visible(False)
    # Adjust the starting position of the left spine to move the plot to the right
    plt.gca().spines['left'].set_position(('outward', 5))
    # Adjust the position of tick labels to the right
    plt.tick_params(axis='y', pad=5)  # Increase the pad to shift labels to the right
    # Turn off xticks
    plt.xticks([])
    # Change yticks color to white and font size
    plt.yticks(color=plot_color, font=b_font, fontweight='bold', fontsize=10)
            
    # Set labels and title
    title_text = 'TOP 10 TEAMS SCORED AGAINST IN ALL COMPS'
    title = plt.text(x=4.0, y=-1.5, s=title_text, ha='center', va='center', fontweight='semibold',
                    font=t_font, color=plot_color, fontsize=12, zorder=2)
    title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Add an endnote and a name text 
    endnote_text = f"{add_note}"
    endnote = plt.text(x=6.3, y=8.0, s=endnote_text, ha='center', va='center', fontweight='medium',
                    font=b_font, color=off_white, fontsize=9, zorder=2) 
    endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    #  Alt Name Text
    name_text = plt.text(x=6.2, y= 8.5, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=9, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    #  FIGURE PADDING
    # Pad Top 
    plt.text(x=0.5, y=-1.5, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    plt.text(x=0.5, y= 1.02, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad left
    plt.text(x=-2.09, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

def Goals_Allowed_Top10():
    top_10_ga = goals_df.groupby('Opponent')['FTOG'].sum().reset_index(name='GA')
    # Sort the DataFrame by 'GA' column in descending order and select the top 10 rows
    top_10_ga = top_10_ga.sort_values(by='GA', ascending=False).head(10)

    x_col = top_10_ga['Opponent']
    y_col = top_10_ga['GA']

    # Create a horizontal barplot
    fig = plt.figure(figsize=(8, 6), facecolor=facecolor)
    bars = plt.barh(x_col, y_col*.5, color='grey')

    # Add count values at the end of each bar
    for i, v in enumerate(y_col*.5):
        count = plt.text(v+.3, i, str(int(v*2)), va='center', color=off_white, font=b_font)
        count.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
        
    # Customize the appearance
    plt.xlabel(' ')
    plt.ylabel(' ')
    plt.gca().invert_yaxis()  # Invert the y-axis to display the highest value at the top
    plt.xlim(0, 10)  # Set the x-axis limits
    plt.gca().set_facecolor(facecolor)  # Set the facecolor to black
    plt.axis('on')
    spines = ['top','bottom','left','right']
    for spine in spines:
        plt.gca().spines[spine].set_visible(False)
    # Adjust the starting position of the left spine to move the plot to the right
    plt.gca().spines['left'].set_position(('outward', 5))
    # Turn off xticks
    plt.xticks([])
    # Change yticks color to white and font size
    plt.yticks(color=plot_color, font=b_font, fontweight='bold', fontsize=10)
            

    # Set labels and title
    title_text = 'TOP 10 TEAMS (GOALS ALLOWED) IN ALL COMPS'
    title = plt.text(x=4.0, y=-1.5, s=title_text, ha='center', va='center', fontweight='semibold',
                    font=t_font, color=plot_color, fontsize=12, zorder=2)
    title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Add an endnote and a name text 
    endnote_text = f"{add_note}"
    endnote = plt.text(x=6.3, y=8.0, s=endnote_text, ha='center', va='center', fontweight='medium',
                    font=b_font, color=off_white, fontsize=9, zorder=2) 
    endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    #  Alt Name Text
    name_text = plt.text(x=6.2, y=8.5, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=9, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])


    #  FIGURE PADDING
    # Pad Top 
    plt.text(x=0.5, y=-1.5, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    plt.text(x=0.5, y= 1.02, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad left
    plt.text(x=-2.09, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

def Home_Goals_For_Top10():
    top_10_hgf = h_games.groupby('Opponent')['FTTG'].sum().reset_index(name='GF')
    # Sort the DataFrame by 'GF' column in descending order and select the top 10 rows
    top_10_hgf = top_10_hgf.sort_values(by='GF', ascending=False).head(10)

    x_col = top_10_hgf['Opponent']
    y_col = top_10_hgf['GF']*.5

    # Create a horizontal barplot
    fig = plt.figure(figsize=(8, 6), facecolor=facecolor)
    bars = plt.barh(x_col, y_col, color='grey')

    # Add count values at the end of each bar
    for i, v in enumerate(y_col):
        count = plt.text(v + .2, i, str(int(v*2)), va='center', color=off_white, font=b_font)
        count.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
        
    # Customize the appearance
    plt.xlabel(' ')
    plt.ylabel(' ')
    plt.gca().invert_yaxis()  # Invert the y-axis to display the highest value at the top
    plt.xlim(0, 10)  # Set the x-axis limits
    plt.gca().set_facecolor(facecolor)  # Set the facecolor to black
    plt.axis('on')
    spines = ['top','bottom','left','right']
    for spine in spines:
        plt.gca().spines[spine].set_visible(False)
    # Adjust the starting position of the left spine to move the plot to the right
    plt.gca().spines['left'].set_position(('outward', 5))
    # Adjust the position of tick labels to the right
    plt.tick_params(axis='y', pad=5)  # Increase the pad to shift labels to the right
    # Turn off xticks
    plt.xticks([])
    # Change yticks color to white and font size
    plt.yticks(color=plot_color, font=b_font, fontweight='bold', fontsize=10)
            
    # Set labels and title
    title_text = 'TOP 10 TEAMS SCORED AGAINST (ON HOMEGROUND) IN ALL COMPS'
    title = plt.text(x=4.0, y=-1.5, s=title_text, ha='center', va='center', fontweight='semibold',
                    font=t_font, color=plot_color, fontsize=12, zorder=2)
    title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Add an endnote and a name text 
    endnote_text = f"{add_note}"
    endnote = plt.text(x=6.3, y=8.0, s=endnote_text, ha='center', va='center', fontweight='medium',
                    font=b_font, color=off_white, fontsize=9, zorder=2) 
    endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    #  Alt Name Text
    name_text = plt.text(x=6.2, y= 8.5, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=9, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    #  FIGURE PADDING
    # Pad Top 
    plt.text(x=0.5, y=-1.5, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    plt.text(x=0.5, y= 1.02, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad left
    plt.text(x=-2.09, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

def Home_Goals_Allowed_Top10():
    top_10_hga = h_games.groupby('Opponent')['FTOG'].sum().reset_index(name='GA')
    # Sort the DataFrame by 'GA' column in descending order and select the top 10 rows
    top_10_hga = top_10_hga.sort_values(by='GA', ascending=False).head(10)

    x_col = top_10_hga['Opponent']
    y_col = top_10_hga['GA']

    # Create a horizontal barplot
    fig = plt.figure(figsize=(8, 6), facecolor=facecolor)
    bars = plt.barh(x_col, y_col*.5, color='grey')

    # Add count values at the end of each bar
    for i, v in enumerate(y_col*.5):
        count = plt.text(v+.3, i, str(int(v*2)), va='center', color=off_white, font=b_font)
        count.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
        
    # Customize the appearance
    plt.xlabel(' ')
    plt.ylabel(' ')
    plt.gca().invert_yaxis()  # Invert the y-axis to display the highest value at the top
    plt.xlim(0, 10)  # Set the x-axis limits
    plt.gca().set_facecolor(facecolor)  # Set the facecolor to black
    plt.axis('on')
    spines = ['top','bottom','left','right']
    for spine in spines:
        plt.gca().spines[spine].set_visible(False)
    # Adjust the starting position of the left spine to move the plot to the right
    plt.gca().spines['left'].set_position(('outward', 5))
    # Turn off xticks
    plt.xticks([])
    # Change yticks color to white and font size
    plt.yticks(color=plot_color, font=b_font, fontweight='bold', fontsize=10)
            
    # Set labels and title
    title_text = 'TOP 10 TEAMS (GOALS ALLOWED ON HOMEGROUND) IN ALL COMPS'
    title = plt.text(x=4.0, y=-1.5, s=title_text, ha='center', va='center', fontweight='semibold',
                    font=t_font, color=plot_color, fontsize=12, zorder=2)
    title.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    # Add an endnote and a name text 
    endnote_text = f"{add_note}"
    endnote = plt.text(x=6.3, y=8.0, s=endnote_text, ha='center', va='center', fontweight='medium',
                    font=b_font, color=off_white, fontsize=9, zorder=2) 
    endnote.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])
    #  Alt Name Text
    name_text = plt.text(x=6.2, y=8.5, s=author, ha='center', va='center', 
                    font=b_font, color=plot_color, alpha=.3, fontsize=9, zorder=2)
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=off_white), 
                                path_effects.Normal()])

    #  FIGURE PADDING
    # Pad Top 
    plt.text(x=0.5, y=-1.5, s=pad_top, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad Bottom
    plt.text(x=0.5, y= 1.02, s=pad_end, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)
    # Pad left
    plt.text(x=-2.09, y= 1.15, s=hspace, color=off_white, linespacing= 2,
                    ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

def Clean_Sheets():
    # create the clean sheet dataframe from goals_df
    csht_df = goals_df.copy()
    # FTR CSHT
    ftr_conditions = [(csht_df['FTOG']==0), (csht_df['FTOG']>0)]
    # cln_sht=1 & 0 if otherwise in CHST column
    ftr_values = [1 , 0]
    # Creating the columns for Opponents
    csht_df['FT_CSHT'] = np.select(ftr_conditions, ftr_values)

    # HTR CSHT
    htr_conditions = [(csht_df['HTOG']==0), (csht_df['HTOG']>0)]
    # cln_sht=1 & 0 if otherwise in CHST column
    htr_values = [1 , 0]
    # Creating the columns for Opponents
    csht_df['HT_CSHT'] = np.select(htr_conditions, htr_values)

    # SHR CSHT
    shr_conditions = [(csht_df['SHOG']==0), (csht_df['SHOG']>0)]
    # cln_sht=1 & 0 if otherwise in CHST column
    shr_values = [1 , 0]
    # Creating the columns for Opponents
    csht_df['SH_CSHT'] = np.select(shr_conditions, shr_values)

    # reordering CSHT columns 
    csht_df = reorder_columns(dataframe=csht_df, col_name='FT_CSHT', new_position=9)
    csht_df = reorder_columns(dataframe=csht_df, col_name='HT_CSHT', new_position=13)
    csht_df = reorder_columns(dataframe=csht_df, col_name='SH_CSHT', new_position=17)

    return csht_df

# Funtion to return WX DX LX for any teamm in oau-giants df
def get_All_time_record(select_opponent):
    # Error checking
    if not isinstance(select_opponent, str):
        raise ValueError("Opponent name must be a string. Please enter a string only.")
    
    # Dictionary to hold all records   
    record_dict = {}
    # Basic Items for records 
    record_dict['Team'] = team
    record_dict['Opponent'] = select_opponent
    
    # Slice Dataframe
    temp_df = goals_df[(goals_df.Opponent == select_opponent)]
    temp_df.reset_index()
    
    # TOTAL MEETINGS
    total_meetings = str(len(temp_df))
    # Add item to dictionary
    record_dict.update({'Competitive Meetings' : total_meetings})
    
    # OUTCOME SUMMARY
    outcome_dict={}
    order = ['W','D','L'] 
    outcomes_vs_team = temp_df.FTR.value_counts().reindex(order, fill_value=0).reset_index()
    for i in range(len(outcomes_vs_team)):
        outcome_dict[outcomes_vs_team['index'][i]] = outcomes_vs_team.FTR[i]  
    
    # Format response String    
    record_vs_team = f"W{outcome_dict['W']} D{outcome_dict['D']} L{outcome_dict['L']}"
    # Add item to dictionary
    record_dict.update({'Match Outcomes' : record_vs_team})
    
    # AGGREGATE SCORE
    total_team_score = temp_df.FTTG.sum()
    total_oppnt_score = temp_df.FTOG.sum()
    agg_score = f"{total_team_score} — {total_oppnt_score}"
    # Add item to dictionary
    record_dict.update({'Aggregate Score' : agg_score})
    
    # CLEAN SHEETS
    # get the clean sheet df 
    csht_df = Clean_Sheets()
    df = csht_df[csht_df.Opponent == select_opponent]
    df.reset_index()
    #calculating clean sheets for team & opponent
    team_csht = df.FT_CSHT.sum()
    oppnt_csht = len(df[df.FTTG == 0])
    clean_sheets = f"{team_csht} — {oppnt_csht}"
    # Add item to dictionary
    record_dict.update({'Clean Sheets' : clean_sheets})
    
    # LARGEST WIN
    largest_win = ' '
    win_index=0
    
    win_df = temp_df[temp_df['FTR']=='W']
    win_df.reset_index()
    
    if len(win_df) > 1:
        for i in range(len(win_df)):
            # getting goal difference
            gd = win_df['FTTG'].iloc[i] - win_df['FTOG'].iloc[i]
            if i != 0:
                # gotten from former iteration
                prev_gd = win_df['FTTG'].iloc[win_index] - win_df['FTOG'].iloc[win_index]
                # Comparing gd
                if (gd - prev_gd) > 0:
                    win_index = i
                if (gd - prev_gd) == 0:
                    # comparing goals in both games when they have equal gd
                    gls_in_gms = win_df['FTTG'].iloc[i] - win_df['FTTG'].iloc[win_index]
                    if gls_in_gms >= 0:
                            win_index = i
                    else:
                        win_index +=0    
            else:
                win_index = 0

        largest_win = f"{win_df['FTTG'].iloc[win_index]} — {win_df['FTOG'].iloc[win_index]}"
        i+=1
    elif len(win_df) == 1:
        largest_win = f"{win_df['FTTG'].iloc[0]} — {win_df['FTOG'].iloc[0]}"
    else:
        largest_win = 'Nil'
    # Add item to dictionary
    record_dict.update({'Largest Win' : largest_win})
    
    # LARGEST DEFEAT
    largest_loss = ' '
    loss_index=0
    
    defeat_df = temp_df[temp_df['FTR']=='L']
    defeat_df.reset_index()
    
    if len(defeat_df) > 1:
        for j in range(len(defeat_df)):
            # getting goal difference
            gd = defeat_df['FTOG'].iloc[j] - defeat_df['FTTG'].iloc[j]
            if j != 0:
                # gotten from former iteration
                prev_gd = defeat_df['FTOG'].iloc[loss_index] - defeat_df['FTTG'].iloc[loss_index]
                # Comparing gd
                if (gd - prev_gd) > 0:
                    loss_index = j
                if (gd - prev_gd) == 0:
                    # comparing goals in both games when they have equal gd
                    gls_in_gms = defeat_df['FTOG'].iloc[j] - defeat_df['FTOG'].iloc[loss_index]
                    if gls_in_gms >= 0:
                            loss_index = j
                    else:
                        loss_index +=0    
            else:
                loss_index = 0

        largest_defeat = f"{defeat_df['FTTG'].iloc[loss_index]} — {defeat_df['FTOG'].iloc[loss_index]}"
        j+=1
    elif len(defeat_df) == 1:
        largest_defeat = f"{defeat_df['FTTG'].iloc[0]} — {defeat_df['FTOG'].iloc[0]}"
    else:
        largest_defeat = 'Nil'
    # Add item to dictionary
    record_dict.update({'Largest Defeat' : largest_defeat})
    record_dict
    return record_dict
# ------------------------------------------------------------------------------ #
# Funtion to return WX DX LX for any competition in oau-giants df
def get_Competition_record(select_comp=None, select_edition=None):             
    # Dictionary to hold all records   
    record_dict = {}
    # Clean Sheets df
    csht_df = Clean_Sheets()

    if (select_comp is not None) and ( select_edition is None):
        selection = select_comp
        # Slice Dataframe
        temp_df = goals_df[(goals_df.CompGroup == select_comp)]
        temp_df.reset_index()
        df = csht_df[csht_df.CompGroup == select_comp]
        df.reset_index()
        proceed_var = True
        
    elif (select_edition is not None):
        selection = select_edition
        # Slice Dataframe
        temp_df = goals_df[(goals_df.Competition == select_edition)]
        temp_df.reset_index()
        # Clean Sheets df
        df = csht_df[csht_df.Competition == select_edition]
        df.reset_index()
        proceed_var = True

    else:
        SelectionError =("Kindly select a Tournament or an Edition of a tournament to view the summary.")
        proceed_var = False
        return SelectionError
        

    if proceed_var is True:
        # Basic Items for records 
        record_dict['Team'] = team
        record_dict['Competition'] = selection
        
        # TOTAL MEETINGS
        total_gms_plyd = len(temp_df)
        # Add item to dictionary
        record_dict.update({'Games Played' : str(total_gms_plyd)})
        
        # OUTCOME SUMMARY
        outcome_dict={}
        order = ['W','D','L'] 
        outcome_in_gms = temp_df.FTR.value_counts().reindex(order, fill_value=0).reset_index()
        for i in range(len(outcome_in_gms)):
            outcome_dict[outcome_in_gms['index'][i]] = outcome_in_gms.FTR[i]  
        
        # Format response String    
        record_vs_team = f"W{outcome_dict['W']} D{outcome_dict['D']} L{outcome_dict['L']}"
        # Add item to dictionary
        record_dict.update({'Outcome Summary' : record_vs_team})
        
        # GOAL DIFFERENCE
        total_gf = temp_df.FTTG.sum()
        total_ga = temp_df.FTOG.sum()
        diff = total_gf - total_ga
        if diff>0:
            gd = f'+{diff}'
        else:
            gd = str(diff)
        # Add item to dictionary
        record_dict.update({'GD' : gd})
        
        # CLEAN SHEETS
        #calculating clean sheets for team & opponent
        team_csht = df.FT_CSHT.sum()
        # Add item to dictionary
        record_dict.update({'Clean Sheets' : str(team_csht)})
        
        
        # LARGEST WIN
        largest_win = ' '
        win_index=0
        
        win_df = temp_df[temp_df['FTR']=='W']
        win_df.reset_index()
        
        if len(win_df) > 1:
            for i in range(len(win_df)):
                # getting goal difference
                gd = win_df['FTTG'].iloc[i] - win_df['FTOG'].iloc[i]
            if i != 0:
                # gotten from former iteration
                prev_gd = win_df['FTTG'].iloc[win_index] - win_df['FTOG'].iloc[win_index]
                # Comparing gd
                if (gd - prev_gd) > 0:
                    win_index = i
                if (gd - prev_gd) == 0:
                    # comparing goals in both games when they have equal gd
                    gls_in_gms = win_df['FTTG'].iloc[i] - win_df['FTTG'].iloc[win_index]
                    if gls_in_gms >= 0:
                            win_index = i
                    else:
                        win_index +=0    
            else:
                win_index = 0

            largest_win = f"{win_df['FTTG'].iloc[win_index]} — {win_df['FTOG'].iloc[win_index]}"
            i+=1
        elif len(win_df) == 1:
            largest_win = f"{win_df['FTTG'].iloc[0]} — {win_df['FTOG'].iloc[0]}"
        else:
            largest_win = 'Nil'
        # Add item to dictionary
        record_dict.update({'Largest Win' : largest_win})
        
        
        # LARGEST DEFEAT
        largest_loss = ' '
        loss_index=0
        
        defeat_df = temp_df[temp_df['FTR']=='L']
        defeat_df.reset_index()
        
        if len(defeat_df) > 1:
            for j in range(len(defeat_df)):
                # getting goal difference
                gd = defeat_df['FTOG'].iloc[j] - defeat_df['FTTG'].iloc[j]
            if j != 0:
                # gotten from former iteration
                prev_gd = defeat_df['FTOG'].iloc[loss_index] - defeat_df['FTTG'].iloc[loss_index]
                # Comparing gd
                if (gd - prev_gd) > 0:
                    loss_index = j
                if (gd - prev_gd) == 0:
                    # comparing goals in both games when they have equal gd
                    gls_in_gms = defeat_df['FTOG'].iloc[j] - defeat_df['FTOG'].iloc[loss_index]
                    if gls_in_gms >= 0:
                            loss_index = j
                    else:
                        loss_index +=0    
            else:
                loss_index = 0

            largest_defeat = f"{defeat_df['FTTG'].iloc[loss_index]} — {defeat_df['FTOG'].iloc[loss_index]}"
            j+=1
        elif len(defeat_df) == 1:
            largest_defeat = f"{defeat_df['FTTG'].iloc[0]} — {defeat_df['FTOG'].iloc[0]}"
        else:
            largest_defeat = 'Nil'
        # Add item to dictionary
        record_dict.update({'Largest Defeat' : largest_defeat})
        
        record_dict
        return record_dict

# Waffle Plot for Team Form 
def Form_Guide(select_period, select_opponent=None, select_range=None, stack=15, select_comp=None,
               adj_stx=None, adj_sty=None, adj_title_x=None, adj_title_y=None,
               adj_endnote_x=None, adj_endnote_y=None):
    """
    select_opponent: Decide whether the Form Guide should be plotted for meetings in all competitions either against All_teams faced or a particular opponent.
    select_period: Decide if plot should consider only Fulltime Results(FTR), Halftime Results (HTR) or Second Half Results.
    select_range:(default=results_df) Dataframe for consideration. Could help when filtering for Home Games or Away Games only.
    select_comp:(default=None) Only works when All_teams is selected as the Opponent
    stack:(default=15) Number of waffle boxes to be plotted per row
    adj_stx: x-coordinates of the bottom-left edge of the first waffle box
    adj_sty: y-coordinates of the bottom-left edge of the first waffle box
    adj_title_x: x-coordinates of the Title text
    adj_title_y: y-coordinates of the Title text
    adj_endnote_x: x-coordinates of the Endnote text
    adj_endnote_y: y-coordinates of the Endnote text
    """
    # Error checking
    # if not isinstance(select_opponent, str):
    #     raise ValueError("Opponent name must be a string. Please enter a string only.")
    if not isinstance(select_period, str):
        raise ValueError("Period must be a string. Please enter a string only.")
    # # Error checking
    # if not isinstance(select_range, str):
    #     raise ValueError("select_range must be a string. Please enter a string only.")
        
    # Create Figure & Plot Axes
    fig, ax = plt.subplots(1,1, figsize=(12, 4), facecolor=facecolor, constrained_layout=True)
    ax.set_facecolor(facecolor)
    ax.axis('off')
        
    # Plot Viz Variables
    # Default Title (Back up Title)
    title=(f"{team} FORM GUIDE ({select_period}) SHOWING <WINS>, <DRAWS> AND\n"
           f"{hspace*15}<LOSSES> IN ALL COMPS")
    # space between waffles     
    pad_y = -.18
    pad_x = .06
    
    #starting x-pos of the waffle boxes & the reset_value (reset_x) to activate row-change
    if adj_stx is not None:
        st_x = reset_x = adj_stx
    else:
        st_x = reset_x = .05  
    
    #starting y-pos of the waffle boxes
    if adj_sty is not None:
        st_y = adj_sty
    else:
        st_y = .80 
    
    # Checking for Adjustments to title 
    if adj_title_x is not None:
        title_x = adj_title_x 
    else:
        title_x = .21
        
    if adj_title_y is not None:
        title_y = adj_title_y
    else:
        title_y = 1.18
        
    # Checking for Adjustments to title 
    if adj_endnote_x is not None:
        endnote_x = adj_endnote_x
    else:
        endnote_x = 0.51
        
    if adj_endnote_y is not None:
        endnote_y = adj_endnote_y
    else:
        endnote_y= -0.23

    # Handling Default Values
    if select_opponent is None:
       select_opponent = "All_teams"
    if select_range is None:
        select_range = "All_Games"

    all_games = home_games = False
    # Decide on the df to use
    if select_range == 'All_Games':
        all_games = True
        form_df = goals_df
        title = (f"{team} FORM GUIDE ({select_period}) SHOWING <WINS>, <DRAWS> AND <LOSSES>\n"
                 f"{hspace*11}AGAINST ALL TEAMS IN ALL COMPS")
    elif select_range == 'Home_Games':
        # select_comp = None
        home_games = True
        form_df = h_games
        title= (f"{team} FORM GUIDE ({select_period}) SHOWING <WINS>, <DRAWS> AND\n"
                f"{hspace*5}<LOSSES> IN ALL COMPS ON HOMEGROUND")
    
    # Title Padding if we want to return form guide
    # per opponent at a particular competition!
    all_gms_per_comp = False

    # Check if an Opponent is selected
    if select_opponent is not None:
        # Error checking
        if not isinstance(select_opponent, str):
            raise ValueError("Opponent name must be a string. Please enter a string only.")
        if select_opponent != 'All_teams': 
            if select_range == "Home_Games":
                if confirm_fixture_on_homeground(select_opponent) is False:
                    return f"No Competitive Meeting on Homeground between the {team} and {select_opponent} in All Comps"
                else:
                    form_df = form_df[form_df['Opponent'] == select_opponent]
                    title_suffix = "IN ALL COMPS ON HOMEGROUND"

                if select_comp is not None:
                    if select_comp in list(set(form_df.CompGroup.to_list())):
                        form_df = form_df[form_df["CompGroup"] == select_comp]
                        title_suffix = f"AT THE {select_comp.upper()} ON HOMEGROUND"
                        all_gms_per_comp = True
                    else:
                        return f"No Competitive Meeting on Homeground between the {team} and {select_opponent} at the {select_comp}"                 
                       
            elif select_range == "All_Games":
                form_df = form_df[form_df['Opponent'] == select_opponent].reset_index(drop=True)
                if select_comp is not None:
                    if select_comp in list(set(form_df.CompGroup.to_list())):
                        form_df = form_df[form_df['CompGroup'] == select_comp]
                        title_suffix = f"IN ALL MEETINGS AT THE {select_comp.upper()}"
                        all_gms_per_comp = True
                    else:
                        return f"No Competitive Meeting between the {team} and {select_opponent} at the {select_comp}"                 
                    
                else:
                    title_suffix = "IN ALL COMPS"

            #  Adjust the Spacing on the Title text based on length of Opponent's Name
            if len(select_opponent)>10:
                title = (f"{team} FORM GUIDE ({select_period}) <WINS>, <DRAWS> AND <LOSSES> AGAINST\n"
                         f"{select_opponent.upper()} {title_suffix}")
            elif len(select_opponent)<10:
                if all_gms_per_comp == True:
                    title_pad = hspace*9
                else:
                    title_pad = hspace*19
                title = (f"{team} FORM GUIDE ({select_period}) <WINS>, <DRAWS> AND <LOSSES> AGAINST\n"
                         f"{title_pad}{select_opponent.upper()} {title_suffix}")

        elif select_opponent == 'All_teams':  
            if select_comp is not None:
                if all_games == True:
                    form_df = form_df[form_df['CompGroup'] == select_comp].reset_index(drop=True)
                    title = (f"{team} FORM GUIDE ({select_period}) SHOWING <WINS>, <DRAWS> AND <LOSSES> IN\n"
                             f"{hspace*19}ALL GAMES AT THE {select_comp.upper()}")
                elif home_games == True:
                    if confirm_comp_on_homeground(select_comp=select_comp) is True: 
                        form_df = form_df[form_df['CompGroup'] == select_comp].reset_index(drop=True)
                        title = (f"{team} FORM GUIDE ({select_period}) SHOWING <WINS>, <DRAWS> AND <LOSSES>\n"
                                 f"{hspace*3} IN MATCHES PLAYED ON HOMEGROUND AT THE {select_comp.upper()}")
                    else:
                        return (f"No Match At The {select_comp} Was Played On Homeground")
                
                else:
                    title = (f"{team} FORM GUIDE ({select_period}) <WINS>, <DRAWS> AND <LOSSES> AGAINST\n"
                             f"{hspace*19}ALL TEAMS AT THE {select_comp.upper()}")

    # Confirm Period over which to calculate Form 
    #(All Matches In that Instance of Team Selection)
    if select_period =='HTR':
        end_fguide = "HTR — Halftime Results"
        
    elif select_period == 'SHR':
        #For Form Guide
        end_fguide = "SHR — Second Half Results"
        
    else:
        #For Form Guide
        end_fguide = "FTR — Fulltime Results" 
        
        
    #  Check count of df or list or array to know how many boxes are needed
    waffle_data = form_df[f'{select_period}'].to_list()
    num_of_boxes = i_rev = len(waffle_data) # i_rev is used to iterate from most recent to oldest match
    
    # colormap for each unique outcome that's expected
    color_dict = {'W' : '#005A32', 
                  'D' : '#D6D37F',
                  'L' : '#5A0028'}

    # Making the Waffle Plot
    for i in range(num_of_boxes): #total num of boxes to be plotted
        #Know When to switch to the next row
        if i % stack == 0 and i > 0:  #For eg (if i % 15 == 0 and i > 0:) would mean 15 boxes a row
            st_y += pad_y
            st_x = reset_x

        #Default Waffle Plot
        waffle_box = plt.Rectangle((st_x, st_y), .05, .15,
                                   fc=color_dict[waffle_data[i_rev-1]], ec='none') #-1 bcos py cnts from 0
        st_x += pad_x
        i_rev -= 1

        # Add Waffle to Axes    
        ax.add_patch(waffle_box)

    # Title Text       
    # Set titles for the figure and the subplot respectively
    h_fig(x=title_x, y=title_y, s=title, color=off_white, highlight_textprops=[{'color': color_dict['W']},
                                                                               {'color': color_dict['D']},
                                                                               {'color': color_dict['L']}],
           font=t_font, fontsize=t_fsize, fontweight='bold', va='center', zorder=2)

    # Endnotes
    endnote_text = ("Matches are arranged L-R: (Most Recent — Oldest)\n"
                    f"{end_fguide} ({data_span})\n"
                    f"{add_note}")
    # writing endnote text on figure
    endnote = fig.text(x=endnote_x, y= endnote_y, s=endnote_text, color='grey', linespacing= 2,
                   ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    # Name Text
    name_text = fig.text(x=endnote_x, y=endnote_y-.22, s=author, ha='center', va='center', 
                   font=b_font, color=plot_color, alpha=.3, fontsize=b_fsize, zorder=2)

    # Path Effects for texts
    endnote.set_path_effects([path_effects.Stroke(linewidth=.018, foreground=off_white),
                          path_effects.Normal()])
    name_text.set_path_effects([path_effects.Stroke(linewidth=.005, foreground=plot_color), 
                            path_effects.Normal()])

    # Figure Paddings
    fig.text(x=title_x, y=title_y+.05, s=pad_top, color=off_white, linespacing= 2,
                ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    fig.text(x=endnote_x, y=endnote_y-.27, s=pad_end, color=off_white, linespacing= 2,
                ha='center', va='center', font=b_font, fontsize=b_fsize, zorder=2)

    return fig

# Define a function to calculate streaks
def calculate_streaks(streak_type, select_range, select_period, select_comp=None):
    """
    1. streak_type: Win_Streak (W) | Draw_Streak (D) | Loss_Streak L) | Unbeaten_Run
    2. select_range: All_Games | Home_Games (if Home_Games, disable select_comp)
    3. select_comp: Input_CompGroup_Name
    4. select_period: FTR | HTR | SHR
    """
    streaks = []
    current_streak = 0
    
    streak_dict = {'Win_Streak'  : 'W',
                   'Draw_Streak' : 'D',
                   'Loss_Streak' : 'L',
                   'Unbeaten_Run' : ['W', 'D']}
    
    if select_range == 'Home_Games':
        select_comp = None
        streak_df = h_games.copy()
        
    elif select_range == 'All_Games':
        if select_comp is not None:
            streak_df = goals_df[goals_df['CompGroup'] == select_comp].reset_index(drop=True)
        else:
            streak_df = goals_df.copy()
                    
                
    for result in streak_df[f'{select_period}']:
        if result in f'{streak_dict[streak_type]}':    #Replace With D or L
            current_streak += 1
        else:
            streaks.append(current_streak)
            current_streak = 0
                
    # Append the last streak
    streaks.append(current_streak)
    longest_streak = max(streaks)

    return streaks, longest_streak

def AllTime_Comp_Results(period):
    # Alt Method
    fig_path = f'assets/ceo-{period.lower()}-per-comp.png'
    return Image.open(fig_path)

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
    #         # Wins, Draws & Loss Count
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
    #         hide_spines(axes=ax, which_spine='all')


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
    #                     font=b_font, color=plot_color, alpha=.3, fontsize=8, zorder=2)
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
    #                                                                     {'color':'#79A19D'},
    #                                                                     {'color':'grey'}],
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

    # return fig

# Expander Section
expander = " "
def add_expander(exp_title, exp_md, val=False):
    """
    val: (bool) True | False
    exp_title: (str) Title of expander section
    exp_md: (markdown) Content of expander section formatted as Markdown

    """
    if val == True:
        global expander
        expander = True

        return exp_title, exp_md

games_played_md = ("""
                    #### **ADDITIONAL INFO FOR CONTEXT**
                    
                    The number of games per year (at competitions) just about reflects the reality of 
                    the collegiate games system in the country. There is little to no (competitive) 
                    action most years unless a major game is happening, this sort of changed slightly 
                    in 2018 when the HiFL started to operate.

                    Furthermore, only a few tournaments had round-robin systems built into them: 
                    NUGA Games, HiFL (started in 2019 as part of the preliminaries) and Peace Cup 
                    for example.
                    
                    Finally, **the most important thing** to note in the Nigerian Collegiate Games setup is 
                    that the competitions are mostly direct elimination formats so **to rack up games, 
                    you need to keep winning!**

                    
                    """)

h2h_form_guide_md = ("""
                     ##### KINDLY NOTE
                     The returned plot is numb to tie descriptions, for instance, if it was a Final 
                     or a match played at a neutral venue. A good instance is the Peace Cup Final 
                     played against Successful Christian Mission FC (also Successful CMFC). 
                     
                     Whereas, the tie should be regarded as one held on a neutral venue but the 
                     system returns the plot as an Homeground fixture since the Final was played 
                     at the designated Homeground of the OAU MFT.
                     """)

gls_plot_md = ("""
                ##### KINDLY NOTE
               When comparing teams H2H with the OAU MFT, the range of games 
               selected is of null effect chiefly because of the few matches played on 
               Homeground in many of the tournaments attended consequently leading 
               to a sparse distribution of teams faced. Basically, there's not 
               enough data to aggregate.
               """)

gls_plot_caution_md = ("""
                       ##### A CAUTION ON FINE DETAILING PER OPPONENT
                       The features on the Head-to-Head page allows you 
                       to get into the fine details of every encounter between 
                       the OAU MFT and any Opponent faced, say you varied meetings 
                       against an Opponent per match outcome in a particular competition.
                       
                       While this returns a result given the available data, **great caution 
                       should be taken!**
                       
                       The plot of the Top 10 teams faced, as you've probably seen from the 
                       *All-Time Stat* section, shows that there were teams against whom 
                       the team only ever had three meetings hence, fine detailing 
                       would not mean much for many teams. 
                       
                       However, given the historical context, you could infer little from 
                       fine detailing if you selected opponents against whom the team had 
                       five meetings or more and even with that, the meetings would still 
                       be sparsely distributed across the different competitions available.

                       There basically just isn't enough data given the peculiarities of the 
                       collegiate sports system in Nigeria.
                    """)

import os
from PIL import Image
import time
# Display Plot
def display_plot(plot_type, plot_alt=None, args=None):
    """
    plot_type (str) : The user selection of stats to see
    plot_alt (str) : For sections with plot alternatives 
    args (dict) : parameters of the affected plot functions
    """
    nl(1)
    # Specifying the chart Area
    chart_area = st.empty()
    chart_area.empty()
    nl(1)
    expander_area = st.empty()

    # Initialize figure to None
    figure = None

    # ----------- PLOTS -----------
    # Check for the requested plot type
    if plot_type == "Honors Won":
        figure = Honors_Won()

    if plot_type == "Match Results":
        corr = "results_corr"
        if plot_alt == "Result Percentages":
            # This helps us know which of plot alternatives the user selected
            # Since we already know the order of parameters the Resilt_Pct()
            # takes, so we just read them from the params dictionary from the main App (args=dict(params))
            # that called the plot function!
            figure = Results_Pct(select_opponent=args.get("select_opponent"),
                                 select_period=args.get("select_period"),
                                 select_range=args.get("select_range"))
        elif plot_alt == "Result Correlation":
            figure = Corr_Heatmap(select_range=args.get("select_range"), corr_type=corr)
        elif plot_alt == "Runs":
            streak_list, longest_streak = calculate_streaks(streak_type=args.get("streak_type"),
                                                            select_period=args.get("select_period"),
                                                            select_range=args.get("select_range"),
                                                            select_comp=args.get('select_comp'))
            # Custom Return Statement for Runs Plot
            figure = (f"**{longest_streak}**"
                     f"\n{hspace*4}The Longest {args.get('run_type')} of the {team} under {coach} ({data_span})")

    if plot_type == "Goals Chart":
        corr = "goals_corr"
        if plot_alt == "Goals Ratio":
            try:
                figure = Goals_Plot(select_period=args.get("select_period"),
                                    select_category=args.get('select_category'),
                                    select_opponent=args.get("select_opponent"),
                                    select_outcome=args.get('select_outcome'))
            except UnboundLocalError:
                pass #do nothing
        elif plot_alt == "Common Scorelines":
            figure = Common_Scoreline(select_opponent=args.get("select_opponent"),
                                      select_period=args.get("select_period"),
                                      select_range=args.get("select_range"),
                                      select_comp=None)
        elif plot_alt == "Goals For (Top 10)":
            if args.get("select_range") == "All_Games":
                figure = Goals_For_Top10()
            elif args.get("select_range") == "Home_Games":
                figure = Home_Goals_For_Top10()
        elif plot_alt == "Goals Allowed (Top 10)":
            if args.get("select_range") == "All_Games":
                figure = Goals_Allowed_Top10()
            elif args.get("select_range") == "Home_Games":
                figure = Home_Goals_Allowed_Top10()
        elif plot_alt == "Goals Correlation":
            figure = Corr_Heatmap(select_range=args.get("select_range"), corr_type=corr)

    if plot_type == "Form Guide":
        figure = Form_Guide(select_opponent=args.get('select_opponent'),
                            select_period=args.get('select_period'),
                            select_range=args.get('select_range'))

    if plot_type == "Teams Faced":
        figure = Teams_Faced()

    if plot_type == "Games Played":
        figure = Games_Played()
        title, content = add_expander(exp_title="For Context", exp_md=games_played_md, val=True)
    
    if plot_type == "Head-to-Head":
        if plot_alt == "Result Percentages":
            figure = Results_Pct(select_opponent=args.get("select_opponent"),
                                 select_period=args.get("select_period"),
                                 select_range=args.get("select_range"))
        elif plot_alt == "Form Guide":
            figure = Form_Guide(select_opponent=args.get('select_opponent'),
                                select_period=args.get('select_period'),
                                select_range=args.get('select_range'),
                                select_comp=args.get('select_comp'))
            title, content = add_expander(exp_title="For Clarity", exp_md=h2h_form_guide_md, 
                                          val=True)
        elif plot_alt == "Goals Ratio":
            figure = Goals_Plot(select_period=args.get("select_period"),
                                select_category=args.get('select_category'),
                                select_opponent=args.get("select_opponent"),
                                select_outcome=args.get('select_outcome'),
                                select_comp=args.get('select_comp'), 
                                select_edition=None)
            with st.expander("How the Goals Averages Plot Works for Head-to-Head?"):
                st.markdown(gls_plot_md)
            title, content = add_expander(exp_title="Caution", exp_md=gls_plot_caution_md,
                                            val=True)
            
        elif plot_alt == "Common Scorelines":
            figure = Common_Scoreline(select_opponent=args.get("select_opponent"),
                                      select_period=args.get("select_period"),
                                      select_range=args.get("select_range"),
                                      select_comp=None)

    if plot_type == "Competitions":
        if plot_alt == "Result Aggregate":
            fig_path = f'assets/ceo-{args.get("select_period").lower()}-per-comp.png'
            figure = Image.open(fig_path)
            # figure = AllTime_Comp_Results(period=args.get("select_period"))
            
        elif plot_alt == "Form Guide":
            figure = Form_Guide(select_opponent=args.get('select_opponent'),
                                select_period=args.get('select_period'),
                                select_range=args.get('select_range'),
                                select_comp=args.get('select_comp'),
                                stack=args.get('stack'))
            # title, content = add_expander(exp_title="For Clarity", exp_md=h2h_form_guide_md, 
            #                               val=True)
        elif plot_alt == "Goals Ratio":
            figure = Goals_Plot(select_period=args.get("select_period"),
                                select_category=args.get('select_category'),
                                select_opponent=args.get("select_opponent"),
                                select_outcome=args.get('select_outcome'),
                                select_comp=args.get('select_comp'), 
                                select_edition=args.get('select_edition'))
            # with st.expander("How the Goals Averages Plot Works for Head-to-Head?"):
            #     st.markdown(gls_plot_md)
            # title, content = add_expander(exp_title="Caution", exp_md=gls_plot_caution_md,
            #                                 val=True)
            
        elif plot_alt == "Common Scorelines":
            figure = Common_Scoreline(select_opponent=args.get("select_opponent"),
                                      select_period=args.get("select_period"),
                                      select_range=args.get("select_range"),
                                      select_comp=args.get('select_comp'))

    nl(1)
    btn_descr = "Confirm Selection and Apply Filters (if any)"
    if st.button("Apply Selection", help=btn_descr):
        with st.spinner("fetching data"):
            time.sleep(1)

        if figure is not None:  # Check if figure is not None
            if isinstance(figure, plt.Figure):
                img_file = 'assets/figure.png'
                plt.savefig(img_file, dpi=100, bbox_inches = "tight")
                fig = Image.open(img_file)
                chart_area.image(fig)
                os.remove(img_file)

            elif isinstance(figure, str):
                if plot_alt == "Runs":
                    chart_area.markdown(f"""# {figure}""")
                else:
                    chart_area.markdown(f"""##### **{figure}**""")

            elif isinstance(figure, Image.Image):
                chart_area.image(figure)

        else:
            chart_area.write("**Unrecognized Return Value**")

        if expander == True:
            nl(1)
            with expander_area.expander(title):
                st.markdown(content)
            
