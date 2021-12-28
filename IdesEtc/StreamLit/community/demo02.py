import streamlit as st

st.title("demo02 - dropdown select - Streamlit")

selectbox = st.selectbox(
    "Select yes or no",
    ["Yes", "No"]
)
st.write(f"You selected {selectbox}")

