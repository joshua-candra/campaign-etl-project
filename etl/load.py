from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from typing import Dict
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # Load DB credentials from .env

# Creates a SQLAlchemy engine using .env config.
def get_engine() -> Engine:
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("[ERROR] DATABASE_URL not found in .env")
    engine = create_engine(db_url)
    print("[LOAD] SQLAlchemy engine created")
    return engine

# Loads transformed DataFrames into SQL tables.
def load_to_db(dataframes: Dict[str, pd.DataFrame]):
    engine = get_engine()
    with engine.begin() as conn:
        for tableName, df in dataframes.items():
            if df.empty:
                print(f"[LOAD] DataFrame for '{tableName}' is empty. Skipping.")
                continue
            stagingTable = f"{tableName}_staging"
            
            # Load data into a staging table.
            try:
                df.to_sql(stagingTable, conn, if_exists='replace', index=False)
                print(f"[LOAD] Inserted {len(df)} records into '{stagingTable}' staging table.")

                # Merge from staging into the final table
                allColumns = ", ".join(f'"{c}"' for c in df.columns)
                mergeSQL = f"""
                    INSERT INTO {tableName} ({allColumns})
                    SELECT {allColumns} FROM {stagingTable};
                """
                result = conn.execute(text(mergeSQL))
                print(f"[LOAD] Merged {result.rowcount} new records into final table '{tableName}'.")
            except Exception as e:
                print(f"[ERROR] Failed to insert into '{tableName}': {e}")
                raise