import streamlit as st
from streamlit_folium import st_folium
import map
import sidebar


st.title("2026 등산 행사 지도 ⛰️")

settings = sidebar.render_sidebar()
show_map = settings["show_map"]
use_simple_tiles = settings["use_simple_tiles"]
show_paths = settings["show_paths"]
show_pline = settings["show_pline"]
selected_courses = settings["selected_courses"]

course_colors = {
    "A": "red",
    "B": "pink",
    "C": "green",
    "D": "orange",
    "E": "purple",
}

tile_name = "Cartodb Positron" if use_simple_tiles else "OpenStreetMap"

if show_map:
    map_view = map.map(
        tiles=tile_name,
        show_paths=show_paths and bool(selected_courses),
        show_pline=show_pline and bool(selected_courses),
        selected_courses=selected_courses,
        color=course_colors,
    )
    st_folium(map_view, use_container_width=True, height=500)
