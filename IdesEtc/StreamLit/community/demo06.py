import streamlit as st

st.title("demo06.py - sidebar select - streamlit")

selectbox = st.sidebar.selectbox(
    "Select yes or no",
    ["Yes", "No"]
)
st.write(f"You selected {selectbox}")