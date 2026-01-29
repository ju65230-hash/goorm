# No.4 함수(나만의 의료 프로토콜 만들어보기)
# 약물 용량 계산
# 총 투여량(ml)=(처방된 용량(mg/kg)*환자체중(kg))/약물 농도(mg/ml)
def calculate_dose(dosage, weight, concentration):
	total_dose=(dosage*weight)/concentration
	return total_dose

dose1=calculate_dose(5, 7.5, 25)

print(f"환자1 투여량: {dose1:.2f} ml")

# No.5 라이브러리(남이 만든 의료기기 가져와보자!)
# e.g. 1) Pandas: 엑셀 다루는 도구, 2) Matplotlib: 그래프 그리는 도구, 3)Math: 수학 계산 도구
# 원기둥 부피 공식
import math

major_radius=5
minor_radius=3
area=math.pi*5*3

print(f"세포 면적: {area:.2f} μm^2")

# No.6 자동 건강검진 판정기
# 상황: 우리 병원에서는 BMI 수치에 따라 비만 여부를 자동으로 판정해 주는 시스템이 필요합니다.
# 미션 목표: 아래 조건에 맞는 'check_obesity'라는 함수를 만들어 보세요.
# 1. 입력값: BMI 수치(숫자)
# 2. 하는 일:
#   - BMI가 30 이상이면 → "비만"
#   - BMI가 25 이상 30 미만이면 → "과체중"
#   - 그 외에는 → "정상"
# 3. 반환값(return): 판정 결과 문자열 ("비만", "과체중", "정상")
def check_obesity(BMI):
	if BMI>=30:
		return "비만"
	elif BMI>=25:
		return "과체중"
	else:
		return "정상"

print(check_obesity(32))
print(check_obesity(24))