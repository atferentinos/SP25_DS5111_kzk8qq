{{ config(
    materialized='table'
) }}


WITH price_ranges AS (
    SELECT
        symbol,
        name,
        price,
        change_percent,
        date,
        day_of_week,
        CASE
            WHEN price < 5 THEN 'Under $5'
            WHEN price BETWEEN 5 AND 10 THEN '$5-$10'
            WHEN price BETWEEN 10 AND 25 THEN '$10-$25'
            WHEN price BETWEEN 25 AND 50 THEN '$25-$50'
            WHEN price BETWEEN 50 AND 100 THEN '$50-$100'
            WHEN price > 100 THEN 'Over $100'
        END AS price_range
    FROM {{ ref('gainers_consolidated') }}
)

SELECT
    price_range,
    COUNT(*) AS symbol_count,
    COUNT(DISTINCT symbol) AS unique_symbols,
    AVG(change_percent) AS avg_change_percent,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY change_percent) AS median_change_percent,
    COUNT(DISTINCT date) AS days_count
FROM price_ranges
GROUP BY price_range
ORDER BY 
    CASE 
        WHEN price_range = 'Under $5' THEN 1
        WHEN price_range = '$5-$10' THEN 2
        WHEN price_range = '$10-$25' THEN 3
        WHEN price_range = '$25-$50' THEN 4
        WHEN price_range = '$50-$100' THEN 5
        WHEN price_range = 'Over $100' THEN 6
    END
