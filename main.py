import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import map

st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

m = map.map()

st.title("2026 학교 등산 행사 지도 ⛰️")
st.header("남동고등학교 인근 지도")

df = pd.read_csv("인천광역시 남동구_고등학교_20240325.csv", encoding="cp949")
df_lation = df[['위도', '경도']]
df_lation = df_lation.rename(columns={'위도': 'lat', '경도': 'lon'})

toggle_map1 = st.toggle("지도 1 보기", value=True)
toggle_map2 = st.toggle("지도 2 보기", value=True)

if toggle_map1:
    st_folium(m, use_container_width=True, height=500)


if toggle_map2:
    st.map(df_lation)





