import streamlit as st
from streamlit_folium import st_folium
import map

st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("2026 학교 등산 행사 지도 ⛰️")

st.sidebar.title("메뉴")
with st.sidebar.expander("설정", expanded=True):
    show_map = st.toggle("지도 보기", value=True)
    use_simple_tiles = st.toggle("간소화 지도 사용", value=False)
    show_schools = st.toggle("인근 학교 표시", value=True)
    show_paths = st.toggle("등산로 지점 표시", value=True)
    show_pline = st.toggle("등산로 연결선 표시", value=False)

with st.sidebar.expander("코스", expanded=True):
    show_course_a = st.toggle("A코스", value=True)
    show_course_b = st.toggle("B코스", value=False)
    show_course_c = st.toggle("C코스", value=False)
    show_course_d = st.toggle("D코스", value=False)
    show_course_e = st.toggle("E코스", value=False)

selected_courses = [
    course_code
    for course_code, is_enabled in [
        ("A", show_course_a),
        ("B", show_course_b),
        ("C", show_course_c),
        ("D", show_course_d),
        ("E", show_course_e),
    ]
    if is_enabled
]

tile_name = "Cartodb Positron" if use_simple_tiles else "OpenStreetMap"

if show_map:
    m = map.map(
        tiles=tile_name,
        show_schools=show_schools,
        show_paths=show_paths and bool(selected_courses),
        show_pline=show_pline and bool(selected_courses),
        selected_courses=selected_courses,
    )
    st_folium(m, use_container_width=True, height=500)

