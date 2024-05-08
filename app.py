import streamlit as st
from streamlit_option_menu import option_menu
from home import home_run
from data import data_run
from prop import prop_run

def main() :
    menu = ["홈", "테슬라 주가 데이터 및 차트", "테슬라 주가 추세 예측"]
    with st.sidebar:
        choice = option_menu("메뉴", menu,
                         icons=['house', 'bi bi-clipboard2-data', 'bi bi-graph-up-arrow'],
                         menu_icon="bi bi-list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "red", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#F29661"},
    }
    )
        st.link_button('데이터 출처 바로가기',url = 'https://www.nasdaq.com/market-activity/stocks/tsla/historical')

    if choice == menu[0] :
        home_run()
    elif choice == menu[1] :
        data_run()
    elif choice == menu[2] :
        prop_run()

if __name__ == '__main__':
    main()
