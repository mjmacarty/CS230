import streamlit as st

import datetime as dt
import pandas_datareader as pdr

today = dt.date.today()
start_date = today - dt.timedelta(days=365)

def user_inputs():

    st.sidebar.header("User Inputs")
    ticker = st.sidebar.text_input('Ticker', 'AAPL')

    start = st.sidebar.date_input('Start Date',start_date)
    end = st.sidebar.date_input('End Date',today)

    button = st.sidebar.button('Get Chart')
    return ticker, start, end, button


def get_data(ticker, start=start_date, end=today):
    data = pdr.get_data_yahoo(ticker, start, end)
    return data

def main():

    ticker, start, end, button = user_inputs()

    if button:
        data = get_data(ticker, start, end)
        st.title('Stock Price Graph for '+ ticker.upper())
        st.line_chart(data.Close)
        st.write("Start Date: " + str(start))
        st.write("End Date: " + str(end))
main()