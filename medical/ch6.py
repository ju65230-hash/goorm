# No.18 Seaborn 라이브러리: Matplotlib보다 훨씬 예쁘고 쉬운 도구
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 한글 깨짐 방지
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('medical/data/patient_data.csv')
print(df.columns)

# No.19 산점도(scatterplot): 나이 많을수록 혈압 높은지 상관관계 확인
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='age', y='blood_pressure')

plt.title('연령별 혈압 수치', fontsize=15, fontweight='bold')
plt.xlabel('나이 (세)', fontsize=12)
plt.ylabel('혈압 (mmHg)', fontsize=12)
plt.show()

# No.20 히스토그램(histplot): 환자 나이 분포 확인
plt.figure(figsize=(8,6))
sns.histplot(data=df, x='age', bins=10, kde=True)

plt.title('환자 나이 분포', fontsize=15, fontweight='bold')
plt.xlabel('나이 (세)', fontsize=12)
plt.ylabel('환자 수 (명)', fontsize=12)
plt.show()

# No.21 박스플롯 (boxplot): 남성과 여성의 혈당 수치 차이 비교
plt.figure(figsize=(8,6))
sns.boxplot(
    data=df,
    x=df['gender'].map({'Male':'남성', 'Female':'여성'}),
    y='diabetes_glucose',
    palette='pastel'
    )

plt.title('성별에 따른 혈당 수치', fontsize=15, fontweight='bold')
plt.xlabel('성별', fontsize=12)
plt.ylabel('혈당 수치 (mg/dL)', fontsize=12)
plt.show()

# No.22 데이터 보고서 그리기
# Kaggle 데이터를 이용해 당뇨병 유무에 따른 혈당 차이 비교
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("medical/data/diabetes.csv")
print(df.columns)

plt.figure(figsize=(8,6))
sns.boxplot(
    data=df,
    x=df['Outcome'].map({0:'정상', 1:'당뇨'}),
    y='Glucose',
    palette='pastel',
    order=['정상', '당뇨']
    )

plt.title('당뇨병 유무에 따른 혈당 차이', fontsize=15, fontweight='bold')
plt.xlabel('진단', fontsize=12)
plt.ylabel('혈당 수치 (mg/dL)', fontsize=12)
plt.show()