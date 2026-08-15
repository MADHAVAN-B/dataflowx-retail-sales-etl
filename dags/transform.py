import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/retail_sales.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_FILE = OUTPUT_DIR / "retail_sales_cleaned.csv"

def validate_data():
    assert not df.empty
    assert df["order_id"].is_unique
    assert (df["quantity"] > 0).all()
    assert (df["unit_price"] > 0).all()

def run_transform():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(RAW_FILE)

    df = df.drop_duplicates(subset=["order_id"], keep="first")

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    df = df.dropna(subset=["order_date", "quantity", "unit_price", "region"])
    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]

    df["product"] = df["product"].str.strip()
    df["category"] = df["category"].str.strip()
    df["region"] = df["region"].str.strip()

    df["revenue"] = df["quantity"] * df["unit_price"]

    df.to_csv(OUTPUT_FILE, index=False)

    print("Transform completed. Cleaned shape:", df.shape)  

if __name__ == "__main__":
    run_transform()