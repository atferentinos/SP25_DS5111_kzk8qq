-- Calculate symbol frequency and stats
SELECT 
    symbol,
    COUNT(*) as appearance_count,
    MIN(date) as first_appearance,
    MAX(date) as last_appearance,
    AVG(price_percent_change) as avg_percent_change
FROM {{ ref('int_daily_combined') }}
GROUP BY symbol
