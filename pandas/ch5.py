# 크기 비교
import pandas as pd 

col = ['col1','col2','col3']
row = ['A','B','C']
df = pd.DataFrame(data=[[10,20,10],
                        [80,30,60],
                        [20,10,70]],index=row,columns=col)

print(df)

# 1. 스칼라
print(df.eq(10)) # 10과 같은 경우 True 표시

# 2. Series
s1 = pd.Series([10,30],index=["col1","col3"])
print(df.gt(s1)) # col1에서 10이상, col3에서 30이상이면 True

# 3. DataFrame
df2 = pd.DataFrame([[50],[50],[50]],index=row,columns=['col1'])
print(df.ge(df2)) # col1에 대해서 각각 50, 50, 50 이상이면 True

# 4. 멀티인덱스
row_mul = [['U','U','U','D','D','D'],['A','B','C','A','B','C']]
df_mul = pd.DataFrame(data=[[10,20,10],
                            [80,30,60],
                            [20,10,70],
                            [30,70,60],
                            [10,90,40],
                            [50,30,80]],index=row_mul,columns=col)
print(df_mul)

print(df.ge(df_mul,level=1)) # A, B, C를 index로 하는 두 DataFrame과의 비교

# select_dtypes
col1 = [1, 2, 3, 4, 5]
col2 = ['one', 'two', 'three', 'four', 'five']
col3 = [1.5, 2.5, 3.5, 4.5, 5.5]
col4 = [True, False, False, True, True]
df = pd.DataFrame({"col1": col1, "col2": col2, "col3": col3, "col4": col4})
print(df)

print(df.dtypes)

result = df.select_dtypes(include =[float,object], exclude=['int64'])
print(result)

# clip
col  = ['col1','col2','col3']
row  = ['row1','row2','row3']
data = [[-7,3,9],
        [6,-8,1],
        [-3,0,-7]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.clip(-4,5)) # df.clip(하한선, 상한선)

s = pd.Series(data=[1,2,3],index=row)
print(s)
print(df.clip(-s,s,axis=0)) # Series로 임계값 지정

# filter
col  = ['alpha','beta','gamma','delta','epsilon']
row  = ['sigma','omega','lambda']
data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.filter(items=['gamma', 'delta']))

print(df.filter(like='ta'))

print(df.filter(regex='[mn]')) # []: []안의 모든 문자가 포함된 경우

# sample
col  = ['col1','col2','col3']
row  = ['row1','row2','row3','row4','row5']
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.sample(10,replace=True)) # replace=True로 중복 추출 허용

print(df.sample(frac=0.4)) # 전체에 대한 추출 비율

s = pd.Series(data=[10,10,3,3,1],index=row)
print(s)
print(df.sample(2,weights=s)) # 가중치 높은 row1,2가 뽑힐 확률이 높음

print(df.sample(5,random_state=7)) # 재현성 위함

# isna, isnull, notna, notnull
import numpy as np

col  = ['col1','col2','col3','col4']
row  = ['row1','row2','row3']
data = [[1,2,pd.NA,4],
        [np.nan,6,7,8],
        [9,10,11,None]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.isna()) # df.isnull()도 동일
print(df.notna()) # df.notnull()도 동일

# dropna
print(df.dropna(axis=0)) # 결측치가 모두 존재하므로 Empty DataFrame 반환됨

print(df.dropna(axis=1, how='any'))

print(df.dropna(thresh=2)) # 정상값 2개 미만인 경우 보정

print(df.dropna(subset='col1')) # col1에 결측치 있는 경우 제거

df.dropna(inplace=True)
print(df) # 원본도 수정

# first_valid_index / last_valid_index
col  = ['col1','col2']
row  = ['row1','row2','row3','row4','row5']
data = [[np.nan,np.nan],[pd.NA,4],[pd.NA,pd.NaT],[5,6],[np.nan,pd.NA]]
df = pd.DataFrame(data,row,col)
print(df)

print(df.first_valid_index()) # 처음으로 결측치 아닌 값
print(df.last_valid_index()) # 마지막으로 결측치 아닌 값

# fillna / backfill / bfill / pad / ffill
dict={'col1':'A', 'col2':'B'}
print(df.fillna(value=dict))

