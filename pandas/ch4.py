# loc
import pandas as pd

df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9]], index=['row1', 'row2', 'row3'], columns=['col1', 'col2', 'col3'])
print(df)

bool = [False, True, False] # row2에 대응되는 값만 True
result = df.loc[bool]
print(result)

# Multi index
index_tuples = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
values = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]
index = pd.MultiIndex.from_tuples(index_tuples) # 인덱스 설정
df = pd.DataFrame(values, columns=['col1', 'col2', 'col3'], index = index)
print(df)

result = df.loc[[('row2','val2')]] # [[ ]] 형태로 인덱싱 -> DataFrame 형태로 반환
print(result)

result = df.loc[('row1','val2') : ('row3','val2')] # row1의 val2부터 row3의 val2까지
print(result)