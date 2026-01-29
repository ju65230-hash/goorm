# No.1 데이터 담기
# 1) 변수를 사용해 환자의 정보가 담긴 상자(이름, 나이, 체온, 혈압, 당뇨여부)를 만들고 출력하기

name="홍길동"
age=24
temperature=36.5
blood_pressure="120/80"
diabetes=True     # 당뇨 여부(True/False)
print(f"이름: {name}, 나이: {age}, 체온: {temperature}, 혈압: {blood_pressure}, 당뇨 여부: {diabetes}")

# 2) 리스트를 사용해 환자의 최근 3일치 혈당 수치 기록을 한번에 묶어 출력시키기(1. 모두 값 꺼내기, 2. 하나씩 값꺼내기)

blood_sugar=[110, 90, 122]
print("최근 3일 혈당 수치:", blood_sugar)
for i in range(3):
    print(f"{i+1}일차 혈당:", blood_sugar[i])

# 3) 딕셔너리로 한 명의 환자 차트 종합 정보(이름표가 있는 데이터)

patient_chart={
    "이름": "홍길동",
    "나이": 24,
    "체온": 36.5,
    "혈압": "120/80",
    "당뇨 여부": True,
    "최근 3일 혈당 수치": [110, 90, 122]
    }
print(patient_chart)
print(patient_chart["이름"])

# No.2 상황판단 만들기
# 1) 의사의 진단 논리를 만들기(만약 ~라면 A를 하고, 아니면 B를 해라)

diabetes=True
if diabetes:
    print("당뇨 환자이므로 혈당을 자주 확인하세요.")
else:
    print("정상 범위입니다.")

# 2) 간호사의 회진(환자의 정보를 반복해서 확인한다)
blood_sugar=[110, 130, 122]
print("간호사 회진 - 혈당 체크")
for day in range(len(blood_sugar)):
    if blood_sugar[day]>=130:
        print(f"{day+1}일차 혈당 {blood_sugar[day]} -> 혈당 높음, 보고 필요")
    else:
        print(f"{day+1}일차 혈당 {blood_sugar[day]} -> 정상 범위")

# No.3 “응급실 분류 시스템 만들기”
# 상황: 응급실에 환자 3명이 도착했습니다. 각 환자의 정보는 아래와 같습니다.
# 규칙 1: 응급도가 1이면 "🚨 [긴급] (이름)님, 즉시 수술실로 이송!" 출력
# 규칙 2: 응급도가 2이면 "⚠️ [주의] (이름)님, 집중 치료실 대기" 출력
# 규칙 3: 그 외에는 "✅ [대기] (이름)님, 일반 진료실로 안내" 출력
# 1) 환자 데이터
patients = [
    {"이름": "환자A", "응급도": 1, "상태": "심정지"},
    {"이름": "환자B", "응급도": 3, "상태": "골절"},
    {"이름": "환자C", "응급도": 2, "상태": "호흡곤란"}
]
for patient in patients:
    name=patient["이름"]
    level=patient["응급도"]
    if level==1:
        print(f"🚨 [긴급] {name}님, 즉시 수술실로 이송!")
    elif level==2:
        print(f"⚠️ [주의] {name}님, 집중 치료실 대기")
    else:
        print(f"✅ [대기] {name}님, 일반 진료실로 안내")