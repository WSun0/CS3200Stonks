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
if st.button('Diagnose Errors', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Jamie_Error_Diagnostics.py')

if st.button('Manage Backups & Restores', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Jamie_Data_Backup.py')

if st.button('Deploy Updates & Patches', 
             type='primary',
             use_container_width=True):
  st.switch_page('pagesJamie_Update_Patches.py')
