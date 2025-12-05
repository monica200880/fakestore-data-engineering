import pandas as pd
import pyarrow as pa
from deltalake import write_deltalake

def create_gold_metrics(df_silver: pd.DataFrame) -> pd.DataFrame:
    """
    Create Gold analytics table with category metrics:
        - avg_price
        - avg_rating
        - total_reviews
        - product_count
    """
    gold_df = df_silver.groupby("category").agg({
        "price": "mean",
        "rating_rate": "mean",
        "rating_count": "sum",
        "id": "count"
    }).reset_index()

    gold_df.columns = ["category", "avg_price", "avg_rating", "total_reviews", "product_count"]

    return gold_df

def save_gold_delta(df_gold: pd.DataFrame, path: str):
    """Save Gold DataFrame as Delta Lake table."""
    table = pa.Table.from_pandas(df_gold)
    write_deltalake(path, table, mode="overwrite")
