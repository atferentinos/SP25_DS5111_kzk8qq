{{ config(
    materialized='table'
) }}

-- This model tracks frequency of symbols appearing in gainer lists
-- It addresses the key question: "Are there symbols that repeat? Is there a pattern?"

SELECT
    symbol,
    MAX(name) AS name,
    COUNT(DISTINCT date) AS appearance_count,
    MIN(date) AS first_appearance,
    MAX(date) AS last_appearance,
    AVG(price) AS avg_price,
    AVG(change_percent) AS avg_change_percent,
    COUNT(DISTINCT source) AS sources_count,
    -- Number of consecutive days (simplified approach)
    DATEDIFF('day', MIN(date), MAX(date)) AS date_span,
    ARRAY_AGG(DISTINCT day_of_week) WITHIN GROUP (ORDER BY day_of_week) AS days_appeared
FROM {{ ref('gainers_consolidated') }}
GROUP BY symbol
ORDER BY appearance_count DESC, avg_change_percent DESC
