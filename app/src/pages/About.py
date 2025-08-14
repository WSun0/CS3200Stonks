import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About Stonks Project")

st.markdown(
    """
    This is a **Stonks Project** application for CS 3200 Database Design course.

    ## Project Overview
    Stonks is a comprehensive stock trading strategy platform that allows users to:
    - **Financial Analysts**: View strategy performance, evaluate strategies, and export results
    - **Backend Developers**: Test APIs and manage system infrastructure  
    - **College Students**: Learn about trading strategies and market analysis
    - **Hobbyist Traders**: Compare stocks, manage backtests, and develop trading strategies

    ## Features
    - **Role-Based Access Control**: Different interfaces for different user types
    - **Strategy Management**: Create, test, and evaluate trading strategies
    - **Performance Analytics**: View detailed backtest results and metrics
    - **Stock Comparison**: Analyze and compare different assets
    - **API Integration**: RESTful backend with MySQL database
    - **Real-time Data**: Access to market data and performance metrics

    ## Technology Stack
    - **Frontend**: Streamlit (Python-based web framework)
    - **Backend**: Flask REST API
    - **Database**: MySQL with comprehensive trading data
    - **Containerization**: Docker with separate services for app, API, and database
    - **Data Analysis**: Python with pandas, numpy, and visualization libraries

    ## Database Schema
    The application includes tables for:
    - Users and authentication
    - Trading strategies and rules
    - Asset information and price history
    - Backtest results and performance metrics
    - Error logging and user activity tracking

    This project demonstrates modern full-stack development practices with a focus on financial data management and user experience design.
    """
)

# Add a button to return to home page
if st.button("Return to Home", type="primary"):
    st.switch_page("Home.py")
