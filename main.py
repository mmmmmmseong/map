import streamlit as st
from PIL import Image

logo = Image.open("logo2.svg")

st.set_page_config(
    page_title="남동고 등산 메이트", 
    page_icon=logo,
    layout="wide"
)

st.logo("logo2.svg")

pages = [
    st.Page("map_page.py", title="지도", default=True),
    st.Page("info_page.py", title="산행 안내"),
    st.Page("info_page2.py", title="페이지 정보")
]

navigation = st.navigation(pages, position="hidden")
navigation.run()

