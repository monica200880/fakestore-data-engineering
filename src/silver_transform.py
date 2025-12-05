import pandas as pd

def clean_silver(df_bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Transform Bronze data into clean Silver data.
    
    Steps:
        - Fix data types
        - Extract rating
        - Normalize categories
        - Drop unused columns
    """
    df = df_bronze.copy()

    # Convert types
    df["id"] = df["id"].astype(int)
    df["price"] = df["price"].astype(float)

    # Extract rating (already a dict)
    df["rating_rate"] = df["rating"].apply(lambda x: x["rate"])
    df["rating_count"] = df["rating"].apply(lambda x: x["count"])

    # Normalize text
    df["category"] = df["category"].str.lower().str.strip()

    # Drop nested column
    df = df.drop(columns=["rating"])

    return df
