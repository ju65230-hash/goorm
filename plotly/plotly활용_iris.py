import plotly.express as px

df = px.data.iris()

# trace 생성
fig=px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species"
    )

# 그래프 크기, margin 설정
fig.update_layout(
    width=400,
    height=400,
    margin_l=20,
    margin_r=20,
    margin_b=10,
    margin_t=10,
    paper_bgcolor="LightSteelBlue"
)

# 축 수정
fig.update_xaxes(
    range=[1,5], 
    title_font_color="gray", 
    title_font_size=15
    )
fig.update_yaxes(
    range=[4,8], 
    title_font_color="gray", 
    title_font_size=15
    )

# tick 생성
fig.update_xaxes(
    ticks="outside", 
    dtick=1, 
    minor_ticks="outside",
    tickangle=30
    )
fig.update_yaxes(
    ticks="outside", 
    dtick=1, 
    minor_ticks="outside",
    tickangle=30
    )

# 그래프 생성
fig.show()