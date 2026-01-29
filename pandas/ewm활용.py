# kaggle - APPLE Stock Data; AAPL price EDA
import pandas as pd

# AAPL 주가 CSV 파일 경로 지정
AAPL = '/Users/jeong-yujin/Desktop/doit/AAPL.csv'

# CSV 파일 읽기
# parse_dates=['Date'] → 'Date' 컬럼을 datetime 형식으로 변환
# drop(columns=['Open', 'High', 'Low', 'Close']) → 필요 없는 컬럼 제거
df = pd.read_csv(filepath_or_buffer=AAPL, parse_dates=['Date']).drop(columns=['Open', 'High', 'Low', 'Close'])
# 새로운 컬럼 생성: 종가(Adj Close) * 거래량 → 하루 거래금액 계산
df['dollars'] = df['Adj Close'] * df['Volume']
# 새로운 컬럼 생성: 날짜에서 연도(year) 추출
df['year'] = df['Date'].dt.year

# 데이터 상위 5행 확인
print(df.head())

# 'Adj Close' 컬럼에 대해 지수 가중 이동 평균(EWM) 계산
# span=10 → 최근 10일 데이터를 더 강조
# adjust=False → 단순 지수 가중 방식 (이전 값의 영향을 누적)
df['AdjClose_EWM_10'] = df['Adj Close'].ewm(span=10, adjust=False).mean()

import matplotlib.pyplot as plt

# 그림 크기 설정
plt.figure(figsize=(12,6))
# 원본 종가(Adj Close) 그래프 그리기
plt.plot(df['Date'], df['Adj Close'], label='Original')
# EWM 계산된 값 그래프 그리기
plt.plot(df['Date'], df['AdjClose_EWM_10'], label='EWM (span=10)')
# 그래프 제목 설정
plt.title("AAPL Adj Close with EWM")
# x축, y축 라벨 설정
plt.xlabel("Date")
plt.ylabel("Price")
# 범례 표시
plt.legend()
# 그래프 출력
plt.show()