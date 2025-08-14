import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Financial Advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Overall Performance', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Alex_View_Performance.py')

if st.button('Evaluate A Strategy', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Alex_Evaluate_Strategy.py')

if st.button('Export Strategy Report', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Alex_Export_Strategy.py')
