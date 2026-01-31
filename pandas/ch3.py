# apply
import pandas as pd
import numpy as np

col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

## 축에 대해 계산할 수 없는 형식 -> 각 요소에 적용
print(df.apply(np.sqrt))

## 축에 대해 적용 가능 -> 축 기준으로 연산 수행
print(df.apply(np.sum))

# result_type에 따른 차이
print(df.apply(lambda x : [1,2,3]))

print(df.apply(lambda x : [1,2,3], axis=1,result_type='expand')) # func를 기준으로 확장하여 columns를 지정

print(df.apply(lambda x : [1,2,3], axis=1,result_type='reduce')) # Series

print(df.apply(lambda x : [1,2,3], axis=1,result_type='broadcast')) # 기존 DataFrame

# pipe
org_data = pd.DataFrame({'info':['삼성전자/3/70000','SK하이닉스/2/100000']})
print(org_data)

def code_name(data):
    result=pd.DataFrame(columns=['name','count','price']) 
    df = pd.DataFrame(list(data['info'].str.split('/'))) # '/ ' 로 구분하여 문자열을 나누어 리스트에 넣음
    result['name'] = df[0] # 여기엔 첫번째 값인 이름이 입력
    result['count']= df[1] # 여기엔 두번째 값인 수량이 입력
    result['price']= df[2] # 여기엔 세번째 값인 가격이 입력
    result = result.astype({'count':int,'price':int}) # count와 price를 int로 바꿈(기존str)
    return result
print(code_name(org_data))

def value_cal(data,unit=''):
    result = pd.DataFrame(columns=['name','value']) 
    result['name'] =data['name'] # 이름은 기존거를 가져옴
    result['value']=data['count']*data['price'] # value는 count * price를 입력함
    result = result.astype({'value':str}) # value를 str로 변경(단위를 붙이기 위함)
    result['value']=result['value']+unit # 단위를 붙임
    return(result)

print(org_data.pipe(code_name).pipe(value_cal,'원'))

# agg
df = pd.DataFrame([[1,4,7],[2,5,8],[3,6,9]])
print(df)

ex1 = df.agg(np.prod) # 문자열 형태도 가능: df.agg('prod')
print(ex1)

ex2 = df.agg([lambda x : min(x) * max(x)])
print(ex2)

def func_sub(input):
    return max(input)-min(input)
func_sub.__name__='내함수'
ex3 = df.agg([func_sub,'sum'])
print(ex3)

## 여러 함수 동시 적용
ex4 = df.agg(['min','max','sum','prod'])
print(ex4)

ex5 = df.agg({0:['sum','prod'],1:['max','min'],2:'mean'}) 
print(ex5)

# transform
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data=[[10,40,70],[20,50,80],[30,60,90]],index=row,columns=col)
print(df)

ex1 = df.transform(lambda x : np.sqrt(x))
print(ex1)

## 여러 함수 동시 적용
ex2 = df.transform(['exp','sqrt']) # list의 경우 multi index처럼 multi columns 생성됨
print(ex2)

# eval
data = [[1,2,3],[4,5,6],[7,8,9]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data = data, index = row, columns= col)
print(df)

print(df.eval('col4=col1*col2-col3'))
print(df)

print(df.eval('col4=col1*col2-col3',inplace=True))
print(df)