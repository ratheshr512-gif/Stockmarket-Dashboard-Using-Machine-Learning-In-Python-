import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Stock Dashboard",
    layout="wide"
)

st.title("Real-Time Stock Market Dashboard")

stock_symbol = st.text_input(
    "Enter Stock Symbol (e.g., AAPL, TSLA, INFY.NS)",
    "AAPL"
)

period = st.selectbox(
    "Select Time Period",
    ["1mo", "3mo", "6mo", "1y", "5y"]
)

@st.cache_data
def load_data(symbol, period):
    stock = yf.Ticker(symbol)
    df = stock.history(period=period)
    return df

df = load_data(stock_symbol, period)

if df.empty:
    st.error("No data found. Check stock symbol.")
else:
    st.subheader(f"Data for {stock_symbol}")
    st.dataframe(df.tail())

    df["MA20"] = df["Close"].rolling(
        window=20
    ).mean()

    df["MA50"] = df["Close"].rolling(
        window=50
    ).mean()

    st.subheader(
        "Price Chart with Moving Averages"
    )

    st.line_chart(
        df[["Close", "MA20", "MA50"]]
    )

    latest_close = df["Close"].iloc[-1]
    ma20 = df["MA20"].iloc[-1]
    ma50 = df["MA50"].iloc[-1]

    st.subheader("Insights")

    if latest_close > ma20 and ma20 > ma50:
        st.success(
            "Uptrend detected (Bullish Signal)"
        )

    elif latest_close < ma20 and ma20 < ma50:
        st.error(
            "Downtrend detected (Bearish Signal)"
        )

    else:
        st.warning(
            "Sideways / Uncertain Trend"
        )

    st.write(
        f"Latest Price: {latest_close:.2f}"
    )

    st.write(
        f"MA20: {ma20:.2f}"
    )

    st.write(
        f"MA50: {ma50:.2f}"
    )