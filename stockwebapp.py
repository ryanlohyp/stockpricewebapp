#import os; import sys; print(os.path.dirname(sys.executable))

import streamlit as st
import yfinance as finance
import datetime as dt

st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Finance Web Application")
st.sidebar.header("Finance Hub")

# Define get_ticker function
def get_ticker(name):
    company = finance.Ticker(name)
    return company 

# Get stock ticker
company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")

# Get date range
now_datetime = dt.datetime.now()
delta_year = 2
start_year = now_datetime.year - delta_year

start_date = dt.date(start_year, now_datetime.month, now_datetime.day).strftime("%Y-%m-%d")
end_date = now_datetime.strftime("%Y-%m-%d")
 
print(start_date)
print(end_date)

# fetches the data: Open, Close, High, Low and Volume
google = finance.download("GOOGL", start=start_date, end=end_date)
microsoft = finance.download("MSFT", start=start_date, end=end_date)
 
# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")
 
# markdown syntax
st.write("""
### Google
""")
 
# detailed summary on Google
st.write(company1.info['longBusinessSummary']) 
st.write(google)
 
# plots the graph
st.line_chart(data1.values) 
 
st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)