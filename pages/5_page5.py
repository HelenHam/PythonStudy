import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat

mat.rcParams['font.family'] = 'Malgun Gothic'
# 한글 깨짐 처리하는 설정

# 데이터 생성
df = pd.DataFrame({
    '이름': ['홍길동', '류관순', '이황'],
    '나이': [19,16,100],
    '키': [145,178,165]
})

# 데이터프레임 데이터 출력
st.dataframe(df,use_container_width=True)

# 막대 차트 설정
fig, ax = plt.subplots()
ax.bar(df['이름'], df['나이'])
st.pyplot(fig)