{{ config(
    materialized='table'
) }}



SELECT
    symbol,
    MAX(name) AS name,
    COUNT(DISTINCT date) AS appearance_count,
    MIN(date) AS first_appearance,
    MAX(date) AS last_appearance,
    AVG(price) AS avg_price,
    AVG(change_percent) AS avg_change_percent,
    -- This is a placeholder for streak calculation
    -- In a real implementation, we would use window functions to calculate actual streaks
    1 AS max_streak_length, 
    COUNT(DISTINCT source) AS sources_count
FROM {{ ref('stg_consolidated_gainers') }}
GROUP BY symbol
ORDER BY appearance_count DESC, avg_change_percent DESC
