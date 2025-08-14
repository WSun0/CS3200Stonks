import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar links for role
SideBarLinks()

st.title("🤝 Share Strategies")
st.write("")
st.write("Share your practice strategies with classmates or professors for feedback.")

# Strategy submission form
with st.form("share_strategy_form"):
    strategy_name = st.text_input("Strategy Name")
    strategy_desc = st.text_area("Describe your strategy")
    recipient = st.text_input("Recipient (email or username)")
    submitted = st.form_submit_button("Share Strategy")

    if submitted:
        st.success(f"✅ Strategy '{strategy_name}' shared successfully with {recipient}!")

# Placeholder for received feedback
st.subheader("📬 Feedback from others")
st.info("You haven't received any feedback yet. Once someone reviews your strategy, it will appear here.")
