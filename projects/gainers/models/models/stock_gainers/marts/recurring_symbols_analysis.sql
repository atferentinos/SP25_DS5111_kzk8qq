{{ config(
    materialized='table'
) }}

-- This model provides deeper insights into recurring symbols
-- Identifies stocks that repeatedly appear as gainers and analyzes their patterns

WITH recurring_symbols AS (
    SELECT
        symbol,
        name,
        appearance_count,
        first_appearance,
        last_appearance,
        avg_price,
        avg_change_percent,
        sources_count,
        date_span,
        days_appeared
    FROM {{ ref('int_symbol_frequency') }}
    WHERE appearance_count > 1  -- Only include symbols appearing multiple times
)

SELECT
    rs.symbol,
    rs.name,
    rs.appearance_count,
    rs.sources_count || ' sources' AS sources,
    -- Calculate approximate days between appearances
    CASE WHEN rs.date_span > 0 AND rs.appearance_count > 1 
         THEN rs.date_span / (rs.appearance_count - 1)
         ELSE 0 
    END AS avg_days_between_appearances,
    -- Calculate appearance frequency as percentage of total available dates
    -- Assuming we have data from 10 distinct dates based on our selection
    (rs.appearance_count / 10.0) * 100 AS appearance_frequency,
    rs.avg_price,
    rs.avg_change_percent,
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
    END AS performance_category,
    -- Day pattern (which days it appears on)
    rs.days_appeared AS appearance_days
FROM recurring_symbols rs
ORDER BY rs.appearance_count DESC, rs.avg_change_percent DESC
