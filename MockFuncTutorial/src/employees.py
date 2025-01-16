import pandas as pd

def load_csv(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    return df

def calculate_len(df: pd.DataFrame) -> int:
    return len(df)