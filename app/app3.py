import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

btn = st.button("누르면 아픕니다.")

if btn:
    st.write(":blue[버튼] 악!")

df = pd.DataFrame({
    "첫번째": [1,2,3],
    "두번째": [4,5,6],
    "세번째": [7,8,9]
})

st.download_button(
    label = "CVS 다운로드",
    data = df.to_csv(),
    file_name = "샘플.csv",
    mime = "text/csv"
)

box = st.checkbox("확인해주세요.")

if box:
    st.write("뒤로 돌아가세요.")

radio = st.radio(
    label = "식사는 하셨나요?",
    options=('먹었어요.', '안 먹었어요.', '생각 중.')
)

if radio == '먹었어요.':
    st.write("배불러요.")
elif radio == '안 먹었어요.':
    st.write("배고파요.")
else:
    st.write("고민이 많네요!")

select = st.selectbox(
    label = "한식 메뉴",
    options = ("김치찌개", "된장찌개", "불백"),
    index = 0
)

if select == "김치찌개":
    st.write("얼큰하당")
elif select == "된장찌개":
    st.write("차돌 넣어서")
else:
    st.write("밥 추가")


multi = st.multiselect(
    "좋아하는 건 뭔가요?",
    ["사과", "배", "망고"],
    ["사과", "배", "망고"]
)

st.write(f"당신의 선택은: :green[{multi}] 입니다.")

sl = st.slider(
    "범위 값을 지정하세요.",
    0.0, 100.0, (30.0, 65.0)
)

st.write("선택 범위: ", sl)

점심 = st.slider(
    "점심 시간은 언제가 좋을까요?",
    min_value=dt(2024,12,5,13,20),
    max_value=dt(2024,12,5,14,30),
    value=dt(2024,12,5,13,30),
    step=datetime.timedelta(minutes=10),
    format="YY.MM.DD HH:mm"
)

st.write(점심, "이 시간이 좋아요.")