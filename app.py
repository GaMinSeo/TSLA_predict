import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io
from home import home_run

def main() :
    menu = ["홈", "테슬라 누적 주가 데이터", "테슬라 향후 주가 예측"]
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

    if choice[0] == menu[0] :
        home_run()  # 함수 호출 부분 수정
    elif choice[1] == menu[1] :
        pass
    elif choice[2] == menu[2] :
        pass

if __name__ == '__main__':
    main()
