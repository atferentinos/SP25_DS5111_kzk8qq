{{ config(
    materialized='table'
) }}


SELECT
    day_of_week,
    COUNT(*) AS gainer_count,
    COUNT(DISTINCT symbol) AS unique_symbols,
    AVG(change_percent) AS avg_change_percent,
    MAX(change_percent) AS max_change_percent,
    MIN(change_percent) AS min_change_percent,
    COUNT(DISTINCT date) AS distinct_dates
FROM {{ ref('gainers_consolidated') }}
GROUP BY day_of_week
ORDER BY 
    CASE 
        WHEN day_of_week = 'Monday' THEN 1
        WHEN day_of_week = 'Tuesday' THEN 2
        WHEN day_of_week = 'Wednesday' THEN 3
        WHEN day_of_week = 'Thursday' THEN 4
        WHEN day_of_week = 'Friday' THEN 5
    END
