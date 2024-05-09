import streamlit as st
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
from prophet.plot import plot_components

# 데이터 프레임 불러오기
prophet = Prophet()

# prophet = joblib.load('./model/prophet.pkl')
df = pd.read_csv('./data/TSLA.csv')

# 예측에 필요한 데이터 프레임 생성
df_prophet = df[['날짜','종가','최고가','최저가']]
df_prophet.columns = ['ds','y','y_upper','y_lower']

# 모델 학습
prophet.fit(df_prophet)

def prop_run():

    st.subheader('원하는 기간으로 테슬라의 추세를 예측합니다.:mag_right:')
    st.image('./image/elon_musk.jpg')

    # 유저가 원하는 값 입력
    st.write('2019 / 5 / 7 부터 2024 / 5 / 6 까지의 데이터를 기준으로 2024 / 5 / 7 부터의 추세를 예측합니다.')

    pro_text = st.number_input('추세 예측을 하기 위해 원하는 기간을 입력해주세요. 7일 부터 365일까지 입력 가능합니다.', min_value = 30, value = 90, max_value = 365, step = 5)  # 기본값을 100으로 설정

    if st.button('예측하기', use_container_width=True):
        # 유저한테 입력 받은 값으로 데이터 프레임 생성 후 예측
        future = prophet.make_future_dataframe(periods=pro_text, freq='B')
        forecast = prophet.predict(future)

        # 예측 결과를 시각화하여 출력
        fig = prophet.plot(forecast)
        plt.xlabel("날짜")
        plt.ylabel("예상 추세")
        st.pyplot(fig)

        # 트렌드와 계절성 그래프 시각화
        fig = prophet.plot_components(forecast)
        st.pyplot(fig)

        st.link_button('데이터 출처 바로가기',url = 'https://www.nasdaq.com/market-activity/stocks/tsla/historical',use_container_width=True)
        