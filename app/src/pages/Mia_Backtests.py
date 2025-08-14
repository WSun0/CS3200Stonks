import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar links for role
SideBarLinks()

st.title("📊 Backtest Strategies")
st.write("")
st.write("Test your investing strategies on historical data without risking real money.")

# Select strategy & time period
strategy = st.selectbox("Choose a strategy to backtest", ["Moving Average Crossover", "Buy and Hold", "RSI Indicator"])
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Run Backtest", type="primary", use_container_width=True):
    st.success(f"✅ Backtest completed for '{strategy}' from {start_date} to {end_date}.")

    # Mock results
    st.subheader("📈 Backtest Results")
    st.write("**Total Return:** +12.5%")
    st.write("**Max Drawdown:** -5.3%")
    st.write("**Sharpe Ratio:** 1.4")

    st.line_chart({"Portfolio Value": [10000, 10200, 10500, 11000, 11250]})
