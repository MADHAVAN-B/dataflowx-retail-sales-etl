import os
from pathlib import Path

from sqlalchemy import create_engine, text

SQL_FILE = Path(__file__).resolve().parent / "sql" / "reports.sql"

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "dataflowx-project-db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "dataflowx_db")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def run_reporting():
    sql = SQL_FILE.read_text(encoding="utf-8")
    engine = create_engine(DATABASE_URL)

    with engine.begin() as conn:
        for statement in sql.split(";"):
            statement = statement.strip()
            if statement:
                conn.execute(text(statement))

    print("Reporting completed. Tables created.")


if __name__ == "__main__":
    run_reporting()