import streamlit as st
import random as rd
import datetime as dt

st.set_page_config(
    initial_sidebar_state="collapsed"
)

st.title(":green[로또 생성기]")

def getLotto():
    lotto = set()

    while len(lotto) < 6:
        num = rd.randint(1,46)
        lotto.add(num)

    return lotto

btn = st.button("로또를 생성해 주세요.")

if btn:
    st.write(getLotto())

btn2 = st.button("로또 5개 생성해 주세요.")

if btn2:
    for i in range(1, 6):
        lotto = getLotto()
        st.write(f"{i} > :red[{lotto}]")
    st.write(f"생성된 시간: :green[{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}]")