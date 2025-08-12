"""
    Play with DataFrames, switching off copilot!
"""
import pandas as pd

def coerce_to_int64(df: pd.DataFrame, *columns: str) -> pd.DataFrame:
    """
    Coerce specified columns in a DataFrame to the Int64 data type.
    In this context, it avoids putative integers displaying as decimal.
    """
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
    return df

def csv_to_json():

    df = pd.read_csv('rulers2.csv') 
    # Optional: inspect the DataFrame
    print(df.head())

    df = coerce_to_int64(df, 'Reign_Start', 'Reign_End')
    print(df.head(10))

    # Write the DataFrame to a JSON file
    df.to_json('rulers2.json', orient='records', indent=4)

if __name__ == '__main__':
    csv_to_json()