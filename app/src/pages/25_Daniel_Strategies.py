import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

import streamlit as st
import pandas as pd
import io

st.set_page_config(layout="wide", page_title="Strategy Import / Export")


st.title("📤 Import & Export Strategy Templates")

# Import Section
st.subheader("📥 Import Strategy Template")
uploaded_file = st.file_uploader("Upload a CSV strategy template", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Template Imported Successfully")
    st.dataframe(df)

# Export Section
st.subheader("📤 Export Strategy Template")
sample_template = pd.DataFrame({
    "Indicator": ["RSI", "EMA", "MACD"],
    "Parameter 1": [14, 50, 12],
    "Parameter 2": [30, 200, 26]
})

buffer = io.BytesIO()
sample_template.to_csv(buffer, index=False)
st.download_button(
    label="Download Sample Strategy Template",
    data=buffer.getvalue(),
    file_name="strategy_template.csv",
    mime="text/csv"
)