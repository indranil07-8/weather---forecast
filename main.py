import streamlit as st
import plotly.express as px

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
def get_data(days):
    dates=["2022-25-10", "2022-26-10" , "2022-27-10"]
    temperatures=[10,11,15]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures

d,t=get_data(days)


figure = px.line(x=d , y=t,  labels={"x":"Dates" , "y":"Temperature(c)"})
st.plotly_chart(figure)