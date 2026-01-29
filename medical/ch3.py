# No.7 판다스 소환하기(import)
import pandas as pd

# No.8 데이터 표 만들기(DataFrame)

data = {
	"이름": ["김철수", "이영희", "박민수", "최지혜", "정수진"],
	"나이": [45, 32, 58, 29, 62],
	"성별": ["남", "여", "남", "여", "여"],
	"혈당": [95, 88, 140, 79, 150]
}

df = pd.DataFrame(data)     # 파일이 있는 경우: df = pd.read_csv("data.csv")

print(df)

# No.9 데이터 엑스레이 찍기(Info, Describe)
# 1. 요약 정보 보기(.info())
df.info()

# 2. 통계 정보 보기(.describe())
# 평균, 표준편차, 최소값, 최대값 계산
print(df.describe())

# No.10 "고위험군 자동 필터링"
# df에서 혈당이 120 이상인 환자만 출력
high_glucose = df[df['혈당'] >= 120]

print(high_glucose)