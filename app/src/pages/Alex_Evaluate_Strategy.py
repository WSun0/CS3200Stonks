import logging
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks

# Configure logging
logger = logging.getLogger(__name__)

# Set the page configuration.
st.set_page_config(layout='wide')

# Show sidebar links.
SideBarLinks()

# --- Page Content: "Backtest Results" for a specific strategy ---
# In a real app, this page would likely be accessed from a link in the table on the previous page.
# It would take an argument (like a strategy ID) to fetch the correct data.
st.title('Backtest Results')
st.write('---')

# --- Mock Data ---
# This mock data is for a single, specific strategy.
# You would replace this with data fetched from your database.
roi = 15.2
drawdown = 4.1
sharpe_ratio = 1.8
profit = 500.0 

# Mock data for the portfolio value chart
portfolio_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01']),
    'Portfolio Value': [100, 110, 105, 120, 135, 130, 145, 150, 160, 155, 170, 180]
})
portfolio_data.set_index('date', inplace=True)

# Mock data for the "Trade-by-Trade Results" table
trade_data = pd.DataFrame({
    'Date': pd.to_datetime(['2023-01-10', '2023-02-15', '2023-03-20', '2023-04-25', '2023-05-30']),
    'Buy/Sell': ['Buy', 'Sell', 'Buy', 'Sell', 'Buy'],
    'Symbol': ['AAPL', 'AAPL', 'GOOG', 'GOOG', 'MSFT'],
    'Profit': [15.20, -5.50, 25.30, 10.10, -2.50]
})

# --- Display KPIs in a four-column layout ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"### ROI")
    st.metric(label="", value=f"{roi}%")

with col2:
    st.markdown(f"### Drawdown")
    st.metric(label="", value=f"{drawdown}%")

with col3:
    st.markdown(f"### Sharpe Ratio")
    st.metric(label="", value=sharpe_ratio)
    
with col4:
    st.markdown(f"### Profit")
    st.metric(label="", value=f"${profit}")

# Add some vertical spacing
st.write('')
st.write('---')

# --- Display Portfolio Value Chart ---
st.write('### Portfolio Value')
st.line_chart(portfolio_data)

st.write('---')

# --- Display Trade-by-Trade Results Table ---
st.write('### Trade-by-Trade Results')
st.dataframe(trade_data, use_container_width=True)
