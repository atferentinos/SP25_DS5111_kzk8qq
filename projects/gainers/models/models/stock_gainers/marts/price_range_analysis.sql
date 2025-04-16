{{ config(
    materialized='table'
) }}


WITH price_data AS (
    SELECT
        pd.price_range,
        pd.symbol_count,
        pd.unique_symbols,
        pd.avg_change_percent,
        cg.symbol,
        sf.appearance_count
    FROM {{ ref('int_price_distribution') }} pd
    JOIN {{ ref('stg_consolidated_gainers') }} cg ON 
        CASE
            WHEN cg.price < 5 THEN 'Under $5'
            WHEN cg.price BETWEEN 5 AND 10 THEN '$5-$10'
            WHEN cg.price BETWEEN 10 AND 25 THEN '$10-$25'
            WHEN cg.price BETWEEN 25 AND 50 THEN '$25-$50'
            WHEN cg.price BETWEEN 50 AND 100 THEN '$50-$100'
            WHEN cg.price > 100 THEN 'Over $100'
        END = pd.price_range
    LEFT JOIN {{ ref('int_symbol_frequency') }} sf ON cg.symbol = sf.symbol
)

SELECT
    price_range,
    MAX(symbol_count) AS symbol_count,
    COUNT(DISTINCT CASE WHEN appearance_count > 1 THEN symbol END) AS recurring_symbols_count,
    (COUNT(DISTINCT CASE WHEN appearance_count > 1 THEN symbol END) / NULLIF(MAX(unique_symbols), 0)) * 100 AS recurring_symbol_percentage,
    AVG(CASE WHEN appearance_count > 1 THEN appearance_count END) AS avg_appearances,
    -- For demonstration - percentage of symbols appearing more than twice
    (COUNT(CASE WHEN appearance_count > 2 THEN 1 END) / 
     NULLIF(COUNT(DISTINCT CASE WHEN appearance_count > 1 THEN symbol END), 0)) * 100 AS high_performers_percentage,
    -- Placeholder for volume data
    0.0 AS avg_volume,
    -- Weighted score based on recurring symbols and average change
    (COUNT(DISTINCT CASE WHEN appearance_count > 1 THEN symbol END) / NULLIF(MAX(unique_symbols), 0)) * 
    AVG(CASE WHEN appearance_count > 1 THEN appearance_count ELSE NULL END) AS weighted_success_score
FROM price_data
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
