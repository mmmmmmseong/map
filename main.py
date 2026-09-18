import streamlit as st
import sidebar


st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

pages = [
    sidebar.MAP_PAGE,
    sidebar.INFO_PAGE,
    sidebar.INFO_PAGE2,
]

navigation = st.navigation(pages, position="hidden")
navigation.run()

