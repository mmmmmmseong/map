import streamlit as st
from streamlit_folium import st_folium
import map

m = map.map()

st_folium(m, width=1500, height=600)

