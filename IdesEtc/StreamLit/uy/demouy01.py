#streamlit run IdesEtc/StreamLit/uy/demouy01.py
import streamlit as st
import pandas

data = {
    "Series_1": [1,3,4,5,7],
    "Series_2": [10,30,40,100,250]
}

df = pandas.DataFrame(data)


st.title("This be the title")
st.subheader("This be the sub-header")
st.write('''This be body text. 
These extra words appear on the same line, not a
different line.
''')

st.write(df)
st.line_chart(df)
st.area_chart(df)
myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is:', myslider * 9/5 + 32)