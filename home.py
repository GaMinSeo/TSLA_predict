import streamlit as st

def home_run():
    st.title('테슬라 주가 예측 앱 대시보드:rocket:')
    st.subheader('이 앱은 테슬라 주가를 예측하는 앱 대시보드 입니다.')
    st.subheader('지난 주가를 확인하고 앞으로의 주가를 예측해봅시다.')
    st.image('./image/elon_musk1.jpg')
    st.markdown('[데이터 출처](https://www.nasdaq.com/market-activity/stocks/tsla/historical)')
    st.markdown('[이미지 출처](https://www.hankyung.com/article/2021051567297)')
