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

# --- Page Content: "Export Strategy Report" ---
st.title('Export Strategy Report')
st.write('---')
st.write('Use this page to generate and download reports for your backtested strategies.')

# --- Mock Data for the report ---
# This DataFrame simulates the trade-by-trade results from the previous page.
# In a real application, this data would be fetched dynamically from your database.
trade_data = pd.DataFrame({
    'Date': pd.to_datetime(['2023-01-10', '2023-02-15', '2023-03-20', '2023-04-25', '2023-05-30']),
    'Buy/Sell': ['Buy', 'Sell', 'Buy', 'Sell', 'Buy'],
    'Symbol': ['AAPL', 'AAPL', 'GOOG', 'GOOG', 'MSFT'],
    'Profit': [15.20, -5.50, 25.30, 10.10, -2.50]
})

# Convert the DataFrame to a CSV string for the download button.
# This is a key step for creating downloadable content in Streamlit.
csv_report = trade_data.to_csv(index=False)

# --- Report Export UI ---
st.subheader('Report Options')

# Create a dropdown to select the report format.
# For now, only CSV is functional. PDF would require a library like reportlab or fpdf.
report_format = st.selectbox(
    'Select a report format:',
    ('CSV', 'PDF')
)

# A download button that triggers the file download.
# The `data` argument is the content to be downloaded.
if st.download_button(
    label="Download Report",
    data=csv_report,
    file_name="backtest_report.csv",
    mime="text/csv",
    use_container_width=True
):
    st.success('Report download initiated!')
    st.balloons()

# A note to explain the functionality
st.write('')
st.info('The PDF option is a placeholder. You would need to add code to generate a PDF file to enable this functionality.')
