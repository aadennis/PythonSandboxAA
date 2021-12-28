import streamlit as st

st.title("demo03.py - checkbox - Streamlit")

checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")

if checkbox_one:
    value = "Yes"
elif checkbox_two:
    value = "No"
else:
    value = "No value selected"

st.write(f"You selected: {value}")

