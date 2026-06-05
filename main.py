import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import map

st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("2026 학교 등산 행사 지도 ⛰️")

st.markdown("### ⚙️ 지도 설정")
st.markdown("""
<div style="background-color: rgba(128, 128, 128, 0.15); padding: 15px; border-radius: 8px;">
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    toggle_map1 = st.toggle("지도 보기", value=True)
with col2:
    toggle_tile = st.toggle("간소화 지도 사용", value=True)
with col3:
    toggle_schools = st.toggle("인근 학교 표시", value=True)
with col4:
    toggle_paths = st.toggle("등산로 지점 표시", value=True)

tile_name = "Cartodb Positron" if toggle_tile else "OpenStreetMap"

if toggle_map1:
    m = map.map(tiles=tile_name, show_schools=toggle_schools, show_paths=toggle_paths)
    st_folium(m, use_container_width=True, height=500)

#####################################################################################################

df = pd.read_csv("인천광역시 남동구_고등학교_20240325.csv", encoding="cp949")
df_lation = df[['위도', '경도']]
df_lation = df_lation.rename(columns={'위도': 'lat', '경도': 'lon'})

toggle_map2 = st.toggle("streamlit map", value=False)

if toggle_map2:
    st.map(df_lation)





