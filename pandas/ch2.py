# 반올림
import pandas as pd
import numpy as np

col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = np.random.rand(3,3)*100
df = pd.DataFrame(data=data, index=row, columns=col)
print(df)

print(df.round(0))
print(df.round(-1))
print(df.round(2))

# 합계
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[1,2,3],[4,5,6],[7,np.nan,9]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

print(df.sum(axis=0))

print(df.sum(axis=0, skipna=False))

print(df.sum(axis=0, min_count=3))

# 절댓값
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[-1,2,-3.5],[4,-5.5, 3+4j],[7,np.nan,0]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

print(df.abs())

# 전치
col = ['col1','col2','col3']
row = ['row1','row2','row3','row4']
data = [['A',1,2],['B',3,4],['C',5,6],['D',7,8]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

print(df.transpose())

# 순위
data = [[5],[5],[pd.NA],[3],[-3.1],[5],[0.4],[6.7],[3]]
row = ['A★','B★','C','D☆','E','F★','G','H','I☆']
df = pd.DataFrame(data=data, index=row, columns=['Value'])
print(df)

## method에 따른 차이
df['average']=df['Value'].rank(method='average')
df['min']=df['Value'].rank(method='min')
df['max']=df['Value'].rank(method='max')
df['first']=df['Value'].rank(method='first')
df['dense']=df['Value'].rank(method='dense')
print(df)

## na_option에 따른 차이 + pct
df['keep']=df['Value'].rank(na_option='keep')
df['top']=df['Value'].rank(na_option='top')
df['bottom']=df['Value'].rank(na_option='bottom')
df['pct']=df['Value'].rank(pct=True)
print(df)

# 이산
a = [1,2,3,4,5,6,7,8]
b = [1,2,4,8,16,32,64,128]
c = [8,7,6,5,4,3,2,1]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)

print(df.diff(axis=0))

print(df.diff(periods=3))

# 백분율
a = [1,1,4,4,1,1]
b = [1,2,4,8,16,32]
c = [1,np.nan,np.nan,np.nan,16,64]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)

print(df.pct_change())

print(df.pct_change(periods=-1))

print(df.bfill().pct_change())

print(df.ffill(limit=2).pct_change())

# 누적 계산
import numba

data = {'col1':[1,2,3,4],'col2':[3,7,5,6]}
idx = ['row1','row2','row3','row4']
df = pd.DataFrame(data = data, index = idx)
print(df)

print(df.expanding().sum())

print(df.expanding(min_periods=4).sum())

print(df.expanding(method='table').sum(engine='numba'))

# 기간이동 계산
period = pd.period_range(start='2022-01-13 00:00:00',end='2022-01-13 02:30:00',freq='30min')
data = {'col1':[1,2,3,4,5,6],'col2':period}
idx = ['row1','row2','row3','row4','row5','row6']
df = pd.DataFrame(data= data, index = idx)
print(df)

print(df['col1'].rolling(window=3).sum()) 

print(df['col1'].rolling(window=3, closed='left').sum())

print(df['col1'].rolling(window=3, closed='neither',min_periods=2).sum())

print(df['col1'].rolling(window=3, center=True).sum())

print(df.rolling(window='60min',on='col2').sum())

# 그룹화 계산
idx=['A','A','B','B','B','C','C','C','D','D','D','D','E','E','E']
col=['col1','col2','col3']
data = np.random.randint(0,9,(15,3))
df = pd.DataFrame(data=data, index=idx, columns=col).reset_index()
print(df)

print(df.groupby('index').agg(['sum','mean']))

## group_keys 인수 사용
def top (df,n=2,col='col1'):
    return df.sort_values(by=col)[-n:]

print(df.groupby('index').apply(top))
print(df.groupby('index',group_keys=False).apply(top))

## observed 인수 사용
df_cat = pd.Categorical(df['index'], categories=['A','B','C','D','E','F']) 
print(df_cat)

print(df['col1'].groupby(df_cat).count()) # observed=False(기본값)

print(df.groupby(['index'],as_index=True).sum())

## level 인수 사용(Multi Index)
idx = [['idx1','idx1','idx2','idx2','idx2'],['row1','row2','row1','row2','row3']]
col = ['col1','col2','col2']
data = np.random.randint(0,9,(5,3))
df = pd.DataFrame(data=data, index = idx, columns = col).rename_axis(index=['lv0','lv1'])
print(df)

print(df.groupby(level=1).sum())
print(df.groupby(['lv1','lv0']).sum())  

# 지수가중함수
data = {'val':[1,4,2,3,2,5,13,10,12,14,np.nan,16,12,20,22]}
df = pd.DataFrame(data).reset_index()
print(df)

import matplotlib.pyplot as plt

df2 = df.assign(ewm=df['val'].ewm(alpha=0.3).mean())
ax = df.plot(kind='bar',x='index',y='val') 
ax2= df2.plot(kind='line',x='index', y='ewm', color='red', ax=ax) 
plt.show()

## span 인수 사용
df2 = df.assign(span_4=df['val'].ewm(span=4).mean())
df3 = df.assign(span_8=df['val'].ewm(span=8).mean())
ax = df.plot(kind='bar',x='index',y='val')
ax2= df2.plot(kind='line',x='index', y='span_4', color='red', ax=ax)
ax3= df3.plot(kind='line',x='index', y='span_8', color='green', ax=ax)
plt.show()