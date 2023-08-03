import streamlit as st

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