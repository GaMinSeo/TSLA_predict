import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import datetime
from comma import comma
import plotly.subplots as ms

def data_run():
    st.subheader('지난 테슬라 주가 데이터:clipboard:')
    st.write('2019년 5월 7일부터 2024년 5월 6일 까지의 테슬라 주가 데이터를 확인 할 수 있습니다.')

    # 달러 원화 가로 선택
    currency = st.radio('화폐 단위 선택:dollar:',['달러', '원화'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.text('원화 환율 계산은 5월 7일 기준 1,360원으로 계산함')
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
    st.write('2019년 5월 7일부터 2024년 5월 6일까지의 범위에서 원하는 날짜를 순서에 맞게 선택해주세요.')

    # 셀렉트 박스로 원하는 날짜 표시
    
    # 시작일과 종료일 생성 
    col1, col2, col3 = st.columns(3)
    with col1:
        start_year = st.selectbox('시작 연도', range(2019, 2025))
    with col2:
        start_month = st.selectbox('시작 월', range(1, 13),4)
    with col3:
        start_day = st.selectbox('시작 일', range(1, 32),6)

    # 시작일을 datetime 객체로 변환
    start_date = datetime.datetime(start_year, start_month, start_day)

    # 종료일 생성
    col4, col5, col6 = st.columns(3)
    with col4:
        end_year = st.selectbox('종료 연도', range(2019, 2025), index=5)
    with col5:
        end_month = st.selectbox('종료 월', range(1, 13),4)
    with col6:
        end_day = st.selectbox('종료 일', range(1, 32),5)

    # 종료일을 datetime 객체로 변환
    end_date = datetime.datetime(end_year, end_month, end_day)

    # datetime 객체를 object로 변환
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')

    # 지정된 날짜를 벗어나면 사용자에게 알리기
    if start_date < df.index.min() or end_date > df.index.max() or start_date >= end_date:
        st.error('2019년 5월 7일부터 2024년 5월 6일까지의 범위에서 원하는 날짜를 순서에 맞게 선택해주세요.')
    else:
        # 데이터프레임을 선택한 날짜 범위에 따라 잘라내기
        df = df[(df.index >= start_date) & (df.index <= end_date)]

        # Tab 생성 + 차트 생성 
        tab1, tab2 = st.tabs(['캔들스틱 차트','라인 차트'])

        # 캔들차트 표출
        with tab1:
            volume_bar = go.Bar(x=df.index, y=df['거래량'])
            
            # 캔들차트 변수 생성
            candle = go.Candlestick(x=df.index   , open=df['시가'], high=df['최고가'], low=df['최저가'  ], close=df['종가'] ,
                                    increasing_line_color='red', decreasing_line_color='blue')
            
            fig = ms.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
            fig.add_trace(candle, row=1, col=1)
            fig.add_trace(volume_bar, row=2, col=1)
            fig.update_layout(
            title='테슬라 주식 가격',
            yaxis1_title='주가',
            yaxis2_title='거래량',
            xaxis2_title='날짜',
            xaxis1_rangeslider_visible=False,
            xaxis2_rangeslider_visible=True,
            )
            st.plotly_chart(fig)
        
        # 라인차트 표출
        with tab2:
            # 라인차트 변수 생성
            line = go.Scatter(x=df.index, y=df['종가'], mode='lines', name='종가')
            fig = ms.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
            fig.add_trace(line, row=1, col=1)
            fig.add_trace(volume_bar, row=2, col=1)
            fig.update_layout(
            title='테슬라 주식 가격',
            yaxis1_title='주가',
            yaxis2_title='거래량',
            xaxis2_title='날짜',
            xaxis1_rangeslider_visible=False,
            xaxis2_rangeslider_visible=True,
            )

            fig.update_layout(title="선택한 기간의 라인 차트", xaxis_title="날짜", yaxis_title="주가")
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
            st.markdown("<h5>선택하신 날짜에서 테슬라의 최고가는" + comma(df_max) + "원 이고, 최저가는 "+ comma(df_min) + "원 입니다.", unsafe_allow_html=True)
            st.markdown("<h5>평균 주가는 " + comma(round(df_mean)) + "원 입니다.", unsafe_allow_html=True)
        
        # 데이터 출처 버튼
        st.link_button('데이터 출처 바로가기',url = 'https://www.nasdaq.com/market-activity/stocks/tsla/historical')
        
            

