import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

CLEAN_FILE = Path("data/processed/retail_sales_cleaned.csv")

DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "dataflowx-project-db"
DB_PORT = "5432"
DB_NAME = "dataflowx_db"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def validate_data():
    assert not df.empty
    assert df["order_id"].is_unique
    assert (df["quantity"] > 0).all()
    assert (df["unit_price"] > 0).all()

def run_load():
    df = pd.read_csv(CLEAN_FILE)
    engine = create_engine(DATABASE_URL)
    df.to_sql(
        name="sales_cleaned",
        con=engine,
        if_exists="replace",
        index=False,
    )
    print("Load completed. Data written to sales_cleaned.")

if __name__ == "__main__":
    run_load()