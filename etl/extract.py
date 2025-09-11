import pandas as pd

def extract_data(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
        print(f"[EXTRACT] Loaded {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        print(f"[EXTRACT ERROR] Failed to read {filepath}: {e}")
        raise