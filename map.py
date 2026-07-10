import pandas as pd
import folium


def map(tiles="Cartodb Positron", show_schools=True, show_paths=True, show_pline=False, selected_courses=None):
    school = pd.read_csv("인천광역시 남동구_고등학교_20240325.csv", encoding="cp949")
    path = pd.read_csv("PathMap.csv", encoding="utf-8-sig")

    if selected_courses is None:
        selected_courses = ["A", "B", "C", "D", "E"]
    elif isinstance(selected_courses, str):
        selected_courses = [selected_courses]

    selected_courses = [course for course in selected_courses if course]

    m = folium.Map(
        location=[37.406046, 126.721473],
        zoom_start=17,
        tiles=tiles,
    )

    m.save("index.html")

    if show_schools:
        for _, s_data in school.iterrows():
            s_name = s_data["학교명"]
            s_loc = [s_data["위도"], s_data["경도"]]
            s_type = s_data["설립구분"]
            s_adress = s_data["주소"]
            s_page = s_data["홈페이지"]
            s_tel = s_data["연락처"]

            icon = folium.Icon(color="gray", icon="info-sign")

            if s_name == "인천남동고등학교":
                icon = folium.Icon(color="blue", icon="home")

            folium.Marker(
                location=s_loc,
                popup=folium.Popup(
                    f"\
                    <h4><strong>{s_name}</strong></h4>\
                    <h6>\
                        {s_adress}, {s_type}\
                        <br>\
                        <a href='{s_page}'>{s_page}</a>\
                        <br>\
                        <br>\
                        {s_tel}\
                    </h6>",
                    max_width=600,
                ),
                tooltip=s_name,
                icon=icon,
            ).add_to(m)

    if show_paths and selected_courses:
        filtered_path = path[path["코스"].isin(selected_courses)]
        for _, p_data in filtered_path.iterrows():
            p_name = p_data["위치명"]
            p_loc = [p_data["위도"], p_data["경도"]]

            folium.Marker(
                location=p_loc,
                tooltip=p_name,
                icon=folium.Icon(color="red", icon="info-sign"),
            ).add_to(m)

    if show_pline and selected_courses:
        filtered_path = path[path["코스"].isin(selected_courses)]
        if not filtered_path.empty:
            path_points = filtered_path[["위도", "경도"]].values.tolist()
            folium.PolyLine(path_points, color="red", weight=2.5, opacity=1).add_to(m)

    return m
