from data_cleaning import clean_data

def process_data():
    df = clean_data()

    #Q1
    genre_df=df.copy()
    genre_df["Genre"]=genre_df["Genre"].str.split(",")
    genre_df=genre_df.explode("Genre")
    genre_df["Genre"]=genre_df["Genre"].str.strip()

    genre_summary=genre_df.groupby("Genre").agg(
        Average_Rating=("IMDB_Rating","mean"),
        Average_Gross=("Gross","mean"),
        Movie_Count=("Series_Title","count")
    )
    genre_summary=genre_summary.sort_values(by="Average_Rating",
                                            ascending=False)
    print(genre_summary)

    overall_Rating=df["IMDB_Rating"].mean()
    overall_Gross=df["Gross"].mean()

    #Q2
    print(df["Runtime"].head())
    print(df["Runtime"].dtype)
    runtime_by_year=(
        df.groupby("Released_Year")["Runtime"].mean().sort_index()
    )
    print(runtime_by_year)
    return genre_summary, overall_Rating, overall_Gross

if __name__ == "__main__":
    process_data()
