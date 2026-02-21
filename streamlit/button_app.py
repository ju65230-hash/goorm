import streamlit as st

st.header('st.button') # 앱의 헤더 텍스트 생성

if st.button('Say hello'): # 버튼에 표시되는 텍스트
     st.write('Why hello there') # 메세지 출력
else:
     st.write('Goodbye') # 메세지 출력