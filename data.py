import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import datetime


import matplotlib.pyplot as plt
def data_run():
    st.subheader('지난 테슬라 주가 데이터:clipboard:')
    st.write('2019년 5월 7일부터 2024년 5월 6일 까지의 테슬라 주가 데이터를 확인 할 수 있습니다.')

    # 달러 원화 가로 선택
    currency = st.radio('화폐 단위 선택:dollar:',['달러', '원화'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.text('원화 환율 계산은 5월 7일 1,360원으로 계산함')
    if currency == '달러' :
        st.success('달러 형식 데이터프레임을 출력합니다.')
        df = pd.read_csv('./data/TSLA.csv')
    elif currency == '원화' :
        st.info('원화 형식 데이터프레임을 출력합니다.')
        df = pd.read_csv('./data/TSLA_KOR.csv')

    # 최신순과 오래된순 가로 선택
    time = st.radio('',['최신순', '오래된순'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if time == '최신순' :
        df_time = df.sort_index()
    elif time == '오래된순' :
        df_time = df.sort_index(ascending=False)

    st.dataframe(df_time, use_container_width = True)
    
    # 캔들 차트 사용을 위해 인덱스 뒤집기
    temp = df.set_index('날짜')
    df.index = temp.index
    df = df.drop('날짜', axis=1)

    st.markdown("<hr style='border-top: 5px solid #aaa;'>", unsafe_allow_html=True) # 두께 5px로 조절
    
    st.subheader('원하는 날짜 내에 테슬라 주가를 확인할수 있습니다.:chart_with_upwards_trend:')       
    # 시작일과 종료일 생성 
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('시작 날짜', datetime.datetime(2019, 5, 7))
        # datetime.date 객체를 object로 변환
        start_date = start_date.strftime('%Y-%m-%d')
    with col2:
        end_date = st.date_input('종료 날짜', datetime.datetime(2024, 5, 6))
        # datetime.date 객체를 object로 변환
        end_date = end_date.strftime('%Y-%m-%d')
    
    # 지정된 날짜를 벗어나면 사용자에게 알리기
    if start_date < df.index.min() or end_date > df.index.max():
        st.error('2019년 5월 7일부터 2024년 5월 6일까지의 범위에서 날짜를 선택해주세요.')
    else:
        # 데이터프레임을 선택한 날짜 범위에 따라 잘라내기
        df = df[(df.index >= start_date) & (df.index <= end_date)]

        # Tab 생성 + 차트 생성 
        tab1, tab2 = st.tabs(['캔들스틱 차트','라인 차트'])
        with tab1:
            fig = go.Figure(go.Candlestick(x=df.index, open=df['시가'], high=df['최고가'], low=df['최저가'], close=df['종가']))
            fig.update_layout(title="선택한 기간 동안의 캔들스틱 차트", xaxis_title="Date", yaxis_title="Price")
            st.plotly_chart(fig)
        with tab2:
            fig = go.Figure(go.Scatter(x=df.index, y=df['종가'], mode='lines', name='종가'))
            fig.update_layout(title="선택한 기간 동안의 라인 차트", xaxis_title="Date", yaxis_title="Price")
            st.plotly_chart(fig)       
        # 지정된 범위 내에서 최고가와 최저점 표시  
        if currency == '달러' :
            df_max = df['종가'].max()
            df_min = df['종가'].min()
            df_mean = df['종가'].mean()
            st.markdown("<h5>선택하신 날짜 내에서 테슬라의 최고가는 $" + str(round(df_max,2)) + " 이고, 최저가는 $"+ str(round(df_min,2)) + " 입니다.", unsafe_allow_html=True)
            st.markdown("<h5>평균 주가는 $" + str(round(df_mean,2)) + " 입니다.", unsafe_allow_html=True)

        elif currency == '원화' :
            df['종가'] = df['종가'].str.replace(',', '').astype(int)
            df_max = df['종가'].max()
            df_min = df['종가'].min()
            df_mean = df['종가'].mean() 
            st.markdown("<h5>선택하신 날짜에서 테슬라의 최고가는" + str(df_max) + "원 이고, 최저가는 "+ str(df_min) + "원 입니다.", unsafe_allow_html=True)
            st.markdown("<h5>평균 주가는 " + str(round(df_mean,2)) + "원 입니다.", unsafe_allow_html=True)
