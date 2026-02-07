# -*- coding: utf-8 -*-
# %%
# 축 스타일
import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="sex", y="tip", histfunc='sum', facet_col='smoker')

fig.update_xaxes(showline=True, linewidth=3, linecolor='black', col=1, mirror=True) # 'col=': 특정 Trace에만 축 스타일 적용
fig.update_yaxes(showline=True, linewidth=3, linecolor='blue', col=1, mirror=True) # mirror: 축 반대편 라인 편집

fig.show()
# %%
# 그리드 설정
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")

fig.update_xaxes(showgrid=True, minor_showgrid=True, griddash='solid', gridcolor='black', minor_griddash="dashdot", minor_gridcolor='LightPink')
fig.update_yaxes(showgrid=True, minor_showgrid=True, griddash='solid', gridcolor='black', minor_griddash="dashdot", minor_gridcolor='LightPink')

fig.show()
# %%
# 여러 개의 그래프 겹쳐 그리기
# express
import plotly.express as px
import plotly.graph_objects as go

# 1. Base 그래프 그리기
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], size = [20]*5)

# 2. 추가할 그래프 그리기
fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16]))

fig.show()

# graph_objects
import plotly.graph_objects as go

#데이터 생성
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# 1. Base 그래프 생성
fig = go.Figure()

# 2. 추가할 그래프 그리기
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', 
                    name='markers'))

fig.show()

# %%
# 여러 개의 그래프 나눠 그리기
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 나눠서 그릴 공간 생성
fig = make_subplots(rows=2, cols=1, subplot_titles=("Plot 1", "Plot 2"), shared_xaxes=True) # subplot_titles: 서브 타이틀 생성

# 각 공간에 Trace 채워 넣기
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=[2, 3, 4], y=[50, 60, 70]),
    row=2, col=1
)

fig.update_layout(title_text="Multiple Subplots with Titles")

fig.show()

# 공간 분할 병합; specs
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{}, {}], # {}: Trace
           [{"colspan": 2}, None]], # 1열을 2열까지 병합(1열: {"colspan": 2}, 2열: None)
           subplot_titles=("First Subplot","Second Subplot", "Third Subplot"))

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]),
                 row=1, col=1)

fig.add_trace(go.Scatter(x=[1, 2], y=[1, 2]),
                 row=1, col=2)
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, 2]),
                 row=2, col=1)


fig.update_layout(showlegend=False, title_text="Specs with Subplot Title")

fig.show()
# %%
# 이중 Y축 표시
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{"secondary_y": True}]]) # 이중 Y축 활성화

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=True,
)

fig.update_layout(
    title_text="Double Y Axis Example"
)

fig.update_xaxes(title_text="xaxis title")

fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

fig.show()
# %%
# 범례 생성
# express
import plotly.express as px

df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="sex") # 분류하려는 데이터 컬럼명 'color='에 입력

fig.update_layout(showlegend=False) # 범례 삭제

fig.show()

# graph_objects
# 1. 데이터 가공
Female = df.loc[df["sex"]=="Female", :]
Female.head()

Male = df.loc[df["sex"]=="Male", :]
Male.head()

# 2. 그래프 그리기
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=Female.total_bill,
    y=Female.tip,
    mode='markers',
    name="Female" # 범례로 표시할 문구
))

fig.add_trace(go.Scatter(
    x=Male.total_bill,
    y=Male.tip,
    mode='markers',
    name="Male"
))

fig.update_layout(
    legend_orientation="h", # 가로로 지정
    legend_entrywidth=70, # 가로 길이
    legend_yanchor="top",
    legend_y=0.99,
    legend_xanchor="left",
    legend_x=0.01
) # 위치 지정

fig.update_layout( 
    legend_title_text='성별',        
    legend_title_font_family = "Times New Roman",
    legend_title_font_color="green",
    legend_title_font_size= 15,
    legend_font_family="Courier",
    legend_font_size=10,
    legend_font_color="black",
    legend_bgcolor="LightSteelBlue",
    legend_bordercolor="Black",
    legend_borderwidth=2
    ) # 스타일 지정

fig.show()
# %%
# 수직선/수평선/사각영역 그리기
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="petal_length", y="petal_width")

# 수평선 추가
fig.add_hline(y=0.9,line_width=3, line_dash="dash",
              line_color="green",
              annotation_text="수평선", 
              annotation_position="bottom right",
              annotation_font_size=15,
              annotation_font_color="green")

# 수직선 추가
fig.add_vline(x=3,line_width=3, line_dash="dash",
              line_color="red",
              annotation_text="수직선", 
              annotation_position="top left",
              annotation_font_size=15,
              annotation_font_color="red")

# 수평 사각영역 그리기
fig.add_hrect(
		y0 = 1.2,
		y1 = 1.5,
		line_width = 0,
		fillcolor = "yellow",
		opacity=0.2,
        annotation_text="수평 영역", 
        annotation_position="top left",
        annotation_font_size=10,
        annotation_font_color="orange"
		)

