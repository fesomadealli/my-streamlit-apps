import streamlit as st
# import plost
import webbrowser

# page layout
st.set_page_config(layout = 'centered', 
                   initial_sidebar_state ='collapsed',
                   page_title = 'Welcome Page')
    
# styling the webpage
# Set custom CSS using the style.css file
def set_custom_style():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function to set custom style
set_custom_style()

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

def redirect_button(url: str, text: str= None, color="#da111b"):
    st.markdown(
    f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: white;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True 
    )
    

# urls 
twitter_url = "twitter.com/fesomadealli" 
medium_url = "medium.com/fesomade.alli"
linkedin_url = "linkedin.com/in/fesomade-alli-680808155"
email_url = "mailto:fesomadealli@gmail.com"
github_url = "github.com/fesomadealli"

# Your Streamlit app code starts here
st.title("Welcome Page")
add_line(True)

# Homepage Content
nl(2)
welcome_text = ("On this page, you can find all the [Data] Apps and visualizations "
                "done by @fesomadealli"
                "\n\nKindly use the expanders below for more information.")

st.write(welcome_text)


nl(2)
# EXPANDER SECTION 
# Quick Guide
with st.expander(label="Quick Guide", 
                 expanded=False):
    exp_text = ("To select an App, access the sidebar by clicking on the icon "
                "on the top left of your screen. This shows you the list of available "
                "Apps and the Main page which you are currently on. "
                "You may proceed to click on any of the enlisted Apps to open them."
                "\n\nYou may switch between Apps on the sidebar at any time but you should "
                "kindly note that the site does not remember your last action when switching Apps.")
    
    st.write(exp_text)

# About Me
with st.expander(label="About Me", 
                 expanded=False):
    exp_text = ("Hardware | Sports | Leading Teams"
                "\n\nA Computer Engineer passionate about sports and technology and, "
                "currently pursuing interests in sports engineering, administration and sport data analytics.")
    st.write(exp_text)
    
    # Define the labels for the buttons
    button_label1 = "View Portfolio"
    button_label2 = "Read Blogs"

    # Use Streamlit's columns to create a layout with columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Add buttons to the columns
    with col1:
        if st.button(button_label1):
            st.write("Button 1 Clicked!")

    with col2:
        if st.button(button_label2):
            st.write("Button 2 Clicked!")

# Connect With Me
with st.expander(label="Connect With Me", 
                 expanded=False):
    exp_text = ("You may wish to view my profiles, follow my work or contact me directly. "
                "Get this done via any of the social network services or online avenues listed below.")
    
    st.write(exp_text)
    
    # Use Streamlit's columns to create a layout with columns
    col_1, col_2, col_3, col_4, col_5 = st.columns(5)    

    # Define the labels for the buttons
    email_btn = "Send Mail"
    twitter_btn = "Twitter"
    linkedin_btn = "LinkedIn"
    medium_btn = "Medium"
    github_btn = "Github"

    with col_1:
        redirect_button(email_url,email_btn)

    with col_2:
        redirect_button(twitter_url,twitter_btn)

    with col_3:
        redirect_button(linkedin_url,linkedin_btn)

    with col_4:
        redirect_button(medium_url,medium_btn)

    with col_5:
        redirect_button(github_url,github_btn)

# Support
with st.expander(label="Support My Work", 
                 expanded=False):
    donate_btn = "Donate"
    exp_text = ("You may support my sport analytics journey by "
                "clicking the button below and following the prompts.")
    
    st.write(exp_text)
    
    if st.button(donate_btn):
        st.write("Button 1 Clicked!")

# sidebar contact
st.sidebar.markdown('''
Created by @fesomadealli\n
[Twitter](twitter.com/fesomadealli)
[Github](github.com/fesomadealli)
[Medium](medium.com/fesomade.alli) 
                    ''')
