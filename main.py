import streamlit as st


st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

pages = [
    st.Page("map_page.py", title="지도", default=True),
    st.Page("info_page.py", title="산행 안내"),
    st.Page("info_page2.py", title="페이지 정보")
]

navigation = st.navigation(pages, position="hidden")
navigation.run()

