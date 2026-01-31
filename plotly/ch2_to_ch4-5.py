# graph_objects 모듈
import plotly.graph_objects as go

fig = go.Figure(
    # Data 입력
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    # layout 입력
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    )
)

fig.show()

# express 모듈을 활용한 생성
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2],title="A Figure Specified By express")

fig.show()

# 그래프 사이즈
# 1. express
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2],width=400, height=400)

fig.show()

# 2. graph_objects
import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])])

fig.update_layout(width=600,height=400)

fig.show()

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

# 3. margin
fig.update_layout(
    width=600,
    height=400,
    margin_l=50,
    margin_r=50,
    margin_b=100,
    margin_t=100,
    # 백그라운드 색 지정, margin 잘 보이게 하기 위함
    paper_bgcolor="LightSteelBlue",
)

fig.show()

# 타이틀
# 1. express 
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])

fig.update_layout(title_text="타이틀 설정하기")

fig.show()

# 2. graph_objects 
fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])])

fig.update_layout(title_text="타이틀 설정하기")

fig.show()

# 축 타이틀
# 1. express
df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip",
    labels=dict(total_bill="Total Bill ($)", tip="Tip ($)")) # 축 타이틀명 변경

fig.show()

# 2. graph_objects
df = px.data.tips()
x = df["total_bill"]
y = df["tip"]
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

fig.update_xaxes(title_text='Total Bill ($)')
fig.update_yaxes(title_text='Tip ($)')

fig.show()

# 축 범위 지정
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")

fig.update_xaxes(range=[0, 5])
fig.update_yaxes(range=[0, 10])

fig.show()

# 축 범위 역방향
fig.update_yaxes(autorange="reversed")

fig.show()