import streamlit as st

st.title("타이틀이에요.")

st.title("스마일:sunglasses:")

st.header("이건 헤더예요.")

st.subheader("이건 서브헤더예요.")

st.caption("이건 캡션이에요.")

st.code("arr = []", language="python")

sample_code ="""
def 함수():
    return 1+1
"""

st.code(sample_code, language="python")

st.text("일반 텍스트예요.")

st.markdown("***웹개발은*** **너무 어려워요.**")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]")

st.markdown("*안녕!* 이건 streamlit을 통해 제 공부거리를 정리하기 위한 곳이에요.")
st.code("이런저런 코드를 많이 넣을 수 있습니다.", language="java")

st.latex(r"\sqrt{x^2+y^2}=1")