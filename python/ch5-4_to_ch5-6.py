# try_except.py
try:
    4/0
except ZeroDivisionError as e:
    print(e)

# many_error.py
try:
    a=[1, 2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a=[1, 2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    a=[1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# try_else.py
try:
    age=int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age<=18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")

# process_score.py
students=["김철수", "이영희", "박민수", "최유진"]

for student in students:
    try:
        with open(f"{student}_성적.txt", 'r') as f:
            score=f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        continue     # 다음 학생으로 넘어감

# error_pass.py
try:
    f=open("설정파일.txt", 'r')
    config=f.read()
    f.close()
except FileNotFoundError:
    pass     # 설정 파일 없어도 계속 진행

print("프로그램이 정상적으로 실행됩니다.")   # 프로그램의 주요 기능은 계속 수행

# error_raise.py
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle=Eagle()
eagle.fly()

# error_make.py
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick=="바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

# positive.py
def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

# filter1.py
def positive(x):
    return x>0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# two_times.py
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result

result=two_times([1, 2, 3, 4])
print(result)

# sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(1)

# random_pop.py
import random
def random_pop(data):
    number=random.randint(0, len(data)-1)
    return data.pop(number)

if __name__=="__main__":
    data=[1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

# choice 사용
def random_pop(data):
    number=random.choice(data)
    data.remove(number)
    return number

# zip.py
students=['한민서', '황지민', '이영철', '이광수', '김승민']
snacks=['사탕','초콜릿','젤리']

result=zip(students, snacks)
print(list(result))

# itertools_zip.py
import itertools

students=['한민서', '황지민', '이영철', '이광수', '김승민']
snacks=['사탕','초콜릿','젤리']

result=itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))

# add.py
def add(data):
    result=0
    for i in data:
        result+=i
    return result

data=[1, 2, 3, 4, 5]
result=add(data)
print(result)

# reduce_test.py
import functools

data=[1, 2, 3, 4, 5]
result=functools.reduce(lambda x, y: x+y, data)
print(result)

# 최댓값 구하기
num_list=[3,2,8,1,6,7]
max_num=functools.reduce(lambda x, y:x if x>y else y, num_list)
print(max_num)

# itemgetter1.py
from operator import itemgetter

students=[("jane", 22, 'A'),("dave",32,'B'), ("sally",17,"B"),]
result=sorted(students, key=itemgetter(1))
print(result)

# itemgetter2.py
from operator import itemgetter

students=[
    {"name":"jane", "age":22, "grade":'A'},
    {"name":"dave", "age":32, "grade":'B'},
    {"name":"sally", "age":17, "grade":'B'}
]

result=sorted(students, key=itemgetter('age'))
print(result)

# attrgetter1.py
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade

students=[
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'B')
]

result=sorted(students, key=attrgetter('age'))
print(result)

# thread_test.py
import time
import threading     # 스레드 생성하기 위해 threading 모듈 필요

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("Start")

threads=[]
for i in range(5):
    t=threading.Thread(target=long_task)     # 스레드 생성
    threads.append(t)

for t in threads:
    t.start()     # 스레드 실행

for t in threads:
    t.join()     # join으로 스레드가 종료될 때까지 기다림

print("End")

# traceback_test.py
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())     # 오류 추적 결과를 문자열로 반환

main()

# webbrower_test.py
import webbrowser

webbrowser.open_new('http://python.org')     # 웹 페이지 새 창으로 열기

# webbrower_test.py
import webbrowser

webbrowser.open_new('http://python.org')     # 웹 페이지 새 창으로 열기

webbrowser.open('http://python.org')     # 이미 열린 브라우저로 열기