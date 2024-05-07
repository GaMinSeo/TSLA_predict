import plotly.graph_objects as go
import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
def data_run():
    st.subheader('지난 테슬라 주가 데이터')
    st.write('2019년 5월 7일부터 2024년 5월 6일 까지의 테슬라 주가 데이터를 확인합시다.')

    # 달러 원화 가로 선택
    currency = st.radio('화폐 단위 선택:dollar:',['달러', '원화'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.text('원화 환율 계산은 5월 7일 1,360원으로 계산함')
    if currency == '달러' :
        st.success('달러 표시 데이터프레임 입니다.')
        df = pd.read_csv('./data/TSLA.csv')
    elif currency == '원화' :
        st.info('원화 표시 데이터프레임 입니다.')
        df = pd.read_csv('./data/TSLA_KOR.csv')

    # 최신순과 오래된순 가로 선택
    time = st.radio('',['최신순', '오래된순'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if time == '최신순' :
        df_time = df.sort_index()
    elif time == '오래된순' :
        df_time = df.sort_index(ascending=False)

    st.dataframe(df_time, use_container_width = True)
    #캔들 차트 사용을 위해 인덱스 뒤집기
    temp = df.set_index('날짜')
    df.index = pd.to_datetime(temp.index)
    df = df.drop('날짜',axis=1,)
    #st.dataframe(df)
    
    
     #Line Chart, Candle Stick 선택형으로 만들기
    chart_type = st.sidebar.radio("원하는 차트를 선택하세요", ("캔들 차트", "라인 차트"))
    candlestick = go.Candlestick(x=df.index, open=df['시가'], high=df['최고가'], low=df['최저가'], close=df['종가'])
    line = go.Scatter(x=df.index, y=df['종가'], mode='lines', name='종가')

    if chart_type == "캔들 차트":
        fig = go.Figure(candlestick)
    elif chart_type == "라인 차트":
        fig = go.Figure(line)
    else:
        st.error("error")

    fig.update_layout(title=f"TSLA Stock {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)

    st.markdown("<hr>", unsafe_allow_html=True)	#구분선 추가
   
   #숫자를 넣을 수 있는 영역 생성
    num_row = st.sidebar.number_input("원하는 최근 날짜까지 보기", min_value= 1, max_value=len(df))
        
    #최근 날짜부터 결과값 보여줌
    st.dataframe(df[-num_row:].reset_index().sort_index(ascending = False).set_index("날짜"))