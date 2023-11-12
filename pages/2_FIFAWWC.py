# import streamlit as st

# # Sidebar navigation
# st.sidebar.title("Navigation")
# pages = ["Home", "About", "Analytics"]
# selected_page = st.sidebar.selectbox("Select Page", pages)

# # Define the layout for each page
# def home_page():
#     st.subheader("Welcome to the Home Page")
#     st.write("This is the Home Page. You can learn more about this app here.")

# def about_page():
#     st.subheader("About")
#     st.write("This is the About page. You can find information about us here.")

# def analytics_page():
#     st.subheader("Analytics")
#     selected_subpage = st.sidebar.selectbox("Select Analytics Subpage", analytics_subpages)
#     st.title(f"Analytics - {selected_subpage}")
#     if selected_subpage == "Bar Charts":
#         st.write("Content for Bar Charts goes here.")
#     elif selected_subpage == "Pie Charts":
#         st.write("Content for Pie Charts goes here.")
#     elif selected_subpage == "Podium Plots":
#         st.write("Content for Podium Plots goes here.")
#     elif selected_subpage == "Time Series":
#         st.write("Content for Time Series goes here.")

# # Subpages under "Analytics"
# analytics_subpages = ["Bar Charts", "Pie Charts", "Podium Plots", "Time Series"]

# # Display the selected page's layout
# if selected_page == "Home":
#     home_page()
# elif selected_page == "About":
#     about_page()
# elif selected_page == "Analytics":
#     analytics_page()
