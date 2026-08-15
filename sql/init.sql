CREATE TABLE IF NOT EXISTS sales_cleaned (
    order_id VARCHAR(20) PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id VARCHAR(20) NOT NULL,
    product VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    region VARCHAR(50) NOT NULL,
    revenue NUMERIC(12,2) NOT NULL,
    load_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);