# %%
# No.15 결측치 처리(isnull, fillna)
# 1. 비어있는 혈압 데이터를 '평균값'으로 채우기
import pandas as pd
import numpy as np

data = {
    "이름": ["김민준", "이서연", "박지훈", "최유진", "정현우"],
    "혈압": [128, np.nan, 150, 118, np.nan],
    "키": [175, 162, 168, 158, 172],
    "몸무게": [72, 55, 80, 50, 78]
}

df = pd.DataFrame(data)

print(df)

df["혈압"] = df["혈압"].fillna(df["혈압"].mean())
print(df)

# 2. 데이터가 없는 행을 지우기(dropna)
data = {
    "이름": ["김민준", "이서연", "박지훈", "최유진", "정현우"],
    "혈압": [128, np.nan, 150, 118, np.nan],
    "키": [175, 162, 168, 158, 172],
    "몸무게": [72, 55, 80, 50, 78]
}

df = pd.DataFrame(data)

drop_df = df.dropna()
print(drop_df)

# No.16 파생변수 만들기
# 키(Height)와 몸무게(Weight) 컬럼을 이용해 'BMI' 컬럼을 새로 만들어 표에 붙이기
df["BMI"] = df["몸무게"]/((df["키"]/100)**2)
print(df)

# %%
# No.17 미션: "BMI 자동 계산기"
# 키(cm)와 몸무게(kg) 데이터가 있는 표를 만들고, 코드로 계산하여 맨 오른쪽 열에 `BMI` 수치를 자동으로 채워 넣기(결측치가 있다면 0으로 채우기)
import pandas as pd
import numpy as np

data = {
    "이름": ["김민준", "이서연", "박지훈", "최유진", "정현우"],
    "키": [175, 162, 168, np.nan, 172],
    "몸무게": [72, 55, 80, 50, np.nan]
}

df = pd.DataFrame(data)

print(df)

df["BMI"] = df["몸무게"]/((df["키"]/100)**2)
df["BMI"] = df["BMI"].fillna(0)
print("\nBMI 자동 계산기:\n", df)