import html

import pandas as pd
import folium
from branca.element import Element

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


def map(
    tiles="Cartodb Positron",
    show_paths=True,
    show_pline=False,
    show_location=False,
    selected_courses=None,
    color=None,
):
    path = pd.read_csv("PathMap.csv", encoding="utf-8-sig")

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
        location=[37.407576,126.719651],
        zoom_start=17,
        tiles=tiles
    )

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

            img_file = p_data["이미지"]

            popup_html = f"""
            <div style="width: 200px; text-align: center; font-family: sans-serif;">
                <h4 style="margin: 5px 0; color: #2c3e50;">
                    {html.escape(p_name)}
                </h4>
                <p style="margin: 2px; font-size: 12px; color: #7f8c8d;">
                    {html.escape(course_code)}코스
                </p>
                <hr style="margin: 5px 0; border: 0; border-top: 1px solid #ddd;">
                 <img src="{img_file}" width="180px"
                     style="border-radius: 6px; margin-top: 5px;">
            </div>
            """

            folium.Marker(
                location=p_loc,
                popup=folium.Popup(popup_html, max_width=220),
                tooltip=f"{p_name} (클릭 시 사진 보기)",
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

    if show_location:
        location_script = f"""
        <style>
            .location-status {{
                background: white;
                border: 2px solid rgba(0, 0, 0, 0.2);
                border-radius: 4px;
                box-shadow: 0 1px 5px rgba(0, 0, 0, 0.35);
                color: #333;
                font: 14px/1.5 sans-serif;
                padding: 6px 10px;
            }}
        </style>
        <script>
            window.setTimeout(function () {{
                var map = {m.get_name()};
                var status = L.control({{ position: 'topleft' }});
                var locationMarker;
                var accuracyCircle;

                status.onAdd = function () {{
                    var element = L.DomUtil.create('div', 'location-status');
                    element.textContent = '현재 위치 확인 중...';
                    return element;
                }};
                status.addTo(map);

                if (!navigator.geolocation) {{
                    status.getContainer().textContent = '브라우저가 위치정보를 지원하지 않습니다.';
                    return;
                }}

                navigator.geolocation.getCurrentPosition(
                    function (position) {{
                        var location = [
                            position.coords.latitude,
                            position.coords.longitude
                        ];
                        var accuracy = position.coords.accuracy;

                        accuracyCircle = L.circle(location, {{
                            radius: accuracy,
                            color: '#1976d2',
                            fillColor: '#1976d2',
                            fillOpacity: 0.12,
                            weight: 1
                        }}).addTo(map);
                        locationMarker = L.circleMarker(location, {{
                            radius: 8,
                            color: '#ffffff',
                            weight: 3,
                            fillColor: '#1976d2',
                            fillOpacity: 1
                        }}).addTo(map);
                        locationMarker.bindPopup(
                            '내 위치<br>위도: ' + location[0].toFixed(6) +
                            '<br>경도: ' + location[1].toFixed(6)
                        );
                        map.setView(location, Math.max(map.getZoom(), 16));
                        status.getContainer().textContent = '현재 위치가 표시되었습니다.';
                    }},
                    function (error) {{
                        var message = '위치정보 이용을 허용해 주세요.';
                        if (error.code === error.POSITION_UNAVAILABLE) {{
                            message = '현재 위치를 확인할 수 없습니다.';
                        }} else if (error.code === error.TIMEOUT) {{
                            message = '위치 확인 시간이 초과되었습니다.';
                        }}
                        status.getContainer().textContent = message;
                    }},
                    {{ enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }}
                );
            }}, 0);
        </script>
        """
        m.get_root().html.add_child(Element(location_script))

    return m