fig.show()
# %%
# 사각형 그리기
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1.5, 4.5],
    y=[0.75, 0.75],
    text=["Unfilled Rectangle", "Filled Rectangle"],
    mode="text",
)) # 텍스트

fig.update_xaxes(range=[0, 7], showgrid=False) # x축 설정
fig.update_yaxes(range=[0, 3.5]) # y축 설정

fig.add_shape(type="rect",
    x0=1, y0=1, x1=2, y1=3,
    line_color="RoyalBlue") # 사각형

fig.add_shape(type="rect",
    x0=3, y0=1, x1=6, y1=2,
    line_color="RoyalBlue",
    line_width=2,
    fillcolor="LightSkyBlue",
    opacity=0.5) # 사각형2

fig.show()

# 원 그리기
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1.5, 3.5],
    y=[0.75, 2.5],
    text=["Unfilled Circle",
          "Filled Circle"],
    mode="text"
))

fig.update_xaxes(range=[0, 4.5])
fig.update_yaxes(range=[0, 4.5])

fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=1, y0=1, x1=3, y1=3,
    line_color="LightSeaGreen",)

fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="PaleTurquoise",
    x0=3, y0=3, x1=4, y1=4,
    line_color="LightSeaGreen")

fig.show()

# 다각형 그리기; 항상 원점으로 돌아가기
fig = go.Figure()

# 육각형
fig.add_trace(go.Scatter(x=[1,1,2,3,4,4,3,2,1], y=[1,2,3,3,2,1,0,0,1], fill="toself"))

fig.show()
# %%
# annotation
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.add_annotation(x=2, y=5,
            text="Text annotation with arrow",
            showarrow=True,
            arrowhead=2,
            arrowside="start")
fig.add_annotation(x=4, y=4,
            text="Text annotation without arrow",
            showarrow=True,
            arrowhead=7,
            yshift=2)

fig.show()
# %%
# 1. 이미지 파일 삽입
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=[0, 0.5, 1, 2, 2.2], y=[1.23, 2.5, 0.42, 3, 1])
)

fig.add_layout_image(
    source="https://images.plot.ly/language-icons/api-home/python-logo.png",
    xref="x",
    yref="y",
    x=0,
    y=3,
    sizex=2,
    sizey=2,
    sizing="stretch",
    opacity=0.5,
    layer="below")

fig.update_layout(template="plotly_white")

fig.show()

# 2. 이미지 파일만 딱 맞게 그리기
import plotly.graph_objects as go

fig = go.Figure()

# 그래프 사이즈 및 비율 지정
img_width = 1600
img_height = 900
scale_factor = 0.5

# x축을 그림 사이즈와 딱 맞게 조정
fig.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

# y축을 그림 사이즈와 딱 맞게 조정
fig.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    scaleanchor="x" # x축을 y축에 맞춤
)

# 그림 삽입하기
fig.add_layout_image(
    x=0,
    sizex=img_width * scale_factor,
    y=img_height * scale_factor,
    sizey=img_height * scale_factor,
    xref="x",
    yref="y",
    opacity=1.0,
    layer="below",
    sizing="stretch",
    source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg"
    )

# Figure 레이아웃 마진을 모두 0으로 맞춤
fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0}
    )

fig.show()
# %%
# Colormap
# 1. express
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

fig = px.bar(df, y="continent", x="pop", color="continent", color_discrete_sequence=px.colors.qualitative.G10)
    # bar차트는 보통 범주형 데이터
    # 불연속 그래프의 색 지정은 color_discrete_sequence
    # 불연속 데이터용 G10으로 자동으로 색 지정
    # 연속형 데이터의 색 지정은 color_continuous_scale

fig.show()

# 2. graph_objects
import plotly.graph_objects as go
import plotly.express as px

fig = go.Figure()

values = list(range(40))

fig.add_trace(go.Scatter(
    x=values,
    y=values,
    marker_size=16,
    marker_cmax=39,
    marker_cmin=0,
    marker_color=values, # values 별로 서로 다른 마커 색깔
    marker_colorbar_title = "Colorbar",
    marker_colorscale = "Viridis", # 연속 데이터용 "Viridis"로 지정
    mode="markers"))

fig.show()
# %%
# facet
import pandas as pd
import plotly.express as px

df = px.data.tips()
df.head() # 범주형 데이터 확인 -> 카테고리별로 나누기 가능

# 1. 열 별 나눠그리기
fig = px.scatter(df, x="total_bill", y="tip", color="smoker", facet_col="sex")
fig.show()

# 2. 행 별 나눠그리기
fig = px.scatter(df, x="total_bill", y="tip", color="smoker", facet_row="sex")
fig.show()

# 3. 행, 열 모두 나눠그리기
fig = px.scatter(df, x="total_bill", y="tip", color="smoker", facet_col="day", facet_row="sex")
fig.show()

# 4. 열 갯수 고정하기
import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', size='pop',facet_col='year', facet_col_wrap=4)
 # 카테고리가 많을 경우 갯수 제한 가능
fig.show()