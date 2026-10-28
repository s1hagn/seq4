from data_processing import process_data

def analyze_data():
    genre_summary, overall_Rating, overall_Gross = process_data()

    #Q1
    result=genre_summary[
        (genre_summary["Average_Rating"] > overall_Rating) &
        (genre_summary["Average_Gross"] > overall_Gross)
    ]
    print(result.to_string())

if __name__ == "__main__":
    analyze_data()
