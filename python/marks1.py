# marks1.py

marks=[90,23,19,67]    # 학생들의 시험 점수 리스트
number=0     # 학생에게 붙여 줄 번호
for mark in marks:
    number+=1
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
        
