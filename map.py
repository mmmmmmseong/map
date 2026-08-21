import pandas as pd
import folium

# 2-1. 코스별 세부 정보 사전 설정 (소요시간, 주의사항 등)
course_info = {
    "A코스": {
        "time": "4~5분",
        "desc": "학교 출발",
        "notice": "경사가 완만하여 초보자에게 추천합니다.",
        "caution": "편안한 운동화를 착용하세요."
    },
    "B코스": {
        "time": "8~9분",
        "desc": "가온어린이공원 경유",
        "notice": "탁 트인 조망과 아름다운 자연 경관을 즐길 수 있습니다.",
        "caution": "낙엽 및 미끄럼 주의, 등산화 권장."
    },
    "C코스": {
        "time": "10~11분",
        "desc": "서해랑길 94코스 출발",
        "notice": "접근성이 뛰어난 완주 코스입니다.",
        "caution": "수분 보충을 위해 물을 챙기세요."
    },
    "D코스": {
        "time": "13~14분",
        "desc": "세븐일레븐 코스",
        "notice": "편의점이 있어 간식 및 음료 구매가 편리합니다.",
        "caution": "쓰레기는 반드시 되가지고 내려오세요."
    },
    "E코스": {
        "time": "12~13분",
        "desc": "논현주공1단지 코스",
        "notice": "입구를 잘 찾아가야하는 코스입니다.",
        "caution": "벌레에 물리지 않도록 벌레기피제 사용을 권장합니다."
    }
}

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

            if p_name == "입구":
                icon = "log-in"
            elif p_name == "정상":
                icon = "flag"
            elif "이정표" in p_name:
                icon = "info-sign"
            else:
                icon = "map-marker"

            folium.Marker(
                location=p_loc,
                tooltip=p_name,
                icon=folium.Icon(color=marker_color, icon=icon),
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

