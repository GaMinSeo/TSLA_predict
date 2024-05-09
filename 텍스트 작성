# **TSLA_predict (Tesla 주식 추세 예측 프로젝트)**


## 프로젝트 소개
최근 테슬라의 주가가 많이 휘청거리기에 많은 주주분들의 마음도 뒤숭숭 할거라 생각됩니다.

저 또한 주식을 보유하고 있기에 앞으로의 긍정적인 주가 전망을 기대하는 마음으로 이 앱을 개발하게 됐습니다.

이 앱은 지난 주가를 분석해보고 앞으로의 추세를 예측합니다.


------
## 주요 기능

- 주식 데이터 분석 및 가공
- 주식 데이터 달러 및 원화로 변경 가능
- 주식 데이터를 원하는 기간으로 가공 가능
- 주식 데이터 캔들차트 시각화
- 주식 데이터 라인차트 시각화
- Prophet 을 활용한 원하는 미래 기간 주식 추세 예측
- Streamlit을 사용한 앱 대시보드 구축

------
## 배포 주소

> URL : <http://ec2-52-78-84-125.ap-northeast-2.compute.amazonaws.com:8502/>

------
## 개발 환경 및 기술 스택

jupyter notebook을 통해, HistoricalData_tsla.csv 파일을 통계 분석하고, plotly 라이브러리를 통해 캔들차트 및 라인차트로 볼 수 있게 데이터 시각화를 진행했습니다.

또한 사용자에게 원하는 기간을 입력 받아 Prophet을 통해 원하는 기간의 주식 추세에 대한 시계열 예측 분석을 진행 하였습니다.

최종적으로 Streamlit을 이용해서, 데이터 분석과 데이터 시각화 및 주가 추세를 예측하는 대시보드 앱을 개발하였고, AWS EC2를 사용하여 서버에 배포하였습니다.

- **데이터 분석 및 시각화** : Jupyter Notebook, pandas, NumPy, Matplotlib, plotly
- **시계열 데이터 분석** : Prophet
- **웹 애플리케이션 개발** : Streamlit
- **버전 관리** : Git
- **편집기** : Visual Studio Code
- **서버** : AWS EC2

------
## 이슈 개선
#### Prophet 예측 그래프 라벨에서 한글이 깨지는 현상 인지

#한글 폰트 사용하기

#필요한 라이브러리 임포트
```bash
import platform

from matplotlib import font_manager, rc
```

#한글 폰트 적용 코드 작성
```bash
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Linux':

    rc('font', family='NanumGothic')
    
elif platform.system() == 'Windows':

    # 윈도우 환경에서 한글 폰트 설정
    
    font_path = "c:\WINDOWS\Fonts\GULIM.TTC"  # 한글 폰트 파일 경로
    
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    
    rc('font', family=font_name)
```
## ✏ 작성자
- 가민서
- e-mail : rkalstj23@naver.com
