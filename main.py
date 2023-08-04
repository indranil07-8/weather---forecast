import streamlit as st
import plotly.express as px
from backend  import get_data

#title
st.title("Weather Forcast for the Next Days")
#input
place = st.text_input("Place:")
#add slider
days=st.slider("Forcast Days", min_value=1,max_value=5,help="select the number of forecasted days")
#selectbox
option=st.selectbox("select data to view",
                    ("Temperature" , "sky"))


st.subheader(f"{option}for the next{days}days in {place}")

#add graph
#created plot figure grap

d,t=get_data(place,days, option)



figure = px.line(x=d , y=t,  labels={"x":"Dates" , "y":"Temperature(c)"})
st.plotly_chart(figure)