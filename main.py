import streamlit as st
from streamlit_folium import st_folium
import map

st.set_page_config(layout="wide")

m = map.map()

st.title("Highschool Map")
st.text("Highschool Map")
st_folium(m, use_container_width=True, height=500)

