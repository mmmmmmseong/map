import streamlit as st
import pandas as pd


def _style_sidebar():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] .stButton {
            margin-bottom: -0.45rem;
        }

        [data-testid="stSidebar"] .stButton > button {
            justify-content: flex-start;
            min-height: 2.25rem;
            padding: 0.35rem 0.7rem;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():
    _style_sidebar()
    st.sidebar.title("메뉴")

    if st.sidebar.button("지도", use_container_width=True):
        st.switch_page("map_page.py")
    if st.sidebar.button("안내", icon="ℹ️", use_container_width=True):
        st.switch_page("info_page.py")

    with st.sidebar.expander("설정", expanded=False):
        show_map = st.toggle("지도 보기", value=True)
        use_simple_tiles = st.toggle("간소화 지도 사용", value=False)
        show_paths = st.toggle("등산로 지점 표시", value=True)
        show_pline = st.toggle("등산로 연결선 표시", value=True)

    path_data = pd.read_csv("PathMap.csv", encoding="utf-8-sig")
    unique_courses = path_data["코스"].dropna().unique().tolist()
    course_options = ["전체 코스 보기"] + unique_courses
    default_course_index = course_options.index("A") if "A" in course_options else 0
    selected_course = st.sidebar.selectbox(
        "가고 싶은 코스를 선택하세요",
        course_options,
        index=default_course_index,
    )

    if selected_course == "전체 코스 보기":
        selected_courses = unique_courses
    else:
        selected_courses = [selected_course]

    return {
        "show_map": show_map,
        "use_simple_tiles": use_simple_tiles,
        "show_paths": show_paths,
        "show_pline": show_pline,
        "selected_courses": selected_courses,
    }
