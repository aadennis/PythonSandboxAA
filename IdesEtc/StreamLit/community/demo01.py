import pandas as pd
import streamlit as st

st.title("demo01.py - dataframe - Streamlit")

st.write("Our first DataFrame")

st.write(
  pd.DataFrame({
      'A': [1, 2, 3, 4],
      'B': [5, 6, 7, 8]
    })
)
