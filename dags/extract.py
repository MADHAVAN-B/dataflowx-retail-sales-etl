from pathlib import Path

RAW_FILE = Path("data/raw/retail_sales.csv")

def run_extract():
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_FILE}")
    print(f"Extract complete: {RAW_FILE}")