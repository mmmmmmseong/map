import streamlit as st


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
            border: 1px solid transparent;
            border-radius: 0.4rem;
            font-weight: 600;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            border-color: rgba(49, 51, 63, 0.2);
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():
    _style_sidebar()
    st.sidebar.title("메뉴")

    if st.sidebar.button("지도", icon="🗺️", use_container_width=True):
        st.switch_page("map_page.py")
    if st.sidebar.button("산행 안내", icon="ℹ️", use_container_width=True):
        st.switch_page("info_page.py")

    with st.sidebar.expander("설정", expanded=False):
        show_map = st.toggle("지도 보기", value=True)
        use_simple_tiles = st.toggle("간소화 지도 사용", value=False)
        show_paths = st.toggle("등산로 지점 표시", value=True)
        show_pline = st.toggle("등산로 연결선 표시", value=False)

    with st.sidebar.expander("코스", expanded=False):
        show_course_a = st.toggle("A코스", value=True)
        show_course_b = st.toggle("B코스", value=False)
        show_course_c = st.toggle("C코스", value=False)
        show_course_d = st.toggle("D코스", value=False)
        show_course_e = st.toggle("E코스", value=False)

    selected_courses = []
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

    return {
        "show_map": show_map,
        "use_simple_tiles": use_simple_tiles,
        "show_paths": show_paths,
        "show_pline": show_pline,
        "selected_courses": selected_courses,
    }
