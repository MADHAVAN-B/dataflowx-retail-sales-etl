-- Daily revenue report
CREATE TABLE IF NOT EXISTS report_daily_revenue AS
SELECT
    order_date,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS order_count
FROM sales_cleaned
GROUP BY order_date
ORDER BY order_date;

-- Category-wise revenue report
CREATE TABLE IF NOT EXISTS report_category_revenue AS
SELECT
    category,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS order_count
FROM sales_cleaned
GROUP BY category
ORDER BY total_revenue DESC;

-- Region-wise revenue report
CREATE TABLE IF NOT EXISTS report_region_revenue AS
SELECT
    region,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS order_count
FROM sales_cleaned
GROUP BY region
ORDER BY total_revenue DESC;