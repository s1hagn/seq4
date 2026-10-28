import pandas as pd
from dash import Dash, html, dcc,dash_table
import plotly.express as px
df=pd.read_csv("imdb_top_1000.csv")
app=Dash(__name__)

df["Gross"]=pd.to_numeric(
    df["Gross"].str.replace(",","",regex=False),
    errors="coerce"
)

genre_df=df.copy()
genre_df["Genre"]=genre_df["Genre"].str.split(",")
genre_df=genre_df.explode("Genre")
genre_df["Genre"]=genre_df["Genre"].str.strip()

genre_df["Earning_per_Score"]=(
    genre_df["Gross"] / genre_df["IMDB_Rating"]
)

earning_by_genre=(
    genre_df.groupby("Genre",as_index=False)
    ["Earning_per_Score"].mean()
)

fig_earning=px.bar(
    earning_by_genre,
    x="Genre",
    y="Earning_per_Score",
    title="Average Earning per Score Point by Genre"
)

df["Runtime"]=pd.to_numeric(
    df["Runtime"].str.replace("min","",regex=False).str.strip(),
    errors="coerce" 
)

df["Released_Year"]=pd.to_numeric(
    df["Released_Year"],
    errors="coerce"
)

runtime_by_year=(
    df.groupby("Released_Year",as_index=False)
    ["Runtime"].mean()
    .sort_values("Released_Year")
)

fig_runtime=px.line(
    runtime_by_year,
    x="Released_Year",
    y="Runtime",
    title="Average Runtime by Year"
)


app.layout=html.Div([
    html.H1("IMDB 1000"),
    dash_table.DataTable(
        data=df.head().to_dict("records"),
        columns=[
            {"name":col,"id":col}
            for col in df.columns
        ],
        style_table={"overflowX":"auto"}
    ),
    dcc.Graph(figure=fig_earning),
    dcc.Graph(figure=fig_runtime)
])

if __name__=="__main__":
    app.run(debug=True)