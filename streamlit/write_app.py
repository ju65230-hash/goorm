import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('st.write')

# 예제 1; 텍스트와 마크다운 형식의 텍스트 표시
st.write('Hello, *World!* :sunglasses:')

# 예제 2; 숫자와 같은 다른 데이터 형식 표시
st.write(1234)

# 예제 3; DataFrame 표시
df = pd.DataFrame({
     '첫 번째 컬럼': [1, 2, 3, 4],
     '두 번째 컬럼': [10, 20, 30, 40]
     })
st.write(df)

# 예제 4; 여러 인수를 전달
st.write('아래는 DataFrame입니다.', df, '위는 dataframe입니다.')

# 예제 5; 그래프 표시
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)