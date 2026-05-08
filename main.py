import streamlit as st
import map.py as map

data = map.get_data()
st.write(data)
