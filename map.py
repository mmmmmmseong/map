import streamlit as st
import pandas as pd
import folium

def map():
    school = pd.read_csv("인천광역시 남동구_고등학교_20240325.csv", encoding="cp949")
    
    tooltip = "클릭해보세요"
    
    m = folium.Map(
    location=[37.406046, 126.721473],
    zoom_start = 11.9,
    tiles='Cartodb Positron'
    )
    
    m.save('index.html')
    
    for i in range(len(school)):
        s_data = school.iloc[i]
        s_name = s_data["학교명"]
        s_loc = [s_data["위도"], s_data["경도"]]
        s_type = s_data["설립구분"]
        s_adress = s_data["주소"]
        s_page = s_data["홈페이지"]
        s_tel = s_data["연락처"]
        
        icon=folium.Icon(color="gray", icon="info-sign")
        
        if s_name == "인천남동고등학교":
            icon=folium.Icon(color="blue", icon="home")
        
        folium.Marker(
            location = s_loc,
            popup = folium.Popup(f"\
            <h4><strong>{s_name}</strong></h4>\
            <h6>\
                {s_adress}, {s_type}\
                <br>\
                <a href='{s_page}'>{s_page}</a>\
                <br>\
                <br>\
                {s_tel}\
            </h6>", max_width=600),
            tooltip= s_name,
            icon = icon
        ).add_to(m)

    return m