print(df.bfill()) # 결측값 바로 아래값과 동일
print(df.ffill()) # 결측값 바로 윗값과 동일

print(df.fillna('A', limit=2))

# asof
row = [10,20,30,40,50,60]
data = {'A':[1,np.nan,np.nan,4,5,6],'B':[7,8,9,10,np.nan,12]}
df = pd.DataFrame(data=data, index = row)
print(df)

print(df.asof(where=[10,45,60]))

print(df.asof(where=[10,35,60],subset='A'))

# sort_values
na = np.nan
data = [[-3,'A',17],
        [na,'D',31],
        [ 7,'D',-8],
        [15,'Z', 3],
        [ 0, na,-7]]
col = ['col1','col2','col3']
row = ['row1','row2','row3','row4','row5']
df = pd.DataFrame(data = data, index = row, columns= col)
print(df)

print(df.sort_values(by=['col2','col3'])) # col2 -> col3 순으로 정렬

print(df.sort_values(by='col3',ascending=False)) # 내림차순

print(df.sort_values(by='col1',na_position='last'))

print(df.sort_values(by='col2',key=lambda col: col.str.lower()))

# sort_index
na = np.nan
index_tuples = [('row1', 'val1'), ('row1', 'val2'), ('row3', 'val3'), ('row3', 'val1'), ('row3', 'val2'), ('row2', 'val5'),('row2', 'val2')]
values = [ [1,2,3], [4,na,6], [7,8,9], [na,11,12], [13,14,15], [16,17,18], [19,20,21]]
index = pd.MultiIndex.from_tuples(index_tuples) # 인덱스 설정
df = pd.DataFrame(values, columns=['col4', 'col1', 'col2'], index = index)
print(df)

print(df.sort_index(axis=0, level=[1,0],ascending=[False,True])) # 각 level에 다른 정렬방식 가능

print(df.sort_index(axis=0, sort_remaining=True)) # 다른 level에도 정렬 적용

# nlargest, nsmallest
print(df.nlargest(n=3,columns='col1',keep='first'))

# combine
n=np.nan
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data1 = [[1,3,4],
         [n,8,2],
         [2,6,7]]
data2 = [[7,2,3],
         [2,4,2],
         [3,1,5]]
df1 = pd.DataFrame(data1,row,col)
df2 = pd.DataFrame(data2,row,col)
print(df1)
print(df2)

print(df1.combine(df2,np.maximum,fill_value=9))

col3 = ['col1','col2']
row3 = ['row1','row2']
data3 = [[1,2],
         [3,4]]
df3 = pd.DataFrame(data3, row3, col3)
print(df3)

print(df1.combine(df3, np.maximum,overwrite=False)) # 기존값
print(df1.combine(df3, np.maximum,overwrite=True)) # 존재하지 않는 열 NaN으로 채워짐

# combine_first
print(df1.combine_first(df2)) # NaN을 같은 위치의 인수로 덮어씀

# join
df1 = pd.DataFrame({'col1':[1,2,3]},index=['row3','row2','row1'])
print(df1)
df2 = pd.DataFrame({'col2':[13,14]},index=['row4','row3'])
print(df2)
df3 = pd.DataFrame({'col1':[23,24]},index=['row4','row3'])
print(df3)

print(df1.join(df2,how='left')) # self 기준
print(df1.join(df2,how='right')) # other 기준
print(df1.join(df2,how='outer')) # 합집합 기준
print(df1.join(df2,how='inner')) # 교집합 기준

print(df1.join(df2,how='left',sort=True)) # 인덱스 정렬

print(df1.join(df3,how='outer',lsuffix="_left",rsuffix='_right')) # 접미사 붙이기

df4 = pd.DataFrame({'IDX':['A','B','C'],'col1':[1,2,3]})
print(df4)
df5 = pd.DataFrame({'IDX':['C','D'],'col2':[13,14]})
print(df5)

print(df4.set_index('IDX').join(df5.set_index('IDX'))) # 기존 인덱스가 열 값으로 변경됨
print(df4.join(df5.set_index('IDX'),on='IDX')) # 열 기준으로 병합
