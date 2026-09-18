import streamlit as st
import sidebar

sidebar.render_sidebar()
st.title("페이지 정보")
st.write("남동고 정보 동아리에서 제작한 학교 등산 행사 안내 지도입니다.")

st.subheader("서비스 소개")
st.markdown(
	"""
	이 서비스에서는 듬배산의 등산 코스별 경로, 지점, 예상 소요시간과 관련 정보를 확인할 수 있습니다.
	사용자가 출발 전에 코스를 쉽게 확인하고 안전하게 이동할 수 있도록 제작했습니다.
	"""
)

st.subheader("제작 목적")
st.markdown(
    """
    학교 등산 행사에 참여하는 학생들이 코스별 경로와 지점을 쉽게 확인하고, 안전하게 이동할 수 있도록 돕기 위해 제작했습니다.
    """
)

st.subheader("소개하는 장소")
st.markdown(
    """
    이 서비스에서는 인천남동고등학교 주변의 **듬배산** 등산 코스와 지점을 안내합니다.
    """
)

st.subheader("제작 동아리")
st.markdown(
	"""
	인천남동고등학교 동아리 **AI 브릿지** 학생들이 코스 자료를 수집·정리하고, 지도 화면을 구성하여 제작했습니다.
	"""
)



