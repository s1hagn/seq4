import pandas as pd

def clean_data():
    df=pd.read_csv('imdb_top_1000.csv')
    print(df.head())
    df.info()
    df["Runtime"]=(
        df['Runtime']
        .str.replace("min","",regex=False)
        .str.strip()
        .astype("Int64")
    )
    df["Released_Year"]=pd.to_numeric(
        df["Released_Year"],
        errors='coerce'
    )
    df["Released_Year"]=df["Released_Year"].astype("Int64")
    df["Gross"]=(
        df["Gross"]
        .str.replace(",","",regex=False)
    )
    df["Gross"]=pd.to_numeric(
        df["Gross"],
        errors='coerce'
    )
    print(df[["Runtime", "Released_Year", "Gross"]].head())
    df[["Runtime", "Released_Year", "Gross"]]
    df.to_csv("imdb_cleaned.csv", index=False)
    return df

if __name__ == "__main__":
    clean_data()
