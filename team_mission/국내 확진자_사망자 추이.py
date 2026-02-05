import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df=pd.read_csv("team_mission/a_national_trend_daily.csv")

df["date"]=pd.to_datetime(df["date"])

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(
    go.Scatter(x=df["date"], y=df["new_cases"], name="신규 확진자", mode="lines"),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(x=df["date"], y=df["new_deaths"], name="신규 사망자", mode="lines"),
    secondary_y=True
)

fig.update_layout(
    title="국내 신규 확진자/사망자 추이",
    title_font_size=20,
    template="plotly_dark",
    legend_yanchor="top",
    legend_y=0.99,
    legend_xanchor="left",
    legend_x=0.01,
    legend_font_family="Arial",
    legend_font_size=13,
    hovermode="x unified"
)

fig.update_xaxes(
    title_text="날짜",
    title_font_family="Arial", 
    title_font_size=15, 
    tickfont_family="Arial",
    showgrid=False
    )
fig.update_yaxes(
    title_text="확진자 수", 
    title_font_family="Arial", 
    title_font_size=15, 
    tickfont_family="Arial",
    secondary_y=False,
    showgrid=False
    )
fig.update_yaxes(
    title_text="사망자 수", 
    title_font_family="Arial",
    title_font_size=15, 
    tickfont_family="Arial",
    secondary_y=True, 
    showgrid=False
    )

fig.show()