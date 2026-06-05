import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import map

st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("2026 학교 등산 행사 지도 ⛰️")

st.sidebar.title("메뉴")
with st.sidebar.expander("설정", expanded=True):
    toggle_map1 = st.toggle("지도 보기", value=True)
    toggle_tile = st.toggle("간소화 지도 사용", value=False)
    toggle_schools = st.toggle("인근 학교 표시", value=True)
    toggle_paths = st.toggle("등산로 지점 표시", value=True)
    toggle_pline = st.toggle("등산로 연결선 표시", value=False)

tile_name = "Cartodb Positron" if toggle_tile else "OpenStreetMap"

if toggle_map1:
    m = map.map(tiles=tile_name, show_schools=toggle_schools, show_paths=toggle_paths, show_pline=toggle_pline)
    st_folium(m, use_container_width=True, height=500)



