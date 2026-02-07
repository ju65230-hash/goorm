import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# -----------------------------
# 데이터 로드
# -----------------------------
def load_data():
    base_dir = Path(__file__).resolve().parent
    data_path = base_dir / "시군구별_월별_확진자_사망_발생현황_통합.csv"
    df = pd.read_csv(data_path)
    df["날짜"] = pd.to_datetime(df["날짜"])

    # 날짜별, 유형별 합계 계산
    df_agg = df.groupby(["날짜", "유형"])["값"].sum().reset_index()

    # 확진자/사망자 컬럼으로 변환
    df_pivot = df_agg.pivot(index="날짜", columns="유형", values="값").fillna(0)
    df_pivot = df_pivot.rename(columns={"확진자":"확진자_수", "사망자":"사망자_수"})
    df_pivot = df_pivot.reset_index()
    
    return df_pivot


# -----------------------------
# 대시보드
# -----------------------------
def build_national_dashboard(df):

    # dashboard
    fig = make_subplots(
        shared_xaxes=True,
        vertical_spacing=0.12,
        specs=[[{"secondary_y": True}]]
        )

    # -------------------------
    # 신규 확진자 / 사망자 (Dual Axis)
    # -------------------------
    fig.add_trace(
        go.Scatter(
            x=df["날짜"],
            y=df["확진자_수"],
            name="신규 확진자",
            mode="lines"
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df["날짜"],
            y=df["사망자_수"],
            name="신규 사망자",
            mode="lines"
        ),
        secondary_y=True
    )

    # -------------------------
    # Layout
    # -------------------------
    fig.update_layout(
        title="대한민국 코로나19 전국 통합 대시보드",
        template="plotly_dark",
        height=850,
        hovermode="x unified",

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="center",
            x=0.5,
            font=dict(family="Arial", size=13)
        ),

        margin=dict(l=60, r=60, t=120, b=60)
    )

    # X axis
    fig.update_xaxes(
        title_text="날짜",
        showgrid=False,
        title_font=dict(family="Arial", size=15),
        tickfont=dict(family="Arial")
    )

    # Y axis (신규 확진자)
    fig.update_yaxes(
        title_text="확진자 수",
        secondary_y=False,
        showgrid=False
    )

    # Y axis (신규 사망자)
    fig.update_yaxes(
        title_text="사망자 수",
        secondary_y=True,
        showgrid=False
    )

    fig.show()

# -----------------------------
# 실행
# -----------------------------
def main():
    df = load_data()
    build_national_dashboard(df)


if __name__ == "__main__":
    main()

