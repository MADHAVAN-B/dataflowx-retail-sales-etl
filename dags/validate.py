import pandas as pd
from pathlib import Path

INPUT_FILE = Path("/opt/airflow/data/processed/retail_sales_cleaned.csv")


def run_validation():
    df = pd.read_csv(INPUT_FILE)

    assert not df.empty, "Cleaned dataset is empty"
    assert df["order_id"].is_unique, "Duplicate order_id values found"
    assert (df["quantity"] > 0).all(), "Invalid quantity found"
    assert (df["unit_price"] > 0).all(), "Invalid unit_price found"

    print("Validation passed.")