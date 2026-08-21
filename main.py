import streamlit as st
from streamlit_folium import st_folium
import map

st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

def map_page():
    st.title("2026 학교 등산 행사 지도 ⛰️")

    st.sidebar.title("메뉴")
    with st.sidebar.expander("설정", expanded=True):
        show_map = st.toggle("지도 보기", value=True)
        use_simple_tiles = st.toggle("간소화 지도 사용", value=False)
        show_paths = st.toggle("등산로 지점 표시", value=True)
        show_pline = st.toggle("등산로 연결선 표시", value=False)

    with st.sidebar.expander("코스", expanded=True):
        show_course_a = st.toggle("A코스", value=True)
        show_course_b = st.toggle("B코스", value=False)
        show_course_c = st.toggle("C코스", value=False)
        show_course_d = st.toggle("D코스", value=False)
        show_course_e = st.toggle("E코스", value=False)

    selected_courses = []
    course_colors = {
        "A": "red",
        "B": "pink",
        "C": "green",
        "D": "orange",
        "E": "purple",
    }

    if show_course_a:
        selected_courses.append("A")
    if show_course_b:
        selected_courses.append("B")
    if show_course_c:
        selected_courses.append("C")
    if show_course_d:
        selected_courses.append("D")
    if show_course_e:
        selected_courses.append("E")

    tile_name = "Cartodb Positron" if use_simple_tiles else "OpenStreetMap"

    if st.sidebar.button("산행 안내", icon="ℹ️", use_container_width=True):
        st.switch_page("info_page.py")

    if show_map:
        m = map.map(
            tiles=tile_name,
            show_paths=show_paths and bool(selected_courses),
            show_pline=show_pline and bool(selected_courses),
            selected_courses=selected_courses,
            color=course_colors,
        )
        st_folium(m, use_container_width=True, height=500)


pages = [
    st.Page(map_page, title="지도", icon="🗺️"),
    st.Page("info_page.py", title="산행 안내", icon="ℹ️"),
]
navigation = st.navigation(pages, position="hidden")
navigation.run()

