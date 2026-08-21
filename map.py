import pandas as pd
import folium


def map(tiles="Cartodb Positron", show_paths=True, show_pline=False, selected_courses=None, color=None):
    path = pd.read_csv("PathMap.csv", encoding="utf-8-sig")
    path["이미지"] = 'images/' + path['코스'] + path['위치명'] + '.jpg'

    if selected_courses is None:
        selected_courses = ["A", "B", "C", "D", "E"]
    elif isinstance(selected_courses, str):
        selected_courses = [selected_courses]

    selected_courses = [course for course in selected_courses if course]

    if color is None:
        color = {
            "A": "red",
            "B": "blue",
            "C": "green",
            "D": "orange",
            "E": "purple",
        }
    elif not isinstance(color, dict):
        raise TypeError("color must be a dictionary of course codes to colors")

    m = folium.Map(
        location=[37.406046, 126.721473],
        zoom_start=17,
        tiles=tiles
    )

    m.save("index.html")

    if show_paths and selected_courses:
        filtered_path = path[path["코스"].isin(selected_courses)]
        for _, p_data in filtered_path.iterrows():
            p_name = p_data["위치명"]
            p_loc = [p_data["위도"], p_data["경도"]]
            course_code = p_data["코스"]

            marker_color = color.get(course_code, "red")

            folium.Marker(
                location=p_loc,
                tooltip=p_name,
                icon=folium.Icon(color=marker_color, icon="info-sign"),
            ).add_to(m)

    if show_pline and selected_courses:
        filtered_path = path[path["코스"].isin(selected_courses)]
        if not filtered_path.empty:
            for course_code in selected_courses:
                course_points = filtered_path[filtered_path["코스"] == course_code][["위도", "경도"]].values.tolist()
                if course_points:
                    line_color = color.get(course_code, "red")
                    folium.PolyLine(course_points, color=line_color, weight=2.5, opacity=1).add_to(m)

    return m
