# closure.py
class Mul:
	def __init__(self, m):
		self.m = m

	def __call__(self, n):
		return self.m * n

if __name__=="__main__":
	mul3=Mul(3)
	mul5=Mul(5)

	print(mul3(10))
	print(mul5(10))

# wrapper.py
def mul(m):
	def wrapper(n):
		return m*n
	return wrapper

if __name__=="__main__":
	mul3=mul(3)
	mul5=mul(5)

	print(mul3(10))
	print(mul5(10))

# decorator.py
import time

def elapsed(original_func):
	def wrapper():
		start=time.time()
		result=original_func()
		end=time.time()
		print("함수 수행시간: %f 초" %(end-start))
		return result
	return wrapper

@elapsed
def myfunc():
	print("함수가 실행됩니다.")

myfunc()

# decorator2.py
import time

def elapsed(original_func):
	def wrapper(*args, **kwargs):
		start=time.time()
		result=original_func(*args, **kwargs)
		end=time.time()
		print("함수 수행시간: %f 초" %(end-start))
		return result
	return wrapper

@elapsed
def myfunc(msg):
	"""데코레이터 확인 함수"""
	print("'%s'을 출력합니다." %msg)

myfunc("hello")

# iterator.py
class MyIterator:
	def __init__(self, data):
		self.data=data
		self.position=0
	
	def __iter__(self):
		return self

	def __next__(self):
		if self.position>=len(self.data):
			raise StopIteration
		result=self.data[self.position]
		self.position+=1
		return result

if __name__=="__main__":
	i=MyIterator([1, 2, 3])
	for item in i:
		print(item)

# reviterator.py
class ReverseIterator:
	def __init__(self, data):
		self.data=data
		self.position=len(self.data)-1

	def __iter__(self):
		return self
		
	def __next__(self):
		if self.position<0:
			raise StopIteration
		result=self.data[self.position]
		self.position-=1
		return result

if __name__=="__main__":
	i=ReverseIterator([1, 2, 3])
	for item in i:
		print(item)

# generator.py
def mygen():
	for i in range(1, 1000):
		result=i*i
		yield result

gen=mygen()

print(next(gen))
print(next(gen))
print(next(gen))

# 제너레이터 표현식
gen=(i*i for i in range(1, 1000))

print(next(gen))
print(next(gen))
print(next(gen))

# generator2.py
import time

def longtime_job():
	print("job start")
	time.sleep(1)
	return "done"

list_job=(longtime_job() for i in range(5))
print(next(list_job))