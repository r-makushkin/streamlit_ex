import yfinance as yf
import streamlit as st


st.header("График котировок акций компании Apple")


tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# суть данного задания понятна, завтра постараюсь запилить сайдбар для выбора периодов