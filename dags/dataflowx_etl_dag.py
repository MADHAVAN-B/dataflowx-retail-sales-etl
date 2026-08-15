from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
from pathlib import Path

PROJECT_ROOT = Path("/opt/airflow")
sys.path.insert(0, str(PROJECT_ROOT))


def extract():
    from extract import run_extract
    run_extract()


def transform():
    from transform import run_transform
    run_transform()


def validate():
    from validate import run_validation
    run_validation()


def load():
    from load import run_load
    run_load()


def reporting():
    from reporting import run_reporting
    run_reporting()


default_args = {
    "owner": "madhavan",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="dataflowx_etl",
    default_args=default_args,
    description="End-to-end ETL pipeline for retail sales data",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["etl", "dataflowx"],
) as dag:

    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    transform_task = PythonOperator(task_id="transform", python_callable=transform)
    validate_task = PythonOperator(task_id="validate", python_callable=validate)
    load_task = PythonOperator(task_id="load", python_callable=load)
    reporting_task = PythonOperator(task_id="reporting", python_callable=reporting)

    extract_task >> transform_task >> validate_task >> load_task >> reporting_task