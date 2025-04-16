{{ config(
    materialized='table'
) }}


WITH recurring_symbols AS (
    SELECT
        symbol,
        name,
        appearance_count,
        first_appearance,
        last_appearance,
        avg_price,
        avg_change_percent,
        sources_count
    FROM {{ ref('int_symbol_frequency') }}
    WHERE appearance_count > 1  -- Only include symbols appearing multiple times
)

SELECT
    rs.symbol,
    rs.name,
    rs.appearance_count,
    rs.sources_count || ' sources' AS sources,
    -- Calculate approximate days between appearances
    DATEDIFF('day', rs.first_appearance, rs.last_appearance) / 
        CASE WHEN rs.appearance_count > 1 
             THEN rs.appearance_count - 1 
             ELSE 1 
        END AS avg_days_between_appearances,
    -- This would be calculated using additional data in a real implementation
    -- For now, using a placeholder
    0.0 AS avg_price_change_between_appearances,
    -- Calculate appearance frequency as percentage of total trading days
    (rs.appearance_count / 
        DATEDIFF('day', rs.first_appearance, rs.last_appearance)) * 100 AS appearance_frequency,
    rs.avg_price AS avg_volume,
    -- Categorize the pattern
    CASE
        WHEN rs.avg_change_percent > 7 THEN 'High Growth'
        WHEN rs.avg_change_percent BETWEEN 5 AND 7 THEN 'Steady Growth'
        ELSE 'Moderate Growth'
    END AS gainer_pattern,
    -- Performance categorization
    CASE
        WHEN rs.appearance_count > 3 AND rs.avg_change_percent > 7 THEN 'Top Performer'
        WHEN rs.appearance_count > 2 AND rs.avg_change_percent > 5 THEN 'Strong Performer'
        ELSE 'Regular Performer'
    END AS performance_category
FROM recurring_symbols rs
ORDER BY rs.appearance_count DESC, rs.avg_change_percent DESC
