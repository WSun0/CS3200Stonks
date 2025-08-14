# pages/Compare_Stocks.py
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
import requests

# Page config
st.set_page_config(layout='wide')

# Navigation sidebar
SideBarLinks()

# Page title
st.title("Compare Current Stocks to Backtest Data")

st.markdown("""
Use this tool to view **live market performance** side-by-side with your
**backtest results** for a chosen strategy.
""")

# --- Strategy selection ---
strategy = st.selectbox("Select Strategy", ["Momentum", "Mean Reversion", "Breakout"])

# --- Stock selection ---
stock_symbol = st.text_input("Stock Symbol (e.g., AAPL, TSLA)", value="AAPL")

col1, col2 = st.columns(2)

with col1:
    if st.button("Load Live Stock Data", use_container_width=True):
        try:
            # Example: replace with real API call
            live_data = pd.DataFrame({
                "Date": pd.date_range(end=pd.Timestamp.today(), periods=5),
                "Price": [150, 152, 149, 151, 153]
            })
            st.session_state["live_data"] = live_data
            st.success(f"Live data for {stock_symbol} loaded.")
        except Exception as e:
            st.error(f"Error loading live data: {e}")
            logger.error(e)

with col2:
    if st.button("Load Backtest Data", use_container_width=True):
        try:
            # Example: replace with real backtest retrieval
            backtest_data = pd.DataFrame({
                "Date": pd.date_range(end=pd.Timestamp.today(), periods=5),
                "Price": [148, 150, 147, 149, 150]
            })
            st.session_state["backtest_data"] = backtest_data
            st.success(f"Backtest data for {strategy} loaded.")
        except Exception as e:
            st.error(f"Error loading backtest data: {e}")
            logger.error(e)

# --- Show comparison ---
if "live_data" in st.session_state and "backtest_data" in st.session_state:
    st.subheader("Performance Comparison")
    comparison_df = st.session_state["live_data"].merge(
        st.session_state["backtest_data"],
        on="Date",
        suffixes=("_Live", "_Backtest")
    )
    st.dataframe(comparison_df, use_container_width=True)

    # Simple chart comparison
    st.line_chart(
        comparison_df.set_index("Date")[["Price_Live", "Price_Backtest"]]
    )
