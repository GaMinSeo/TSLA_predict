import streamlit as st

def home_run():
    st.title('테슬라 주가 예측 앱 대시보드:rocket:')
    st.image('./image/elon_musk1.jpg')
    st.subheader('이 앱은 2019년 5월 7일부터 2024년 5월 6일 까지의')
    st.subheader('데이터로 테슬라 주가를 예측하는 앱 대시보드 입니다.')
    st.subheader('지난 주가를 확인하고 앞으로의 주가를 예측해봅시다.')
    st.write('참고 데이터는 2019년 5월 7일부터 2024년 5월 6일 까지의 테슬라 주가 데이터로 사용됐습니다.')
    st.link_button('데이터 출처 바로가기',url = 'https://www.nasdaq.com/market-activity/stocks/tsla/historical')

