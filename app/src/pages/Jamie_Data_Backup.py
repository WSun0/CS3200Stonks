import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Data Backup & Restore Management")

st.write("Create and restore backups to ensure data integrity.")

if st.button("Create Backup", type='primary'):
    st.success("Backup created successfully! (connect to backup system)")

if st.button("Restore from Backup", type='secondary'):
    st.warning("Restoring from backup... (connect to restore system)")
