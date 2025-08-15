# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

### General Sidebar Links
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/About.py", label="About", icon="🧠")


### Alex Sidebar Links
def AlexHomeNav():
    st.sidebar.page_link("pages/Alex_Home.py", label="Alex Home Page", icon="👤")

def AlexViewPerformanceNav():
    st.sidebar.page_link("pages/Alex_View_Performance.py", label="View Strategy Performance", icon="🏦")

def AlexEvaluateStrategyNav():
    st.sidebar.page_link("pages/Alex_Evaluate_Strategy.py", label="Evaluate Strategy", icon="🗺️")

def AlexExportStrategyNav():
    st.sidebar.page_link("pages/Alex_Export_Strategy.py", label="Export Strategy", icon="🗺️")

### Mia Sidebar Links
## TBD

### Daniel Sidebar Links
def DanielHomeNav():
    st.sidebar.page_link("pages/Daniel_Home.py", label="Daniel Home Page", icon="👤")

def DanBacktestsNav():
    st.sidebar.page_link("pages/Daniel_Backtests.py", label="Backtests", icon="📊")

def DanStockCompareNav():
    st.sidebar.page_link("pages/Daniel_Compare_Strategy.py", label="Compare Strategies", icon="🗺️")

def DanStrategiesNav():
    st.sidebar.page_link("pages/Daniel_Import_Export.py", label="Import/Export", icon="📄")

### Jamie Sidebar Links
def JamieHomeNav():
    st.sidebar.page_link("pages/Jamie_Home.py", label="Jamie Home Page", icon="👤")

def JamieDataBackupNav():
    st.sidebar.page_link("pages/Jamie_Data_Backup.py", label="Data Backup", icon="📊")

def JamieErrorDiagnosticsNav():
    st.sidebar.page_link("pages/Jamie_Error_Diagnostics.py", label="Error Diagnostics", icon="🗺️")

def JamieUpdatePatchesNav():
    st.sidebar.page_link("pages/Jamie_Update_Patches.py", label="Update Patches", icon="📄")


### Main Function
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=210)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Alex's flows on the sidebar
        if st.session_state["first_name"] == 'Alex':
            AlexHomeNav()
            AlexEvaluateStrategyNav()
            AlexExportStrategyNav()
            AlexViewPerformanceNav()

        # Mia's flows on the sidebar
        if st.session_state["first_name"] == 'Mia':
            pass  # TBD - placeholder for Mia's navigation

        # Jamie's flows on the sidebar
        if st.session_state["first_name"] == 'Jamie':
            JamieHomeNav()
            JamieDataBackupNav()
            JamieErrorDiagnosticsNav()
            JamieUpdatePatchesNav()

        # Daniel's flows on the sidebar
        if st.session_state["first_name"] == 'Daniel':
            DanielHomeNav()
            DanBacktestsNav()
            DanStockCompareNav()
            DanStrategiesNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Try Different User"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
    