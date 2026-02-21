# %%
# Hover
# 1. Closest -> 기본 설정값, 커서 바로 옆 생성

# 2. X or Y 위치 -> 커서와 동일 축 위치의 그래프 정보 생성
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country")
fig.update_traces(mode="markers+lines")

fig.update_layout(hovermode="x") # hover x축으로

fig.show()

# 3. Unified 모드
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country")
fig.update_traces(mode="markers+lines")

fig.update_layout(
    hovermode="x unified", # 평행선+정보 모으기
    hoverlabel_bgcolor="black",
    hoverlabel_font_size=12,
    hoverlabel_font_color="white" # 스타일 편집
    ) 

fig.show()

# Hover 텍스트 내용 편집
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", text="pop")
fig.update_traces(mode="markers+lines")

fig.update_traces(hovertemplate='연도: %{x} <br>'+ # %{x}: 그래프에서의 x값
                                'pop: %{text} <br>'+ # %{text}: df 내의 "pop" 열의 값
                                'lifeExp : %{y}') # %{y}: 그래프에서의 y 값 

fig.update_xaxes(showspikes=True, 
                 spikecolor="green", 
                 spikesnap="cursor", 
                 spikemode="across") # 수평선
fig.update_yaxes(showspikes=True, 
                 spikecolor="orange", 
                 spikethickness=2) # 수직선

fig.show()
# %%
