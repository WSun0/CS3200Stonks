import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
# This function is correct, but the issue was in the button links below.
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

# Fix the button links to point to Daniel's specific pages
if st.button('View Backtest Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Daniel_Backtests.py')

if st.button('Compare Stocks', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Daniel_Compare_Strategy.py')

if st.button('Import and Export Strategies', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Daniel_Import_Export.py')
