import streamlit as st
from streamlit_folium import st_folium
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
    if selected_courses:
        path_data = pd.read_csv("PathMap.csv", encoding="utf-8-sig")
        filtered_path = path_data[path_data["코스"].isin(selected_courses)]

    map_column, info_column = st.columns([1.7, 1], gap="large")

    with map_column:
        st_folium(map_view, use_container_width=True, height=400)

    with info_column:
        if selected_courses:
            for course_code in selected_courses:
                info = map.course_info.get(f"{course_code}코스", {})
                st.subheader(f"{course_code}코스 안내")
                st.write(f"🔔 {info.get('notice', '즐거운 등산 되세요!')}")
                st.metric(label="⏱️ 예상 소요시간", value=info.get("time", "-"))
                st.warning(
                    f"💊 **주의사항**: {info.get('caution', '등산화를 착용하세요.') }"
                )
        else:
            st.info("선택된 코스가 없습니다.")

    if selected_courses:
        st.markdown("---")
        st.subheader("📸 지점별 포인트 사진")
        for course_code in selected_courses:
            course_path = filtered_path[filtered_path["코스"] == course_code]
            with st.expander(
                f"{course_code}코스 지점별 포인트 사진",
                expanded=False,
            ):
                for _, row in course_path.iterrows():
                    st.write(f"📍 **{row['위치명']}**")
                    image_path = row.get("이미지")
                    if isinstance(image_path, str) and image_path:
                        st.image(
                            image_path,
                            caption=row["위치명"],
                            use_container_width=True,
                        )
                    else:
                        st.caption("📷 *(해당 지점 이미지 파일 준비 중)*")
