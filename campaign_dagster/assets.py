from dagster import asset
from pathlib import Path
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_db

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "dime_recipients_1979-2024.csv"

@asset
def extract():
    return extract_data(DATA_PATH)

@asset
def transform(extract):
    return transform_data(extract)

@asset
def load(transform):
    load_to_db(transform)