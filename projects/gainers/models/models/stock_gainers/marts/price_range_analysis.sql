{{ config(
    materialized='table'
) }}

-- This model analyzes which price ranges have the most recurring symbols and best performance
-- Helps identify optimal price segments for finding consistent gainers

WITH price_ranges AS (
    SELECT 
        pd.price_range,
        pd.symbol_count,
        pd.unique_symbols,
        pd.avg_change_percent,
        pd.median_change_percent
    FROM {{ ref('int_price_distribution') }} pd
),

recurring_by_price AS (
    SELECT
        CASE
            WHEN gc.price < 5 THEN 'Under $5'
            WHEN gc.price BETWEEN 5 AND 10 THEN '$5-$10'
            WHEN gc.price BETWEEN 10 AND 25 THEN '$10-$25'
            WHEN gc.price BETWEEN 25 AND 50 THEN '$25-$50'
            WHEN gc.price BETWEEN 50 AND 100 THEN '$50-$100'
            WHEN gc.price > 100 THEN 'Over $100'
        END AS price_range,
        sf.symbol,
        sf.appearance_count
    FROM {{ ref('gainers_consolidated') }} gc
    JOIN {{ ref('int_symbol_frequency') }} sf 
    ON gc.symbol = sf.symbol
    WHERE sf.appearance_count > 1  -- Only recurring symbols
)

SELECT
    pr.price_range,
    pr.symbol_count,
    pr.unique_symbols,
    COUNT(DISTINCT rbp.symbol) AS recurring_symbols_count,
    (COUNT(DISTINCT rbp.symbol) / NULLIF(pr.unique_symbols, 0)) * 100 AS recurring_symbol_percentage,
    AVG(rbp.appearance_count) AS avg_appearances,
    -- Calculate high performers percentage (symbols appearing more than twice)
    (COUNT(DISTINCT CASE WHEN rbp.appearance_count > 2 THEN rbp.symbol END) / 
     NULLIF(COUNT(DISTINCT rbp.symbol), 0)) * 100 AS high_performers_percentage,
    pr.avg_change_percent,
    -- Weighted success score based on recurring symbols and average change
    (COUNT(DISTINCT rbp.symbol) / NULLIF(pr.unique_symbols, 0)) * 
    AVG(rbp.appearance_count) * pr.avg_change_percent AS weighted_success_score
FROM price_ranges pr
LEFT JOIN recurring_by_price rbp ON pr.price_range = rbp.price_range
GROUP BY 
    pr.price_range,
    pr.symbol_count, 
    pr.unique_symbols,
    pr.avg_change_percent,
    pr.median_change_percent
ORDER BY weighted_success_score DESC
