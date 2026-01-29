# 연산
import pandas as pd

data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

data2  = [[3],[4],[5]]
df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'],columns=['col1'])
print(df2)

## 덧셈
result = df.add(1)
print(result)

result = df.add(df2)
print(result)

result = df.add(df2,fill_value=0)
print(result)

## 뺄셈
result = df.sub(df2,fill_value=0)
print(result)

## 곱셈
result = df.mul(df2,fill_value=0)
print(result)

## 나눗셈
result = df.div(df2,fill_value=1)
print(result)

## 나머지
result = df.mod(df2,fill_value=1)
print(result)

## 거듭제곱
result = df.pow(df2,fill_value=1)
print(result)

## 행렬
col = ['col1','col2']
row = ['row1','row2']
data1 = [[1,2],[3,4]]
data2 = [[5,6],[7,8]]
df1 = pd.DataFrame(data=data1)
df2 = pd.DataFrame(data=data2)
print(df1)
print(df2)

df3 = df1.dot(df2)
print(df3)