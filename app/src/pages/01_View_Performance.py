import logging
import pandas as pd
import streamlit as st
from modules.nav import SideBarLinks

# Configure logging (good practice)
logger = logging.getLogger(__name__)

# Set the page configuration, just as in your original files.
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged in user.
# In a full application, this would determine what Alex sees in the sidebar.
SideBarLinks()

# --- Page Content: "Backtest Results" ---
# This is the main title for the page, as seen in your wireframe.
st.title('Backtest Results')
st.write('---')

# --- Mock Data ---
# This data is hardcoded to match the numbers in the wireframe.
# For a real application, you would connect to a database or API here
# to fetch the real results for Alex.
total_strategies = 12
successful_strategies = 8
avg_roi = 15.2

# Mock data for the portfolio value chart
portfolio_data = pd.DataFrame({
    'date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01']),
    'Portfolio Value': [100, 110, 105, 120, 135, 130, 145, 150, 160, 155, 170, 180]
})
portfolio_data.set_index('date', inplace=True)

# Mock data for the strategies table
strategies_data = pd.DataFrame({
    'Strategy': [f'Strategy {i}' for i in range(1, 7)],
    'Avg. ROI (%)': [5.1, 10.5, 3.2, 18.0, 7.8, 12.1],
    'Win Rate (%)': [65, 78, 55, 90, 72, 85],
    'Max Drawdown': [2.5, 4.1, 6.7, 1.8, 3.9, 2.2],
    'Sharpe Ratio': [1.2, 1.8, 0.9, 2.5, 1.5, 2.0]
})

# --- Display KPIs in a three-column layout ---
# This section uses Streamlit's columns to lay out the three key metrics
# side-by-side, matching the top section of the wireframe.
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"### Total Strategies")
    st.metric(label="", value=total_strategies)

with col2:
    st.markdown(f"### Successful Strategies")
    st.metric(label="", value=successful_strategies)

with col3:
    st.markdown(f"### Avg. ROI (%)")
    st.metric(label="", value=avg_roi)
    
# Add some vertical spacing
st.write('')

# --- Display Portfolio Value Chart ---
# This section creates the line chart.
st.write('### Portfolio Value')
st.line_chart(portfolio_data)

st.write('---')

# --- Display Strategies Table ---
# This section creates the table.
st.write('### Strategies')
st.dataframe(strategies_data, use_container_width=True)