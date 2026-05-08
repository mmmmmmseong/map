import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import map

st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

m = map.map()

st.title("2026 학교 등산 행사 지도")
#st.text("Incheon - Namdong")
st_folium(m, use_container_width=True, height=500)

