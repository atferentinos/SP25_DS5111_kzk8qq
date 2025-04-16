{{ config(
    materialized='table'
) }}

-- Pull data from the sample gainers table created in Snowflake
SELECT
    symbol,
    name,
    price,
    change,
    change_percent,
    source,
    timestamp,
    DATE(timestamp) as date,
    DAYNAME(DATE(timestamp)) as day_of_week
FROM KZK8QQ.sample_gainers
