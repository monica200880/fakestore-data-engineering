import requests
import pandas as pd
import pyarrow as pa
from deltalake import write_deltalake

def fetch_api_data(url: str) -> list:
    """
    Fetch data from a REST API endpoint.
    
    Parameters:
        url (str): API endpoint.
    
    Returns:
        list: JSON decoded list of dictionaries.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def bronze_ingest(url: str, bronze_path: str):
    """
    Extract data from API and write to Delta Lake (Bronze layer).
    
    Parameters:
        url (str): API endpoint.
        bronze_path (str): Local or cloud Delta Lake path.
    """
    data = fetch_api_data(url)

    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)

    write_deltalake(bronze_path, table, mode="overwrite")

    return df
