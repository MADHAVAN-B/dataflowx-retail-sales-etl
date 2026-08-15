# DataFlowX Retail Sales ETL

## Overview

DataFlowX is a containerized retail-sales ETL pipeline built with Apache Airflow, Pandas, PostgreSQL, and Docker.

## Pipeline

extract -> transform -> validate -> load -> reporting

## Components

- Apache Airflow: workflow orchestration
- Pandas: data cleaning and transformation
- PostgreSQL: curated and reporting storage
- Docker Compose: reproducible local environment

## Data Quality Rules

- Remove duplicate order IDs
- Validate order dates
- Require positive quantities
- Require positive unit prices
- Require non-empty regions
- Calculate revenue as quantity multiplied by unit price

## Run the Project

```powershell
docker compose up -d
```

Open Airflow:

```text
http://localhost:8080
```

## Verify the Database

```powershell
docker exec -it dataflowx-project-db psql -U postgres -d dataflowx_db
```

## DAG Tasks

1. Extract raw CSV data
2. Transform and clean records
3. Validate data quality
4. Load curated data into PostgreSQL
5. Generate daily revenue reporting