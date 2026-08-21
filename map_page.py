import streamlit as st
from streamlit_folium import st_folium
from pathlib import Path
import pandas as pd
import map
import sidebar


st.title("학교 등산 행사 지도 ⛰️")

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
    map_column, info_column = st.columns([1.7, 1], gap="large")

    with map_column:
        map_result = st_folium(map_view, use_container_width=True, height=400)

    with info_column:
        st.subheader("코스 주의 사항")
        if selected_courses:
            for course_code in selected_courses:
                course = map.course_info.get(f"{course_code}코스")
                if course:
                    st.markdown(f"**{course_code}코스**")
                    st.write(course["caution"])
        else:
            st.info("선택된 코스가 없습니다.")

    clicked_marker = map_result.get("last_object_clicked")
    if clicked_marker:
        path_data = pd.read_csv("PathMap.csv", encoding="utf-8-sig")
        clicked_lat = clicked_marker.get("lat")
        clicked_lng = clicked_marker.get("lng")
        matching_path = path_data[
            (path_data["위도"].sub(clicked_lat).abs() < 0.00001)
            & (path_data["경도"].sub(clicked_lng).abs() < 0.00001)
        ]

        if not matching_path.empty:
            selected_path = matching_path.iloc[0]
            location_name = selected_path["위치명"]
            course_code = selected_path["코스"]
            image_path = Path("images") / f"{course_code}{location_name}.jpg"

            st.subheader(f"{course_code}코스 · {location_name}")
            if image_path.exists():
                st.image(str(image_path), use_container_width=True)
            else:
                st.info("이 지점에 등록된 사진이 없습니다.")
