# pip install plotly
import streamlit as st
import plotly.graph_objects as go


st.title("Demo05.py - Streamlit - pie chart")

fig = go.Figure(
    data=[go.Pie(
        labels=['A', 'B', 'C'],
        values=[30, 20, 50]
    )]
)
fig = fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=15
)

st.write("Pie chart in Streamlit")
st.plotly_chart(fig)
