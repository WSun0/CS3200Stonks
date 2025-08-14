import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar links for role
SideBarLinks()

st.title("📘 Tutorials & Tooltips")
st.write("")
st.write("Learn investing concepts explained in **plain language**, with examples tailored for beginners.")

# Example metric explanations
metrics = {
    "P/E Ratio": "Price-to-Earnings ratio — shows how much investors are willing to pay per $1 of earnings.",
    "Dividend Yield": "Annual dividends as a percentage of the stock price. Higher isn't always better.",
    "Beta": "A measure of how volatile a stock is compared to the overall market."
}

selected_metric = st.selectbox("Choose a metric to learn about:", list(metrics.keys()))
st.info(metrics[selected_metric])

# Expandable tutorial sections
with st.expander("📈 How to read stock charts"):
    st.write("Stock charts can look intimidating, but here’s how to break them down...")
with st.expander("📊 Understanding risk and reward"):
    st.write("Risk is the chance of losing money; reward is the potential for profit...")
