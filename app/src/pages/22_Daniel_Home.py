import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
<<<<<<< HEAD
# This function is correct, but the issue was in the button links below.
=======
>>>>>>> 87a9cb74fbb54dc7b67742b3c21ad4b18b7a7bab
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

<<<<<<< HEAD
# Fix the button links to point to Daniel's specific pages
=======
>>>>>>> 87a9cb74fbb54dc7b67742b3c21ad4b18b7a7bab
if st.button('View Backtest Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Daniel_backtests.py')

if st.button('Compare Stocks', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_Daniel_StockCompare.py')

if st.button('Import and Export Strategies', 
             type='primary',
             use_container_width=True):
<<<<<<< HEAD
  st.switch_page('pages/25_Daniel_Strategies.py')
=======
  st.switch_page('pages/25_Daniel_Strategies.py')
>>>>>>> 87a9cb74fbb54dc7b67742b3c21ad4b18b7a7bab
