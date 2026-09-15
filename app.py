import time

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Watchlist Explorer", layout="wide")
st.title("Watchlist Explorer")
st.caption("Six tech stocks, weekly, 2018-2019. Indexed to 1.00 on 2018-01-01.")

@st.cache_data
def load_data():
    time.sleep(2) # stand-in for a slow API / database call — delete in a real app
    wide = px.data.stocks()
    wide["date"] = pd.to_datetime(wide["date"])
    long = wide.melt(id_vars="date", var_name="ticker", value_name="price")
    return long.sort_values(["ticker", "date"])


df = load_data()
st.dataframe(df.head(20))