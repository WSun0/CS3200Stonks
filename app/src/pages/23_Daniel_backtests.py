# pages/Run_Backtests.py
import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(layout='wide')

# Sidebar navigation
SideBarLinks()

# Page title
st.title("🚀 Run Backtests")

st.markdown("""
Use this tool to run **quick backtests** on selected stocks and strategies.
""")

# --- Backtest Form ---
with st.form("backtest_form"):
    col1, col2, col3 = st.columns(3)
    stock_symbol = col1.text_input("Stock Symbol", value="AAPL")
    strategy = col2.selectbox("Strategy", ["Momentum", "Mean Reversion", "Breakout"])
    time_range = col3.selectbox("Time Range", ["1 Month", "3 Months", "6 Months"])

    submitted = st.form_submit_button("Run Backtest", use_container_width=True, type="primary")
    if submitted:
        # Placeholder: replace with actual backtest function
        st.success(f"✅ Backtest started for {stock_symbol} using {strategy} over {time_range}.")
        logger.info(f"Backtest run: {stock_symbol}, {strategy}, {time_range}")

        # Example simulated backtest results
        backtest_results = pd.DataFrame({
            "Date": pd.date_range(end=datetime.today(), periods=5),
            "Stock": [stock_symbol]*5,
            "Strategy": [strategy]*5,
            "ROI %": [10, 12, 9, 11, 13],
            "Max Drawdown %": [4, 5, 3, 4, 6],
            "Win Rate %": [65, 70, 60, 68, 72],
            "Trades Taken": [20, 22, 19, 21, 23]
        })

        st.subheader("Backtest Results")
<<<<<<< HEAD
        st.dataframe(backtest_results, use_container_width=True)
=======
        st.dataframe(backtest_results, use_container_width=True)
>>>>>>> 87a9cb74fbb54dc7b67742b3c21ad4b18b7a7bab
