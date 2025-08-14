import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Deploy Updates & Patches")

st.write("Deploy system updates without disrupting users.")

update_version = st.text_input("Update Version", placeholder="e.g. v1.3.2")

if st.button("Deploy Update", type='primary'):
    st.success(f"Update {update_version} deployed successfully! (connect to deployment pipeline)")
