# add_data.py
f=open("C:/doit/새파일.txt", 'a')
for i in range(11, 20):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# block scope
with open("test.txt", 'w') as f:
    content="Hello, Python!"
    f.write(content)

# calculator.py
print("=== 간단한 계산기 ===")

num1=float(input("첫 번째 숫자를 입력하세요: "))
num2=float(input("두 번째 숫자를 입력하세요: "))

print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}*{num2}={num1*num2}")

if num2!=0:
     print(f"{num1}/{num2}={num1/num2}")
else:
    print("0으로 나눌 수 없습니다.")

# coffee.py
coffee=10
while True:
    money=int(input("Insert money.: "))
    if money==300:
        print("Dispense coffee.")
        coffee-=1
    elif money>300:
        print("Return %d change, dispense coffee." %(money-300))
        coffee-=1
    else:
        print("Return payment, no coffee dispensed.")
        print("%d coffees left." %coffee)
    if coffee==0:
        print("Out of coffee. Sales stopped.")
        break

# defalut1.py
def say_myself(name, age, man=True):
               print("나의 이름은 %s입니다." %name)
               print("나이는 %d살입니다." %age)
               if man:
                   print("남자입니다.")
               else:
                   print("여자입니다.")

# file_with.py
with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

# marks1.py
marks=[90,23,19,67]    # 학생들의 시험 점수 리스트
number=0     # 학생에게 붙여 줄 번호
for mark in marks:
    number+=1
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

# marks2.py
marks=[90,23,10,75]
number=0
for mark in marks:
    number+=1
    if mark<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)
    
# marks3.py
marks=[30,59,98,45,80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))

# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__=="__main__":
    print(add(1, 4))
    print(sub(4, 2))

# mod2.py
PI=3.141592

class Math:
    def solv(self, r):
        return PI*(r**2)

def add(a, b):
    return a+b

# multistring.py
print("="*50)
print("My Program")
print("="*50)

# newfile.py
f=open("새파일.txt", 'w')
f.close()

# newfile2.py
f=open("C:/doit/새파일.txt", 'w')
f.close()

# read_for.py
f=open("C:/doit/새파일.txt", 'r')
for line in f:
    print(line)
f.close()

# read.py
f=open("C:/doit/새파일.txt", 'r')
data=f.read()
print(data)
f.close()

# readline_all.py
f=open("C:/doit/새파일.txt", 'r')
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

# readline_test.py
f=open("C:/doit/새파일.txt", 'r')
line=f.readline()
print(line)
f.close()

# readlines.py
f=open("C:/doit/새파일.txt", 'r')
lines=f.readlines()
for line in lines:
       print(line)
f.close()

# strip.py
f=open("C:/doit/새파일.txt", 'r')
lines=f.readlines()
for line in lines:
    line=line.strip()
    print(line)
f.close()

# sys1.py
import sys

args=sys.argv[1:]
for i in args:
    print(i)

# sys2.py
import sys
args=sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

# vartest_global.py
a=1
def vartest():
    global a
    a+=1

vartest()
print(a)

# vartest_return.py
a=1
def vartest(a):
    a+=1
    return a

a=vartest(a)
print(a)

# vartest_return.py
a=1
def vartest(a):
    a+=1
    return a

a=vartest(a)
print(a)

# write_data.py
f=open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data="%d번째 줄입니다.\n" %i
    f.write(data)

f.close()