{{ config(
    materialized='table'
) }}


WITH volume_data AS (
    SELECT
        symbol,
        name,
        price,
        change_percent,
        date,
        day_of_week,
        -- This assumes you have volume in your dataset
        -- If not, you may need to modify this or make it conditional
        TRY_CAST(volume AS FLOAT) AS volume_value, 
        CASE
            WHEN TRY_CAST(volume AS FLOAT) < 100000 THEN 'Low Volume (<100K)'
            WHEN TRY_CAST(volume AS FLOAT) BETWEEN 100000 AND 500000 THEN 'Medium Volume (100K-500K)'
            WHEN TRY_CAST(volume AS FLOAT) BETWEEN 500000 AND 1000000 THEN 'High Volume (500K-1M)'
            WHEN TRY_CAST(volume AS FLOAT) > 1000000 THEN 'Very High Volume (>1M)'
            ELSE 'Unknown'
        END AS volume_range
    FROM {{ ref('stg_consolidated_gainers') }}
    WHERE TRY_CAST(volume AS FLOAT) IS NOT NULL
)

SELECT
    volume_range,
    COUNT(*) AS symbol_count,
    COUNT(DISTINCT symbol) AS unique_symbols,
    AVG(change_percent) AS avg_change_percent,
    AVG(price) AS avg_price,
    COUNT(DISTINCT date) AS days_count
FROM volume_data
WHERE volume_range != 'Unknown'
GROUP BY volume_range
ORDER BY 
    CASE 
        WHEN volume_range = 'Low Volume (<100K)' THEN 1
        WHEN volume_range = 'Medium Volume (100K-500K)' THEN 2
        WHEN volume_range = 'High Volume (500K-1M)' THEN 3
        WHEN volume_range = 'Very High Volume (>1M)' THEN 4
    END
