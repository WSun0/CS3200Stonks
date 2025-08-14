import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show sidebar links for the role of the currently logged-in user
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Student's specific actions
if st.button('Learn About Metrics', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Mia_Learn_Metrics.py')

if st.button('Share Strategies', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Mia_Share_Strategies.py')

if st.button('Backtest Simple Strategies', 
             type='primary',
             use_container_width=True):
    st.switch_page('pages/Mia_Backtests.py')
