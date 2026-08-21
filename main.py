import streamlit as st


st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

pages = [
    st.Page("map_page.py", title="지도", icon="🗺️", default=True),
    st.Page("info_page.py", title="산행 안내", icon="ℹ️"),
]

navigation = st.navigation(pages, position="hidden")
navigation.run()

