import geopandas as gpd
import streamlit as st
import pandas as pd
st.write("hello welcome")

st.text("text")
df = pd.read_csv('requirements.txt', sep='|')
st.dataframe(df)

